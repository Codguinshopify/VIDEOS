"""Validate the actual V14 export against current timing, facts and soundtrack."""
from pathlib import Path
import subprocess, json, hashlib, re, importlib.util, argparse
import numpy as np
P = Path(__file__).resolve().parent.parent
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    config = json.loads((P / 'resources/qa-contract-v14.json').read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video', type=Path, default=P / config['render_file'])
    args = parser.parse_args()
    video = args.video.resolve()
    info = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(video)]))
    v = next(x for x in info['streams'] if x['codec_type'] == 'video')
    a = next(x for x in info['streams'] if x['codec_type'] == 'audio')
    assert [v['width'], v['height']] == config['dimensions']
    assert int(v['nb_frames']) == config['expected_frames'] and v['r_frame_rate'] == f"{config['fps']}/1"
    assert v['codec_name'] == 'h264' and v['pix_fmt'] == 'yuv420p' and v['color_space'] == 'bt709'
    assert abs(float(info['format']['duration']) - config['duration_seconds']) < .06
    assert a['codec_name'] == 'aac' and a['sample_rate'] == '48000' and a['channels'] == 2
    subprocess.run(['ffmpeg', '-v', 'error', '-xerror', '-i', str(video), '-f', 'null', '-'], capture_output=True, check=True)
    mix = P / 'assets/mix-v14.wav'
    provenance_path = P / 'resources/audio/provenance-v14.json'
    provenance = json.loads(provenance_path.read_text())
    recorded_hash = provenance.get('output_sha256', provenance.get('mix_sha256'))
    assert recorded_hash and sha(mix) == recorded_hash, 'V14 mix/provenance hash mismatch'
    def pcm(path):
        return np.frombuffer(subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(path), '-vn',
                               '-ar', '48000', '-ac', '2', '-f', 'f32le', '-']), dtype='<f4').reshape(-1, 2)
    encoded, source = pcm(video), pcm(mix)
    n = min(len(encoded), len(source))
    assert abs(len(encoded) - len(source)) <= 2048
    correlation = float(np.corrcoef(encoded[:n].reshape(-1), source[:n].reshape(-1))[0, 1])
    assert correlation > .98
    clipped = int(np.sum(np.abs(encoded) >= 1))
    assert clipped == 0
    measured = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(video), '-af',
                              'loudnorm=I=-16:TP=-1.8:LRA=7:print_format=json', '-f', 'null', '-'],
                             capture_output=True, text=True, check=True)
    levels = json.loads(re.findall(r'\{[^{}]*"input_i"[^{}]*\}', measured.stderr, re.S)[-1])
    assert float(levels['input_tp']) < 0
    spec = importlib.util.spec_from_file_location('active_source_validation', P / 'scripts/validate-source.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    source_report = module.validate_source(write_report=True)
    runtime_file = P / 'review/runtime-inspection-v14.json'
    runtime = json.loads(runtime_file.read_text()) if runtime_file.is_file() else None
    report = {'ok': True, 'version': 'V14', 'file': video.name, 'sha256': sha(video), 'bytes': video.stat().st_size,
              'duration': float(info['format']['duration']), 'frames': config['expected_frames'],
              'dimensions': config['dimensions'], 'fps': config['fps'], 'video_codec': v['codec_name'],
              'pixel_format': v['pix_fmt'], 'color_space': v['color_space'], 'audio_codec': a['codec_name'],
              'audio_rate': 48000, 'audio_channels': 2, 'full_decode_passed': True,
              'soundtrack_sha256': sha(mix), 'provenance_sha256': sha(provenance_path),
              'encoded_mix_correlation': correlation, 'clipped_samples': clipped, 'loudness': levels,
              'active_metric': source_report['active_metric'], 'metric_independently_verified': False,
              'old_screenshot_not_referenced': True, 'unique_real_footage_union_seconds': source_report['unique_footage_union_seconds'],
              'runtime_watermark_inspection': runtime, 'narration_present': False,
              'hook_pixel_identity_required': False, 'reference_audio_reused': False,
              'subjective_listening_performed': False, 'continuous_playback_performed': False,
              'visual_quality_approved_by_this_script': False}
    (P / 'review/output-validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
