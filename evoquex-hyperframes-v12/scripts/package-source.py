from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import json,hashlib
P=Path(__file__).resolve().parent.parent;out=P/'renders/evoquex-hyperframes-v12-projeto.zip';files=set()
for n in ['index.html','style.css','motion.js','DESIGN.md','STORYBOARD.md','REFERENCE-IMPLEMENTATION.md','README.md','AGENTS.md','package.json','package-lock.json','hyperframes.json','meta.json','.gitignore']:files.add(P/n)
for d in ['assets','vendor','scripts','resources']:
 files.update(f for f in (P/d).rglob('*') if f.is_file() and '__pycache__' not in f.parts)
for pat in ['output-validation.json','hf-v12-sampling.json','source-validation.json','final-check.json','motion-review.json','final-review.md','source-reproduction.json','independent-visual-review.md','independent-audio-review.md','audio-validation-v12.json','hf-v12-full-*.jpg','hf-v12-hook-*.jpg','hf-v12-cuts-*.jpg','hf-v12-states-*.jpg','hf-v12-phone-*.png']:
 files.update((P/'review').glob(pat))
files.add(P/'review/animation-map/animation-map.json')
with ZipFile(out,'w',ZIP_DEFLATED,compresslevel=6) as z:
 for f in sorted(files):
  assert not f.name.startswith('.env') and 'node_modules' not in f.parts
  z.write(f,'evoquex-hyperframes-v12/'+f.relative_to(P).as_posix())
with ZipFile(out) as z:
 assert z.testzip() is None
 for n in ['index.html','style.css','motion.js','assets/campanha.mp4','assets/mix-v12.wav','assets/DM-Sans.woff2','vendor/evoquex-v12-effects.js','package-lock.json']:assert z.read('evoquex-hyperframes-v12/'+n)==(P/n).read_bytes()
 assert not any('/review/reference/' in n or '/node_modules/' in n or '/.env' in n for n in z.namelist())
r={'file':out.name,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'crc_verified':True,'files':len(files),'self_contained_assets':True,'reference_video_frames_and_audio_excluded':True,'node_modules_and_secrets_excluded':True}
(P/'review/package-validation.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
