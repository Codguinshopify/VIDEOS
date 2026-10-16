"""Extract explicitly timed V14 frames; extraction is not continuous playback."""
from pathlib import Path
from PIL import Image, ImageDraw
import subprocess, json, sys, hashlib, csv, math

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / 'resources/qa-contract-v14.json').read_text())
WINDOWS = CONFIG['review_windows']
FPS = CONFIG['fps']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    video = ROOT / (sys.argv[1] if len(sys.argv) > 1 else 'renders/evoquex-hyperframes-v14.mp4')
    video_sha = sha(video)
    tag = 'hf-v14'
    folder = ROOT / 'review' / (tag + '-' + video_sha[:10])
    folder.mkdir(parents=True, exist_ok=True)
    inventory = []
    sheet_paths = []

    def run(*args):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', *map(str, args)], check=True)

    def sheets(items, name, cols=6, per=24):
        for start in range(0, len(items), per):
            chunk = items[start:start + per]
            canvas = Image.new('RGB', (216 * cols, 418 * math.ceil(len(chunk) / cols)), '#E0E6EE')
            draw = ImageDraw.Draw(canvas)
            for i, (path, frame) in enumerate(chunk):
                x, y = i % cols * 216, i // cols * 418
                with Image.open(path) as picture:
                    picture.load()
                    assert picture.size == (216, 384), (path, picture.size)
                    canvas.paste(picture.convert('RGB'), (x, y))
                draw.text((x + 5, y + 388), f'f{frame:04d} | {frame / FPS:.4f}s', fill='#11132B')
            target = ROOT / 'review' / f'{tag}-{name}-{start // per + 1:02d}.jpg'
            canvas.save(target, quality=94)
            sheet_paths.append(str(target.relative_to(ROOT)))

    def register(path, frame, category):
        inventory.append({'category': category, 'frame': frame, 'time_seconds': frame / FPS,
                          'path': str(path.relative_to(ROOT)), 'sha256': sha(path)})
        return path, frame

    full_folder = folder / 'full-2fps'
    full_folder.mkdir(exist_ok=True)
    run('-i', video, '-vf', 'select=not(mod(n\\,15)),scale=216:384',
        '-fps_mode', 'passthrough', '-start_number', 0, full_folder / 'sample-%04d.png')
    full = [register(full_folder / f'sample-{i:04d}.png', i * 15, 'full-2fps') for i in range(math.ceil(CONFIG['expected_frames'] / 15))]
    sheets(full, 'full')

    hook_folder = folder / 'hook-consecutive'
    hook_folder.mkdir(exist_ok=True)
    run('-i', video, '-frames:v', 120, '-vf', 'scale=216:384',
        '-fps_mode', 'passthrough', '-start_number', 0, hook_folder / 'frame-%04d.png')
    hook = [register(hook_folder / f'frame-{i:04d}.png', i, 'hook-consecutive') for i in range(120)]
    sheets(hook, 'hook')

    windows = []
    for number, (start, end) in enumerate(WINDOWS, 1):
        first, stop = math.ceil(start * FPS - 1e-7), math.ceil(end * FPS - 1e-7)
        name = f'motion-{number:02d}-{start:g}-{end:g}s'
        dest = folder / name
        dest.mkdir(exist_ok=True)
        expression = f'select=gte(n\\,{first})*lt(n\\,{stop}),scale=216:384'
        run('-i', video, '-vf', expression, '-fps_mode', 'passthrough',
            '-start_number', first, dest / 'frame-%04d.png')
        sequence = [register(dest / f'frame-{f:04d}.png', f, name) for f in range(first, stop)]
        assert len(sequence) == stop - first
        sheets(sequence, f'motion-{number:02d}')
        windows.append({'index': number, 'start_seconds': start, 'end_seconds_exclusive': end,
                        'first_frame': first, 'last_frame_inclusive': stop - 1,
                        'consecutive_frames': len(sequence), 'folder': str(dest.relative_to(ROOT))})

    for name, frame in CONFIG['phone_check_frames'].items():
        target = ROOT / 'review' / f'{tag}-phone-{name}.png'
        run('-i', video, '-vf', f'select=eq(n\\,{frame}),scale=360:640', '-frames:v', 1, target)

    csv_path = ROOT / 'review' / f'{tag}-sampling-frames.csv'
    with csv_path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['category', 'frame', 'time_seconds', 'path', 'sha256'])
        writer.writeheader()
        writer.writerows(inventory)
    report = {'video': video.name, 'sha256': video_sha, 'version': 'V14', 'fps': FPS,
              'sampling_folder': folder.name, 'full_duration_samples': len(full),
              'full_sample_times': [frame / FPS for _, frame in full],
              'opening_frames': len(hook), 'hook_interval': '[0,4)', 'hook_pixel_identity_required': False, 'motion_windows': windows,
              'transition_consecutive_frames': sum(x['consecutive_frames'] for x in windows),
              'sheets': sheet_paths, 'frame_inventory_csv': str(csv_path.relative_to(ROOT)),
              'frame_inventory_csv_sha256': sha(csv_path), 'phone_checks': len(CONFIG['phone_check_frames']),
              'continuous_playback_performed': False, 'subjective_audio_playback_available': False,
              'visual_inspection_status': 'Frames extracted for review; this script does not claim visual approval.'}
    (ROOT / 'review' / f'{tag}-sampling.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
