"""Create a self-contained V15 source archive bound to a validated render.

Include active runtime dependencies, reproducible audio inputs named in provenance,
source scripts, pinned dependencies and compact documentation. Exclude caches,
reference movies, original archives, node_modules and frame dumps.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('qa_v15', ROOT / 'scripts/qa-v15.py')
qa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qa)


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)
    elif isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from strings(item)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=ROOT / 'renders/evoquex-hyperframes-v15-projeto.zip')
    args = parser.parse_args()
    source = qa.source_report()
    validation = json.loads((ROOT / 'review/output-validation-v15.json').read_text())
    video_hash = qa.sha(args.video)
    assert validation['video_sha256'] == video_hash, 'Output QA belongs to another render'
    assert validation['source_bundle_id'] == source['bundle_id'], 'Source changed since rendered output validation'
    _, paths, _ = qa.discover_inputs()
    paths.update(ROOT / name for name in source['source_sha256'])
    # Keep the current stems for later narration work; the score for the old V15
    # is historical and no longer participates in the active mix.
    for name in ('resources/audio/music-v15r1.wav', 'resources/audio/effects-v15r1.wav',
                 'resources/audio/track-source/mixkit-close-up.mp3'):
        if (ROOT / name).is_file():
            paths.add(ROOT / name)
    for name in ('package.json', 'package-lock.json', 'hyperframes.json', 'README.md', 'AGENTS.md', 'DESIGN.md',
                 'STORYBOARD.md', 'REFERENCE-IMPLEMENTATION.md', 'NARRATION-HANDOFF.md', 'meta.json', '.gitignore'):
        path = ROOT / name
        if path.is_file():
            paths.add(path)
    for path in (ROOT / 'scripts').rglob('*'):
        if path.is_file() and path.suffix in {'.py', '.js', '.mjs', '.sh', '.md', '.json'} and '__pycache__' not in path.parts:
            paths.add(path)
    for path in (ROOT / 'resources').rglob('*'):
        if not path.is_file() or path.suffix.lower() not in {'.md', '.json', '.txt', '.csv', '.mid', '.midi'}:
            continue
        if re.search(r'v(?:[1-9]|1[0-4])(?=\D|$)', path.name, re.I):
            continue
        paths.add(path)
        if path.suffix == '.json':
            for raw in strings(json.loads(path.read_text())):
                if len(raw) > 300 or '\n' in raw or '\0' in raw or raw.startswith(('https:', 'http:')):
                    continue
                # JSON also contains prose; only stat plausible media paths.
                if Path(raw).suffix.lower() not in {'.wav', '.mp3', '.mp4', '.mov', '.webm', '.png', '.jpg', '.woff2', '.mid', '.midi', '.svg'}:
                    continue
                if any(len(part.encode()) > 255 for part in Path(raw).parts):
                    continue
                for candidate in (ROOT / raw, path.parent / raw):
                    candidate = candidate.resolve()
                    if candidate.is_relative_to(ROOT) and candidate.is_file() and 'node_modules' not in candidate.parts:
                        if candidate.suffix.lower() in {'.wav', '.mp3', '.mp4', '.mov', '.webm', '.png', '.jpg', '.woff2', '.mid', '.midi', '.svg'}:
                            paths.add(candidate)
    for folder in ('assets', 'vendor', 'resources'):
        for path in (ROOT / folder).rglob('*'):
            if path.is_file() and (re.search(r'license|notice|ofl', path.name, re.I) or path.name in {'GSAP-README.md', 'GSAP-package.json'}):
                paths.add(path)
    active_reports = {
        'audio-validation-v15r1.json', 'output-validation-v15.json',
        'source-validation-v15.json', 'sampling-v15.json',
        'final-approval-v15r1.json', 'hyperframes-check-focused-v15r1.json',
        'visual-review-v15r1.md',
    }
    for path in (ROOT / 'review').iterdir():
        if not path.is_file() or path.stat().st_size >= 3_000_000:
            continue
        if path.name in active_reports:
            paths.add(path)
        elif path.name.startswith('source-bundle-') and json.loads(path.read_text()).get('bundle_id') == source['bundle_id']:
            paths.add(path)
    approved = ROOT / 'review/final-approval-v15r1.json'
    if approved.is_file():
        approval = json.loads(approved.read_text())
        assert approval.get('video_sha256') == video_hash, 'Final visual approval belongs to another render'
    manifest = {}
    for path in sorted(paths):
        relative = path.relative_to(ROOT)
        assert not path.is_symlink(), f'Symlink would escape archive closure: {relative}'
        assert not any(part in {'node_modules', '.git', '.hyperframes', '__pycache__'} for part in relative.parts)
        assert not path.name.startswith('.env')
        assert path.suffix.lower() not in {'.rar', '.zip', '.exe', '.dll', '.aep', '.mogrt', '.sf2'}
        assert not re.search(r'/assets/mix-v1[0-4]\.wav$', '/' + str(relative))
        assert not (relative.parts[0] == 'review' and path.suffix.lower() in {'.png', '.jpg', '.mp4', '.wav'})
        manifest[str(relative)] = qa.sha(path)
    manifest_path = ROOT / 'review/source-file-manifest-v15r1.json'
    qa.save(manifest_path, {'version': 'V15R1', 'video_sha256': video_hash, 'source_bundle_id': source['bundle_id'], 'files': manifest})
    paths.add(manifest_path)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(args.output, 'w', ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(paths):
                archive.write(path, 'evoquex-hyperframes-v15r1/' + str(path.relative_to(ROOT)))
    with ZipFile(args.output) as archive:
        assert archive.testzip() is None
        for path in paths:
            assert archive.read('evoquex-hyperframes-v15r1/' + str(path.relative_to(ROOT))) == path.read_bytes(), path
    result = {'version': 'V15R1', 'archive': str(args.output), 'sha256': qa.sha(args.output),
              'bytes': args.output.stat().st_size, 'files': len(paths), 'validated_video_sha256': video_hash,
              'source_bundle_id': source['bundle_id'], 'crc_verified': True, 'all_entries_equal_local': True,
              'runtime_dependencies_included': True, 'node_modules_and_frame_dumps_excluded': True,
              'note': 'Prepared source archive; installation/reproduction in isolation is a separate check.'}
    qa.save(ROOT / 'review/package-validation-v15r1.json', result)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
