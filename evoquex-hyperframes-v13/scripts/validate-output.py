"""Validate the actual V13 MP4; technical audio checks do not imply listening."""
from pathlib import Path
import subprocess, json, hashlib, re, importlib.util
import numpy as np

P = Path(__file__).resolve().parent.parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate():
    video = P / 'renders/evoquex-hyperframes-v13.mp4'
    q = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(video)]))
    v = next(x for x in q['streams'] if x['codec_type'] == 'video')
    a = next(x for x in q['streams'] if x['codec_type'] == 'audio')
    assert (v['width'], v['height'], v['nb_frames'], v['r_frame_rate']) == (1080, 1920, '900', '30/1')
    assert v['codec_name'] == 'h264' and v['pix_fmt'] == 'yuv420p' and v['color_space'] == 'bt709'
    assert abs(float(q['format']['duration']) - 30) < .06
    assert a['codec_name'] == 'aac' and a['sample_rate'] == '48000' and a['channels'] == 2
    subprocess.run(['ffmpeg', '-v', 'error', '-xerror', '-i', str(video), '-f', 'null', '-'], capture_output=True, check=True)
    expected = {'campanha.mp4': '01144794dd01f913af3d6fe1c24563a74ee89461b44289ac4a0dd5534139d335',
                'clevelandia.jpg': 'a5bba18170e69a3b9db2203d0babbb39b341217772a1794495718afaa7b331a1',
                'resultados.jpg': 'e99bf6462689f5d84b7e47f23af46c9fa60b7dd310f0fb5d9c9b324a90ed0147'}
    for name, digest in expected.items():
        assert sha(P / 'assets' / name) == digest, name
    mix = P / 'assets/mix-v13.wav'
    provenance_path = P / 'resources/audio/provenance-v13.json'
    provenance = json.loads(provenance_path.read_text())
    assert sha(mix) == provenance['output_sha256']

    def pcm(path):
        raw = subprocess.check_output(['ffmpeg', '-v', 'error', '-i', str(path), '-vn', '-ar', '48000', '-ac', '2', '-f', 'f32le', '-'])
        return np.frombuffer(raw, dtype='<f4').reshape(-1, 2)

    encoded, source = pcm(video), pcm(mix)
    n = min(len(encoded), len(source))
    assert abs(len(encoded) - len(source)) <= 2048, 'Audio length differs from source mix'
    correlation = float(np.corrcoef(encoded[:n].reshape(-1), source[:n].reshape(-1))[0, 1])
    assert correlation > .98
    clipped = int(np.sum(np.abs(encoded) >= 1))
    assert clipped == 0
    x = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(video), '-af',
                        'loudnorm=I=-16:TP=-1.8:LRA=7:print_format=json', '-f', 'null', '-'],
                       capture_output=True, text=True, check=True)
    levels = json.loads(re.findall(r'\{[^{}]*"input_i"[^{}]*\}', x.stderr, re.S)[-1])
    assert float(levels['input_tp']) < 0
    spec = importlib.util.spec_from_file_location('v13_validate_source', P / 'scripts/validate-source.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    source_report = module.validate_source(write_report=True)
    report = {'ok': True, 'file': video.name, 'version': 'V13',
              'engine': 'HyperFrames 0.8.162 / HTML, SVG, GSAP 3.14.2',
              'duration': float(q['format']['duration']), 'frames': 900, 'dimensions': [1080, 1920], 'fps': 30,
              'video_codec': v['codec_name'], 'pixel_format': v['pix_fmt'], 'color_space': v['color_space'],
              'audio_codec': a['codec_name'], 'audio_rate': 48000, 'audio_channels': 2,
              'mix_v13_sha256': sha(mix), 'mix_provenance_sha256': sha(provenance_path),
              'new_v13_mix_correlation': correlation, 'clipped_samples': clipped, 'loudness': levels,
              'full_decode_passed': True, 'same_original_media_sha256': expected,
              'metrics': {'reach': 13064, 'impressions': 20981}, 'business': 'Danny’s Presentes',
              'source_copy_contract': source_report['copy_contract'],
              'narration_present': False, 'original_footage_playback_count': 1,
              'original_footage_audio_gain': 0, 'reference_audio_reused': False,
              'subjective_listening_performed': False, 'continuous_playback_performed': False,
              'bytes': video.stat().st_size, 'sha256': sha(video)}
    (P / 'review').mkdir(exist_ok=True)
    (P / 'review/output-validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    validate()
