"""Analyze decoded V13 motion and hook SSIM; never claim audiovisual playback.

The NumPy fallback is local differential Lucas-Kanade flow, not semantic object
tracking. Its estimates can fail on blur, large jumps, occlusion and low texture.
Usage: python scripts/analyze-motion.py [--video PATH] [--baseline PATH]
"""
from pathlib import Path
import argparse, csv, hashlib, json, math, re, subprocess
import numpy as np
try:
    import cv2
except ImportError:
    cv2 = None

P = Path(__file__).resolve().parent.parent
FPS = 30
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


def hook_ssim(baseline, candidate, review):
    for path in (baseline, candidate):
        meta = probe(path)
        video = next(x for x in meta['streams'] if x['codec_type'] == 'video')
        assert (video['width'], video['height'], video['r_frame_rate']) == (1080, 1920, '30/1')
    output = review / 'hook-ssim-v13.log'
    graph = ('[0:v]trim=start_frame=0:end_frame=120,setpts=PTS-STARTPTS,format=yuv420p[a];'
             '[1:v]trim=start_frame=0:end_frame=120,setpts=PTS-STARTPTS,format=yuv420p[b];'
             f'[a][b]ssim=stats_file={output}[compared]')
    command = ['ffmpeg', '-v', 'error', '-i', str(baseline), '-i', str(candidate),
               '-filter_complex', graph, '-map', '[compared]', '-frames:v', '120', '-an', '-f', 'null', '-']
    subprocess.run(command, capture_output=True, check=True)
    rows = []
    for line in output.read_text().splitlines():
        match = re.search(r'n:(\d+).*?All:([0-9.]+)', line)
        if match:
            frame = int(match.group(1)) - 1
            rows.append({'frame': frame, 'time_seconds': frame / FPS, 'ssim_all': float(match.group(2))})
    assert len(rows) == 120 and [x['frame'] for x in rows] == list(range(120)), 'Hook SSIM frame coverage incomplete'
    write_csv(review / 'hook-ssim-v13.csv', rows)
    return {'baseline': str(baseline), 'baseline_sha256': sha(baseline), 'candidate_sha256': sha(candidate),
            'frames': len(rows), 'interval': '[0,4)', 'resolution': [1080, 1920],
            'minimum_ssim': min(x['ssim_all'] for x in rows),
            'mean_ssim': float(np.mean([x['ssim_all'] for x in rows])),
            'frames_below_0_999': [x['frame'] for x in rows if x['ssim_all'] < .999],
            'command': command, 'log': 'review/hook-ssim-v13.log', 'csv': 'review/hook-ssim-v13.csv',
            'meaning': 'Per-frame similarity of decoded H264 exports. SSIM alone does not prove lossless pixel identity.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video', type=Path, default=P / 'renders/evoquex-hyperframes-v13.mp4')
    parser.add_argument('--baseline', type=Path, default=P.parent / 'evoquex-hyperframes-v12/renders/evoquex-hyperframes-v12.mp4')
    args = parser.parse_args()
    review = P / 'review'
    review.mkdir(exist_ok=True)
    meta = probe(args.video)
    video = next(x for x in meta['streams'] if x['codec_type'] == 'video')
    assert (video['width'], video['height'], video['r_frame_rate'], video['nb_frames']) == (1080, 1920, '30/1', '900')
    hook = hook_ssim(args.baseline, args.video, review)
    rows, previous, cumulative_x, cumulative_y = [], None, 0., 0.
    for frame, current in enumerate(frames(args.video)):
        if frame in (0, 120, 240, 450, 630):
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
    assert len(rows) == 900
    write_csv(review / 'motion-flow-v13.csv', rows)
    pacing = []
    for second in range(30):
        part = rows[second * FPS:(second + 1) * FPS]
        pacing.append({'start_seconds': second, 'end_seconds_exclusive': second + 1,
                       'median_flow_scaled_pixels_per_frame': float(np.median([x['median_flow_scaled_pixels_per_frame'] for x in part])),
                       'maximum_p95_flow_scaled_pixels_per_frame': max(x['p95_flow_scaled_pixels_per_frame'] for x in part),
                       'mean_center_roi_frame_difference': float(np.mean([x['center_roi_mean_abs_frame_difference'] for x in part])),
                       'low_motion_signal_candidate_frames': sum(x['low_motion_signal_candidate'] for x in part),
                       'large_change_or_cut_candidate_frames': sum(x['large_change_or_cut_candidate'] for x in part)})
    write_csv(review / 'motion-pacing-v13.csv', pacing)
    artifact_names = ['hook-ssim-v13.csv', 'hook-ssim-v13.log', 'motion-flow-v13.csv', 'motion-pacing-v13.csv']
    report = {'version': 'V13', 'video': args.video.name, 'video_sha256': sha(args.video),
              'full_ffmpeg_decode_passed': True, 'decoded_frames': len(rows), 'analysis_dimensions': [WIDTH, HEIGHT],
              'fps': FPS, 'flow_method': 'OpenCV Farneback' if cv2 is not None else 'NumPy local differential Lucas-Kanade 8x8 cells',
              'cv2_available': cv2 is not None, 'new_dependencies_installed': False,
              'estimated_trajectories_are_semantic_object_tracks': False,
              'cumulative_estimate_resets_at_seconds': [0, 4, 8, 15, 21],
              'low_motion_candidates_are_quality_failures': False, 'hook_ssim': hook,
              'artifacts_sha256': {name: sha(review / name) for name in artifact_names},
              'continuous_playback_performed': False, 'subjective_listening_performed': False,
              'limitations': ['Differential flow assumes local texture and small motion; blur, cuts, large jumps and occlusion can invalidate estimates.',
                              'Cumulative scene displacement is an image-flow estimate, not an identified object trajectory.',
                              'Moving grain/glow can contribute motion; review semantic objects and consecutive frames separately.',
                              'Static reading/proof holds can be intentional; numerical motion is not a quality score.',
                              'Decoded-export SSIM does not replace the protected-hook source/lossless identity contract.',
                              'No audiovisual playback or subjective sound review is performed by this script.']}
    (review / 'motion-analysis-v13.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
