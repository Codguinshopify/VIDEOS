"""Retimed original Evoquex score + real user-pack SFX; no voice/TTS/network.

The V14 authored note score is explicitly reused and re-rendered onto V15 scene
anchors, not advertised as a new melody. The old mixed audio and old procedural
SFX are never loaded. Keep cue data and stems separate for future external VO.
"""
from pathlib import Path
import ctypes as ct
import ctypes.util
import hashlib
import json
import os
import subprocess
import wave

import numpy as np
from scipy.signal import butter, sosfilt

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "resources/audio"
REVIEW = ROOT / "review"
ASSETS = ROOT / "assets"
for directory in (RES, REVIEW, ASSETS):
    directory.mkdir(parents=True, exist_ok=True)

RATE = 48000
CUE_PATH = RES / "cues-v15.json"
CUES = json.loads(CUE_PATH.read_text())
LENGTH = CUES["duration"]
N = round(LENGTH * RATE)
TIMES = np.arange(N) / RATE
SOURCE_SCORE = RES / "source-score-v14.json"
SCORE = json.loads(SOURCE_SCORE.read_text())
SF = Path(os.environ.get("EVOQUEX_SF2", "/workspace/.cache/evoquex-audio/GeneralUser-GS.sf2"))
SF_SHA = "9575028c7a1f589f5770fccc8cff2734566af40cd26ed836944e9a5152688cfe"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_wav(path, pcm):
    assert pcm.shape == (N, 2) and np.isfinite(pcm).all()
    assert np.max(np.abs(pcm)) < 1, f"Clipping before quantization: {path.name}"
    with wave.open(str(path), "wb") as target:
        target.setnchannels(2)
        target.setsampwidth(2)
        target.setframerate(RATE)
        target.writeframes(np.round(pcm * 32767).astype("<i2").tobytes())


def read_audio(path, filters=None):
    command = ["ffmpeg", "-v", "error", "-i", str(path)]
    if filters:
        command += ["-af", filters]
    command += ["-ar", str(RATE), "-ac", "2", "-f", "f32le", "pipe:1"]
    result = subprocess.run(command, capture_output=True, check=True)
    return np.frombuffer(result.stdout, dtype="<f4").reshape(-1, 2).astype(np.float64)


def retime(t):
    return float(np.interp(t, CUES["old_music_anchors"], CUES["new_music_anchors"]))


# Preserve note identity and harmonic language; re-render at new performance times.
assert SF.is_file(), "Recomposition needs GeneralUser GS; a normal video render only needs the final WAV."
assert sha(SF) == SF_SHA, "Unexpected soundfont contents"
notes = []
for old in SCORE["notes"]:
    note = dict(old)
    start, end = retime(old["time"]), retime(old["time"] + old["duration"])
    # CTA has no drum fill; the musical resolution gets room to finish.
    if note["channel"] == 9 and start >= 22.45:
        continue
    note.update(time=round(start, 6), duration=round(max(.035, end - start), 6))
    if start >= 22.45 and note["channel"] in (1, 2):
        note["velocity"] = max(20, round(note["velocity"] * .82))
    notes.append(note)

library = ct.CDLL(ctypes.util.find_library("fluidsynth"))


def api(name, result, arguments):
    function = getattr(library, name)
    function.restype, function.argtypes = result, arguments
    return function


P, I, D, S = ct.c_void_p, ct.c_int, ct.c_double, ct.c_char_p
settings = api("new_fluid_settings", P, [])()
setnum = api("fluid_settings_setnum", I, [P, S, D])
setint = api("fluid_settings_setint", I, [P, S, I])
setnum(settings, b"synth.sample-rate", RATE)
setnum(settings, b"synth.gain", .48)
for key in (b"synth.reverb.active", b"synth.chorus.active"):
    setint(settings, key, 0)
setint(settings, b"synth.cpu-cores", 1)
synth = api("new_fluid_synth", P, [P])(settings)
assert api("fluid_synth_sfload", I, [P, S, I])(synth, str(SF).encode(), 1) >= 0
program = api("fluid_synth_program_change", I, [P, I, I])
control = api("fluid_synth_cc", I, [P, I, I, I])
noteon = api("fluid_synth_noteon", I, [P, I, I, I])
noteoff = api("fluid_synth_noteoff", I, [P, I, I])
render = api("fluid_synth_write_float", I, [P, I, P, I, I, P, I, I])
for channel, preset in {0: 5, 1: 39, 2: 11, 3: 89}.items():
    program(synth, channel, preset)
for channel, volume in {0: 78, 1: 88, 2: 76, 3: 48, 9: 82}.items():
    pan = {0: 48, 1: 64, 2: 80, 3: 66, 9: 64}[channel]
    for controller, value in ((7, volume), (10, pan), (91, 0), (93, 0)):
        control(synth, channel, controller, value)

