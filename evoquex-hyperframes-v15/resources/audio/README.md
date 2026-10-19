# Áudio V15 — trilha autoral retimada e efeitos reais do pack

O arquivo ativo é `assets/mix-v15.wav`, estéreo a 48 kHz, com 27,6 segundos.
Não há narração, geração TTS nem áudio do clipe original nesta etapa. O usuário
fornecerá posteriormente a locução externa do ElevenLabs.

A música aproveita o **score autoral da V14**, reexecutado por FluidSynth com os
tempos da V15. Não é anunciado como uma composição inédita. As notas, acordes e
instrumentos foram preservados, mas as frases agora seguem os nove blocos, a
percussão é retirada da chamada final e o acorde de assinatura começa em 25,1 s.
O mix antigo e o stem de efeitos sintéticos da V14 não são lidos pelo script.

O sound design usa gravações efetivamente extraídas do pack do usuário:

| Original preservado | Uso na V15 | Tratamento |
| --- | --- | --- |
| `SFX - Fast Swoosh 1.wav` | Faixa do hook, abertura da cidade, tinta que revela o vídeo, borda que vira seta, seta/pino, flare, passagem à estratégia e convite | Recortes de 0,32–0,62 s, alteração temporal sem alterar pitch, filtros, panorama moderado e envelopes |
| `SFX - Impact 1.wav` | Primeiro quadro, pergunta coral, contato discreto do pino, chegada de `20 mil` e resolução da marca | Recortes de 0,14–1,05 s, filtro e níveis próprios para cada gesto |

São **dois arquivos-fonte e treze acentos**, não treze assets distintos. O maior
impacto ocorre em 16,20 s; não há som em cada palavra. O espectador recebe espaço
de leitura em 17,4–19,1 s e 24–25 s. A última resolução musical é seguida por
decay, com fade integral até 27,6 s. Os acentos quietos do pino e da assinatura
são trechos filtrados do Impact 1, não sons de interface fabricados ou arquivos
inexistentes.

Os WAV originais pequenos estão em `pack-sources/`, com hashes e origem em
`provenance-v15.json`. A autorização comercial explícita do usuário é registrada
sem inventar uma licença genérica do fornecedor. O pack Viral foi inspecionado
pelo agente de assets e não continha novos efeitos de áudio utilizáveis; a música
de demonstração de terceiros não foi extraída.

`music-v15.wav` e `pack-effects-v15.wav` são stems separados. `cues-v15.json`
mantém cenas, âncoras, volumes, filtros e automação musical. O máximo de energia
medido de cada efeito é alinhado à transformação, permitindo antecipação declarada
em whooshes. A medição tem janela de 10 ms; não constitui escuta subjetiva.

Para recompor: `python3 scripts/build-audio-v15.py`. Requer Python, NumPy, SciPy,
FFmpeg, libfluidsynth e o SoundFont GeneralUser GS preservado por hash. O banco
fica no cache `/workspace/.cache/evoquex-audio/GeneralUser-GS.sf2`; um caminho
alternativo pode ser passado em `EVOQUEX_SF2`. Fonte fixada:
`https://github.com/mrbumpy409/GeneralUser-GS` revisão
`684543d5e5efaef08d02be50dcda8d552478fa60`, SHA-256
`9575028c7a1f589f5770fccc8cff2734566af40cd26ed836944e9a5152688cfe`.
A licença original está em `GeneralUser-GS-LICENSE.txt`. A exportação normal do
vídeo usa somente o WAV pronto e não precisa executar esse sintetizador.

Quando a voz real chegar, atualizar as âncoras de cenas, sincronizar os cues e as
animações às frases, adicionar a locução em stem separado e aplicar automação de
volume guiada pela fala antes de masterizar novamente. Não aplicar ducking de voz
agora: não há locução presente. A soma atual usa apenas ducking musical breve para
valorizar as transições e os impactos.

Validação técnica em `review/audio-validation-v15.json`: duração integral,
decodificação, clipping, LUFS, pico verdadeiro, encerramento e procedência. A
aceitação é cerca de −16 LUFS e pico verdadeiro até −1,8 dBTP. A interface não
fornece escuta subjetiva: não afirmar que a mixagem foi ouvida ou aprovada por
audição. O áudio do MP4 final ainda precisa ser medido e correlacionado com este
WAV depois da exportação do vídeo.
