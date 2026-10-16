"""Package only active V14 sources/media and compact QA, excluding old projects and frame dumps."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import importlib.util, json, hashlib, re

P = Path(__file__).resolve().parent.parent
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('active_render_inputs', P / 'scripts/validate-source.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _, references, _ = module.discover_render_inputs()
    out = P / 'renders/evoquex-hyperframes-v14-projeto.zip'
    out.parent.mkdir(exist_ok=True)
    active_video_sha256 = sha(P / 'renders/evoquex-hyperframes-v14.mp4')
    for report_name, hash_key in [('output-validation.json', 'sha256'), ('final-approval-v14.json', 'video_sha256')]:
        report = json.loads((P / 'review' / report_name).read_text())
        assert report[hash_key] == active_video_sha256, f'Stale final report: {report_name}'
    files = set()
    essential = ['index.html', 'style.css', 'motion.js', 'DESIGN.md', 'STORYBOARD.md',
                 'REFERENCE-IMPLEMENTATION.md', 'README.md', 'AGENTS.md', 'package.json',
                 'package-lock.json', 'hyperframes.json', 'meta.json', '.gitignore']
    for name in essential:
        assert (P / name).is_file(), f'Required source missing: {name}'
        files.add(P / name)
    files.update(P / item['path'] for item in references)
    for name in ['assets/DM-Sans-OFL.txt', 'assets/Lucide-LICENSE.txt', 'vendor/GSAP-README.md', 'vendor/GSAP-package.json']:
        if (P / name).is_file():
            files.add(P / name)
    for path in (P / 'scripts').rglob('*'):
        if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc' and path.name != 'analyze-reference.py':
            files.add(path)
    historical = re.compile(r'v(?:[1-9]|1[0-3])(?=\D|$)', re.I)
    for path in (P / 'resources').rglob('*'):
        if not path.is_file() or '__pycache__' in path.parts or path.suffix == '.pyc':
            continue
        if historical.search(path.name):
            continue
        if path.name == 'SOURCES.json' and path.parent == P / 'resources':
            # A copied global manifest described earlier productions; active provenance lives under audio/.
            if not re.search(r'V14|v14', path.read_text()):
                continue
        files.add(path)
    allowed_review = {'output-validation.json', 'source-validation.json', 'final-check.json', 'native-check-final.json', 'final-review.md',
                      'source-reproduction.json', 'studio-readiness.json', 'independent-motion-review-final.md',
                      'director-motion-review-final.md', 'independent-visual-review-final.md',
                      'independent-audio-review-final.md', 'source-file-sha256-final.json'}
    for path in (P / 'review').iterdir():
        if not path.is_file() or path.suffix not in {'.json', '.csv', '.md'}:
            continue
        if any(token in path.name.lower() for token in ['first', 'second', 'preflight', 'premaster', 'mastering', 'partial', 'legacy-prune']):
            continue
        if 'v14' in path.name.lower() or path.name in allowed_review:
            files.add(path)
    animation_map = P / 'review/animation-map/animation-map.json'
    if animation_map.is_file():
        files.add(animation_map)
    manifest = {path.relative_to(P).as_posix(): sha(path) for path in sorted(files)}
    manifest_file = P / 'review/source-file-sha256.json'
    manifest_file.parent.mkdir(exist_ok=True)
    manifest_file.write_text(json.dumps({'version': 'V14', 'files': manifest}, indent=2) + '\n')
    files.add(manifest_file)
    with ZipFile(out, 'w', ZIP_DEFLATED, compresslevel=6) as archive:
        for path in sorted(files):
            relative = path.relative_to(P)
            assert not path.name.startswith('.env') and 'node_modules' not in path.parts
            assert not any(part in {'reference', 'reference-frames', 'references'} for part in relative.parts), relative
            assert not (relative.parts[0] == 'review' and path.suffix in {'.png', '.jpg', '.mp4', '.wav'}), relative
            assert path.suffix not in {'.exe', '.dll'}, relative
            archive.write(path, 'evoquex-hyperframes-v14/' + relative.as_posix())
    with ZipFile(out) as archive:
        assert archive.testzip() is None
        for name in ['index.html', 'style.css', 'motion.js', 'assets/mix-v14.wav', 'assets/DM-Sans.woff2',
                     'vendor/evoquex-v14-motion.js', 'package-lock.json', 'resources/case-facts-v14.json']:
            assert archive.read('evoquex-hyperframes-v14/' + name) == (P / name).read_bytes()
        for path in files:
            assert archive.read('evoquex-hyperframes-v14/' + path.relative_to(P).as_posix()) == path.read_bytes(), f'ZIP/local bytes differ: {path}'
        names = archive.namelist()
        assert not any('/node_modules/' in name or '/.env' in name for name in names)
        assert not any(re.search(r'/assets/(?:mix-v1[0-3]\.wav|resultados\.jpg|poster-hook-end\.jpg)', name) for name in names)
        assert not any('/review/' in name and name.endswith(('.png', '.jpg', '.mp4', '.wav')) for name in names)
    report = {'version': 'V14', 'file': out.name, 'sha256': sha(out), 'bytes': out.stat().st_size,
              'crc_verified': True, 'all_selected_entries_match_local_bytes': True, 'validated_final_video_sha256': active_video_sha256, 'files': len(files), 'self_contained_active_render_assets': True,
              'source_hash_manifest': 'review/source-file-sha256.json', 'review_frame_dumps_excluded': True,
              'historical_briefings_and_unused_media_excluded': True, 'comparison_renders_excluded': True,
              'node_modules_and_secrets_excluded': True, 'delivery_to_user': 'MP4 only; this ZIP is an internal source backup.'}
    (P / 'review/package-validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
