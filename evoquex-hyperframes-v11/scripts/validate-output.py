"""Validate the actual V11 MP4 and its factual/audio inputs."""
from pathlib import Path
import subprocess,json,hashlib,re
import numpy as np
P=Path(__file__).resolve().parent.parent;video=P/'renders/evoquex-hyperframes-v11.mp4'
q=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]));v=next(x for x in q['streams'] if x['codec_type']=='video');a=next(x for x in q['streams'] if x['codec_type']=='audio')
assert (v['width'],v['height'],v['nb_frames'],v['r_frame_rate'])==(1080,1920,'990','30/1')
assert v['codec_name']=='h264' and v['pix_fmt']=='yuv420p' and v['color_space']=='bt709'
assert abs(float(q['format']['duration'])-33)<.06
assert a['codec_name']=='aac' and a['sample_rate']=='48000' and a['channels']==2
subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(video),'-f','null','-'],capture_output=True,check=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected={'campanha.mp4':'01144794dd01f913af3d6fe1c24563a74ee89461b44289ac4a0dd5534139d335','clevelandia.jpg':'a5bba18170e69a3b9db2203d0babbb39b341217772a1794495718afaa7b331a1','resultados.jpg':'e99bf6462689f5d84b7e47f23af46c9fa60b7dd310f0fb5d9c9b324a90ed0147'}
for name,h in expected.items():assert sha(P/'assets'/name)==h,name
provenance=json.loads((P/'resources/audio-provenance.json').read_text());assert sha(P/'assets/mix-v11.wav')==provenance['output_sha256']
def pcm(path):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(path),'-vn','-ar','48000','-ac','2','-f','f32le','-']),dtype='<f4').reshape(-1,2)
encoded=pcm(video);source=pcm(P/'assets/mix-v11.wav');n=min(len(encoded),len(source));correlation=float(np.corrcoef(encoded[:n].reshape(-1),source[:n].reshape(-1))[0,1]);assert correlation>.98
clipped=int(np.sum(np.abs(encoded)>=1));assert clipped==0
x=subprocess.run(['ffmpeg','-hide_banner','-i',str(video),'-af','loudnorm=I=-16:TP=-1.8:LRA=7:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
levels=json.loads(re.findall(r'\{[^{}]*"input_i"[^{}]*\}',x.stderr,re.S)[-1]);assert float(levels['input_tp'])<0
html=(P/'index.html').read_text();js=(P/'motion.js').read_text();assert 'Danny’s Presentes' in html and '13064' in js and '20981' in js
assert not re.search(r'dany[’\x27]s|dannys\s+presentes',html,re.I)
assert html.count('<video ')==1 and 'muted playsinline data-volume="0"' in html
for x in ['Math.random(','Date.now(','requestAnimationFrame(']:assert x not in js
report={'file':video.name,'engine':'HyperFrames 0.8.162 / HTML, SVG, GSAP 3.14.2','duration':q['format']['duration'],'frames':990,'dimensions':[1080,1920],'fps':30,'video_codec':v['codec_name'],'pixel_format':v['pix_fmt'],'color_space':v['color_space'],'audio_codec':a['codec_name'],'audio_rate':48000,'audio_channels':2,'new_v11_mix_correlation':correlation,'clipped_samples':clipped,'loudness':levels,'full_decode_passed':True,'same_original_media_sha256':expected,'metrics':{'reach':13064,'impressions':20981},'business':'Danny’s Presentes','narration_present':False,'original_footage_playback_count':1,'reference_audio_reused':False,'subjective_listening_performed':False,'bytes':video.stat().st_size,'sha256':sha(video)}
(P/'review/output-validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
