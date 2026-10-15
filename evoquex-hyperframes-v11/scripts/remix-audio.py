"""Recompose existing legal instrumental/effect stems to V11's authored cues."""
from pathlib import Path
import numpy as np,subprocess,wave,json,hashlib
P=Path(__file__).resolve().parent.parent;old=P;rate=48000;n=33*rate
music_path=P/'resources/audio/music-source.wav';fx_path=P/'resources/audio/effects-source.wav'
def read(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-ar','48000','-ac','2','-f','f32le','-']),dtype='<f4').reshape(-1,2)
music=read(music_path)[:n].copy()*.88;source=read(fx_path);fx=np.zeros_like(music)
clips={'hit':source[:int(.29*rate)],'tick':source[int(.4*rate):int(.455*rate)],'sweep':source[int(1.43*rate):int(1.73*rate)]}
# These clips exist in the prior stems. No reference audio or synthetic voice.
cues=[(0,'hit',.5),(1.2,'sweep',.4),(2.45,'sweep',.45),(4.3,'sweep',.6),(5.15,'tick',.4),(9.4,'sweep',.6),(10.6,'sweep',.4),(11.8,'tick',.4),(14.45,'sweep',.6),(15.5,'hit',.55),(17.65,'sweep',.5),(18.4,'hit',.55),(21,'sweep',.55),(21.85,'tick',.4),(24.1,'sweep',.4),(25.65,'hit',.4),(27,'sweep',.5),(28.75,'hit',.5),(29.2,'tick',.35)]
for t,kind,gain in cues:
 a=max(0,int((t-(.17 if kind=='sweep' else 0))*rate));clip=clips[kind]*gain;end=min(n,a+len(clip));fx[a:end]+=clip[:end-a]
fade=np.ones(n);fade[:int(.08*rate)]=np.linspace(.3,1,int(.08*rate));fade[-int(.85*rate):]=np.linspace(1,0,int(.85*rate));mix=(music+fx)*fade[:,None]
raw=P/'review/audio-premaster.wav'
with wave.open(str(raw),'wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(rate);w.writeframes((np.clip(mix,-.98,.98)*32767).astype('<i2').tobytes())
subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-af','loudnorm=I=-16:TP=-1.8:LRA=7','-ar','48000','-c:a','pcm_s16le',str(P/'assets/mix-v11.wav')],check=True)
report={'duration':33,'new_narration_present':False,'rejected_voice_used':False,'original_clip_audio_gain':0,'reference_audio_reused':False,'music':'Existing Evoquex V7 instrumental stem; GeneralUser GS licensed instruments','effects':'Reused isolated hit/tick/sweep samples from existing V7 effects stem','events':[{'time':t,'type':k,'gain':g} for t,k,g in cues],'sources_sha256':{str(p.relative_to(old)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [music_path,fx_path]},'output_sha256':hashlib.sha256((P/'assets/mix-v11.wav').read_bytes()).hexdigest(),'subjective_listening_performed':False}
(P/'resources/audio-provenance.json').write_text(json.dumps(report,indent=2)+'\n');print('33-second real mix produced, 19 synchronized effects, no narration.')
