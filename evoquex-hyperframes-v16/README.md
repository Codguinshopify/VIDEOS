# Evoquex — Danny’s Presentes · V16

Vídeo vertical de 44 s, 1080 × 1920, 30 fps. Abertura herdada da V15R1 (0–3 s); cenas restantes recriadas no HyperFrames com composição e movimentos estudados nas referências Oto Criativo e Park Criativo. Sem locução nesta etapa; a faixa `resources/audio/music-v16.wav` e os efeitos `resources/audio/effects-v16.wav` são stems separados para sincronizar a futura voz do ElevenLabs.

## Estrutura

- 0–3 s: abertura aprovada da V15R1.
- 3–8 s: campo escuro e frase com órbitas e desenho de linha. A redação “Quem é visto não é lembrado” segue exatamente a confirmação do cliente.
- 8–15 s: cartão central com o vídeo original da campanha, ladeado por cartões.
- 15–22 s: imagem aérea de Clevelândia, marcador e confirmação da exibição local.
- 22–29 s: “mais de 20 mil visualizações” como única métrica.
- 29–37 s: celular, flecha e alvo modelados e animados no Blender; o vídeo real passa na tela.
- 37–44 s: convite e assinatura EvoqueX Custom.

## Arquivos principais

- `index.html`, `style.css`, `motion.js`: composição HyperFrames/GSAP.
- `assets/campanha.mp4`: original preservado; `assets/campanha-loop.mp4`: loop editado para o cartão.
- `assets/phone-arrow-target.mp4`: plano 3D inserido na composição.
- `resources/phone-arrow-target.blend` e `scripts/build-3d.py`: fonte e gerador do plano 3D.
- `assets/evoquex-logo.png`: recorte transparente reconstruído a partir da imagem da marca enviada na conversa; substituir pelo arquivo mestre se ele for disponibilizado.
- `assets/packs/flare-transition.mp4`, `dots-light-burn.mp4`: efeitos reais da biblioteca enviada.
- `assets/mix-v16.wav` e `resources/audio/cues-v16.json`: mix final e âncoras sonoras.

Para refazer o plano 3D: `blender -b --python scripts/build-3d.py` e `bash scripts/encode-3d.sh`. Os MP4 usados no HyperFrames têm quadros-chave a cada segundo para busca precisa.

Execução: `node scripts/hf.mjs lint --json`; render: `node scripts/hf.mjs render --output renders/evoquex-hyperframes-v16.mp4 --fps 30 --quality delivery --workers 3 --no-browser-gpu`.

A música de fundo é “Close Up” (Michael Ramir C.) conforme a licença gratuita da Mixkit para anúncios online. Os efeitos dos packs foram fornecidos e autorizados pelo cliente. O vídeo original não tem áudio no mix desta etapa; isso deixa espaço para a futura locução. A foto aérea é uma foto estática, animada na composição, não uma gravação de drone.
