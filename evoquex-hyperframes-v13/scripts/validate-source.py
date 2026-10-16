"""Resolve V13 render dependencies and validate protected copy/source contracts."""
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


def protected_hook_contract(contract):
    protected = contract.get('protected_hook') if isinstance(contract, dict) else None
    if not protected:
        return {'present': False, 'validated': False}
    assert protected['duration_seconds'] == 4 and protected['frames'] == 120
    baseline = (P / protected['baseline_path']).resolve()
    if not all((baseline / name).is_file() for name in ['index.html', 'style.css', 'motion.js']):
        return {'present': True, 'validated': False, 'baseline_available': False,
                'reason': 'Protected baseline source is not available in this checkout; no hook identity claimed.'}
    baseline_html = (baseline / 'index.html').read_text()
    baseline_css = (baseline / 'style.css').read_text()
    baseline_js = (baseline / 'motion.js').read_text()
    before_middle = re.split(r'<div\b[^>]*\bid=[\"\x27]middle-mask[\"\x27]', baseline_html, maxsplit=1)[0]
    assert before_middle != baseline_html, 'Baseline middle-mask boundary missing'
    expected_css = baseline_css.split('/* One physical track', 1)[0] + '\n.question-top{color:var(--red)}\n'
    expected_js = baseline_js.split('// LOCAL:', 1)[0]
    digest = lambda value: hashlib.sha256(value.encode()).hexdigest()
    assert digest(before_middle) == protected['html_prefix_sha256'], 'Baseline hook HTML changed since contract'
    assert digest(expected_css) == protected['css_prefix_sha256'], 'Baseline hook CSS changed since contract'
    assert digest(expected_js) == protected['js_prefix_sha256'], 'Baseline hook JS changed since contract'

    def hook_section(html):
        cleaned = re.sub(r'\sdata-hf-id=[\"\x27][^\"\x27]*[\"\x27]', '', html)
        cleaned = cleaned.replace('evoquex-hf-v13', 'evoquex-hf-v12')
        match = re.search(r'<section\b[^>]*\bid=[\"\x27]hook[\"\x27][^>]*>.*?</section>', cleaned, re.S)
        assert match, 'Protected hook section missing'
        return match.group(0).strip()

    actual_html = hook_section((P / 'index.html').read_text())
    expected_html = hook_section(baseline_html)
    assert actual_html == expected_html, 'Protected hook section changed'
    actual_css = (P / 'style.css').read_text().split('/* V13:', 1)[0].strip()
    assert actual_css == expected_css.strip(), 'Protected hook CSS prefix changed'
    actual_js = (P / 'motion.js').read_text().split('// V13:', 1)[0]
    actual_js = actual_js.replace('evoquex-hf-v13', 'evoquex-hf-v12').strip()
    assert actual_js == expected_js.strip(), 'Protected hook JS prefix changed'
    return {'present': True, 'validated': True, 'baseline_available': True,
            'baseline': str(baseline), 'interval': '[0,4)', 'frames': 120,
            'html_hook_section_equal': True, 'css_prefix_equal': True, 'js_prefix_equal': True,
            'normalized_hook_section_sha256': digest(actual_html),
            'normalized_css_prefix_sha256': digest(actual_css),
            'normalized_js_prefix_sha256': digest(actual_js),
            'normalization': 'Ignore Studio data-hf-id, surrounding whitespace, added head scripts and V13 composition-id rename.',
            'visual_pixel_identity_verified_here': False}


class SourceHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.text = []
        self.skip = []
        self.inline_styles = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if tag in ('script', 'style'):
            self.skip.append(tag)
        if attrs.get('style'):
            self.inline_styles.append(attrs['style'])

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
    assert not url.scheme and not url.netloc, f'External runtime reference: {ref}'
    assert not ref.startswith('//'), ref
    local = (owner.parent / unquote(url.path)).resolve()
    assert local.is_relative_to(P.resolve()), f'Render reference escapes composition: {ref}'
    assert local.is_file(), f'Missing runtime reference in {owner.name}: {ref}'
    return local