queue = []
for note in notes:
    queue.append((round(note["time"] * RATE), 1, note["channel"], note["pitch"], note["velocity"]))
    queue.append((round((note["time"] + note["duration"]) * RATE), 0, note["channel"], note["pitch"], 0))
queue.sort()
music = np.zeros((N, 2), dtype=np.float64)
cursor = 0


def render_until(end):
    global cursor
    end = min(end, N)
    count = end - cursor
    if count <= 0:
        return
    left, right = np.zeros(count, np.float32), np.zeros(count, np.float32)
    assert render(synth, count, left.ctypes.data, 0, 1, right.ctypes.data, 0, 1) == 0
    music[cursor:end] = np.column_stack((left, right))
    cursor = end


for sample, state, channel, pitch, velocity in queue:
    if sample >= N:
        break
    render_until(sample)
    if state:
        noteon(synth, channel, pitch, velocity)
    else:
        noteoff(synth, channel, pitch)
render_until(N)
api("delete_fluid_synth", None, [P])(synth)
api("delete_fluid_settings", None, [P])(settings)
reflections = sosfilt(butter(2, 4200, fs=RATE, output="sos"), music, axis=0)
for seconds, gain, swap in ((.073, .13, True), (.137, .075, False)):
    delay = round(seconds * RATE)
    layer = reflections[:-delay, ::-1] if swap else reflections[:-delay]
    music[delay:] += layer * gain

source_paths = {
    "swoosh": RES / "pack-sources/SFX - Fast Swoosh 1.wav",
    "impact": RES / "pack-sources/SFX - Impact 1.wav",
}
source_data = {kind: read_audio(path) for kind, path in source_paths.items()}
effects = np.zeros((N, 2), dtype=np.float64)
actual_events = []
for cue in CUES["events"]:
    kind = cue["source"]
    if kind == "swoosh":
        # Resample the time envelope without changing the pitch. Every treatment
        # remains traceable to the actual supplied WAV, not synthetic placeholder.
        ratio = (len(source_data[kind]) / RATE) / cue["duration"]
        clip = read_audio(source_paths[kind], f"atempo={ratio:.9f}")
    else:
        clip = source_data[kind][:round(cue["duration"] * RATE)].copy()
    clip = clip[:round(cue["duration"] * RATE)]
    clip = sosfilt(butter(2, [40, cue["lowpass"]], btype="bandpass", fs=RATE, output="sos"), clip, axis=0)
    attack, release = round(.003 * RATE), round(min(.12, cue["duration"] * .35) * RATE)
    clip[:attack] *= np.linspace(0, 1, attack)[:, None]
    clip[-release:] *= np.linspace(1, 0, release)[:, None]
    peak = max(np.max(np.abs(clip)), 1e-12)
    clip *= 10 ** (cue["level_dbfs"] / 20) / peak
    pan = cue["pan"]
    clip *= np.array([np.sqrt(1 - pan), np.sqrt(1 + pan)])
    # The measured short-window energy maximum, not file start, is synchronized.
    block = round(.01 * RATE)
    energy = np.array([np.mean(clip[i:i+block] ** 2) for i in range(0, len(clip)-block+1, block)])
    peak_offset = (int(np.argmax(energy)) * block + block / 2) / RATE
    audible_anchor = cue["anchor"] - cue["peak_lead"]
    start = max(0, round((audible_anchor - peak_offset) * RATE))
    end = min(N, start + len(clip))
    effects[start:end] += clip[:end-start]
    actual_events.append({**cue, "source_path": str(source_paths[kind].relative_to(ROOT)),
                          "source_sha256": sha(source_paths[kind]), "start": start / RATE,
                          "end": end / RATE, "measured_energy_peak": start / RATE + peak_offset,
                          "alignment_error_seconds": start / RATE + peak_offset - audible_anchor,
                          "peak_measurement_window_seconds": .01,
                          "treatment": "atempo + bandpass + edge envelope + stereo pan" if kind == "swoosh" else "trim + bandpass + edge envelope"})

energy = np.array(CUES["music_energy_points"], dtype=float)
music_envelope = np.interp(TIMES, energy[:, 0], energy[:, 1])
for event in actual_events:
    anchor = event["anchor"]
    floor = .67 if event["source"] == "impact" else .83
    duck = np.interp(TIMES, [max(0, anchor-.055), anchor, anchor+.06, anchor+.24], [1, floor, floor, 1])
    music_envelope *= duck
