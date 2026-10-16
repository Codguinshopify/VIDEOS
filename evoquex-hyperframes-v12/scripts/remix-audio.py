"""Reproducible 30 s V12 score edit: existing legal stems only, no TTS.

Requires the already available NumPy + FFmpeg. Does not call a network service.
The sample transformations below are tape-speed/reverse/envelope/pan edits of
real PCM in resources/audio, not references to absent effects or voice files.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import wave
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
RATE = 48000
DURATION = 30
N = RATE * DURATION
T = np.arange(N, dtype=np.float64) / RATE
RES = ROOT / 'resources' / 'audio'
REVIEW = ROOT / 'review'
ASSETS = ROOT / 'assets'
for folder in [RES, REVIEW, ASSETS]:
    folder.mkdir(parents=True, exist_ok=True)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def decode(path):
    raw = subprocess.check_output(['ffmpeg','-v','error','-i',str(path),
        '-ar',str(RATE),'-ac','2','-f','f32le','-'])
    return np.frombuffer(raw, dtype='<f4').reshape(-1,2).astype(np.float64)

def write(path, data):
    assert len(data) == N
    assert np.isfinite(data).all()
    assert np.max(np.abs(data)) < 1, 'Premaster clipping; lower linear gain.'
    with wave.open(str(path),'wb') as out:
        out.setnchannels(2)
        out.setsampwidth(2)
        out.setframerate(RATE)
        out.writeframes((data * 32767).round().astype('<i2').tobytes())

MUSIC = RES / 'music-source.wav'
EFFECTS = RES / 'effects-source.wav'
music_source, effect_source = decode(MUSIC), decode(EFFECTS)
assert len(music_source) >= int(33 * RATE)
assert sha(MUSIC) == '0d63fd67f4a100e30b9d0a7a488ae35417ad96fc78b57a092e78eac3b9754f6c'
assert sha(EFFECTS) == 'ae73af41be8f7e24365700778f7f8e59eaa4c8773cbebe70f04f92f7a299bd20'

# Original V7 composition is 120 BPM. Every musical source splice preserves its
# half-second beat phase; 16 ms linear overlaps remove edit-boundary clicks.
sections = [
    {'out':[0,4], 'source':[8,12], 'gain':0.90, 'role':'Immediate dense hook; no empty intro'},
    {'out':[4,8], 'source':[12,16], 'gain':0.92, 'role':'Local recognition, continuous pulse'},
    {'out':[8,15], 'source':[16,23], 'gain':1.00, 'role':'Actual production case / film reveal'},
    {'out':[15,21], 'source':[8,14], 'gain':0.84, 'role':'Proof and breathing room for metrics'},
    {'out':[21,25.5], 'source':[24,28.5], 'gain':0.92, 'role':'Strategy and message'},
    {'out':[25.5,30], 'source':[28,32.5], 'gain':1.04, 'role':'CTA expansion and controlled resolve'},
]
music = np.zeros((N,2), np.float64)
for section in sections:
    start,end = [round(x * RATE) for x in section['out']]
    source_start = round(section['source'][0] * RATE)
    music[start:end] = music_source[source_start:source_start+end-start] * section['gain']
half = round(.008 * RATE)
for left,right in zip(sections,sections[1:]):
    at = round(left['out'][1] * RATE)
    left_center = round(left['source'][1] * RATE)
    right_center = round(right['source'][0] * RATE)
    a = music_source[left_center-half:left_center+half] * left['gain']
    b = music_source[right_center-half:right_center+half] * right['gain']
    w = np.linspace(0,1,half*2)[:,None]
    music[at-half:at+half] = a*(1-w)+b*w

# Editorial intensity automation; the short 7.7 s gate clears the film arrival.
intensity_points = [
    [0,.74],[.06,.90],[2.50,.90],[2.65,.30],[2.96,.88],
    [3.85,.78],[4.05,.96],[7.65,.96],[7.72,.36],[7.96,.12],
    [8.10,.48],[8.27,.97],[14.60,.97],[14.85,.34],[15.18,.32],
    [15.58,.84],[20.60,.87],[20.85,.30],[21.20,.88],
    [25.27,.96],[25.5,.45],[25.78,1.0],[29.1,1.0],[30,0],
]
automation = np.interp(T, *np.asarray(intensity_points).T)

# Source regions are isolated effects already present in V7; no reference sound.
samples = {
    'impact': {'source_seconds':[0,.29], 'description':'Existing short low-frequency hit'},
    'tick': {'source_seconds':[.4,.455], 'description':'Existing short tonal/noise accent'},
    'sweep': {'source_seconds':[1.43,1.73], 'description':'Existing filtered-noise movement'},
}

# anchor = intended visual emphasis. A sweep starts early so its maximum lands
# near the anchor; tiny accents are not attached to every individual letter.
events = [
    {'anchor':0, 'kind':'impact','rate':1.2,'gain':.62,'pan':0,'offset':0,'role':'First-frame hook hit'},
    {'anchor':.8, 'kind':'sweep','rate':1.8,'gain':.48,'pan':-.38,'offset':-.10,'role':'Word flip'},
    {'anchor':1.65, 'kind':'sweep','rate':1.45,'gain':.60,'pan':.38,'offset':-.12,'role':'Typographic whip'},
    {'anchor':2.65, 'kind':'impact','rate':.82,'gain':.76,'pan':0,'offset':0,'role':'Red VISTA? emphasis'},
    {'anchor':3.85, 'kind':'sweep','rate':1.1,'gain':.67,'pan':-.26,'offset':-.17,'reverse':True,'role':'Into local recognition'},
    {'anchor':5.8, 'kind':'tick','rate':.84,'gain':.82,'pan':.18,'offset':0,'role':'Local identity accent'},
    {'anchor':7.7, 'kind':'sweep','rate':1.0,'gain':.58,'pan':.20,'offset':-.17,'reverse':True,'role':'Gated preparation for film'},
    {'anchor':8.1, 'kind':'impact','rate':.9,'gain':.72,'pan':0,'offset':0,'role':'Original campaign film reveal'},
    {'anchor':10.4, 'kind':'sweep','rate':1.4,'gain':.56,'pan':-.35,'offset':-.13,'role':'Plane / camera depth change'},
    {'anchor':12.8, 'kind':'tick','rate':1.2,'gain':.82,'pan':.30,'offset':0,'role':'Distribution packet accent'},
    {'anchor':14.85, 'kind':'sweep','rate':1.7,'gain':.68,'pan':-.2,'offset':-.10,'reverse':True,'role':'Paper-to-proof change'},
    {'anchor':15.35, 'kind':'impact','rate':1.0,'gain':.70,'pan':0,'offset':0,'role':'20.981 impressions settles'},
    {'anchor':18.2, 'kind':'impact','rate':1.35,'gain':.62,'pan':.06,'offset':0,'role':'13.064 reach settles'},
    {'anchor':20.85, 'kind':'sweep','rate':1.0,'gain':.68,'pan':.30,'offset':-.17,'role':'Proof-to-strategy transfer'},
    {'anchor':23.4, 'kind':'tick','rate':.9,'gain':.82,'pan':-.15,'offset':0,'role':'Strategy emphasis'},
    {'anchor':25.5, 'kind':'impact','rate':.78,'gain':.70,'pan':0,'offset':0,'role':'CTA expansion'},
    {'anchor':25.5, 'kind':'sweep','rate':.9,'gain':.50,'pan':-.15,'offset':-.21,'reverse':True,'role':'Shared CTA expansion lift'},
    {'anchor':28.1, 'kind':'sweep','rate':1.8,'gain':.47,'pan':.5,'offset':-.10,'role':'Final arrow / invitation'},
]
fx = np.zeros((N,2), np.float64)
ducks = []
for event in events:
    sample = samples[event['kind']]
    s,e = [round(x * RATE) for x in sample['source_seconds']]
    # Existing stereo sample is narrowed to mono, then panned explicitly.
    mono = effect_source[s:e].mean(axis=1)
    if event.get('reverse',False):
        mono = mono[::-1]
    new_length = round(len(mono) / event['rate'])
    pos = np.arange(new_length) * event['rate']
    mono = np.interp(pos,np.arange(len(mono)),mono)
    # 4 ms/18 ms edge envelopes: no discontinuity after tape-speed transforms.
    attack = min(round(.004*RATE),len(mono)//2)
    release = min(round(.018*RATE),len(mono)//2)
    mono[:attack] *= np.linspace(0,1,attack)
    mono[-release:] *= np.linspace(1,0,release)
    pan = event['pan']
    stereo = np.column_stack([mono*np.sqrt((1-pan)/2), mono*np.sqrt((1+pan)/2)])
    start = round((event['anchor']+event['offset'])*RATE)
    assert start >= 0
    length = min(len(stereo),N-start)
    fx[start:start+length] += stereo[:length] * event['gain']
    event.update({'start_seconds':start/RATE,'duration_seconds':length/RATE,
        'source_seconds':sample['source_seconds'],
        'semitones_tape_speed':round(12*np.log2(event['rate']),5),
        'reverse':event.get('reverse',False),
        'envelope_seconds':{'attack':.004,'release':.018}})
    # Drop music at major hits, a smaller amount for movement cues. Ticks keep
    # the bed steady; no indiscriminate pump under every little graphic.
    if event['kind'] != 'tick':
        at = event['anchor']
        floor = .53 if event['kind'] == 'impact' else .76
        points = [max(0,at-.035),at,at+.055,at+.19]
        gain = [1,floor,floor,1]
        automation = np.minimum(automation,np.interp(T,points,gain))
        ducks.append({'anchor_seconds':at,'points_seconds':points,'gains':gain})

music *= automation[:,None]
# Very short safety fade at first frame, deliberate long final resolve.
fade = np.ones(N)
fade[:round(.004*RATE)] = np.linspace(0,1,round(.004*RATE))
fade[-round(.85*RATE):] = np.linspace(1,0,round(.85*RATE))
music *= fade[:,None]
fx *= fade[:,None]
mix = music + fx
linear_gain = min(1.0,.92/max(np.max(np.abs(mix)),1e-12))
mix *= linear_gain
premaster = REVIEW / 'audio-premaster-v12.wav'
write(premaster,mix)

def parse_loudnorm(log):
    begin,end = log.rfind('{'),log.rfind('}')+1
    assert begin >= 0 and end > begin
    return json.loads(log[begin:end])

analysis = subprocess.run(['ffmpeg','-hide_banner','-i',str(premaster),
    '-af','loudnorm=I=-16:TP=-1.8:LRA=7:print_format=json','-f','null','-'],
    check=True,capture_output=True,text=True)
measured = parse_loudnorm(analysis.stderr)
master_filter = ('loudnorm=I=-16:TP=-1.8:LRA=7:'
    f'measured_I={measured["input_i"]}:measured_TP={measured["input_tp"]}:'
    f'measured_LRA={measured["input_lra"]}:measured_thresh={measured["input_thresh"]}:'
    f'offset={measured["target_offset"]}:linear=true:print_format=json')
output = ASSETS / 'mix-v12.wav'
mastering = subprocess.run(['ffmpeg','-hide_banner','-y','-i',str(premaster),
    '-af',master_filter,'-ar',str(RATE),'-ac','2','-t',str(DURATION),
    '-c:a','pcm_s16le',str(output)],check=True,capture_output=True,text=True)
(REVIEW/'audio-mastering-v12.log').write_text(analysis.stderr+'\nSECOND PASS\n'+mastering.stderr)

data = decode(output)
verification = subprocess.run(['ffmpeg','-hide_banner','-i',str(output),
    '-af','loudnorm=I=-16:TP=-1.8:LRA=7:print_format=json','-f','null','-'],
    check=True,capture_output=True,text=True)
levels = parse_loudnorm(verification.stderr)
probe = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams',
    '-show_format','-of','json',str(output)]))
clipped = int(np.count_nonzero(np.abs(data) >= 32767/32768))
report = {
    'ok':len(data)==N and clipped==0 and abs(float(levels['input_i'])+16)<=.35
        and float(levels['input_tp']) <= -1.7,
    'file':'assets/mix-v12.wav','sha256':sha(output),
    'duration_seconds':len(data)/RATE,'sample_rate':RATE,'channels':2,
    'sample_frames':len(data),'codec':probe['streams'][0]['codec_name'],
    'integrated_lufs':float(levels['input_i']),
    'true_peak_dbfs':float(levels['input_tp']),
    'loudness_range_lu':float(levels['input_lra']),
    'sample_peak_dbfs':round(20*np.log10(max(np.max(np.abs(data)),1e-12)),3),
    'clipped_samples':clipped,'finite_samples':bool(np.isfinite(data).all()),
    'left_rms_dbfs':round(20*np.log10(np.sqrt(np.mean(data[:,0]**2))),3),
    'right_rms_dbfs':round(20*np.log10(np.sqrt(np.mean(data[:,1]**2))),3),
    'final_100ms_rms_dbfs':round(20*np.log10(max(np.sqrt(np.mean(data[-4800:]**2)),1e-12)),3),
    'effect_events':len(events),'music_edit_sections':len(sections),
    'narration_present':False,'original_clip_audio_gain':0,
    'reference_audio_reused':False,'rejected_voice_reused':False,
    'technical_decode_performed':True,'subjective_listening_performed':False,
    'limits':'Technical audio validation only. No playback/listening tool is available in this interface.',
}
provenance = {
    'duration_seconds':DURATION,'sample_rate':RATE,'new_narration_present':False,
    'original_clip_audio_gain':0,'reference_audio_reused':False,'rejected_voice_used':False,
    'subjective_listening_performed':False,
    'music_origin':'Existing Evoquex V7 original 120 BPM instrumental stem; no reference music reused.',
    'effects_origin':'Isolated regions of existing Evoquex V7 effects stem; tape-speed/reverse/pan/envelope edits only.',
    'license':'GeneralUser GS v2.0.3 / License v2.0, included unmodified in resources/audio/GeneralUser-GS-LICENSE.txt. Author expressly permits commercial musical recordings; complete sample-provenance qualifications preserved.',
    'source_repository':'https://github.com/mrbumpy409/GeneralUser-GS',
    'source_soundfont_git_commit':'684543d5e5efaef08d02be50dcda8d552478fa60',
    'source_soundfont_sha256':'9575028c7a1f589f5770fccc8cff2734566af40cd26ed836944e9a5152688cfe',
    'files_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [MUSIC,EFFECTS,RES/'GeneralUser-GS-LICENSE.txt']},
    'output_sha256':sha(output),'music_sections':sections,
    'music_splice_crossfade_seconds':.016,'music_intensity_points':intensity_points,
    'effect_source_regions':samples,'events':events,'music_short_ducks':ducks,
    'premaster_linear_gain':linear_gain,'final_fade_seconds':.85,
    'mastering':{'method':'FFmpeg two-pass loudnorm','target_lufs':-16,'true_peak_limit_dbfs':-1.8,'loudness_range_target':7,'second_pass_filter':master_filter},
    'requirements':['Python 3','NumPy (already installed)','FFmpeg (already installed)'],
    'regenerate':'python scripts/remix-audio.py',
}
(RES/'provenance-v12.json').write_text(json.dumps(provenance,indent=2)+'\n')
(REVIEW/'audio-validation-v12.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
assert report['ok'], 'Audio technical acceptance failed; see review/audio-validation-v12.json'
