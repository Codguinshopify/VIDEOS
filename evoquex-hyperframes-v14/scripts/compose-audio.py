"""Original V14 score and sound design. Does NOT read any V7/V12/V13 stem.

The MIDI composition is new: 100 BPM, E minor / extended open voicings, three
non-looped editorial sections, vibraphone, EP2, synth-bass2, pad and percussion.
FluidSynth renders the verified licensed GeneralUser bank already in cache.
Whooshes/folds/impacts are original deterministic PCM synthesis, not stock audio.
No network, TTS, voice model or paid service is called.
"""
from pathlib import Path
import ctypes as ct
import ctypes.util
import hashlib
import json
import os
import struct
import subprocess
import wave
import numpy as np
from scipy.signal import butter, sosfilt

ROOT = Path(__file__).resolve().parent.parent
RES, REVIEW, ASSETS = ROOT/'resources/audio', ROOT/'review', ROOT/'assets'
for folder in [RES, REVIEW, ASSETS]: folder.mkdir(parents=True,exist_ok=True)
RATE, LENGTH, BPM = 48000, 26.0, 100
N = round(RATE*LENGTH)
TIMES = np.arange(N)/RATE
PIN = '684543d5e5efaef08d02be50dcda8d552478fa60'
SF_SHA = '9575028c7a1f589f5770fccc8cff2734566af40cd26ed836944e9a5152688cfe'
SF = Path(os.environ.get('EVOQUEX_SF2','/workspace/.cache/evoquex-audio/GeneralUser-GS.sf2'))
assert SF.is_file(), 'Recomposition requires verified GeneralUser GS SF2, via EVOQUEX_SF2. Rendering the video only needs assets/mix-v14.wav.'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(SF)==SF_SHA, 'SoundFont hash differs from the licensed pinned source.'
TIMING=ROOT/'resources/scene-timing-v14.json'
assert TIMING.is_file(), 'Wait for the MD scene timing before final mastering.'
timing_doc=json.loads(TIMING.read_text())
assert timing_doc['duration']==LENGTH, 'Scene duration changed; retime the composition before mastering.'

def wav(path, pcm):
    assert pcm.ndim==2 and pcm.shape[1]==2 and np.isfinite(pcm).all()
    assert np.max(np.abs(pcm))<1, f'Clipping before PCM quantization: {path.name}'
    with wave.open(str(path),'wb') as w:
        w.setnchannels(2);w.setsampwidth(2);w.setframerate(RATE)
        w.writeframes((pcm*32767).round().astype('<i2').tobytes())

# New composition, explicitly authored notes. No cyclic four-chord sequencer.
notes=[]
def note(t,ch,pitch,velocity,duration,section):
    if t<0 or t>=LENGTH-.08:return
    notes.append({'time':round(float(t),6),'channel':ch,'pitch':pitch,
        'velocity':velocity,'duration':round(min(duration,LENGTH-t-.04),6),'section':section})
def chord(t,ch,pitches,velocity,duration,section):
    for i,pitch in enumerate(pitches):note(t+i*.009,ch,pitch,velocity-(i%3)*2,duration-i*.009,section)

# A — individually phrased hook/local recognition, rather than a backing loop.
for t,p,v,d in [(0,76,50,.11),(.42,83,35,.09),(1.1,79,47,.12),
               (1.85,78,50,.105),(2.75,83,54,.16),(3.85,74,42,.18),
               (4.15,76,39,.13),(4.8,79,46,.12),(5.45,83,43,.25)]:
    note(t,2,p,v,d,'A_hook_local')
for t,p,v in [(0,40,72),(1.85,47,55),(2.75,40,77),(4.15,36,61),(5.45,43,58)]:
    note(t,1,p,v,.24,'A_hook_local')
chord(0,0,[55,59,66],27,.3,'A_hook_local')
chord(3.85,3,[55,59,62,66],30,1.3,'A_hook_local')
chord(5.45,0,[55,59,64],32,.4,'A_hook_local')
for t,p,v in [(0,36,77),(1.1,37,42),(1.85,36,69),(2.75,36,84),(3.85,42,35),(4.8,39,38),(5.45,36,58)]:
    note(t,9,p,v,.06,'A_hook_local')

