"""Prepare a real supplied recording with program ducking. Does not synthesize voice.
Usage: python scripts/prepare-voice.py /path/to/narration.wav
Writes review/mix-with-voice.wav for review; does NOT silently switch final HTML.
Before use: measure cues and retime the visuals/effects to the approved recording.
"""
from pathlib import Path
import subprocess,json,sys
P=Path(__file__).resolve().parent.parent
if len(sys.argv)!=2:raise SystemExit(__doc__)
voice=Path(sys.argv[1]).resolve()
if not voice.is_file():raise SystemExit('Real narration file not found; no replacement generated.')
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-of','json',str(voice)]))
duration=float(probe['format']['duration'])
if duration>30:raise SystemExit('Recording exceeds 30s; retime scenes and soundtrack first. No automatic speed-up.')
out=P/'review/mix-with-voice.wav'
subprocess.run(['ffmpeg','-v','error','-y','-i',str(P/'assets/mix-v13.wav'),'-i',str(voice),
 '-filter_complex','[1:a]aresample=48000,apad,atrim=0:30,asplit=2[v][sc];[0:a][sc]sidechaincompress=threshold=0.025:ratio=8:attack=15:release=240[bed];[bed][v]amix=inputs=2:normalize=0,loudnorm=I=-16:TP=-1.8:LRA=7[out]',
 '-map','[out]','-ar','48000','-ac','2',str(out)],check=True)
print('Review mix created. Inspect intelligibility and retime before wiring this real audio into HTML.')
