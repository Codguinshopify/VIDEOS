# Evoquex V13 — continuidade tipográfica

Composição vertical de **30 segundos, 1080 × 1920, 30 fps**, em HyperFrames 0.8.162
com GSAP 3.14.2. A V13 protege o hook aprovado da V12, no intervalo de 0 a 4 segundos,
e reconstrói a execução visual de 4 a 30 segundos. O conteúdo do roteiro foi mantido;
a coerência textual não é objeto desta revisão.

A nova composição utiliza tipografia que revela a fotografia, câmera entre estações,
uma única filmagem que muda de enquadramento e hierarquia, palavras e números em
fatias, documento em painéis complementares, troca de eixo das métricas, conexão por
curva e um CTA integrado à fronteira entre dois campos.

## Direção, fontes e recursos

`DESIGN.md` registra a direção visual e `STORYBOARD.md` detalha cada passagem.
`REFERENCE-IMPLEMENTATION.md` relaciona as oito técnicas selecionadas às referências,
aos trechos da V13, ao código e aos critérios de confirmação no MP4. O estudo que
precedeu a implementação está em `resources/reference-motion-study-v13.md`.

Foram consultados quatro arquivos únicos de referência, preservados na biblioteca:
Park/Shard Cloud, Park/Virgílio Contabilidade, OtoCriativo e Park/Weven. Reenvios
idênticos não contam como referências adicionais. O acervo HyperFrames auditado reúne
21 exemplos oficiais; as adaptações ficam separadas dos originais.

As versões do motor foram mantidas, sem nova dependência. A composição conserva a
DM Sans local, sob OFL, os vetores Lucide, sob ISC, a paleta e os materiais originais.
A fotografia, a filmagem e a captura da campanha são documentais; nenhum asset de IA
foi necessário para substituir esses materiais ou os vetores disponíveis.

## Executar

Na raiz desta composição:

```bash
npm ci --offline --cache /workspace/.npm --no-audit --no-fund
npm run check
npm run snapshots
npm run dev
node scripts/hf.mjs preview --status
npm run render
python scripts/validate-source.py
python scripts/validate-output.py
python scripts/review-output.py
python scripts/analyze-motion.py
node scripts/hf.mjs preview --stop
```

O wrapper local utiliza Chromium em `/usr/bin/chromium` e caches graváveis, sem
alterar `HOME`. O preview é gerenciado: confirme seu status e a resposta HTTP após
restaurar o projeto; encerre-o ao concluir. A saída de render é
`renders/evoquex-hyperframes-v13.mp4`.

O mapa de animações deve receber dimensões verticais explícitas:

```bash
node scripts/animation-map/animation-map.mjs . --out review/animation-map --width 1080 --height 1920 --fps 30
```

O helper e suas limitações estão documentados no diretório `scripts/animation-map`.
Asserções automáticas de motion desativadas não devem ser relatadas como executadas.

Para empacotar as fontes e os relatórios selecionados:

```bash
python scripts/package-source.py
```

O ZIP exclui `node_modules`, caches, credenciais, renders comparativos e os vídeos
originais das referências, que continuam preservados na biblioteca do repositório.

## Fatos, áudio e packs

O case é da **Danny’s Presentes**. A evidência registra **20.981 impressões** e
**13.064 pessoas alcançadas**. A Evoquex produziu o vídeo e divulgou a campanha por
sua conta, com anúncios direcionados somente a Clevelândia. Ir além dos seguidores é
um objetivo; não há quantidade comprovada desse público, vendas, conversões ou ROI.
Luciane continua desativada, sem placeholder ou tempo reservado no render.

`assets/mix-v13.wav` é um áudio real, com instrumental e efeitos de origem registrada
em `resources/audio/`. Há 24 acentos: cinco preservados no hook e 19 após o segundo 4.
Os primeiros quatro segundos do WAV preservam os 192.000 frames PCM estéreo da V12;
o restante foi reeditado e masterizado separadamente. Não foram utilizados a voz
rejeitada, áudio das referências ou efeitos de procedência não confirmada.

A locução feminina brasileira permanece pendente. Não houve geração autenticada com
ElevenLabs, compra ou simulação de voz. Os cues continuam sendo janelas editoriais
estimadas; um áudio real deverá orientar o alinhamento futuro.

A auditoria do Git recuperou os três volumes do pack 6000 Motion, listou 11.829
entradas do RAR interno e preservou cinco amostras pequenas, somando aproximadamente
3,96 MB. Isso não significa que todos os projetos tenham sido executados. A licença
comercial dos efeitos não foi encontrada, portanto os candidatos foram catalogados e
não inseridos na peça. Do pack Glitch, apenas um prefixo e previews de 250 × 141 foram
inspecionados; não são overlays HD. Detalhes em `resources/git-library-audit-v13.md`.

## Estado da revisão

**A revisão final da V13 está em curso.** O primeiro MP4 está em
`review/first-v13.mp4`; ele serve à inspeção e não deve ser tratado como entrega final.
Os contratos de fonte e texto têm verificações próprias, mas não substituem o exame
do arquivo definitivo, associado ao seu hash.

A interface não oferece playback contínuo ou escuta subjetiva. Sequências consecutivas
do MP4, trajetórias estimadas, SSIM do hook e checks técnicos de áudio ajudam a revisar
a edição, mas não equivalem a assistir em tempo real ou ouvir como espectador. Essas
limitações devem permanecer explícitas.

`resources/production-report-v13.md` prepara o relatório solicitado pelo usuário:
técnicas, recursos, correções e limites. Seu estado é de rascunho até a confirmação do
MP4 final. Não gerar montagem comparativa nem declarar concluído o QA antes dessa etapa.