# B — four different phrases follow actual film/distribution/locality/proof.
phrases=[
    (6.35,9.0,40,[55,59,62,66],[(0,76),(.3,79),(.9,83),(1.35,78),(1.95,74),(2.4,79)]),
    (9.0,11.35,36,[55,59,62,64],[(.15,76),(.6,74),(1.2,71),(1.8,79)]),
    (11.35,13.6,43,[55,59,64,67],[(.15,74),(.75,79),(1.05,76),(1.65,83)]),
    (13.6,17.6,38,[57,62,64,69],[(1.05,78),(1.8,76),(2.55,74),(3.15,81)]),
]
for j,(start,end,bass,voicing,melody) in enumerate(phrases):
    role=['B_case','B_distribution','B_locality','B_proof_breath'][j]
    # Soft EP offbeats, low bass interventions and differently shaped melodies.
    chord(start+.02,0,voicing,33 if j<3 else 26,.22 if j<3 else .5,role)
    chord(start+1.05,0,[p+12 if i==0 else p for i,p in enumerate(voicing)],27,.16,role)
    chord(start+.05,3,voicing,24 if j<3 else 31,min(1.6,end-start-.1),role)
    for k,(offset,pitch) in enumerate(melody):
        note(start+offset,2,pitch,43-4*(k%3)+(2 if j==2 else 0),.105+.025*(k%2),role)
    for k,offset in enumerate([0,.9,1.8]):
        if start+offset<end-.15:
            note(start+offset,1,bass+(12 if k==2 and j%2==0 else 0),67-k*5,.18 if j<3 else .28,role)
    if j<3:
        for k,(off,pitch) in enumerate([(0,36),(.6,39),(1.2,36),(1.8,39)]):
            if start+off<end-.1:note(start+off,9,pitch,68 if pitch==36 else 45,.055,role)
        for k,t in enumerate(np.arange(start+.3,end-.12,.3)):
            note(float(t),9,42,[26,17,22,15,28,18][k%6],.035,role)
        # Each turnaround uses a different short fill rather than a loop restart.
        for k in range(j+1):note(end-.23+k*.065,9,37 if k%2==0 else 42,28+k*3,.03,role)
    else:
        for off,pitch,vel in [(.55,36,65),(1.15,37,31),(2.35,39,37),(2.95,42,20)]:
            note(start+off,9,pitch,vel,.05,role)

# C — renewed pulse, upward phrase, then a resolved chord and a full reading tail.
chord(18.1,3,[55,59,62,64],30,1.65,'C_strategy')
chord(18.1,0,[55,59,64],35,.25,'C_strategy')
for t,p in [(18.1,36),(19.3,43),(19.9,48)]:note(t,1,p,65,.2,'C_strategy')
for t,p,v in [(18.8,76,43),(19.45,79,45),(19.9,83,44)]:note(t,2,p,v,.13,'C_strategy')
chord(20.45,3,[57,62,64,66],32,1.85,'C_CTA_lift')
chord(20.45,0,[57,62,66],36,.22,'C_CTA_lift')
for t,p,v in [(20.45,38,69),(21.35,45,63),(22.0,50,65)]:note(t,1,p,v,.2,'C_CTA_lift')
for t,p,v in [(20.45,78,43),(21.05,81,45),(21.65,83,48),(22.25,86,51)]:note(t,2,p,v,.11,'C_CTA_lift')
for t,p,v in [(18.1,36,68),(18.7,39,46),(19.3,36,66),(19.9,37,39),
               (20.45,36,76),(21.05,39,52),(21.65,36,78),(22.25,39,57),(22.55,37,34)]:
    note(t,9,p,v,.06,'C_strategy_CTA')
for k,t in enumerate(np.arange(18.4,22.7,.3)):
    note(float(t),9,42,[20,26,18,28,23,31][k%6],.035,'C_strategy_CTA')
# No drum loop underneath the last CTA. Musical invitation resolves, then breathes.
chord(23.0,0,[55,59,64,66],40,.75,'C_invitation_resolve')
note(23.0,1,40,66,.55,'C_invitation_resolve')
note(23.0,9,36,61,.08,'C_invitation_resolve')
chord(24.5,0,[55,59,64,66,71],35,1.05,'C_signature_resolve')
chord(24.5,3,[55,59,64,66],27,1.15,'C_signature_resolve')
note(24.5,2,83,35,.6,'C_signature_resolve')

# Preserve actual MIDI as an editable score; no mido dependency is needed.
programs={0:5,1:39,2:11,3:89}
volumes={0:78,1:88,2:76,3:48,9:82}
pans={0:48,1:64,2:80,3:66,9:64}
def vlq(n):
    a=[n&127];n>>=7
    while n:a.append((n&127)|128);n>>=7
    return bytes(reversed(a))
