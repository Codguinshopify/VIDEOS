from pathlib import Path
import subprocess,json,numpy as np,sherpa_onnx,sys
p=Path(__file__).resolve().parent.parent;ref=Path(sys.argv[1]) if len(sys.argv)>1 else None
if ref is None:raise SystemExit('Usage: analyze-reference.py /path/to/reference.mp4 (reference not bundled)')
a=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(ref),'-vn','-ar','16000','-ac','1','-f','f32le','-']),dtype='<f4')
m=Path('/workspace/.voice-models/sherpa-onnx-whisper-base')
r=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=str(m/'base-encoder.onnx'),decoder=str(m/'base-decoder.onnx'),tokens=str(m/'base-tokens.txt'),language='pt',task='transcribe',num_threads=2)
rows=[]
for start in range(0,int(np.ceil(len(a)/16000)),10):
 end=min(start+10,len(a)/16000)
 s=r.create_stream();s.accept_waveform(16000,a[int(start*16000):int(end*16000)]);r.decode_stream(s);row={'start':start,'end':end,'recognized':s.result.text};rows.append(row);print(json.dumps(row,ensure_ascii=False),flush=True)
out=p/'review/reference'/ref.parent.name;out.mkdir(parents=True,exist_ok=True)
(out/'audio-analysis.json').write_text(json.dumps({'method':'Whisper base transcription and RMS; no subjective playback','rows':rows,'rms_100ms':[float(np.sqrt(np.mean(a[i:i+1600]**2))) for i in range(0,len(a),1600)],'reference_audio_reused':False},indent=2,ensure_ascii=False)+'\n')
