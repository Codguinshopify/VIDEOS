from pathlib import Path
import json,subprocess,re,hashlib
root=Path(__file__).resolve().parent.parent
video=root/'renders/evoquex-hyperframes-v16.mp4'
def run(*cmd):
 return subprocess.run(cmd,check=True,capture_output=True,text=True)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
probe=json.loads(run('ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)).stdout)
streams=probe['streams'];v=next(s for s in streams if s['codec_type']=='video');a=next(s for s in streams if s['codec_type']=='audio')
duration=float(probe['format']['duration'])
assert v['width']==1080 and v['height']==1920
assert v['r_frame_rate']=='30/1' and abs(duration-44)<.06
assert a['codec_name']=='aac' and int(a['sample_rate']) in (48000,44100)
assert int(v.get('nb_frames',1320))==1320
text=(root/'index.html').read_text()
assert 'DANNY’S' in text
assert not re.search(r'\bDANY(?:[’\x27]S)?\b',text,re.IGNORECASE)
assert 'MAIS DE' in text and '20' in text and 'VISUALIZAÇÕES' in text
assert 'Quem é visto não é lembrado' not in text # quote is split typographically; user-approved words are present below
assert 'QUEM É <strong>VISTO</strong>' in text and 'NÃO É<br><strong>LEMBRADO.' in text
decode=run('ffmpeg','-v','error','-i',str(video),'-f','null','-')
loud=run('ffmpeg','-hide_banner','-i',str(video),'-af','loudnorm=I=-16:TP=-2.5:LRA=7:print_format=json','-f','null','-')
raw=loud.stderr;loudness=json.loads(raw[raw.rfind('{'):raw.rfind('}')+1])
assert -17<float(loudness['input_i'])<-15 and float(loudness['input_tp'])<=-2
black=run('ffmpeg','-hide_banner','-i',str(video),'-vf','blackdetect=d=0.3:pix_th=0.03:pic_th=0.98','-an','-f','null','-')
events=[x for x in black.stderr.splitlines() if 'black_start:' in x]
report={'file':str(video),'sha256':sha(video),'size_bytes':video.stat().st_size,'duration':duration,'video':{'codec':v['codec_name'],'width':v['width'],'height':v['height'],'fps':v['r_frame_rate'],'frames':v.get('nb_frames')},'audio':{'codec':a['codec_name'],'sample_rate':a['sample_rate'],'channels':a['channels'],'lufs':float(loudness['input_i']),'true_peak_db':float(loudness['input_tp'])},'black_intervals':events,'decode_errors':decode.stderr.strip(),'ok':not events and not decode.stderr.strip()}
(root/'review/output-validation-v16.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
assert report['ok']
