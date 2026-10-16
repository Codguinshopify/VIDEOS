"""Reproducible 30 s V13 score edit with bit-exact approved 0–4 s PCM.

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
HOOK = RATE * 4
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
    assert data.ndim == 2 and data.shape[1] == 2
    assert np.isfinite(data).all()
    assert np.max(np.abs(data)) < 1, 'Premaster clipping; lower linear gain.'
    with wave.open(str(path),'wb') as out:
        out.setnchannels(2)
        out.setsampwidth(2)
        out.setframerate(RATE)
        out.writeframes((data * 32767).round().astype('<i2').tobytes())

MUSIC = RES / 'music-source.wav'
EFFECTS = RES / 'effects-source.wav'
APPROVED = ASSETS / 'mix-v12.wav'
assert sha(APPROVED) == 'cde124ba505d0fe60ab30f239ccf510c2f452e012b59c551419ca9009cd6fdb7'
with wave.open(str(APPROVED),'rb') as approved_wave:
    assert (approved_wave.getframerate(),approved_wave.getnchannels(),approved_wave.getsampwidth()) == (RATE,2,2)
    approved_pcm = np.frombuffer(approved_wave.readframes(approved_wave.getnframes()),dtype='<i2').reshape(-1,2).copy()
approved_prefix = approved_pcm[:HOOK].tobytes()
inherited_events = [dict(e,inherited_approved_prefix=True) for e in json.loads((RES/'provenance-v12.json').read_text())['events'] if e['anchor'] < 4]
music_source, effect_source = decode(MUSIC), decode(EFFECTS)
assert len(music_source) >= int(33 * RATE)
assert sha(MUSIC) == '0d63fd67f4a100e30b9d0a7a488ae35417ad96fc78b57a092e78eac3b9754f6c'
assert sha(EFFECTS) == 'ae73af41be8f7e24365700778f7f8e59eaa4c8773cbebe70f04f92f7a299bd20'

# Original V7 composition is 120 BPM. Every musical source splice preserves its
# half-second beat phase; 16 ms linear overlaps remove edit-boundary clicks.
sections = [
    {'out':[4,8], 'source':[24,28], 'gain':0.94, 'role':'New chord phrase under kinetic locality / type mask'},
    {'out':[8,15], 'source':[16,23], 'gain':1.00, 'role':'Actual production case / film reveal'},
    {'out':[15,21], 'source':[8,14], 'gain':0.87, 'role':'Fragmented numerals and real evidence panels'},
    {'out':[21,25.5], 'source':[24,28.5], 'gain':0.94, 'role':'Opposing type planes, message/public links'},
    {'out':[25.5,30], 'source':[28,32.5], 'gain':1.02, 'role':'Two-line CTA articulation and signature resolve'},
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
    [0,0],[4,.92],[5.05,.92],[5.15,.65],[5.45,.96],
    [7.52,.96],[7.72,.34],[7.96,.18],[8.10,.48],[8.30,.97],
    [9.55,.97],[9.6,.76],[9.85,.97],[10.45,.65],[10.7,.92],
    [14.48,.94],[14.7,.35],[15.05,.44],[15.65,.83],
    [17.68,.89],[17.85,.55],[18.45,.88],[20.62,.9],[20.85,.32],
    [21.20,.92],[23.55,.92],[23.65,.68],[24.1,.88],
    [25.2,.94],[25.35,.48],[25.7,1.0],[28.4,.94],[29.15,.94],[30,0],
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
    {'anchor':4.05, 'kind':'tick','rate':1.12,'gain':.66,'pan':-.18,'offset':0,'role':'Opposing typography planes'},
    {'anchor':5.15, 'kind':'sweep','rate':1.25,'gain':.62,'pan':.32,'offset':-.12,'role':'Type becomes city-image mask'},
    {'anchor':7.7, 'kind':'sweep','rate':1.0,'gain':.60,'pan':-.24,'offset':-.15,'reverse':True,'role':'Vertical camera handoff preparation'},
    {'anchor':8.1, 'kind':'impact','rate':.9,'gain':.70,'pan':0,'offset':0,'role':'Campaign film arrives'},
    {'anchor':9.6, 'kind':'sweep','rate':1.65,'gain':.46,'pan':.36,'offset':-.085,'role':'Media advances while typography recedes'},
    {'anchor':10.45, 'kind':'sweep','rate':1.2,'gain':.60,'pan':-.34,'offset':-.125,'reverse':True,'role':'Distribution flip'},
    {'anchor':11.15, 'kind':'tick','rate':.78,'gain':.8,'pan':.12,'offset':0,'role':'Evoquex segmented label assembles'},
    {'anchor':12.75, 'kind':'sweep','rate':1.4,'gain':.54,'pan':.3,'offset':-.10,'role':'Clevelândia window extends'},
    {'anchor':14.7, 'kind':'sweep','rate':1.1,'gain':.64,'pan':-.28,'offset':-.14,'reverse':True,'role':'Camera delivers evidence plane'},
    {'anchor':15.65, 'kind':'impact','rate':1.0,'gain':.70,'pan':0,'offset':0,'role':'20.981 sliced numeral resolves'},
    {'anchor':16.3, 'kind':'tick','rate':1.18,'gain':.64,'pan':.26,'offset':0,'role':'Evidence screenshot opens in panels'},
    {'anchor':17.85, 'kind':'sweep','rate':1.5,'gain':.57,'pan':.28,'offset':-.10,'role':'Metric changes direction'},
    {'anchor':18.45, 'kind':'impact','rate':1.35,'gain':.58,'pan':.04,'offset':0,'role':'13.064 reach numeral resolves'},
    {'anchor':20.85, 'kind':'sweep','rate':1.0,'gain':.62,'pan':-.30,'offset':-.14,'role':'Lateral camera into strategy'},
    {'anchor':22.25, 'kind':'tick','rate':.94,'gain':.70,'pan':.24,'offset':0,'role':'Message and audience links connect'},
    {'anchor':23.65, 'kind':'sweep','rate':1.55,'gain':.52,'pan':-.28,'offset':-.095,'reverse':True,'role':'Connector becomes layout boundary'},
    {'anchor':25.35, 'kind':'impact','rate':.87,'gain':.62,'pan':0,'offset':0,'role':'Two-line CTA assembles'},
    {'anchor':26.4, 'kind':'sweep','rate':1.85,'gain':.40,'pan':.3,'offset':-.08,'role':'Empresa-to-serviço directional word change'},
    {'anchor':28.4, 'kind':'tick','rate':.82,'gain':.58,'pan':0,'offset':0,'role':'Final signature and arrow resolve'},
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
    assert start >= HOOK, 'No new effect may alter the approved first four seconds.'
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
fade[-round(.85*RATE):] = np.linspace(1,0,round(.85*RATE))
music *= fade[:,None]
fx *= fade[:,None]
mix = music + fx
linear_gain = min(1.0,.92/max(np.max(np.abs(mix)),1e-12))
mix *= linear_gain
premaster = REVIEW / 'audio-premaster-post4-v13.wav'
write(premaster,mix[HOOK:])

def parse_loudnorm(log):
    begin,end = log.rfind('{'),log.rfind('}')+1
    assert begin >= 0 and end > begin
    return json.loads(log[begin:end])

analysis = subprocess.run(['ffmpeg','-hide_banner','-i',str(premaster),
    '-af','loudnorm=I=-16.1:TP=-2:LRA=7:print_format=json','-f','null','-'],
    check=True,capture_output=True,text=True)
measured = parse_loudnorm(analysis.stderr)
master_filter = ('loudnorm=I=-16.1:TP=-2:LRA=7:'
    f'measured_I={measured["input_i"]}:measured_TP={measured["input_tp"]}:'
    f'measured_LRA={measured["input_lra"]}:measured_thresh={measured["input_thresh"]}:'
    f'offset={measured["target_offset"]}:linear=true:print_format=json')
postmaster = REVIEW / 'audio-post4-master-v13.wav'
mastering = subprocess.run(['ffmpeg','-hide_banner','-y','-i',str(premaster),
    '-af',master_filter,'-ar',str(RATE),'-ac','2','-t',str(DURATION-4),
    '-c:a','pcm_s16le',str(postmaster)],check=True,capture_output=True,text=True)
(REVIEW/'audio-mastering-v13.log').write_text(analysis.stderr+'\nPOST-4-SECOND SECOND PASS\n'+mastering.stderr)

with wave.open(str(postmaster),'rb') as w:
    post_pcm = np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').reshape(-1,2).copy()
assert len(post_pcm) == N-HOOK
# A 64 ms equal-sum raised-cosine bridge begins AT 4.000 s, never before it.
# Prefix PCM is copied literally after all DSP; no re-quantization or limiting.
bridge = round(.064*RATE)
weights = (1-np.cos(np.linspace(0,np.pi,bridge)))/2
post_pcm[:bridge] = np.round(approved_pcm[HOOK:HOOK+bridge]*(1-weights[:,None]) + post_pcm[:bridge]*weights[:,None]).astype('<i2')
output = ASSETS / 'mix-v13.wav'
final_pcm = np.concatenate([approved_pcm[:HOOK],post_pcm],axis=0)
with wave.open(str(output),'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(RATE)
    w.writeframes(final_pcm.tobytes())
assert final_pcm[:HOOK].tobytes() == approved_prefix
with wave.open(str(output),'rb') as written_wave:
    written_prefix = written_wave.readframes(HOOK)
assert written_prefix == approved_prefix, 'Disk WAV prefix is not the approved PCM.'
hook_report = {
    'approved_source':'assets/mix-v12.wav','source_file_sha256':sha(APPROVED),
    'preserved_start_seconds':0,'preserved_end_seconds_exclusive':4,
    'preserved_stereo_frames':HOOK,'preserved_scalar_channel_samples':HOOK*2,
    'preserved_pcm_bytes':len(approved_prefix),
    'approved_prefix_pcm_sha256':hashlib.sha256(approved_prefix).hexdigest(),
    'output_prefix_pcm_sha256':hashlib.sha256(written_prefix).hexdigest(),
    'exact_equal':True,'modified_frames_before_4s':0,
    'crossfade_start_seconds':4,'crossfade_end_seconds':4.064,
    'crossfade_curve':'Raised cosine; equal-sum complementary weights',
    'global_normalization_applied':False,'post_4s_only_normalization_applied':True,
}

data = decode(output)
verification = subprocess.run(['ffmpeg','-hide_banner','-i',str(output),
    '-af','loudnorm=I=-16:TP=-1.5:LRA=7:print_format=json','-f','null','-'],
    check=True,capture_output=True,text=True)
levels = parse_loudnorm(verification.stderr)
probe = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams',
    '-show_format','-of','json',str(output)]))
clipped = int(np.count_nonzero(np.abs(data) >= 32767/32768))
report = {
    'ok':len(data)==N and clipped==0 and abs(float(levels['input_i'])+16)<=.4
        and float(levels['input_tp']) <= -1.5 and hook_report['exact_equal'],
    'file':'assets/mix-v13.wav','sha256':sha(output),
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
    'effect_events':len(inherited_events)+len(events),'approved_hook_effect_events':len(inherited_events),
    'new_post4_effect_events':len(events),'music_edit_sections':len(sections),
    'hook_preservation':hook_report,
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
    'files_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [MUSIC,EFFECTS,APPROVED,RES/'GeneralUser-GS-LICENSE.txt']},
    'output_sha256':sha(output),'music_sections':sections,
    'approved_hook_preservation':hook_report,
    'music_splice_crossfade_seconds':.016,'music_intensity_points':intensity_points,
    'effect_source_regions':samples,'events':inherited_events+events,'new_post4_events':events,'music_short_ducks':ducks,
    'premaster_linear_gain':linear_gain,'final_fade_seconds':.85,
    'mastering':{'method':'FFmpeg two-pass loudnorm on 4–30 s ONLY; approved 0–4 s PCM copied literally afterwards','post4_target_lufs':-16.1,'post4_true_peak_limit_dbfs':-2,'complete_mix_true_peak_acceptance_dbfs':-1.5,'loudness_range_target':7,'second_pass_filter':master_filter},
    'requirements':['Python 3','NumPy (already installed)','FFmpeg (already installed)'],
    'regenerate':'python scripts/remix-audio.py',
}
(RES/'provenance-v13.json').write_text(json.dumps(provenance,indent=2)+'\n')
(REVIEW/'audio-validation-v13.json').write_text(json.dumps(report,indent=2)+'\n')
(REVIEW/'audio-hook-preservation-v13.json').write_text(json.dumps(hook_report,indent=2)+'\n')
print(json.dumps(report,indent=2))
assert report['ok'], 'Audio technical acceptance failed; see review/audio-validation-v13.json'
