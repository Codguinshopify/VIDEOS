"""Validate active V15 inputs/MP4 and extract hash-bound review material.

This produces technical evidence, not subjective audiovisual approval. The input
bundle must be frozen immediately before rendering and unchanged afterward.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from fractions import Fraction
import argparse
import hashlib
import json
import math
import re
import subprocess
import unicodedata

ROOT = Path(__file__).resolve().parent.parent
TIMING = ROOT / 'resources/scene-timing-v15.json'
USAGE = ROOT / 'resources/asset-usage-v15.json'
METRIC = '20 mil visualizações de pessoas de Clevelândia'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def save(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')


def run(args, **kwargs):
    return subprocess.run(args, check=True, capture_output=True, **kwargs)


def normalized(text):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', text)).strip()


def compact(text):
    return re.sub(r'\s+', '', normalized(text)).casefold()


class HTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.elements, self.text, self.stack = [], [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        inherited = bool(self.stack and self.stack[-1][1])
        excluded = inherited or tag in {'style', 'script'} or attrs.get('aria-hidden') == 'true'
        label = attrs.get('aria-label')
        if label and not excluded:
            # Clipped duplicates can form one semantic number. Inspect the real
            # render separately; don't mistake three visual slices for three claims.
            self.text.append(label)
        if tag not in {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}:
            self.stack.append((tag, excluded or bool(label)))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                self.stack = self.stack[:index]
                break

    def handle_data(self, value):
        if not (self.stack and self.stack[-1][1]) and value.strip():
            self.text.append(value)


def reference(path_string, owner):
    raw = path_string.strip()
    if not raw or raw.startswith(('#', 'data:', 'blob:')):
        return None
    url = urlsplit(raw)
    assert not url.scheme and not url.netloc, f'Non-local render dependency: {raw}'
    path = (owner.parent / unquote(url.path)).resolve()
    assert path.is_relative_to(ROOT), f'Render input leaves project: {raw}'
    assert path.is_file(), f'Missing file {path} referenced by {owner}'
    return path


def discover_inputs():
    """Resolve HTML, CSS URLs/imports and literal module imports recursively."""
    pending, scanned, edges = [ROOT / 'index.html'], set(), []
    root_parser = None
    while pending:
        owner = pending.pop()
        if owner in scanned:
            continue
        scanned.add(owner)
        if owner.suffix not in {'.html', '.css', '.js', '.mjs', '.svg'}:
            continue
        source = owner.read_text()
        refs = []
        if owner.suffix in {'.html', '.svg'}:
            parser = HTML()
            parser.feed(source)
            if owner.name == 'index.html':
                root_parser = parser
            for _, attrs in parser.elements:
                refs.extend(attrs[k] for k in ('src', 'href', 'xlink:href', 'poster') if attrs.get(k))
        if owner.suffix in {'.html', '.css', '.svg'}:
            refs.extend(s.strip().strip('\"\'') for s in re.findall(r'url\(\s*([^)]*?)\s*\)', source))
            refs.extend(re.findall(r'@import\s+[\"\']([^\"\']+)[\"\']', source))
        if owner.suffix in {'.js', '.mjs'}:
            refs.extend(re.findall(r'(?:from\s+|import\s*\()([\"\'])(\.[^\"\']+)\1', source))
            refs = [r[1] if isinstance(r, tuple) else r for r in refs]
        for ref in refs:
            item = reference(ref, owner)
            if item:
                edges.append({'owner': str(owner.relative_to(ROOT)), 'reference': ref, 'path': str(item.relative_to(ROOT))})
                pending.append(item)
    assert root_parser is not None
    return root_parser, scanned, edges


def timing():
    data = json.loads(TIMING.read_text())
    duration = float(data.get('duration', data.get('duration_seconds', 0)))
    fps = float(data.get('fps', 30))
    scenes = data['scenes']
    if isinstance(scenes, dict):
        scenes = [dict(value, id=key) for key, value in scenes.items()]
    for i, scene in enumerate(scenes):
        scene.setdefault('id', scene.get('name', f'scene-{i + 1}'))
        scene['start'] = float(scene.get('start', scene.get('start_seconds', 0)))
        scene['end'] = float(scene.get('end', scene.get('end_seconds', scene['start'] + scene.get('duration', 0))))
        assert 0 <= scene['start'] < scene['end'] <= duration + .001, scene
    assert duration > 0 and fps == 30
    return data, duration, fps, scenes


def source_report():
    data, duration, fps, scenes = timing()
    parser, paths, edges = discover_inputs()
    text = normalized(' '.join(parser.text))
    packed = compact(text)
    assert compact('Danny’s Presentes') in packed, 'Correct business name missing from DOM text'
    assert compact(METRIC) in packed, 'Exact user-attested views statement missing'
    for phrase in ["Dany’s", "Dany's", 'Dannys Presentes', '20.981', '13.064', 'pessoas únicas', 'pessoas alcançadas', 'impressões']:
        assert compact(phrase) not in packed, f'Wrong spelling/unsupported metric: {phrase}'
    roots = [attrs for _, attrs in parser.elements if attrs.get('data-composition-id')]
    assert any(float(a.get('data-duration', 0)) == duration and float(a.get('data-width', 0)) == 1080
               and float(a.get('data-height', 0)) == 1920 for a in roots), 'Root dimensions/duration differ from scene timing'
    media = []
    for tag, attrs in parser.elements:
        if tag not in {'video', 'audio'}:
            continue
        start, length = float(attrs.get('data-start', 0)), float(attrs.get('data-duration', 0))
        assert 0 <= start < duration and length > 0 and start + length <= duration + .05, attrs
        if tag == 'video':
            assert 'muted' in attrs and float(attrs.get('data-volume', 0)) == 0, f'Uncontrolled source audio: {attrs}'
        media.append({'type': tag, 'id': attrs.get('id'), 'path': attrs.get('src'), 'start': start, 'duration': length})
    assert any(m['type'] == 'audio' for m in media), 'Soundtrack missing'
    assert not any('mix-v14' in str(p) or 'narration' in str(p).lower() or 'kokoro' in str(p).lower() for p in paths)
    paths.update(ROOT / name for name in ('package.json', 'package-lock.json', 'hyperframes.json', 'resources/scene-timing-v15.json', 'resources/briefing-v15.txt'))
    for path in (ROOT / 'resources').rglob('*.json'):
        paths.add(path)
    for name in ('motion.js', 'meta.json'):
        if (ROOT / name).is_file():
            paths.add(ROOT / name)
    audio_provenance = ROOT / 'resources/audio/provenance-v15.json'
    pack_audio = []
    if audio_provenance.is_file():
        audio_data = json.loads(audio_provenance.read_text())
        for name, expected in audio_data.get('source_files', {}).items():
            path = ROOT / name
            assert path.is_file() and sha(path) == expected, f'Pack audio source changed: {name}'
            paths.add(path)
            events = [e for e in audio_data.get('events', []) if e.get('source_path') == name]
            assert events, f'Audio source copied but no production cue uses it: {name}'
            assert all(0 <= e['start'] < e['end'] <= duration + .001 for e in events)
            pack_audio.append({'path': name, 'sha256': expected, 'production_cues': len(events),
                               'events': [e['id'] for e in events]})
        generator = ROOT / 'scripts/build-audio-v15r1.py'
        if generator.is_file():
            paths.add(generator)
    pack_visual = sorted({e['path'] for e in edges if e['path'].startswith('assets/packs/')})
    assert pack_visual, 'No actual pack visual asset dependency in this composition'
    assert pack_audio, 'No actual pack audio source/cue provenance'
    usage = json.loads(USAGE.read_text()) if USAGE.is_file() else None
    live = {str(path.relative_to(ROOT)) for path in paths}
    usage_check = []
    if usage:
        records = usage.get('assets', usage.get('usage', [])) if isinstance(usage, dict) else usage
        for entry in records:
            asset = entry.get('runtime_path', entry.get('asset', entry.get('path', entry.get('file'))))
            if not asset:
                continue
            path = ROOT / asset
            assert path.is_file(), f'Provenance references missing asset: {asset}'
            direct = asset in live
            usage_check.append({'asset': asset, 'direct_runtime_reference': direct,
                                'source': entry.get('source', entry.get('origin')),
                                'role': entry.get('role', entry.get('function')),
                                'needs_generation_provenance': not direct})
    source_hashes = {str(path.relative_to(ROOT)): sha(path) for path in sorted(paths)}
    bundle = hashlib.sha256(json.dumps(source_hashes, sort_keys=True).encode()).hexdigest()
    return {'version': 'V15', 'ok': True, 'bundle_id': bundle, 'source_sha256': source_hashes,
            'duration': duration, 'fps': fps, 'expected_frames': round(duration * fps), 'scenes': scenes,
            'normalized_dom_text': text, 'active_metric': METRIC, 'metric_provenance': 'Explicit user statement in briefing-v15.txt; not independently proved by the historical screenshot.',
            'media': media, 'render_dependencies': edges, 'asset_usage': usage_check,
            'pack_visual_runtime_dependencies': pack_visual, 'pack_audio_generation_inputs': pack_audio,
            'pack_usage_note': 'Runtime references prove dependency use, not aesthetic value. Audio baked into a mix additionally requires generator provenance and decoded waveform validation.',
            'narration_requested_this_stage': False, 'visual_quality_approved_by_this_script': False}


def probe(path):
    return json.loads(run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)], text=True).stdout)


def check_output(video, source):
    import numpy as np
    info = probe(video)
    vs = [s for s in info['streams'] if s['codec_type'] == 'video']
    aas = [s for s in info['streams'] if s['codec_type'] == 'audio']
    assert len(vs) == len(aas) == 1, 'Expected one video stream and one audio stream'
    v, a = vs[0], aas[0]
    assert [v['width'], v['height']] == [1080, 1920]
    assert float(Fraction(v['avg_frame_rate'])) == source['fps']
    assert int(v['nb_frames']) == source['expected_frames']
    assert v['codec_name'] == 'h264' and v['pix_fmt'] == 'yuv420p'
    assert abs(float(info['format']['duration']) - source['duration']) < .06
    assert a['codec_name'] == 'aac' and int(a['sample_rate']) == 48000 and a['channels'] == 2
    run(['ffmpeg', '-v', 'error', '-xerror', '-i', str(video), '-f', 'null', '-'])
    def pcm(path):
        raw = run(['ffmpeg', '-v', 'error', '-i', str(path), '-vn', '-ar', '48000', '-ac', '2', '-f', 'f32le', '-']).stdout
        return np.frombuffer(raw, dtype='<f4').reshape(-1, 2)
    audio = pcm(video)
    clipped = int(np.sum(np.abs(audio) >= 1))
    assert clipped == 0, f'Clipped decoded samples: {clipped}'
    measured = run(['ffmpeg', '-hide_banner', '-i', str(video), '-vn', '-af',
                    'loudnorm=I=-16:TP=-1.8:LRA=7:print_format=json', '-f', 'null', '-'], text=True)
    levels = json.loads(re.findall(r'\{[^{}]*"input_i"[^{}]*\}', measured.stderr, re.S)[-1])
    assert float(levels['input_tp']) < 0
    assert -25 < float(levels['input_i']) < -10, levels
    audio_sources = [m for m in source['media'] if m['type'] == 'audio']
    correlation = None
    if len(audio_sources) == 1 and audio_sources[0]['start'] == 0:
        target = pcm(ROOT / audio_sources[0]['path'])
        count = min(len(audio), len(target))
        assert abs(len(audio) - len(target)) <= 2048
        correlation = float(np.corrcoef(audio[:count].reshape(-1), target[:count].reshape(-1))[0, 1])
        assert correlation > .98, f'Encoded mix differs from input: {correlation}'
    return {'version': 'V15', 'ok': True, 'video_path': str(video), 'video_sha256': sha(video),
            'bytes': video.stat().st_size, 'source_bundle_id': source['bundle_id'], 'source_sha256': source['source_sha256'],
            'duration': float(info['format']['duration']), 'fps': source['fps'], 'frames': int(v['nb_frames']),
            'dimensions': [v['width'], v['height']], 'video_codec': v['codec_name'], 'pixel_format': v['pix_fmt'],
            'color_space': v.get('color_space'), 'audio_codec': a['codec_name'], 'audio_rate': int(a['sample_rate']),
            'audio_channels': a['channels'], 'full_decode_passed': True, 'loudness': levels,
            'clipped_samples': clipped, 'encoded_mix_correlation': correlation,
            'active_metric': METRIC, 'narration_present': False, 'subjective_listening_performed': False,
            'continuous_playback_performed': False, 'visual_quality_approved_by_this_script': False}


def create_samples(video, source, video_hash):
    from PIL import Image, ImageDraw
    import numpy as np
    fps, count = source['fps'], source['expected_frames']
    dest = ROOT / 'review' / ('v15-' + video_hash[:12])
    frames = dest / 'all-frames'
    frames.mkdir(parents=True, exist_ok=True)
    run(['ffmpeg', '-v', 'error', '-y', '-i', str(video), '-vf', 'scale=216:384', '-fps_mode', 'passthrough',
         '-start_number', '0', str(frames / 'frame-%04d.png')])
    assert len(list(frames.glob('frame-*.png'))) == count
    sheet_paths, frame_statistics = [], []
    previous = None
    for index in range(count):
        with Image.open(frames / f'frame-{index:04d}.png') as img:
            pixels = np.asarray(img.convert('RGB'), dtype=np.float32)
        frame_statistics.append({'frame': index, 'time': index / fps, 'mean': float(pixels.mean()),
            'std': float(pixels.std()), 'fraction_near_black': float(np.mean(np.max(pixels, axis=2) < 8)),
            'fraction_near_white': float(np.mean(np.min(pixels, axis=2) > 247)),
            'mean_change_from_previous': float(np.mean(np.abs(pixels - previous))) if previous is not None else None})
        previous = pixels

    def sheets(indices, label):
        for first in range(0, len(indices), 24):
            chunk = indices[first:first + 24]
            canvas = Image.new('RGB', (1296, 410 * math.ceil(len(chunk) / 6)), '#E5E9F1')
            draw = ImageDraw.Draw(canvas)
            for i, frame in enumerate(chunk):
                x, y = i % 6 * 216, i // 6 * 410
                with Image.open(frames / f'frame-{frame:04d}.png') as img:
                    canvas.paste(img.convert('RGB'), (x, y))
                draw.text((x + 5, y + 389), f'f{frame:04d} | {frame / fps:.3f}s', fill='#111827')
            path = dest / f'{label}-{first // 24 + 1:02d}.jpg'
            canvas.save(path, quality=94)
            sheet_paths.append(str(path.relative_to(ROOT)))

    full = sorted(set(range(0, count, round(fps / 2))) | {count - 1})
    opening_end = min(4, source['scenes'][0]['end'])
    opening = list(range(math.ceil(opening_end * fps)))
    sheets(full, 'full')
    sheets(opening, 'opening')
    raw, _, _, scenes = timing()
    windows = []
    for scene in scenes[1:]:
        at = scene['start']
        windows.append({'id': 'transition-' + str(scene['id']), 'start': max(0, at - .55), 'end': min(source['duration'], at + .85)})
    for i, window in enumerate(raw.get('review_windows', [])):
        if isinstance(window, (list, tuple)):
            window = {'start': window[0], 'end': window[1]}
        windows.append({'id': window.get('id', f'critical-{i + 1}'), 'start': float(window['start']), 'end': float(window['end'])})
    for media in source['media']:
        if media['type'] == 'video':
            for label, at in [('start', media['start']), ('end', media['start'] + media['duration'])]:
                windows.append({'id': f'media-{media["id"] or "clip"}-{label}', 'start': max(0, at - .1), 'end': min(source['duration'], at + .2)})
    for i, window in enumerate(windows):
        start, stop = max(0, math.ceil(window['start'] * fps - 1e-7)), min(count, math.ceil(window['end'] * fps - 1e-7))
        indices = list(range(start, stop))
        window.update(first_frame=start, last_frame_inclusive=stop - 1, consecutive_frames=len(indices))
        sheets(indices, f'critical-{i + 1:02d}')
    phone = []
    for scene in scenes:
        at = min(scene['end'] - 1 / fps, scene['start'] + (scene['end'] - scene['start']) * .68)
        frame = round(at * fps)
        name = re.sub(r'[^a-zA-Z0-9_-]', '-', str(scene['id']))
        path = dest / f'phone-{name}.png'
        run(['ffmpeg', '-v', 'error', '-y', '-i', str(video), '-vf', f'select=eq(n\\,{frame}),scale=360:640', '-frames:v', '1', str(path)])
        phone.append({'scene': scene['id'], 'frame': frame, 'path': str(path.relative_to(ROOT))})
    save(dest / 'frame-statistics.json', frame_statistics)
    report = {'video_sha256': video_hash, 'source_bundle_id': source['bundle_id'], 'decoded_frames': count,
              'all_frames_folder': str(frames.relative_to(ROOT)), 'full_duration_samples': len(full),
              'opening_consecutive_frames': len(opening), 'windows': windows, 'sheets': sheet_paths,
              'phone_checks': phone, 'statistics': str((dest / 'frame-statistics.json').relative_to(ROOT)),
              'near_uniform_frame_candidates': [s['frame'] for s in frame_statistics if s['std'] < 3],
              'statistics_are_review_prompts_not_automatic_visual_failures': True,
              'subjective_listening_performed': False, 'continuous_playback_performed': False,
              'visual_inspection_status': 'Frames extracted; human/model image inspection must be recorded separately.'}
    save(dest / 'sampling.json', report)
    save(ROOT / 'review/sampling-v15.json', report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video', type=Path)
    parser.add_argument('--freeze', action='store_true', help='Write immutable input bundle immediately before rendering')
    parser.add_argument('--bundle', type=Path, help='Previously frozen input bundle required for output checks')
    parser.add_argument('--samples', action='store_true')
    args = parser.parse_args()
    source = source_report()
    save(ROOT / 'review/source-validation-v15.json', source)
    if args.freeze:
        bundle_path = ROOT / 'review' / f'source-bundle-{source["bundle_id"][:16]}.json'
        save(bundle_path, source)
        print(json.dumps({'ok': True, 'bundle': str(bundle_path), 'bundle_id': source['bundle_id']}))
    if args.video:
        assert args.bundle, '--bundle frozen immediately before render is required'
        prior = json.loads(args.bundle.read_text())
        assert prior['bundle_id'] == source['bundle_id'], 'Source bundle changed after freeze; regenerate render and freeze'
        report = check_output(args.video.resolve(), source)
        save(ROOT / 'review/output-validation-v15.json', report)
        if args.samples:
            create_samples(args.video.resolve(), source, report['video_sha256'])
        print(json.dumps({k: report[k] for k in ('ok', 'video_sha256', 'source_bundle_id', 'duration', 'frames', 'loudness')}, ensure_ascii=False))
    elif not args.freeze:
        print(json.dumps({'ok': True, 'duration': source['duration'], 'dependencies': len(source['render_dependencies']), 'bundle_id': source['bundle_id']}))


if __name__ == '__main__':
    main()
