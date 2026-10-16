# Evoquex V13 — execução de motion após o hook aprovado

Leia `../AGENTS.md`, `DESIGN.md`, `STORYBOARD.md`, `REFERENCE-IMPLEMENTATION.md`,
`resources/briefing-v13.md` e `../biblioteca/README.md`. Consulte diretamente as cinco
skills locais quando aplicáveis; não presuma registro ou descoberta automática em
serviços de skills. Verifique a disponibilidade real das ferramentas e da documentação.

## Contratos protegidos

O hook da V12, no intervalo `[0,4)`, e o conteúdo do roteiro estão protegidos. Não
reescreva frases nem corrija a estrutura narrativa nesta etapa. Compare as fontes com
`resources/copy-contract.json` e a base aprovada, além de conferir os frames do render.
Os primeiros 192.000 frames PCM estéreo do áudio também estão preservados; a ponte
para a nova mixagem ocorre depois de 4 segundos. Frames PCM não são frames de vídeo.

## Implementação e validação

Use HyperFrames 0.8.162 e GSAP 3.14.2, com DM Sans local. A composição tem 30 segundos,
900 frames, resolução de 1080 × 1920 e 30 fps. Um único timeline raiz pausado está
registrado como `evoquex-hf-v13`. Mantenha determinismo, mídias locais e áudio separado.
A filmagem original aparece uma única vez, de 8,1 a 13,16 segundos, com áudio zerado.

O mundo contínuo visita estações em `y = 0 / 1920 / 3840` e `x = 0 / 1080`; o
contorno global acompanha a mídia. Não altere fontes durante a captura de um render.
Clipping breve de transição deve ser interpretado pelo movimento; colisões sustentadas
entre texto, nome e prova precisam ser corrigidas.

Execute `npm run check`, snapshots e render. Os scripts de validação são
`validate-source.py`, `validate-output.py`, `review-output.py` e `analyze-motion.py`,
todos em `scripts/`. O mapa separado exige `--width 1080 --height 1920 --fps 30`.
O motion automático nativo desativado não equivale a teste executado.

Revisão por sequências consecutivas e fluxo óptico estimado não é playback contínuo
em tempo real. A interface não oferece escuta subjetiva. Registre as verificações
técnicas de áudio sem afirmar audição, naturalidade da voz ou impacto sonoro percebido.
A locução feminina natural permanece pendente; não reutilize a voz Kokoro rejeitada,
não conecte arquivo inexistente e não compre planos.

## Fatos, packs e entrega

A grafia é **Danny’s Presentes**. Preserve **20.981 impressões/exibições do anúncio**
e **13.064 pessoas alcançadas**. A Evoquex produziu o vídeo e o divulgou por sua conta,
com campanha somente para Clevelândia. Ir além dos seguidores é objetivo, não alcance
efetivo desse grupo comprovado. Não invente vendas, conversões, ROI ou visualizações.
Luciane permanece desativada, sem cena fictícia.

A auditoria V13 confirmou os três volumes completos do pack 6000 Motion no cache LFS
e listou seu RAR interno. Não repita a afirmação antiga de que falta a terceira parte.
A licença comercial dos efeitos não foi encontrada; os candidatos foram catalogados,
sem serem forçados na peça. Do Glitch, apenas o prefixo e previews foram inspecionados.
Leia `resources/git-library-audit-v13.md` antes de generalizar compatibilidade ou uso.
Mantenha arquivos gigantes fora do Git normal e preserve catálogos e amostras pequenas
na biblioteca.

O QA final deve apontar o hash do MP4 efetivamente revisado. Não reutilize uma aprovação
da V12 ou do primeiro render da V13 para um arquivo posterior. Entregue vídeo e o
relatório objetivo pedido nesta etapa, sem montagens comparativas. Prefira link direto
GitHub `/raw/refs/heads/.../entrega/...mp4`.
