from pathlib import Path
import subprocess, json, hashlib, wave
import numpy as np
from scipy.signal import butter,sosfilt
root=Path(__file__).resolve().parent.parent
res=root/'resources/audio';rate=48000;length=44;count=rate*length
sources={
 'impact':res/'pack-sources/SFX - Impact 1.wav',
 'swoosh':res/'pack-sources/SFX - Fast Swoosh 1.wav',
 'select':res/'selected-sfx-v15r1/tech-select.wav',
 'slide':res/'selected-sfx-v15r1/tech-slide.wav',
 'click':res/'selected-sfx-v15r1/interface-click.wav',
 'confirm':res/'selected-sfx-v15r1/high-tech-confirmation.wav',
 'metal':res/'selected-sfx-v15r1/metal-sweep.wav'}
cues=[(3.0,'impact',-19),(3.4,'metal',-22),(5.0,'swoosh',-20),(5.7,'impact',-18),(6.27,'slide',-22),(7.76,'swoosh',-18),(8.42,'impact',-17),(8.95,'slide',-23),(9.45,'click',-22),(10.3,'select',-23),(12.3,'slide',-25),(14.74,'swoosh',-18),(15.85,'impact',-18),(16.65,'confirm',-19),(18,'select',-23),(21.75,'metal',-20),(22.65,'impact',-14),(23.48,'swoosh',-22),(25.05,'slide',-23),(28.75,'metal',-19),(29.43,'impact',-18),(32.35,'swoosh',-18),(33.85,'metal',-16),(34.47,'impact',-12),(36.72,'swoosh',-18),(37.7,'impact',-18),(39.55,'select',-21),(41.45,'metal',-17),(42.1,'confirm',-18)]
def decode(path,seconds=None):
 cmd=['ffmpeg','-v','error','-i',str(path)]
 if seconds:cmd+=['-t',str(seconds)]
 cmd+=['-ar',str(rate),'-ac','2','-f','f32le','pipe:1']
 return np.frombuffer(subprocess.run(cmd,check=True,capture_output=True).stdout,dtype='<f4').reshape(-1,2).astype(np.float64)
def wav(path,data):
 with wave.open(str(path),'wb') as w:
  w.setnchannels(2);w.setsampwidth(2);w.setframerate(rate);w.writeframes(np.rint(np.clip(data,-.999,.999)*32767).astype('<i2').tobytes())
music=decode(res/'track-source/mixkit-close-up.mp3',length)
music=np.pad(music[:count],((0,max(0,count-len(music))),(0,0)))
time=np.arange(count)/rate
env=np.interp(time,[0,3,8,15,22,29,34.5,37,41.5,44],[.42,.52,.54,.5,.56,.56,.42,.55,.5,0])
music*=env[:,None]
effects=np.zeros_like(music)
old_hook=decode(res/'effects-v15r1.wav',3)
effects[:len(old_hook)]+=old_hook
manifest=[]
for at,key,db in cues:
 c=decode(sources[key])
 if key in ('impact','click','select','confirm'):c=c[:int(.8*rate)]
 else:c=c[:int(1.35*rate)]
 if not len(c):continue
 sos=butter(2,[60,15000],btype='bandpass',fs=rate,output='sos')
 c=sosfilt(sos,c,axis=0)
 fade=min(len(c)//3,int(.045*rate));c[:fade]*=np.linspace(0,1,fade)[:,None];c[-fade:]*=np.linspace(1,0,fade)[:,None]
 c*=10**(db/20)/max(np.max(np.abs(c)),1e-8)
 begin=int(at*rate);end=min(count,begin+len(c));effects[begin:end]+=c[:end-begin]
 manifest.append({'time':at,'source':str(sources[key].relative_to(root)),'level_dbfs':db})
mix=music+effects
gain=min(1,.88/max(np.max(np.abs(mix)),1e-8))
music*=gain;effects*=gain;mix*=gain
for data,path in [(music,res/'music-v16.wav'),(effects,res/'effects-v16.wav'),(mix,root/'review/audio-premix-v16.wav')]:wav(path,data)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(root/'review/audio-premix-v16.wav'),'-af','loudnorm=I=-16:TP=-2.5:LRA=7','-ar',str(rate),'-ac','2','-c:a','pcm_s16le',str(root/'assets/mix-v16.wav')],check=True)
(root/'resources/audio/cues-v16.json').write_text(json.dumps({'duration':44,'events':manifest,'music':'Mixkit Close Up','no_narration':True},indent=2))
print('audio peaks',float(np.max(np.abs(mix))),len(manifest))