def make_track(events):
    events=sorted(events,key=lambda x:(x[0],x[1]));buf=bytearray();last=0
    for tick,order,payload in events:
        buf+=vlq(tick-last)+payload;last=tick
    buf+=b'\0\xff\x2f\0'
    return b'MTrk'+struct.pack('>I',len(buf))+buf
resolution=960; tempo=round(60_000_000/BPM);tps=resolution*1_000_000/tempo
conductor=make_track([(0,0,b'\xff\x51\x03'+tempo.to_bytes(3,'big')),
    (0,1,b'\xff\x58\x04\x04\x02\x18\x08')])
tracks=[conductor]
for ch in [0,1,2,3,9]:
    ev=[]
    if ch in programs:ev.append((0,0,bytes([0xc0+ch,programs[ch]])))
    for controller,val in [(7,volumes[ch]),(10,pans[ch]),(91,0),(93,0)]:
        ev.append((0,1,bytes([0xb0+ch,controller,val])))
    for n in notes:
        if n['channel']!=ch:continue
        ev.append((round(n['time']*tps),3,bytes([0x90+ch,n['pitch'],n['velocity']])))
        ev.append((round((n['time']+n['duration'])*tps),2,bytes([0x80+ch,n['pitch'],0])))
    tracks.append(make_track(ev))
midi=RES/'evoquex-original-score-v14.mid'
midi.write_bytes(b'MThd'+struct.pack('>IHHH',6,1,len(tracks),resolution)+b''.join(tracks))

# Actual new instrument rendering. Disable non-deterministic global effects;
# spatial depth is added with deterministic filtered stereo taps below.
lib=ct.CDLL(ctypes.util.find_library('fluidsynth'))
def api(name,ret,args):
    f=getattr(lib,name);f.restype=ret;f.argtypes=args;return f
ptr,I,F,S=ct.c_void_p,ct.c_int,ct.c_double,ct.c_char_p
settings=api('new_fluid_settings',ptr,[])()
setnum=api('fluid_settings_setnum',I,[ptr,S,F]);setint=api('fluid_settings_setint',I,[ptr,S,I])
setnum(settings,b'synth.sample-rate',RATE);setnum(settings,b'synth.gain',.48)
setint(settings,b'synth.reverb.active',0);setint(settings,b'synth.chorus.active',0)
setint(settings,b'synth.cpu-cores',1)
synth=api('new_fluid_synth',ptr,[ptr])(settings)
assert api('fluid_synth_sfload',I,[ptr,S,I])(synth,str(SF).encode(),1)>=0
program=api('fluid_synth_program_change',I,[ptr,I,I]);cc=api('fluid_synth_cc',I,[ptr,I,I,I])
on=api('fluid_synth_noteon',I,[ptr,I,I,I]);off=api('fluid_synth_noteoff',I,[ptr,I,I])
render=api('fluid_synth_write_float',I,[ptr,I,ptr,I,I,ptr,I,I])
for ch,preset in programs.items():program(synth,ch,preset)
for ch in volumes:
    for controller,val in [(7,volumes[ch]),(10,pans[ch]),(91,0),(93,0)]:cc(synth,ch,controller,val)
queue=[]
for n in notes:
    queue.append((round(n['time']*RATE),1,n['channel'],n['pitch'],n['velocity']))
    queue.append((round((n['time']+n['duration'])*RATE),0,n['channel'],n['pitch'],0))
queue.sort();music=np.zeros((N,2),np.float64);cursor=0
def render_to(end):
    global cursor
    end=min(end,N);count=end-cursor
    if count<=0:return
    left=np.zeros(count,np.float32);right=np.zeros(count,np.float32)
    assert render(synth,count,left.ctypes.data,0,1,right.ctypes.data,0,1)==0
    music[cursor:end]=np.column_stack([left,right]);cursor=end
for sample,state,ch,pitch,vel in queue:
    if sample>=N:break
    render_to(sample)
    if state:on(synth,ch,pitch,vel)
    else:off(synth,ch,pitch)
render_to(N)
api('delete_fluid_synth',None,[ptr])(synth);api('delete_fluid_settings',None,[ptr])(settings)
# Deterministic depth: two quiet cross-channel, low-passed early reflections.
low=sosfilt(butter(2,4200,fs=RATE,output='sos'),music,axis=0)
for delay,gain,swap in [(.073,.13,True),(.137,.075,False)]:
    shift=round(delay*RATE);layer=low[:-shift,::-1] if swap else low[:-shift]
    music[shift:]+=layer*gain

