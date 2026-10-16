"""Validate V14 render inputs against the active user-attested facts and timing."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import hashlib, json, re, unicodedata

P = Path(__file__).resolve().parent.parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def normalize(text):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', text)).strip()


def compact(text):
    return re.sub(r'\s+', '', normalize(text))


class SourceHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.elements, self.text, self.skip = [], [], []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))
        if tag in ('script', 'style'):
            self.skip.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag in ('script', 'style'):
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if self.skip and self.skip[-1] == tag:
            self.skip.pop()

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.text.append(data)


def resolve_reference(ref, owner):
    ref = ref.strip()
    if not ref or ref.startswith(('#', 'data:', 'blob:')):
        return None
    url = urlsplit(ref)
    assert not url.scheme and not url.netloc and not ref.startswith('//'), f'External runtime asset: {ref}'
    local = (owner.parent / unquote(url.path)).resolve()
    assert local.is_relative_to(P.resolve()), f'Render dependency escapes project: {ref}'
    assert local.is_file(), f'Missing dependency from {owner.name}: {ref}'
    return local


def discover_render_inputs():
    html_path = P / 'index.html'
    parser = SourceHTML()
    parser.feed(html_path.read_text())
    refs = []
    css_owners = set()
    for _, attrs in parser.elements:
        for key in ('src', 'href', 'xlink:href', 'poster'):
            if attrs.get(key):
                path = resolve_reference(attrs[key], html_path)
                if path:
                    refs.append({'owner': 'index.html', 'reference': attrs[key], 'path': path.relative_to(P).as_posix()})
                    if path.suffix == '.css':
                        css_owners.add(path)
    scanned = set()
    while css_owners - scanned:
        owner = sorted(css_owners - scanned)[0]
        scanned.add(owner)
        for raw in re.findall(r'url\(\s*([^)]+?)\s*\)', owner.read_text()):
            ref = raw.strip().strip('\"\'')
            path = resolve_reference(ref, owner)
            if path:
                refs.append({'owner': owner.relative_to(P).as_posix(), 'reference': ref, 'path': path.relative_to(P).as_posix()})
                if path.suffix == '.css':
                    css_owners.add(path)
    return parser, refs, scanned


def union_duration(intervals):
    intervals = sorted(intervals)
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(end, merged[-1][1])
        else:
            merged.append([start, end])
    return sum(end - start for start, end in merged), merged


def validate_source(write_report=True):
    config = json.loads((P / 'resources/qa-contract-v14.json').read_text())
    timing = json.loads((P / config['timing_source']).read_text())
    facts_path = P / config['facts_source']
    facts = json.loads(facts_path.read_text())
    metric = facts['active_metric']
    assert metric['value'] == 20000 and metric['unit'] == 'visualizações'
    assert metric['source_type'] == 'explicit_user_attestation'
    assert metric['display'] == config['active_metric']
    assert metric['unique_people_claimed'] is False
    assert metric['independently_documented_by_old_screenshot'] is False
    brief = P / 'resources' / metric['source']
    assert brief.is_file() and sha(brief) == metric['brief_sha256'], 'Metric source briefing hash differs'
    assert timing['duration'] == config['duration_seconds'] and timing['fps'] == config['fps']
    assert round(timing['duration'] * timing['fps']) == config['expected_frames']
    parser, refs, css_files = discover_render_inputs()
    html = (P / 'index.html').read_text()
    js = (P / 'motion.js').read_text()
    text = normalize(' '.join(parser.text))
    packed = compact(text)
    roots = [attrs for _, attrs in parser.elements if attrs.get('data-composition-id') == config['composition_id']]
    assert len(roots) == 1, 'V14 root composition missing or duplicated'
    for key, expected in [('data-duration', config['duration_seconds']), ('data-width', config['dimensions'][0]),
                          ('data-height', config['dimensions'][1]), ('data-fps', config['fps'])]:
        assert float(roots[0][key]) == expected, (key, roots[0].get(key))
    assert compact(facts['business_name']) in packed
    assert compact(metric['display']) in packed, 'Active views statement missing or changed'
    assert not re.search(r'dany[’\x27]s|dannys\s*presentes', packed, re.I)
    for forbidden in ['20.981', '20981', '13.064', '13064', 'impressões', 'pessoas alcançadas', '20 mil pessoas únicas', 'Luciane']:
        assert compact(forbidden).casefold() not in packed.casefold(), f'Inactive/unsupported copy: {forbidden}'
    for forbidden in ['reach:13064', 'impressions:20981', 'Math.random(', 'Date.now(', 'requestAnimationFrame(', 'setInterval(']:
        assert forbidden not in js, f'Unsupported/non-deterministic source: {forbidden}'
    assert not any('resultados.jpg' in item['path'] for item in refs), 'Old screenshot is not evidence of active views'
    videos = [attrs for tag, attrs in parser.elements if tag == 'video']
    assert videos, 'Real campaign excerpt missing'
    intervals = []
    clips = []
    for attrs in videos:
        assert 'muted' in attrs and 'playsinline' in attrs and float(attrs.get('data-volume', -1)) == 0
        start, duration = float(attrs['data-start']), float(attrs['data-duration'])
        assert duration > 0 and duration <= config['maximum_real_footage_union_seconds']
        intervals.append((start, start + duration))
        clips.append({'id': attrs.get('id'), 'source': attrs.get('src'), 'start': start, 'duration': duration, 'audio_gain': 0})
    excerpt_duration, merged = union_duration(intervals)
    assert excerpt_duration <= config['maximum_real_footage_union_seconds'] + .001
    planned = config.get('planned_real_footage_window')
    if planned:
        assert len(merged) == 1 and abs(merged[0][0] - planned[0]) < .034 and abs(merged[0][1] - planned[1]) < .034
    slit = next((attrs for tag, attrs in parser.elements if tag.lower() == 'clippath' and attrs.get('id') == 'film-slit'), None)
    slat_rects = [attrs for tag, attrs in parser.elements if tag == 'rect' and attrs.get('id', '').startswith('slit-')]
    assert slit is not None and len(slat_rects) == config['planned_slats'], 'Three-lamella film mask missing'
    assert all(float(attrs.get('height', -1)) == 0 for attrs in slat_rects), 'Slat HTML initial state must be closed to prevent the first active-frame flash'
    audio = [attrs for tag, attrs in parser.elements if tag == 'audio']
    assert len(audio) == 1 and audio[0].get('src') == 'assets/mix-v14.wav'
    assert float(audio[0].get('data-duration', 0)) == timing['duration']
    assert 'narration.wav' not in html
    paths = {'index.html', 'style.css', 'motion.js', 'package.json', 'package-lock.json', 'hyperframes.json', 'meta.json'}
    paths.update(item['path'] for item in refs)
    report = {'ok': True, 'version': 'V14', 'duration_seconds': timing['duration'], 'expected_frames': config['expected_frames'],
              'local_refs_resolved': refs, 'no_external_assets': True,
              'source_sha256': {name: sha(P / name) for name in sorted(paths)},
              'active_metric': metric, 'metric_facts_file_sha256': sha(facts_path),
              'metric_independently_verified': False, 'old_screenshot_not_referenced': True,
              'normalized_dom_text': text, 'real_film_clips': clips,
              'normalized_unique_footage_intervals': merged, 'unique_footage_union_seconds': excerpt_duration,
              'simultaneous_slat_instances_count_as_one_excerpt': True, 'film_mask_slats': len(slat_rects),
              'film_mask_initial_heights': [float(attrs['height']) for attrs in slat_rects],
              'hook_pixel_identity_required': False, 'runtime_watermark_inspection_pending': True,
              'subjective_listening_performed': False, 'continuous_playback_performed': False}
    if write_report:
        (P / 'review').mkdir(exist_ok=True)
        (P / 'review/source-validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return report


if __name__ == '__main__':
    result = validate_source()
    print(json.dumps({'ok': result['ok'], 'local_refs': len(result['local_refs_resolved']),
                      'unique_footage_seconds': result['unique_footage_union_seconds']}, ensure_ascii=False))
