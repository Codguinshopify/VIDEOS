"""Build the revised continuous licensed music bed and cue-driven effects.

The Mixkit track and sounds are preserved by hash. The original two user-pack
effects remain in the edit. No voice or original campaign audio is mixed.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import wave

import numpy as np
from scipy.signal import butter, sosfilt

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "resources/audio"
ASSETS = ROOT / "assets"
REVIEW = ROOT / "review"
RATE = 48_000
CUES_PATH = RES / "cues-v15r1.json"
CUES = json.loads(CUES_PATH.read_text())
LENGTH = float(CUES["duration"])
COUNT = round(LENGTH * RATE)
TIME = np.arange(COUNT) / RATE

SOURCES = {
    "pack-impact": RES / "pack-sources/SFX - Impact 1.wav",
    "pack-swoosh": RES / "pack-sources/SFX - Fast Swoosh 1.wav",
    "tech-select": RES / "selected-sfx-v15r1/tech-select.wav",
    "tech-slide": RES / "selected-sfx-v15r1/tech-slide.wav",
    "interface-click": RES / "selected-sfx-v15r1/interface-click.wav",
    "high-tech-confirmation": RES / "selected-sfx-v15r1/high-tech-confirmation.wav",
    "metal-sweep": RES / "selected-sfx-v15r1/metal-sweep.wav",
}
MUSIC_SOURCE = ROOT / CUES["music"]["local_source"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(path, *, duration=None, speed=None):
    cmd = ["ffmpeg", "-v", "error", "-i", str(path)]
    if speed is not None:
        cmd += ["-af", f"atempo={speed:.7f}"]
    if duration is not None:
        cmd += ["-t", f"{duration:.6f}"]
    cmd += ["-ar", str(RATE), "-ac", "2", "-f", "f32le", "pipe:1"]
    raw = subprocess.run(cmd, check=True, capture_output=True).stdout
    return np.frombuffer(raw, dtype="<f4").reshape(-1, 2).astype(np.float64)


def write_wav(path, signal):
    assert signal.shape == (COUNT, 2)
    assert np.isfinite(signal).all() and np.max(np.abs(signal)) < 1
    with wave.open(str(path), "wb") as out:
        out.setnchannels(2)
        out.setsampwidth(2)
        out.setframerate(RATE)
        out.writeframes(np.rint(signal * 32767).astype("<i2").tobytes())


def loudness(path):
    proc = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(path), "-af",
         "loudnorm=I=-16:TP=-2.5:LRA=7:print_format=json", "-f", "null", "-"],
        check=True, capture_output=True, text=True,
    )
    return json.loads(proc.stderr[proc.stderr.rfind("{"):proc.stderr.rfind("}") + 1])


assert MUSIC_SOURCE.is_file()
assert all(path.is_file() for path in SOURCES.values())
music = decode(MUSIC_SOURCE, duration=LENGTH)
assert len(music) >= COUNT - 20, "Music source is shorter than the edit"
music = np.pad(music[:COUNT], ((0, max(0, COUNT - len(music))), (0, 0)))
music = sosfilt(butter(2, 30, fs=RATE, btype="highpass", output="sos"), music, axis=0)
envelope_points = np.array(CUES["music"]["energy_points"], dtype=float)
assert envelope_points[0, 0] == 0 and envelope_points[-1, 0] == LENGTH
music_envelope = np.interp(TIME, envelope_points[:, 0], envelope_points[:, 1])
for cue in CUES["events"]:
    if cue["source"] in {"pack-impact", "metal-sweep"}:
        center = cue["anchor"]
        lower = .74 if cue["id"] == "result-impact" else .87
        music_envelope *= np.interp(
            TIME, [max(0, center - .06), center, center + .10, center + .28],
            [1, lower, lower, 1],
        )
music *= music_envelope[:, None]
effects = np.zeros((COUNT, 2), dtype=np.float64)
events = []
for cue in CUES["events"]:
    path = SOURCES[cue["source"]]
    duration = cue["duration"]
    if cue["source"] == "pack-impact":
        clip = decode(path, duration=duration)
    else:
        original = decode(path)
        speed = (len(original) / RATE) / duration
        clip = decode(path, speed=speed)[:round(duration * RATE)]
    target_length = round(duration * RATE)
    clip = np.pad(clip[:target_length], ((0, max(0, target_length - len(clip))), (0, 0)))
    high = min(cue["lowpass_hz"], RATE * .47)
    clip = sosfilt(butter(2, [42, high], btype="bandpass", fs=RATE, output="sos"), clip, axis=0)
    attack = min(len(clip), round(.003 * RATE))
    release = min(len(clip), round(min(.105, duration * .29) * RATE))
    clip[:attack] *= np.linspace(0, 1, attack)[:, None]
    clip[-release:] *= np.linspace(1, 0, release)[:, None]
    peak = max(float(np.max(np.abs(clip))), 1e-12)
    clip *= 10 ** (cue["level_dbfs"] / 20) / peak
    pan = cue["pan"]
    clip *= np.array([np.sqrt(1 - pan), np.sqrt(1 + pan)])
    window = round(.01 * RATE)
    energy = np.array([np.mean(clip[i:i + window] ** 2)
                       for i in range(0, len(clip) - window + 1, window)])
    peak_offset = (int(np.argmax(energy)) * window + window / 2) / RATE
    start = max(0, round((cue["anchor"] - peak_offset) * RATE))
    end = min(COUNT, start + len(clip))
    effects[start:end] += clip[:end-start]
    events.append({**cue, "source_path": str(path.relative_to(ROOT)),
                   "source_sha256": sha(path), "start": start / RATE,
                   "end": end / RATE, "measured_energy_peak": start / RATE + peak_offset,
                   "alignment_error_seconds": start / RATE + peak_offset - cue["anchor"],
                   "treatment": "filtered, envelope shaped, gain matched, panned; tempo adjusted on non-impact effects"})

fade = np.ones(COUNT)
fade[:round(.12 * RATE)] = np.linspace(0, 1, round(.12 * RATE))
fade[-round(.44 * RATE):] = np.linspace(1, 0, round(.44 * RATE))
music *= fade[:, None]
effects *= fade[:, None]
premix = music + effects
headroom = min(1, .86 / max(float(np.max(np.abs(premix))), 1e-12))
music *= headroom
effects *= headroom
music_path = RES / "music-v15r1.wav"
effects_path = RES / "effects-v15r1.wav"
premix_path = REVIEW / "audio-premix-v15r1.wav"
write_wav(music_path, music)
write_wav(effects_path, effects)
write_wav(premix_path, music + effects)
first = loudness(premix_path)
filter_string = (
    "loudnorm=I=-16:TP=-2.5:LRA=7:"
    f"measured_I={first['input_i']}:measured_TP={first['input_tp']}:"
    f"measured_LRA={first['input_lra']}:measured_thresh={first['input_thresh']}:"
    f"offset={first['target_offset']}:linear=true"
)
output = ASSETS / "mix-v15r1.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(premix_path),
                "-af", filter_string, "-ar", str(RATE), "-ac", "2", "-t", str(LENGTH),
                "-c:a", "pcm_s16le", str(output)], check=True)
measured = loudness(output)
decoded = decode(output)
report = {
    "version": "V15R1", "file": str(output.relative_to(ROOT)), "sha256": sha(output),
    "duration": len(decoded) / RATE, "channels": 2, "sample_rate": RATE,
    "integrated_lufs": float(measured["input_i"]),
    "actual_true_peak_dbtp": float(measured["input_tp"]),
    "clipped_samples": int(np.count_nonzero(np.abs(decoded) >= 32767/32768)),
    "last_sample_abs": float(np.max(np.abs(decoded[-1]))),
    "cue_count": len(events), "distinct_effect_sources": len(set(e["source_path"] for e in events)),
    "continuous_music": True, "narration_present": False, "subjective_listening_performed": False,
}
report["ok"] = (len(decoded) == COUNT and abs(report["integrated_lufs"] + 16) < .5
                and report["actual_true_peak_dbtp"] <= -2.0 and report["clipped_samples"] == 0)
sources = {str(path.relative_to(ROOT)): sha(path) for path in SOURCES.values()}
provenance = {
    "version": "V15R1", "source_music": {**CUES["music"], "sha256": sha(MUSIC_SOURCE)},
    "music_license_evidence": "Mixkit page lists Close Up under Stock Music Free License; free-music FAQ states online advertising use and no attribution required.",
    "music_license_url": "https://mixkit.co/license/#musicFree",
    "user_pack_origin": "Original 6000+ Motion Graphics Pack V5.1; user authorized commercial use.",
    "mixkit_effect_license_url": "https://mixkit.co/license/#sfxFree",
    "source_files": sources, "events": events,
    "music_energy_points": CUES["music"]["energy_points"],
    "mixing": {"headroom_gain": headroom, "master_filter": filter_string,
               "music_stem_sha256": sha(music_path), "effects_stem_sha256": sha(effects_path)},
    "narration_present": False, "subjective_listening_performed": False,
    "future_voice": "Retain stems, retime to external ElevenLabs recording and apply speech-guided ducking later.",
}
(RES / "provenance-v15.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")
(REVIEW / "audio-validation-v15r1.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False, indent=2))
assert report["ok"], "Revised audio mastering failed acceptance"
