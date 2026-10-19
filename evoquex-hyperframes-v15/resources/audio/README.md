# Áudio ativo da revisão V15R1

O arquivo reproduzido pela composição é `assets/mix-v15r1.wav`: 23,4 s, 48 kHz,
estéreo. Ele inclui a trilha instrumental contínua **Close Up**, de Michael Ramir
C. (Mixkit), cinco efeitos Mixkit e dois efeitos do pack fornecido pelo usuário.
Há 17 acentos sonoros ligados a movimentos concretos; nenhum áudio de locução ou
voz original da filmagem entra no mix. Os níveis da música variam em torno das
entradas gráficas e do número, sem interromper a trilha.

Origem, URLs de licença, hashes, janelas e funções de cada som estão em
`cues-v15r1.json` e `provenance-v15.json`. Os arquivos `music-v15r1.wav` e
`effects-v15r1.wav` são stems separados para facilitar a futura integração da
locução do ElevenLabs. Para reconstruir o mix, execute
`python scripts/build-audio-v15r1.py`. O relatório técnico fica em
`review/audio-validation-v15r1.json`. A música Mixkit usa a Stock Music Free
License, que permite uso em publicidade online; os efeitos Mixkit seguem a
licença gratuita de SFX. O usuário autorizou uso comercial dos seus packs.

O projeto V15 original tinha outro áudio, preservado como histórico. Sua receita
continua em `scripts/build-audio-v15.py`, mas não é usada por esta versão.

Quando a voz chegar, ajustar cenas e âncoras às frases, aplicar ducking por fala e
renderizar novamente. Nenhum julgamento de naturalidade da voz é possível antes de
receber o arquivo real. O relatório atual mede loudness, pico verdadeiro, duração
e clipping; ele não equivale a escuta subjetiva da mixagem.
