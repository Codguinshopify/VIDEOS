# Evoquex V14 — matéria em movimento

Produção vertical em HyperFrames 0.8.162 e GSAP 3.14.2, com render final de **26 segundos,
780 frames, 1080 × 1920 e 30 fps**. O timing foi confirmado no MP4 exportado. A revisão visual por sequências de frames
e os checks técnicos estão concluídos para o arquivo final identificado abaixo.

A V14 reconstrói substancialmente o pós-hook: a tipografia abre a paisagem, a paisagem
entrega lâminas do filme, as lâminas conduzem uma forma facetada e essa forma muda de
função até a prova e o convite. O hook de quatro segundos é o benchmark de qualidade
e pode ser aprimorado. Não existe mais uma exigência de identidade de pixels ou de
preservação do áudio do hook da V13.

## Direção e referências

Leia `DESIGN.md`, `STORYBOARD.md`, `REFERENCE-IMPLEMENTATION.md`,
`resources/briefing-v14.txt`, `resources/case-facts-v14.json` e
`resources/scene-timing-v14.json`. As instruções persistentes do agente MD ficam em
`../.agents/agents/md.md`; sua existência local não comprova registro em um serviço.

Quatro referências originais permanecem na biblioteca: Park/Shard Cloud,
Park/Virgílio Contabilidade, OtoCriativo e Park/Weven. **Os três primeiros MP4 devem
ser abertos novamente em cada produção ou revisão**, antes de definir a abordagem
visual. Confira os caminhos e hashes em `../biblioteca/referencias/catalogo.json`.
Weven continua disponível como estudo adicional. Os reenvios idênticos da V14 não
substituem nem duplicam esses originais. Música, voz, marcas e imagens das referências
não são material de campanha.

A biblioteca HyperFrames, o Git e os packs precisam ser auditados no estado atual.
Consulte `../biblioteca/hyperframes/catalogo.json`,
`../biblioteca/componentes/catalogo.json` e `../biblioteca/packs/inventario.json`;
compatibilidade e licença devem ser verificadas antes de cada uso. Não confunda um
inventário, a presença de um RAR ou um projeto AEP com um efeito executado no vídeo.

## Conteúdo e evidência

O case é da **Danny’s Presentes**, com vídeo produzido pela Evoquex e campanha
direcionada somente a Clevelândia. O dado ativo desta edição é **“20 mil
visualizações de pessoas de Clevelândia”**, atestado explicitamente pelo usuário no
briefing V14. Não houve verificação documental independente desse total ou de sua
distribuição geográfica. Visualizações não significam pessoas únicas, alcance,
impressões, vendas ou retorno financeiro.

A captura histórica de 20.981 impressões e 13.064 pessoas alcançadas não comprova o
novo dado e não deve aparecer como sua prova. Ela e os registros antigos são
preservados nas versões anteriores, sem alteração retroativa. Não produzir um
dashboard, depoimento ou documento fictício para suprir essa diferença de evidência.

As mensagens e a estrutura narrativa são mantidas, com ajustes mínimos quando
indispensáveis ao ritmo e à leitura. O material real da Danny’s Presentes é uma
intervenção breve, integrada a máscaras e recortes; o timing atual prevê 6,9–9,46 s.
Não manter Evoquex ou Clevelândia como marca-d’água depois de cinco segundos.

## Reprodução técnica

Na raiz desta composição, usando o cache disponível neste ambiente:

```bash
npm ci --offline --cache /workspace/.npm --no-audit --no-fund
npm run check
npm run snapshots
npm run dev
node scripts/hf.mjs preview --status
npm run render
node scripts/hf.mjs preview --stop
```

Sem o cache, utilize `npm ci` com acesso ao registro. O wrapper usa Chromium local e
caches graváveis sem alterar `HOME`. Não altere as fontes enquanto houver uma captura
ou render ativo. O destino configurado é `renders/evoquex-hyperframes-v14.mp4`.

Os validadores em `scripts/` conferem o contrato ativo da V14, de 26 s, o texto e a
mídia final. Execute depois do render:

```bash
python scripts/validate-source.py
node scripts/inspect-runtime.mjs
python scripts/validate-output.py
python scripts/review-output.py
python scripts/analyze-motion.py
```

A inspeção nativa registra poses e possíveis rótulos persistentes; exige confirmação
visual no MP4. Não faz OCR nem alega playback. A mera presença dos validadores, um
lint aprovado ou um snapshot não
substituem a revisão do MP4. Registre internamente o hash exato de cada arquivo
revisado e refaça os checks depois de mudanças relevantes. Não reaproveite aprovações
ou hashes da V13. O mapa opcional de animações exige dimensões verticais explícitas:

```bash
node scripts/animation-map/animation-map.mjs . --out review/animation-map --width 1080 --height 1920 --fps 30
```

## Áudio e revisão

A música anterior foi rejeitada por repetição. A V14 tem **uma nova composição
musical original já produzida**, com MIDI e instrumental próprios em `resources/audio/`,
sound design sincronizado aos marcos do timing e mix em `assets/mix-v14.wav`. Não se
trata de preservar o hook sonoro antigo ou apenas retimar seu loop. A procedência,
as licenças e a validação do novo mix devem acompanhar a versão efetivamente usada.

A locução feminina brasileira continua pendente, conforme
`resources/voice-status.json`. Não houve geração autenticada de voz nesta etapa,
contratação, compra ou troca de plano. Não reutilizar Kokoro nem ligar arquivo de
voz inexistente. Luciane permanece desativada.

O QA do arquivo final examinou abertura, passagens consecutivas, amostras de toda a
duração, hierarquia, textos, dado ativo e marca. O áudio passou por verificação técnica.
As evidências estão em `review/final-approval-v14.json`, `review/output-validation.json`
e nos pareceres finais independentes. SHA-256 do MP4 revisado:
`a07de6cdbab452fb10e0d65c731710d4f64d14caa94a100730dec78838964417`.
Inspeção por frames e checagem técnica de áudio não equivalem a playback contínuo
ou escuta subjetiva; registre o método realmente disponível. Não declarar voz natural
ou mix ouvido quando não houve audição.

**A entrega solicitada é somente o MP4 final.** Fontes, biblioteca e QA ficam para
continuidade interna. Não enviar ao usuário relatório técnico, inventário, comparação,
lista de alterações, código ou descrição do processo. Se houver bloqueio real,
comunicar somente o impedimento específico. Preferir link direto GitHub no formato
`/raw/refs/heads/<branch>/entrega/<arquivo>.mp4`.
