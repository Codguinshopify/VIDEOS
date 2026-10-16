"""Package V13 sources and selected evidence, without comparison renders or secrets."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json, hashlib

P = Path(__file__).resolve().parent.parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    out = P / 'renders/evoquex-hyperframes-v13-projeto.zip'
    out.parent.mkdir(exist_ok=True)
    files = set()
    essential = ['index.html', 'style.css', 'motion.js', 'DESIGN.md', 'STORYBOARD.md',
                 'REFERENCE-IMPLEMENTATION.md', 'README.md', 'AGENTS.md', 'package.json',
                 'package-lock.json', 'hyperframes.json', 'meta.json', '.gitignore']
    for name in essential:
        assert (P / name).is_file(), f'Required source missing: {name}'
        files.add(P / name)
    for directory in ['assets', 'vendor', 'scripts', 'resources']:
        files.update(path for path in (P / directory).rglob('*')
                     if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc')
    patterns = ['output-validation.json', 'hf-v13-sampling.json', 'hf-v13-sampling-frames.csv',
                'source-validation.json', 'final-check.json', 'motion-review.json', 'motion-review-v13.json', 'final-review.md',
                'source-reproduction.json', '*reproduction*.json',
                'independent-visual-review.md', 'independent-motion-review.md', 'independent-audio-review.md', 'studio-readiness.json',
                'audio-validation-v13.json', 'audio-hook-preservation-v13.json',
                'audio-cue-validation-v13.json', 'motion-analysis-v13.json', 'motion-flow-v13.csv',
                'motion-pacing-v13.csv', 'hook-ssim-v13.csv', 'hook-ssim-v13.log',
                'hook-preservation*.json', 'hook-preservation*.csv', '*hook*v13*.json',
                '*hook*v13*.csv', 'copy-validation*.json', '*copy*v13*.json',
                'hf-v13-full-*.jpg', 'hf-v13-hook-*.jpg', 'hf-v13-motion-*.jpg', 'hf-v13-phone-*.png']
    for pattern in patterns:
        files.update((P / 'review').glob(pattern))
    animation_map = P / 'review/animation-map/animation-map.json'
    if animation_map.is_file():
        files.add(animation_map)
    manifest = {path.relative_to(P).as_posix(): sha(path) for path in sorted(files)}
    hashes_file = P / 'review/source-file-sha256.json'
    hashes_file.parent.mkdir(exist_ok=True)
    hashes_file.write_text(json.dumps({'version': 'V13', 'files': manifest}, indent=2) + '\n')
    files.add(hashes_file)
    with ZipFile(out, 'w', ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(files):
            relative = path.relative_to(P)
            assert not path.name.startswith('.env') and 'node_modules' not in path.parts
            assert not any(part in {'reference', 'reference-frames', 'references'} for part in relative.parts), relative
            assert path.suffix not in {'.exe', '.dll'}, relative
            archive.write(path, 'evoquex-hyperframes-v13/' + relative.as_posix())
    with ZipFile(out) as archive:
        assert archive.testzip() is None
        required = ['index.html', 'style.css', 'motion.js', 'assets/campanha.mp4', 'assets/mix-v13.wav',
                    'assets/DM-Sans.woff2', 'vendor/evoquex-v12-effects.js',
                    'vendor/evoquex-v13-motion.js', 'vendor/MotionPathPlugin.min.js', 'package-lock.json']
        for name in required:
            assert archive.read('evoquex-hyperframes-v13/' + name) == (P / name).read_bytes()
        assert not any('/node_modules/' in name or '/.env' in name for name in archive.namelist())
    report = {'version': 'V13', 'file': out.name, 'sha256': sha(out), 'bytes': out.stat().st_size,
              'crc_verified': True, 'files': len(files), 'self_contained_assets': True,
              'source_hash_manifest': 'review/source-file-sha256.json',
              'reference_video_frames_and_audio_excluded': True,
              'comparison_renders_excluded': True, 'node_modules_and_secrets_excluded': True}
    (P / 'review/package-validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
