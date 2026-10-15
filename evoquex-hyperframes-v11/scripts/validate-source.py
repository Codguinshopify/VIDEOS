"""Resolve actual render dependencies and protect original factual/source content."""
from pathlib import Path
import json,hashlib,re
P=Path(__file__).resolve().parent.parent
html=(P/'index.html').read_text();refs=re.findall(r'(?:src|href)="([^"#]+)"',html)
for ref in refs:
    assert not re.match(r'https?://',ref),ref
    assert (P/ref).is_file(),ref
assert not re.search(r'Dany[’\x27]s|Dannys Presentes',html,re.I)
assert html.count('<video ')==1 and 'muted playsinline data-volume="0"' in html
assert 'Danny’s Presentes' in html and '13.064' in html and '20.981' in html
assert 'narration.wav' not in html
sources=['index.html','style.css','motion.js','vendor/evoquex-motion-kit.js','package-lock.json','DESIGN.md','STORYBOARD.md']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
shared=P.parent/'biblioteca/componentes/motion-kit.js'
same=(sha(shared)==sha(P/'vendor/evoquex-motion-kit.js')) if shared.exists() else None
if same is not None:assert same
report={'ok':True,'local_refs_resolved':refs,'no_external_assets':True,'motion_kit_matches_permanent_library':same,'source_sha256':{n:sha(P/n) for n in sources},'original_footage_plays_once':True,'voice_file_not_referenced':True,'voice_windows':'resources/voice-cues.json'}
(P/'review').mkdir(exist_ok=True)
(P/'review/source-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'ok':True,'local_refs':len(refs),'hashed_source_files':len(sources)}))
