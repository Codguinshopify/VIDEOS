# Evoquex V12 — instruções específicas

Leia primeiro `../AGENTS.md`, `../biblioteca/README.md`, `DESIGN.md`,
`STORYBOARD.md` e `REFERENCE-IMPLEMENTATION.md`. Consulte as três referências
permanentes disponíveis no catálogo, incluindo Oto; preserve as anteriores.
As skills HyperFrames, CLI, GSAP e registry orientam o motor e sua versão instalada.

As skills locais de produção estão em `../.agents/skills/<nome>/SKILL.md`:
`ai-visual-asset-design`, `reference-analysis`, `asset-library-research` e
`motion-quality-control`. Leia os arquivos diretamente quando aplicáveis. São
arquivos versionáveis; não alegue que foram registrados ou descobertos automaticamente
pelas ferramentas de skills em nuvem. Pesquise o acervo antes de desenhar ou gerar.
Nesta versão não houve geração de assets por IA: os recursos reais e nativos bastam.

## Implementação e reprodução

Composição de **30 segundos, 900 frames, 1080 × 1920, 30 fps**. Um timeline raiz
pausado registrado em `window.__timelines['evoquex-hf-v12']`, sem aleatoriedade,
timers ou playback manual. Use HyperFrames **0.8.162**, GSAP **3.14.2** e o lockfile:
`npm ci --cache /workspace/.npm`. Não reintroduza dependências desnecessárias.
Vídeo real reproduzido uma única vez, mudo; áudio separado em `assets/mix-v12.wav`.

Toda alteração HTML exige `npm run check`. Revise avisos; não desative verificações
para forçar aprovação. Use os comandos do `package.json`, não nomes ou durações de
produções anteriores. Os scripts de validação devem conferir a V12/30s/900frames.
Asserções automáticas de motion são desabilitadas por padrão; não declare que esse
módulo executou. O helper de mapa requer `--width 1080 --height 1920 --fps 30`.

Preview gerenciado: `npm run dev`, depois `node scripts/hf.mjs preview --status`.
Verifique resposta HTTP e snapshots; mantenha durante revisão e encerre com
`node scripts/hf.mjs preview --stop`. Não dependa de um shell em background que
termine. Se houve edição no aplicativo desktop, execute catch-up antes de alterar
fontes. Mantenha originais de catálogo como `.html.txt`, porque o Studio pode injetar
identificadores em HTML de composição.

## Fatos e módulos

A grafia é **Danny’s Presentes**. Evoquex produziu o vídeo e a campanha foi somente
para Clevelândia. Prova real: **13.064 pessoas alcançadas** e **20.981 impressões**.
Não invente vendas, ROI, conversões, visualizações ou quantidade de não seguidores.
Ir além dos seguidores é objetivo confirmado no briefing, não medição comprovada.
Preserve o documento real e não o substitua por interface ou dados gerados.

Luciane permanece apenas como módulo **desativado** no scene manifest, sem placeholder,
título, mídia ou tempo reservado no render. Ative somente mediante novo conteúdo e
pedido correspondente; não invente o case para completar a estrutura.

## Voz, som e revisão

Voz feminina brasileira natural **pendente**. Não há ferramenta funcional ElevenLabs
exposta nem chave disponível nesta sessão; isso não comprova instalação ou plano.
Não reutilize Kokoro rejeitado, não simule voz e não compre assinaturas. Verifique
termos e limites atuais antes de uso futuro; nunca exponha credenciais.

`resources/voice-cues.json` contém janelas editoriais estimadas, sem alinhamento real.
Uma gravação verdadeira é pré-requisito para `prepare-voice.py`; confirme entradas e
duração V12, meça a fala e retime visual/FX/ducking. Não acelere artificialmente uma
gravação para caber e não conecte arquivo inexistente ao HTML. Nunca prometa voz
natural por configuração ou ASR.

Stems, licença e automações estão em `resources/audio/`; não reutilize áudio das
referências. Não há escuta subjetiva nesta interface. Separe análise técnica de
audição e declare essa limitação. Depois de renderizar, examine o MP4 real completo,
abertura quadro a quadro, transições, leitura, grafia, métricas e áudio. Confirme o
hash revisado; compilar e renderizar não bastam. Não declare QA final antes de fazê-lo.

Entregue somente o vídeo editado, sem comparativos, mantendo fontes e QA no
repositório. Prefira o link GitHub direto `/raw/refs/heads/.../entrega/...mp4`.