# Original PCM sound effects. Source is documented formulas/seed, not a pack.
rng=np.random.default_rng(140026)
effects=np.zeros((N,2),np.float64)
events=[]
def place(at,data,gain,pan):
    start=round(at*RATE);assert start>=0
    if data.ndim==1:data=np.column_stack([data*np.sqrt((1-pan)/2),data*np.sqrt((1+pan)/2)])
    end=min(N,start+len(data));effects[start:end]+=data[:end-start]*gain
    return start/RATE,(end-start)/RATE
def moving_noise(duration,reverse=False,bright=2600):
    t=np.arange(round(duration*RATE))/RATE
    noise=rng.standard_normal(len(t));band=sosfilt(butter(2,[260,bright],btype='bandpass',fs=RATE,output='sos'),noise)
    band/=max(np.max(np.abs(band)),1e-8)
    env=np.maximum(np.sin(np.pi*np.arange(len(t))/max(len(t)-1,1)),0)**1.8
    signal=band*env*.25
    return signal[::-1] if reverse else signal
def impact(duration=.28):
    t=np.arange(round(duration*RATE))/RATE
    # New two-stage frequency fall, not the old stem's hit sample.
    phase=2*np.pi*(42*t+2.9*(1-np.exp(-t*24)))
    s=np.sin(phase)*np.exp(-t*18)*(1-np.exp(-t*1600))*.34
    tick=sosfilt(butter(2,[1600,6500],btype='bandpass',fs=RATE,output='sos'),rng.standard_normal(len(t)))
    return s+tick*np.exp(-t*210)*.018
def tick(pitch=1150,duration=.042):
    t=np.arange(round(duration*RATE))/RATE
    return (np.sin(2*np.pi*pitch*t)+.2*np.sin(2*np.pi*pitch*1.497*t))*np.exp(-t*160)*(1-np.exp(-t*2000))*.095
def fold(duration=.32):
    out=moving_noise(duration,reverse=True,bright=3900)*.65
    for index,at in enumerate([.06,.11,.17]):
        sample=tick(900+index*280,.035);a=round(at*RATE)
        out[a:a+len(sample)]+=sample*.48
    return out

