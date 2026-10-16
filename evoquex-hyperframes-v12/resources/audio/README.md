# Mixagem V12 — 30 segundos

`assets/mix-v12.wav` é um arquivo real PCM estéreo de 48 kHz, produzido com os dois stems preservados neste diretório. Não utiliza áudio das referências, fala do anúncio original, ElevenLabs, Kokoro ou voz simulada.

A composição original da Evoquex, em 120 BPM, foi reeditada em seis seções. Os pontos de corte mantêm a fase dos pulsos de 0,5 segundo e recebem crossfades de 16 ms. A intensidade diminui antes da entrada do filme e das métricas e volta a crescer no convite final. Há 18 acentos, derivados de três regiões reais do stem de efeitos: impacto, tick e movimento filtrado. Velocidade de reprodução, reversão, panorâmica e envelopes criam variações sem depender de arquivos externos. O instrumental recebe ducking curto nos impactos e nas passagens maiores.

Execute `python scripts/remix-audio.py` a partir da raiz do projeto para refazer o WAV. O script usa apenas Python, NumPy e FFmpeg já instalados, verifica os SHA-256 dos stems, masteriza em duas passagens e grava `review/audio-validation-v12.json`. A licença integral do banco GeneralUser GS foi preservada sem alterações. As informações e ressalvas de procedência do autor constam do texto da licença.

`provenance-v12.json` registra os recortes, velocidades, inversões, posições estéreo, envelopes, automações, tempos de cada efeito e hashes. O roteiro visual deve sincronizar os acentos com esses marcos, em vez de acrescentar um som por letra.

A aprovação técnica confere duração, codec, quantidade de amostras, loudness, true peak, canais, fade e ausência de clipping. **Não houve escuta subjetiva**: não existe ferramenta de reprodução auditiva disponível nesta interface. A locução natural permanece pendente e não foi representada como concluída.
