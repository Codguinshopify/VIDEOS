"""Verify permanent original references and usable pack media; no external paths."""
from pathlib import Path
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[2];B=ROOT/'biblioteca'
checks=[]
for rel,key in [('referencias/catalogo.json','references'),('packs/inventario.json','items'),('componentes/catalogo.json','items')]:
    for item in json.loads((B/rel).read_text())[key]:
        f=ROOT/item['path'];assert f.is_file(),str(f)
        assert hashlib.sha256(f.read_bytes()).hexdigest()==item['sha256'],str(f)
        if f.suffix.lower() in ['.mp4','.png','.wav']:
            subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(f),'-f','null','-'],capture_output=True,check=True)
        checks.append({'path':item['path'],'sha256':item['sha256'],'ok':True})
for item in json.loads((B/'hyperframes/catalogo.json').read_text())['items']:
    d=ROOT/item['path'];assert (d/(item['name']+'.html.txt')).is_file();assert (d/'registry-item.json').is_file()
    for name,digest in item['sha256'].items():assert hashlib.sha256((d/name).read_bytes()).hexdigest()==digest,str(d/name)
assert (ROOT/'AGENTS.md').is_file()
report={'ok':True,'media_and_component_checks':checks,'catalogue_sources':len(json.loads((B/'hyperframes/catalogo.json').read_text())['items']),'full_pack_extraction_claimed':False}
(B/'validacao.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'ok':True,'checked_media_and_component_files':len(checks),'catalogue_sources':len(json.loads((B/'hyperframes/catalogo.json').read_text())['items'])}))