def copy_contract(parser, text):
    path = P / 'resources/copy-contract.json'
    if not path.exists():
        return {'present': False, 'validated': False, 'reason': 'Contract not created yet.'}
    contract = json.loads(path.read_text())
    actual = compact(text)
    required = contract if isinstance(contract, list) else next(
        (contract[k] for k in ('required_text', 'phrases', 'texts', 'expected_text', 'expected_phrases')
         if k in contract), [])
    if isinstance(required, dict):
        required = list(required.values())
    assert isinstance(required, list), 'Copy contract text list required'
    checked = []
    for item in required:
        if isinstance(item, dict):
            value = item.get('text', item.get('phrase', item.get('value')))
        else:
            value = item
        assert isinstance(value, str), f'Unsupported copy contract item: {item}'
        assert compact(value) in actual, f'Missing protected copy: {value}'
        checked.append(value)
    forbidden = contract.get('forbidden_text', []) if isinstance(contract, dict) else []
    for value in forbidden:
        assert compact(value) not in actual, f'Forbidden copy present: {value}'
    if isinstance(contract, dict):
        expected_hash = contract.get('normalized_text_sha256', contract.get('baseline_text_sha256'))
        if expected_hash:
            assert hashlib.sha256(normalize(text).encode()).hexdigest() == expected_hash, 'Normalized DOM text differs from contract'
        expected_fragments = contract.get('text_fragments')
        if expected_fragments is not None:
            assert sorted(map(normalize, parser.text)) == sorted(map(normalize, expected_fragments)), 'DOM text fragments changed'
    return {'present': True, 'validated': True, 'contract_sha256': sha(path),
            'required_phrases_checked': checked, 'forbidden_phrases_checked': forbidden,
            'normalized_dom_text_sha256': hashlib.sha256(normalize(text).encode()).hexdigest(),
            'protected_hook': protected_hook_contract(contract),
            'scope': 'Static DOM copy and optional explicit full-text/fragment contract; dynamic setters also require contract/hook review.'}


