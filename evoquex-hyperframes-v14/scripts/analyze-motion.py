"""Analyze decoded V14 motion; never claim audiovisual playback.

The NumPy fallback is local differential Lucas-Kanade flow, not semantic object
tracking. Its estimates can fail on blur, large jumps, occlusion and low texture.
Usage: python scripts/analyze-motion.py [--video PATH]
"""
from pathlib import Path
import argparse, csv, hashlib, json, math, re, subprocess
import numpy as np
try:
    import cv2
except ImportError:
    cv2 = None

P = Path(__file__).resolve().parent.parent
CONFIG = json.loads((P / 'resources/qa-contract-v14.json').read_text())
TIMING = json.loads((P / CONFIG['timing_source']).read_text())
FPS = CONFIG['fps']
WIDTH, HEIGHT = 180, 320


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_csv(path, rows):
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def probe(path):
    return json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-show_streams',
                                              '-show_format', '-of', 'json', str(path)]))


def frames(path):
    process = subprocess.Popen(['ffmpeg', '-v', 'error', '-xerror', '-i', str(path), '-an',
                                '-vf', f'scale={WIDTH}:{HEIGHT}:flags=area,format=gray',
                                '-fps_mode', 'passthrough', '-pix_fmt', 'gray', '-f', 'rawvideo', '-'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    size = WIDTH * HEIGHT
    try:
        while True:
            payload = process.stdout.read(size)
            if not payload:
                break
            assert len(payload) == size, 'Truncated decoded raw frame'
            yield np.frombuffer(payload, dtype=np.uint8).reshape(HEIGHT, WIDTH).copy()
        error = process.stderr.read().decode(errors='replace')
        code = process.wait()
        assert code == 0, f'FFmpeg decode failed: {error}'
    finally:
        if process.poll() is None:
            process.terminate()
            process.wait()
        process.stdout.close()
        process.stderr.close()


def local_lucas_kanade(previous, current, block=8):
    """Least-squares differential flow for well-conditioned 8x8 image cells."""
    first, second = previous.astype(np.float32), current.astype(np.float32)
    dy0, dx0 = np.gradient(first)
    dy1, dx1 = np.gradient(second)
    gx, gy, temporal = (dx0 + dx1) * .5, (dy0 + dy1) * .5, second - first
    h, w = HEIGHT // block * block, WIDTH // block * block

    def sums(value):
        return value[:h, :w].reshape(h // block, block, w // block, block).sum(axis=(1, 3))

    xx, xy, yy = sums(gx * gx), sums(gx * gy), sums(gy * gy)
    xt, yt = sums(gx * temporal), sums(gy * temporal)
    determinant = xx * yy - xy * xy
    minimum_eigenvalue = .5 * (xx + yy - np.sqrt(np.maximum((xx - yy) ** 2 + 4 * xy * xy, 0)))
    valid = (minimum_eigenvalue > 25) & (determinant > 10000)
    u, v = np.zeros_like(xx), np.zeros_like(xx)
    u[valid] = (xy[valid] * yt[valid] - yy[valid] * xt[valid]) / determinant[valid]
    v[valid] = (xy[valid] * xt[valid] - xx[valid] * yt[valid]) / determinant[valid]
    # Large per-frame changes violate the differential small-motion assumption.
    valid &= (np.abs(u) <= 12) & (np.abs(v) <= 12)
    center_y, center_x = np.indices(u.shape)
    valid &= (center_y >= 3) & (center_y < u.shape[0] - 3)
    valid &= (center_x >= 2) & (center_x < u.shape[1] - 2)
    return u[valid], v[valid], float(valid.sum() / valid.size)


def flow(previous, current):
    if cv2 is None:
        return local_lucas_kanade(previous, current)
    field = cv2.calcOpticalFlowFarneback(previous, current, None, .5, 3, 15, 3, 5, 1.2, 0)
    roi = field[32:-32, 18:-18]
    gradient = np.hypot(*np.gradient(current.astype(np.float32)))[32:-32, 18:-18]
    valid = gradient > 4
    return roi[..., 0][valid], roi[..., 1][valid], float(valid.mean())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video', type=Path, default=P / 'renders/evoquex-hyperframes-v14.mp4')
    args = parser.parse_args()
    review = P / 'review'
    review.mkdir(exist_ok=True)
    meta = probe(args.video)
    video = next(x for x in meta['streams'] if x['codec_type'] == 'video')
    assert (video['width'], video['height'], video['r_frame_rate'], video['nb_frames']) == (1080, 1920, f'{FPS}/1', str(CONFIG['expected_frames']))
    reset_frames = {round(scene['start'] * FPS) for scene in TIMING['scenes']}
    rows, previous, cumulative_x, cumulative_y = [], None, 0., 0.
    for frame, current in enumerate(frames(args.video)):
        if frame in reset_frames:
            cumulative_x, cumulative_y = 0., 0.
        if previous is None:
            dx, dy, speed, p95, coverage, mae = 0., 0., 0., 0., 0., 0.
        else:
            u, v, coverage = flow(previous, current)
            magnitudes = np.hypot(u, v)
            dx = float(np.median(u)) if len(u) else 0.
            dy = float(np.median(v)) if len(v) else 0.
            speed = float(np.median(magnitudes)) if len(u) else 0.
            p95 = float(np.percentile(magnitudes, 95)) if len(u) else 0.
            mae = float(np.mean(np.abs(current[32:-32, 18:-18].astype(float) - previous[32:-32, 18:-18].astype(float))))
            cumulative_x += dx
            cumulative_y += dy
        rows.append({'frame': frame, 'time_seconds': frame / FPS, 'median_dx_scaled_pixels': dx,
                     'median_dy_scaled_pixels': dy, 'median_flow_scaled_pixels_per_frame': speed,
                     'p95_flow_scaled_pixels_per_frame': p95, 'valid_flow_cell_fraction': coverage,
                     'center_roi_mean_abs_frame_difference': mae,
                     'cumulative_estimated_scene_dx_scaled_pixels': cumulative_x,
                     'cumulative_estimated_scene_dy_scaled_pixels': cumulative_y,
                     'low_motion_signal_candidate': bool(frame > 0 and coverage > .01 and p95 < .12 and mae < .9),
                     'large_change_or_cut_candidate': bool(mae > 22)})
        previous = current
    assert len(rows) == CONFIG['expected_frames']
    write_csv(review / 'motion-flow-v14.csv', rows)
    pacing = []
    for second in range(math.ceil(CONFIG['duration_seconds'])):
        part = rows[second * FPS:(second + 1) * FPS]
        pacing.append({'start_seconds': second, 'end_seconds_exclusive': second + 1,
                       'median_flow_scaled_pixels_per_frame': float(np.median([x['median_flow_scaled_pixels_per_frame'] for x in part])),
                       'maximum_p95_flow_scaled_pixels_per_frame': max(x['p95_flow_scaled_pixels_per_frame'] for x in part),
                       'mean_center_roi_frame_difference': float(np.mean([x['center_roi_mean_abs_frame_difference'] for x in part])),
                       'low_motion_signal_candidate_frames': sum(x['low_motion_signal_candidate'] for x in part),
                       'large_change_or_cut_candidate_frames': sum(x['large_change_or_cut_candidate'] for x in part)})
    write_csv(review / 'motion-pacing-v14.csv', pacing)
    artifact_names = ['motion-flow-v14.csv', 'motion-pacing-v14.csv']
    report = {'version': 'V14', 'video': args.video.name, 'video_sha256': sha(args.video),
              'full_ffmpeg_decode_passed': True, 'decoded_frames': len(rows), 'analysis_dimensions': [WIDTH, HEIGHT],
              'fps': FPS, 'flow_method': 'OpenCV Farneback' if cv2 is not None else 'NumPy local differential Lucas-Kanade 8x8 cells',
              'cv2_available': cv2 is not None, 'new_dependencies_installed': False,
              'estimated_trajectories_are_semantic_object_tracks': False,
              'cumulative_estimate_resets_at_seconds': [scene['start'] for scene in TIMING['scenes']],
              'low_motion_candidates_are_quality_failures': False, 'hook_pixel_identity_required': False,
              'artifacts_sha256': {name: sha(review / name) for name in artifact_names},
              'continuous_playback_performed': False, 'subjective_listening_performed': False,
              'limitations': ['Differential flow assumes local texture and small motion; blur, cuts, large jumps and occlusion can invalidate estimates.',
                              'Cumulative scene displacement is an image-flow estimate, not an identified object trajectory.',
                              'Moving grain/glow can contribute motion; review semantic objects and consecutive frames separately.',
                              'Static reading/proof holds can be intentional; numerical motion is not a quality score.',
                              'The hook is a quality benchmark in V14; no pixel-identity constraint or baseline comparison is imposed.',
                              'No audiovisual playback or subjective sound review is performed by this script.']}
    (review / 'motion-analysis-v14.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