# Editorial accents follow the confirmed MD timing, not every animated letter.
specs=[
    (0,'impact',.72,0,0,'First-frame hook'),
    (1.1,'tick',.72,-.22,0,'É conhecida'),
    (1.85,'sweep',.64,.28,-.12,'Local word motion'),
    (2.75,'impact',.84,0,0,'Mas é vista?'),
    (3.85,'sweep',.72,-.32,-.13,'Iris into recognition'),
    (5.45,'sweep',.57,.30,-.13,'City image aperture'),
    (6.35,'fold',.71,-.25,-.16,'Forms lead to production'),
    (7.05,'impact',.67,0,0,'Real footage slit reveal'),
    (7.85,'tick',.58,.18,0,'Danny’s Presentes identity'),
    (9.0,'fold',.68,.25,-.15,'Lamellae fold toward distribution'),
    (10.0,'tick',.71,-.18,0,'Evoquex authored label'),
    (11.35,'sweep',.66,.28,-.13,'Shape pulls into locality'),
    (12.15,'tick',.61,0,0,'Clevelândia resolves'),
    (13.6,'fold',.67,-.25,-.15,'Marker becomes proof aperture'),
    (14.15,'impact',.78,0,0,'20 mil visualizações emphasis'),
    (17.6,'sweep',.7,.32,-.13,'Camera exits evidence'),
    (18.8,'tick',.62,-.16,0,'Uma estratégia'),
    (19.45,'tick',.62,.24,0,'Message/audience connection'),
    (20.45,'sweep',.71,-.3,-.13,'CTA camera push'),
    (22.0,'tick',.55,.18,0,'Company/service word exchange'),
    (23.0,'impact',.49,0,0,'Conversa invitation'),
    (24.5,'tick',.43,0,0,'Signature musical resolve'),
]
for anchor,kind,gain,pan,offset,role in specs:
    if kind=='impact':clip=impact()
    elif kind=='tick':clip=tick(pitch=920+(len(events)%4)*165)
    elif kind=='fold':clip=fold()
    else:clip=moving_noise(.26,reverse=len(events)%2==0,bright=2300+(len(events)%3)*600)
    # All synth effects receive actual edge envelopes before being written.
    attack=min(round(.002*RATE),len(clip)//2);release=min(round(.012*RATE),len(clip)//2)
    clip[:attack]*=np.linspace(0,1,attack);clip[-release:]*=np.linspace(1,0,release)
    start,duration=place(anchor+offset,clip,gain,pan)
    events.append({'anchor_seconds':anchor,'start_seconds':start,'duration_seconds':duration,
        'kind':kind,'gain':gain,'pan':pan,'role':role,'source':'New original deterministic PCM synthesis in compose-audio.py','seed':140026})

# Phase/phrase energy, deliberate breaths; no identical loop bed through proofs.
energy_points=[(0,.78),(.06,.9),(2.6,.88),(2.75,.52),(3.0,.9),
    (6.2,.9),(6.35,.55),(6.6,1.0),(8.8,1.0),(9.0,.66),(9.3,.98),
    (11.2,.98),(11.35,.7),(11.7,.96),(13.35,.96),(13.6,.24),
    (14.02,.22),(14.15,.68),(14.6,.84),(16.9,.84),(17.42,.18),
    (17.7,.18),(18.05,.76),(18.8,.9),(20.3,.95),(20.45,.65),
    (20.75,1.0),(22.45,1.05),(23.0,.72),(23.5,.82),(24.5,.88),(25.15,.75),(26,0)]
envelope=np.interp(TIMES,*np.asarray(energy_points).T)
ducks=[]
for e in events:
    if e['kind']=='tick':continue
    t=e['anchor_seconds'];floor=.58 if e['kind']=='impact' else .77
    points=[max(0,t-.035),t,t+.05,t+.19];gains=[1,floor,floor,1]
    envelope=np.minimum(envelope,np.interp(TIMES,points,gains))
    ducks.append({'anchor':t,'points':points,'gains':gains})
music*=envelope[:,None]
fade=np.ones(N);fade[:round(.003*RATE)]=np.linspace(0,1,round(.003*RATE));fade[-round(.85*RATE):]=np.linspace(1,0,round(.85*RATE))
music*=fade[:,None];effects*=fade[:,None]
# Instrument velocities retain articulation; the bed is balanced above effects,
# rather than allowing sparse low-frequency hits to dominate the mastering.
music*=3.4;effects*=.85
gain=min(1,.92/max(np.max(np.abs(music+effects)),1e-12))
music*=gain;effects*=gain
music_path=RES/'music-original-v14.wav';effects_path=RES/'effects-original-v14.wav'
wav(music_path,music);wav(effects_path,effects)
premix=REVIEW/'audio-premix-v14.wav';wav(premix,music+effects)
premaster=REVIEW/'audio-premaster-v14.wav'
compression='acompressor=threshold=0.05:ratio=2.3:attack=3:release=110:makeup=1:knee=2.5'
subprocess.run(['ffmpeg','-v','error','-y','-i',str(premix),'-af',compression,
    '-ar',str(RATE),'-c:a','pcm_s16le',str(premaster)],check=True)

def levels(log):return json.loads(log[log.rfind('{'):log.rfind('}')+1])
analysis=subprocess.run(['ffmpeg','-hide_banner','-i',str(premaster),'-af',
    'loudnorm=I=-16:TP=-2:LRA=7:print_format=json','-f','null','-'],check=True,capture_output=True,text=True)
measured=levels(analysis.stderr)
filt=('loudnorm=I=-16:TP=-2:LRA=7:'+f'measured_I={measured["input_i"]}:measured_TP={measured["input_tp"]}:'+f'measured_LRA={measured["input_lra"]}:measured_thresh={measured["input_thresh"]}:'+f'offset={measured["target_offset"]}:linear=true:print_format=json')
output=ASSETS/'mix-v14.wav'
master=subprocess.run(['ffmpeg','-hide_banner','-y','-i',str(premaster),'-af',filt,
    '-ar',str(RATE),'-ac','2','-t',str(LENGTH),'-c:a','pcm_s16le',str(output)],check=True,capture_output=True,text=True)
(REVIEW/'audio-mastering-v14.log').write_text(analysis.stderr+'\nSECOND PASS\n'+master.stderr)
verify=subprocess.run(['ffmpeg','-hide_banner','-i',str(output),'-af',
    'loudnorm=I=-16:TP=-1.7:LRA=7:print_format=json','-f','null','-'],check=True,capture_output=True,text=True)
l=levels(verify.stderr)
with wave.open(str(output),'rb') as w:
    assert (w.getnchannels(),w.getframerate(),w.getsampwidth())==(2,RATE,2)
    encoded=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').reshape(-1,2)
decoded=encoded.astype(np.float64)/32768
report={'ok':len(decoded)==N and np.count_nonzero(np.abs(encoded.astype(np.int32))>=32767)==0
    and abs(float(l['input_i'])+16)<.4 and float(l['input_tp'])<=-1.7,
    'file':'assets/mix-v14.wav','sha256':sha(output),'duration_seconds':len(decoded)/RATE,
    'sample_rate':RATE,'channels':2,'sample_frames':len(decoded),'codec':'pcm_s16le',
    'integrated_lufs':float(l['input_i']),'true_peak_dbtp':float(l['input_tp']),
    'loudness_range_lu':float(l['input_lra']),'clipped_samples':int(np.count_nonzero(np.abs(encoded.astype(np.int32))>=32767)),
    'sample_peak_dbfs':float(20*np.log10(max(np.max(np.abs(decoded)),1e-12))),
    'original_new_music':True,'midi_notes':len(notes),'sfx_events':len(events),
    'old_music_stem_read_or_reused':False,'old_sfx_stem_read_or_reused':False,
    'reference_audio_reused':False,'narration_present':False,'rejected_voice_reused':False,
    'subjective_listening_performed':False,'continuous_playback_performed':False}
provenance={'version':'V14','music':'New original composition authored as MIDI and rendered with FluidSynth; not a remix or repeat of the V7/V12/V13 backing stems.',
    'bpm':BPM,'key_center':'E minor; open Em9/Cmaj9/G6/Dadd9 voicings','sections':[
        {'range':[0,6.35],'role':'Sparse individually phrased kinetic hook/local recognition'},
        {'range':[6.35,17.6],'role':'Four different melodic/harmonic phrases for case/distribution/locality/proof, with a metric breath'},
        {'range':[17.6,26],'role':'Renewed ascending CTA phrase, then chord resolution and an open final reading tail'}],
    'instruments':{'0':{'gm_program_zero_based':5,'name':'Electric Piano2'},'1':{'gm_program_zero_based':39,'name':'Synth Bass2'},
        '2':{'gm_program_zero_based':11,'name':'Vibraphone'},'3':{'gm_program_zero_based':89,'name':'Warm Pad'},'9':{'name':'Standard percussion'}},
    'soundfont':{'repository':'https://github.com/mrbumpy409/GeneralUser-GS','commit':PIN,'sha256':SF_SHA,
        'local_path_used':str(SF),'license':'GeneralUser GS License2.0 permits private/commercial musical recordings; complete original sample-provenance qualifications preserved in license file.',
        'required_for_recomposition_only':True,'required_to_render_video_from_wav':False},
    'effects':'New deterministic procedural PCM: pitch-drop impact, filtered-noise movement, staggered lamella fold and short tuned click. Formulas in compose-audio.py; seed140026. Not stock recordings or reference extractions.',
    'midi_file':str(midi.relative_to(ROOT)),'midi_sha256':sha(midi),'notes':notes,'events':events,
    'music_energy_points':energy_points,'music_short_ducks':ducks,'final_fade_seconds':.85,'premaster_linear_gain':gain,
    'timing_manifest_sha256':sha(TIMING),'output_sha256':sha(output),
    'source_files_sha256':{str(x.relative_to(ROOT)):sha(x) for x in [music_path,effects_path,RES/'GeneralUser-GS-LICENSE.txt']},
    'old_music_stem_read_or_reused':False,'old_sfx_stem_read_or_reused':False,'reference_audio_reused':False,'narration_present':False,
    'subjective_listening_performed':False,'premaster_compressor':compression,
    'instrument_vs_effects_balance':{'music_linear_gain':3.4,'effects_linear_gain':.85},'master_filter':filt,
    'requirements':['Python3','NumPy','SciPy','libfluidsynth3','FFmpeg','Verified GeneralUser GS SF2 for recomposition'],
    'regenerate':'python scripts/compose-audio.py; set EVOQUEX_SF2 only when the verified bank is outside the default cache'}
(RES/'provenance-v14.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
(REVIEW/'audio-validation-v14.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));assert report['ok'],'Audio mastering acceptance failed.'