def validate_source(write_report=True):
    html = (P / 'index.html').read_text()
    js = (P / 'motion.js').read_text()
    parser = SourceHTML()
    parser.feed(html)
    text = normalize(' '.join(parser.text))
    refs = []
    owners = {P / 'index.html'}
    for tag, attrs in parser.elements:
        for key in ('src', 'href', 'xlink:href', 'poster'):
            if attrs.get(key):
                local = resolve_reference(attrs[key], P / 'index.html')
                if local:
                    refs.append({'owner': 'index.html', 'ref': attrs[key], 'path': local.relative_to(P).as_posix()})
                    if local.suffix == '.css':
                        owners.add(local)
        if attrs.get('srcset'):
            for candidate in attrs['srcset'].split(','):
                value = candidate.strip().split()[0]
                local = resolve_reference(value, P / 'index.html')
                if local:
                    refs.append({'owner': 'index.html', 'ref': value, 'path': local.relative_to(P).as_posix()})
    scanned = set()
    while owners - scanned:
        owner = sorted(owners - scanned)[0]
        scanned.add(owner)
        body = owner.read_text()
        for raw in re.findall(r'url\(\s*([^)]+?)\s*\)', body):
            ref = raw.strip().strip('\"\'')
            local = resolve_reference(ref, owner)
            if local:
                refs.append({'owner': owner.relative_to(P).as_posix(), 'ref': ref, 'path': local.relative_to(P).as_posix()})
                if local.suffix == '.css':
                    owners.add(local)
    root = [attrs for _, attrs in parser.elements if attrs.get('data-composition-id') == 'evoquex-hf-v13']
    assert len(root) == 1, 'V13 root composition missing or duplicated'
    for key, expected in [('data-duration', 30), ('data-width', 1080), ('data-height', 1920), ('data-fps', 30)]:
        assert float(root[0][key]) == expected, (key, root[0].get(key))
    assert any(attrs.get('id') == 'motion-world' for _, attrs in parser.elements), 'Shared motion world missing'
    videos = [attrs for tag, attrs in parser.elements if tag == 'video']
    assert len(videos) == 1 and videos[0].get('id') == 'real-film'
    film = videos[0]
    assert float(film['data-start']) == 8.1 and abs(float(film['data-duration']) - 5.06) < .001
    assert film.get('data-volume') == '0' and 'muted' in film and 'playsinline' in film
    assert film.get('src') == 'assets/campanha.mp4'
    assert any(tag == 'image' and attrs.get('href', attrs.get('xlink:href')) == 'assets/clevelandia.jpg'
               for tag, attrs in parser.elements), 'Real city image missing from SVG mask'
    proofs = [attrs for tag, attrs in parser.elements if tag == 'div' and 'paper-piece' in attrs.get('class', '').split()]
    assert len(proofs) == 3, f'Expected three complementary original-proof panels, got {len(proofs)}'
    proof_images = [attrs for tag, attrs in parser.elements if tag == 'img' and attrs.get('src') == 'assets/resultados.jpg']
    assert not proof_images, 'Proof must use complementary CSS-background panels, not duplicate discovered img media'
    style_text = '\n'.join(owner.read_text() for owner in scanned if owner.suffix == '.css')
    assert re.search(r'background(?:-image)?\s*:[^;}]*url\(\s*[\"\x27]?assets/resultados\.jpg', style_text), 'Original proof CSS background missing'
    assert 'Danny’sPresentes' in compact(text), 'Incorrect/missing business name'
    assert not re.search(r'dany[’\x27]s|dannys\s*presentes', compact(text), re.I)
    assert '13.064' in compact(text) and '20.981' in compact(text)
    assert 'Luciane' not in text, 'Disabled case must not be rendered'
    audio = [attrs for tag, attrs in parser.elements if tag == 'audio']
    assert len(audio) == 1 and audio[0].get('src') == 'assets/mix-v13.wav'
    assert float(audio[0].get('data-duration', 0)) == 30
    assert 'narration.wav' not in html and 'Kokoro' not in html
    for forbidden in ['Math.random(', 'Date.now(', 'requestAnimationFrame(', 'setInterval(']:
        assert forbidden not in js, f'Non-deterministic animation: {forbidden}'
    assert 'evoquex-hf-v13' in html
    assert (P / 'vendor/MotionPathPlugin.min.js').is_file()
    assert 'MotionPathPlugin' in html or 'MotionPathPlugin' in js
    kit = P / 'vendor/evoquex-v12-effects.js'
    shared = P.parent / 'biblioteca/componentes/evoquex-v12-effects.js'
    same = sha(kit) == sha(shared) if shared.is_file() else None
    if same is not None:
        assert same, 'Preserved V12 helper differs from shared source'
    assert (P / 'vendor/evoquex-v13-motion.js').is_file()
    sources = ['index.html', 'style.css', 'motion.js', 'vendor/evoquex-v12-effects.js',
               'vendor/evoquex-v13-motion.js', 'vendor/MotionPathPlugin.min.js',
               'package.json', 'package-lock.json', 'hyperframes.json', 'meta.json']
    contract = copy_contract(parser, text)
    hook_manifests = []
    for name in ['resources/hook-contract.json', 'resources/hook-preservation-manifest.json', 'resources/hook-preservation.json']:
        if (P / name).is_file():
            hook_manifests.append({'file': name, 'sha256': sha(P / name)})
    report = {'ok': True, 'version': 'V13', 'duration_seconds': 30, 'expected_frames': 900,
              'local_refs_resolved': refs, 'no_external_assets': True,
              'motion_kit_matches_permanent_library': same,
              'source_sha256': {name: sha(P / name) for name in sources},
              'copy_contract': contract, 'hook_manifest_files': hook_manifests,
              'hook_visual_identity_checked_here': False,
              'normalized_dom_text': text, 'original_footage_plays_once': True,
              'original_footage_audio_muted': True, 'original_proof_complementary_panels': len(proofs),
              'original_proof_img_elements': len(proof_images),
              'voice_file_not_referenced': True, 'voice_windows': 'resources/voice-cues.json'}
    if write_report:
        (P / 'review').mkdir(exist_ok=True)
        (P / 'review/source-validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return report


if __name__ == '__main__':
    result = validate_source()
    print(json.dumps({'ok': result['ok'], 'local_refs': len(result['local_refs_resolved']),
                      'copy_contract': result['copy_contract']['validated']}, ensure_ascii=False))