music *= music_envelope[:, None] * 3.1
fade = np.ones(N)
fade[:round(.003 * RATE)] = np.linspace(0, 1, round(.003 * RATE))
fade[-round(.4 * RATE):] = np.linspace(1, 0, round(.4 * RATE))
music *= fade[:, None]
effects *= fade[:, None]
gain = min(1.0, .91 / max(np.max(np.abs(music + effects)), 1e-12))
music *= gain
effects *= gain
music_path, effects_path = RES / "music-v15.wav", RES / "pack-effects-v15.wav"
write_wav(music_path, music)
write_wav(effects_path, effects)
premix = REVIEW / "audio-premix-v15.wav"
write_wav(premix, music + effects)
premaster = REVIEW / "audio-premaster-v15.wav"
compression = "highpass=f=35,acompressor=threshold=0.065:ratio=2:attack=4:release=110:makeup=1:knee=2.5"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(premix), "-af", compression,
                "-ar", str(RATE), "-c:a", "pcm_s16le", str(premaster)], check=True)


def loudness(path):
    result = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(path), "-af",
                             "loudnorm=I=-16:TP=-2:LRA=7:print_format=json", "-f", "null", "-"],
                            capture_output=True, text=True, check=True)
    text = result.stderr
    return json.loads(text[text.rfind("{"):text.rfind("}")+1]), text


measured, first_log = loudness(premaster)
normalization = ("loudnorm=I=-16:TP=-2:LRA=7:"
                 f"measured_I={measured['input_i']}:measured_TP={measured['input_tp']}:"
                 f"measured_LRA={measured['input_lra']}:measured_thresh={measured['input_thresh']}:"
                 f"offset={measured['target_offset']}:linear=true:print_format=json")
output = ASSETS / "mix-v15.wav"
master = subprocess.run(["ffmpeg", "-hide_banner", "-y", "-i", str(premaster), "-af", normalization,
                         "-ar", str(RATE), "-ac", "2", "-t", str(LENGTH), "-c:a", "pcm_s16le", str(output)],
                        capture_output=True, text=True, check=True)
levels, final_log = loudness(output)
decoded = read_audio(output)
tail_rms = float(np.sqrt(np.mean(decoded[-round(.01*RATE):] ** 2)))
report = {
    "file": "assets/mix-v15.wav", "sha256": sha(output), "duration": len(decoded)/RATE,
    "sample_rate": RATE, "channels": 2, "sample_frames": len(decoded), "codec": "pcm_s16le",
    "integrated_lufs": float(levels["input_i"]), "true_peak_dbtp": float(levels["input_tp"]),
    "loudness_range_lu": float(levels["input_lra"]), "clipped_samples": int(np.count_nonzero(np.abs(decoded)>=32767/32768)),
    "tail_10ms_rms_dbfs": float(20*np.log10(max(tail_rms,1e-12))),
    "final_sample_abs": float(np.max(np.abs(decoded[-1]))),
    "music": "Re-rendered and retimed inherited original Evoquex V14 score, with thinner CTA percussion",
    "notes": len(notes), "pack_sfx_events": len(actual_events), "distinct_pack_files_used": len(source_paths),
    "narration_present": False, "reference_audio_reused": False, "old_mix_or_effect_stem_loaded": False,
    "subjective_listening_performed": False, "continuous_playback_performed": False,
    "cue_manifest_sha256": sha(CUE_PATH), "source_score_sha256": sha(SOURCE_SCORE),
    "soundfont_sha256": sha(SF), "music_stem_sha256": sha(music_path), "effects_stem_sha256": sha(effects_path)
}
report["ok"] = (len(decoded)==N and abs(report["integrated_lufs"]+16)<.4 and report["true_peak_dbtp"]<=-1.8
                and report["clipped_samples"]==0 and report["final_sample_abs"]<.0001)
provenance = {
    "version": "V15", "music_score_origin": "V14 original authored MIDI notes, preserved in source-score-v14.json",
    "retiming": {"old": CUES["old_music_anchors"], "new": CUES["new_music_anchors"]}, "notes": notes,
    "pack_origin": "User supplied 6000+ Motion Graphics Pack V5.1; original extractions preserved in biblioteca/packs/6000-motion-audit-v13",
    "usage_authorization": "User explicitly authorized supplied resources, including commercial usage; no invented blanket third-party license",
    "source_files": {str(path.relative_to(ROOT)): sha(path) for path in source_paths.values()},
    "events": actual_events, "music_energy_points": CUES["music_energy_points"],
    "source_music_license": "GeneralUser-GS-LICENSE.txt; verified SF2 only needed for music recomposition",
    "premix_gain": gain, "master_filter": normalization, "premaster_filter": compression,
    "subjective_listening_performed": False, "narration_present": False,
    "future_voice_workflow": "Use separate music-v15.wav/pack-effects-v15.wav; retime scene anchors and cues from actual external ElevenLabs recording, then add voice-led ducking and remaster. No TTS required."
}
(RES / "provenance-v15.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2)+"\n")
(REVIEW / "audio-validation-v15.json").write_text(json.dumps(report, indent=2)+"\n")
(REVIEW / "audio-mastering-v15.log").write_text(first_log+"\nSECOND PASS\n"+master.stderr+"\nFINAL\n"+final_log)
print(json.dumps(report, indent=2))
assert report["ok"], "Audio mastering acceptance failed"
