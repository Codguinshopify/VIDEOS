"""Inspect every section, all transitions and every opening frame of the MP4."""
from pathlib import Path
from PIL import Image,ImageDraw
import subprocess,json,sys,hashlib
ROOT=Path(__file__).resolve().parent.parent
video=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'renders/evoquex-hyperframes-v11.mp4')
tag='hf-v11'
video_sha256=hashlib.sha256(video.read_bytes()).hexdigest()
folder=ROOT/'review'/(tag+'-'+video_sha256[:10]);folder.mkdir(exist_ok=True)
def run(*args):subprocess.run(['ffmpeg','-v','error','-y',*map(str,args)],check=True)
def sheets(items,name,cols=6,per=24):
 for start in range(0,len(items),per):
  chunk=items[start:start+per];canvas=Image.new('RGB',(216*cols,412*((len(chunk)+cols-1)//cols)),'#E0E6EE');d=ImageDraw.Draw(canvas)
  for i,(p,label) in enumerate(chunk):
   x=i%cols*216;y=i//cols*412;canvas.paste(Image.open(p).convert('RGB'),(x,y));d.text((x+6,y+391),label,fill='#11132B')
  canvas.save(ROOT/'review'/f'{tag}-{name}-{start//per+1:02d}.jpg',quality=94)
run('-i',video,'-vf','fps=2,scale=216:384',folder/'full-%03d.png')
full=sorted(folder.glob('full-*.png'));sheets([(p,f'{(i+.5)/2:.2f}s') for i,p in enumerate(full)],'full')
run('-i',video,'-frames:v','31','-vf','scale=216:384',folder/'hook-%03d.png')
hook=sorted(folder.glob('hook-*.png'));sheets([(p,f'Opening frame {i}') for i,p in enumerate(hook)],'hook',per=24)
def extract(f,name):
 p=folder/f'{name}-{f:04d}.png';run('-ss',f/30,'-i',video,'-frames:v','1','-vf','scale=216:384',p);return p
cuts=[]
for at in [125,282,432,630,810]:
 for delta in [-1,0,3,6,9,12,15]:
  f=at+delta;cuts.append((extract(f,'cut'),f'Cut {at} +{delta}'))
sheets(cuts,'cuts',cols=7,per=28)
states=[]
for f in [0,8,31,42,68,86,105,125,138,165,200,255,285,305,340,390,420,435,455,471,510,534,540,547,560,580,605,620,645,661,680,705,734,765,810,840,869,900,950,989]:
 states.append((extract(f,'state'),f'State {f}'))
sheets(states,'states')
for name,f in [('hook',85),('production',220),('city',400),('proof',595),('strategy',745),('cta',950)]:
 run('-ss',f/30,'-i',video,'-frames:v','1','-vf','scale=360:640',ROOT/'review'/f'{tag}-phone-{name}.png')
report={'video':video.name,'sha256':video_sha256,'sampling_folder':folder.name,'full_duration_samples':len(full),'opening_frames':len(hook),'transition_samples':len(cuts),'internal_states':len(states),'phone_checks':6,'subjective_audio_playback_available':False}
(ROOT/'review'/f'{tag}-sampling.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
