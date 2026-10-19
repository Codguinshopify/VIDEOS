# Evoquex — HyperFrames V15R1

Produção vertical da Danny’s Presentes, com HyperFrames 0.8.162, GSAP 3.14.2,
1080 × 1920 e 30 fps. A duração vigente e os limites das cenas ficam em
`resources/scene-timing-v15.json`; não presumir que continuam iguais aos da V14.

O pedido ativo é `resources/briefing-v15.txt`. Esta etapa entrega o vídeo visual
com trilha e sound design. A voz será produzida externamente no ElevenLabs e
integrada depois. Nenhuma ferramenta de TTS faz parte desta entrega.

A revisão V15R1 mantém o projeto e as nove cenas, mas reduz o corte de 27,6 s para
23,4 s. `resources/revision-v15r1.json` registra a mudança. O mix ativo é
`assets/mix-v15r1.wav`, construído por `scripts/build-audio-v15r1.py` a partir da
música instrumental licenciada e dos efeitos efetivamente usados. Os masters V15
anteriores continuam históricos; não são dependências desta versão.

## Executar

```bash
npm ci --no-audit --no-fund
node scripts/hf.mjs lint --json
node scripts/hf.mjs check --json
node scripts/hf.mjs preview --background
```

Use as dependências fixadas no lockfile e o wrapper do projeto. No ambiente atual,
`npm ci --offline --cache /workspace/.npm --no-audit --no-fund` reaproveita o cache.
FFmpeg/ffprobe, Python com NumPy/Pillow e Chromium são necessários para os checks.
Os checks não instalam nem atualizam dependências automaticamente.

## Render e revisão

1. Confirme `scene-timing-v15.json`, os arquivos de mídia e o mix ativo.
2. Execute `python scripts/qa-v15.py --freeze` imediatamente antes do render.
   Guarde o caminho `review/source-bundle-<hash>.json` devolvido pelo comando.
3. Renderize com o wrapper HyperFrames, 30 fps, H.264/MP4:
   `node scripts/hf.mjs render --output renders/evoquex-hyperframes-v15-revisado.mp4 --fps 30 --quality high --crf 18 --workers 3 --no-browser-gpu`.
4. Execute `python scripts/qa-v15.py --video renders/evoquex-hyperframes-v15-revisado.mp4 --bundle review/source-bundle-<hash>.json --samples`.
5. Inspecione as folhas de quadros identificadas pelo SHA do MP4 em `review/v15-<hash>/`,
   incluindo duração inteira, todos os quadros da abertura, todas as transições,
   início/fim das mídias e tamanho de telefone. Corrija problemas e repita os checks
   afetados. O script não declara aprovação estética nem escuta subjetiva.
6. Registre a decisão visual com o SHA do arquivo efetivamente revisado. Nunca
   aprove o render final usando quadros ou relatórios de uma tentativa anterior.

Para um backup portátil das fontes depois da validação:

```bash
python scripts/package-v15.py --video renders/evoquex-hyperframes-v15-revisado.mp4 --output renders/evoquex-hyperframes-v15-revisado-projeto.zip
```

O pacote contém dependências ativas de mídia, fontes, código, lockfile e documentação;
exclui `node_modules`, RARs originais, outras versões, renders de tentativa e dumps de
quadros. A instalação e o teste desse ZIP numa pasta isolada são uma validação separada.

## Bibliotecas e informações

Os componentes do catálogo HyperFrames e os assets dos packs são materiais de produção.
`resources/asset-usage-v15.json` registra o que entrou na composição e a função de cada
recurso. Um asset apenas copiado não conta como utilizado; arquivos presentes na mixagem
precisam também de procedência no gerador e nos registros de áudio.

A declaração ativa é **20 mil visualizações de pessoas de Clevelândia**, fornecida
pelo usuário no briefing. Ela não significa 20 mil pessoas únicas e não é comprovada
pela captura histórica de impressões/alcance. Não acrescentar vendas ou retorno financeiro.

A imagem aérea disponível é uma fotografia real. Um movimento aplicado a ela não a
transforma numa filmagem aérea original. Preserve essa distinção nos registros.

O usuário autorizou o uso, inclusive comercial, dos materiais que forneceu. Conserve a
origem dos arquivos e registre impedimentos técnicos concretos sem repetir dúvidas
genéricas de licença. AEP/MOGRT/presets nativos não executam diretamente em HyperFrames.

Consulte `NARRATION-HANDOFF.md` para a futura integração da voz.
