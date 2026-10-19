# V15 exported audio review

Technical checks pass for `renders/evoquex-hyperframes-v15.mp4`, SHA-256 `b49533215c68181ad225d74de8aa58de6e4ee496e5a330bdec9d62caa1724e1d`, frozen source bundle `c2968c97deb6c129d7c87d098da4c27f10e080d6bf28817a98b2e4cfe49138d6`. All frozen input hashes still match. No runtime, source, audio-generation or QA script was changed.

The exported AAC is 48 kHz stereo over 27.6 s. Existing full-program output validation reports −16.22 LUFS, −1.55 dBTP, 6.70 LU loudness range and zero clipped samples. These are the loudnorm **input** measurements of the actual export; its diagnostic `output_tp=-1.80` is not the exported peak. Source WAV measurements are −16.21 LUFS and −1.98 dBTP. AAC increases true peak by 0.43 dB, leaving 1.55 dB headroom. The source meets the README's −1.8 dBTP source threshold; the AAC is 0.25 dB above that value. Enforcing −1.8 dBTP on the encoded deliverable would require a newly mastered/frozen/rendered version.

Whole-program correlation between exported AAC and the intended WAV is 0.9996935. The campaign clip has both `muted` and `data-volume="0"`, and the only active audio element is the prepared music/effects mix. An independent decode of the full 6.74–10.30 s campaign window correlates 0.9998466 with the same WAV segment, with a difference RMS of −52.16 dBFS. Together with the frozen generator's music/pack-only inputs, this supports no original campaign voice being mixed. It is not a subjective speech-listening claim.

The two actual pack WAVs match their preserved library originals by SHA-256. Independently reconstructing all thirteen treated cues from those WAVs reproduces `pack-effects-v15.wav` exactly at PCM level: zero sample differences, with 437,251 nonzero channel samples. The premix equals the two stems' sum within one PCM least-significant bit, as expected from separate quantization. Thus the effects have waveform evidence beyond filenames and provenance declarations.

All thirteen isolated energy maxima match `anchor − peak_lead` at sample precision using the declared 10 ms windows. Scene boundaries agree with the active timing contract; three cue scene names are semantic aliases (`location`/`target`, `invitation`/`cta`, `signature`/`brand`). The principal proof impact is at 16.20 s; swooshes intentionally anticipate their listed visual cue by 30–120 ms. This validates declared placement, not subjective perceptual audiovisual synchronization.

A separate decode of the final second confirms the last 10 ms and final sample are exactly silent. The source WAV also ends at zero. No voice/TTS was generated or configured; separate stems and the external ElevenLabs handoff remain available.

No subjective listening or continuous playback was possible. Full-program measurements were reused from `output-validation-v15.json`; this review independently checked current hashes, source treatment reconstruction, the campaign window, cue placement, stem summing and the final sample tail. Detailed measurements and methods are in `export-audio-review-v15.json`.

## Replacement render and superseded result

The reviewed deliverable is now SHA-256 `b49533215c68181ad225d74de8aa58de6e4ee496e5a330bdec9d62caa1724e1d`, bundle `c2968c97deb6c129d7c87d098da4c27f10e080d6bf28817a98b2e4cfe49138d6`. The prior candidate, `review/candidate-e69aa4b4fdcb.mp4` (SHA-256 `e69aa4b4fdcb99395b2707bbca27c59dd67cba64f50347eeb1684a8b630913bc`, bundle `014ead5abeff35217566d3aaab8de48a8ed9f8bffa2e49982aad432e1233b9d5`), is superseded after a visual CSS correction. Frozen input comparison confirms that only `style.css` changed.

Both AAC streams are byte-identical after lossless ADTS extraction: 696,315 bytes each, SHA-256 `1cb341676f3da54e25e0d433307a85955f235ba09dfc2997dd6fc82c3636dd78`. All audio packet timestamps, durations, flags and side data, plus selected stream timing metadata, also match exactly. The prior independent segment and tail checks therefore apply unchanged to the replacement. Current output QA independently confirms the same −16.22 LUFS, −1.55 dBTP, zero clipping and 0.9996935 source correlation for the new MP4. Subjective listening remains unavailable.
