# V14 — recursos atuais, decisões práticas e procedência

Auditoria de recursos para a produção gráfica de26s. Sem alterar composição visual,
roteiro, áudio ou helpers de produçãoV14. Entrega ao usuário continua somente o vídeo;
este relatório é documentação interna para continuidade do trabalho.

## Git remoto consultado nesta etapa

BaselineV13:`b2129c5738e63a21b79b5dcec39f2bd7285002d0`.
Baselinepacks:`b1e0a83a28f424143601f134d9e1de2570eaf54c`.

Executados novamente `git ls-remote --heads`, `git ls-tree -rl` das9branches,
metadados de ancestralidade e diff dospacks. Não se presumiu que o acervo seria igual:
**o resultado da consulta atual é que os heads relevantes permanecem iguais**.
Não há branch nova descendente daV13 nem commit novo em `packs-lfs`; o diff dospacks
é vazio. Não há novoRAR, ZIP, preset, SVG, áudio, biblioteca ou script de usuário
adicionado ao remoto após esses baselines. Árvores/caminhos constam de
`git-current-audit.json`; o índice principal permanece vazio e HEADunborn em`work`.
Nenhum checkout/reset/stage foi usado.

|Branch|Head atual|Arquivos|
|---|---|---:|
|hyperframes-v13-motion-continuo|b2129c5738e63a21b79b5dcec39f2bd7285002d0|445|
|packs-lfs|b1e0a83a28f424143601f134d9e1de2570eaf54c|24|
|hyperframes-v12-motion-publicitario|ef13b86ed238901ca92564b0ce501bb0b7c1dbee|293|

As demais seis branches são históricas. Elas não foram confundidas com novos uploads
ou com exclusões da entrega atual. As mudanças locais da produçãoV14 em curso e os
exemplos aceitos abaixo são trabalho deste turno, não packs externos recém-chegados.

## Cache e packs: reutilização com limite real

Os três volumes6000Motion continuam no cacheLFS com tamanhos esperados:
1.048.576.000,1.048.576.000 e680.009.440bytes. Foram reutilizados osSHA-256 verificados
independentemente naV13; nesta etapa foram conferidas existência/tamanho, sem reler
ou baixar novamente gigabytes. O RAR interno foi recuperado/listado integralmente na
V13:11.829entradas e3.400.442.578bytes de contêiner. Isso não equivale a executar todos
os206AEP/1.354MOGRT nem a decodificar todas as83mídiasMP4/567WAV.

As12amostras/documentos permanentes tiveram seus hashes novamente conferidos.
Os cinco candidatos pequenosV13 continuam em
`biblioteca/packs/6000-motion-audit-v13/` (2WAV,1flareMP4,2documentos), sem licença
específica de uso comercial/redistribuição encontrada. Nenhum termo novo surgiu,
pois não houve atualização remota. Não afirmar autorização comercial. O flare não
possuialpha; fundos pretos necessitamblend/conversão. AEP/MOGRT/ATOM não executam no
HyperFrames. Não há motivo para forçar esses efeitos na peça.

Glitch continua com apenas8MiB de prefixo analisado, apesar dos3pointersLFS presentes.
OsGIF/PNG250×141 identificados são previews de baixa resolução, não overlaysHD. Não
houve download adicional nem alegação de integridade da coleção inteira. O estado
continua registrado em`biblioteca/packs/inventario.json` e`packs/README.md`.

## Recursos concretos escolhidos com o agenteMD

Instalação real conferida:HyperFrames**0.8.162** eGSAP**3.14.2**. Sem upgrade,
`hyperframes add` ou dependência nova. Consultados os21itens jápreservados, o clone
oficial fixado em`08ee1bd5ad59987a7f2525222683e24ca30971f9`, seusmetadados/scripts e
rotas da distribuição instalada (`dist/skills/hyperframes/references/routes/motion-graphics.md`).
A rota instalada descreve unidades curtas de motion; o briefing de26s governa esta
produção completa, portanto não foi tratado como preset pronto ou motivo para
abandonar storyboard/validação.

Foram investigados11candidatosnovos no catálogo oficial, inclusivefacet-morph,
caption-camera-follow, vector-editor-rig, rubber-band-bumper, ticker-takeover,
morph-text e mecanismosCanvas/SVG. Apenas **dois** foram preservados porque o agenteMD
aceitou aplicações concretas; catálogo passou de21para23itens. Não foram adicionados
exemplos somente para aumentar o inventário.

|Recurso aceito|Função/mecânica real|Uso planejado peloMD naV14|Compatibilidade e limite|
|---|---|---|---|
|facet-morph|`FORMS`, triangulação36faces, `progressAt(t)`, `wobbleAmpAt(t)`, `render(t)`; tabelas18vérticesexternos+9internos e centro; coordenadas+cores escritas como atributosSVG por uma função fechada do tempo|Ator nasce das lâminas/recorte de filme6,7–9,1s; transforma-se em seta/público9,2–11,6; marcador11,6–14; conduz à apresentação de20mil14–18|GSAP+SVG locais. Preset original sóblob/mark/badge; seta/marcador exigem novas tabelas com correspondência topológica. Pseudoshading porfaceta, nãoCGI físico. Não basta passar`forms:'arrow'`, que seria descartado pelaAPI|
|caption-camera-follow|`poseFor(box,margin)` calcula escala para enquadrar bounds e aplica um transform único no mundo; palavras ficam fixas. BézierStep(.31,0,.11,1) eWide(.42,0,.14,1)|Câmera tipográfica na prova14–18 e encerramento20,5–26; caixasDMfixas mantêm leitura portrait e continuidade|DOM/GSAP locais. Original tem14palavras inglesas/9s, rulerHelvetica e`gsap.defaults`global. Adaptar função/poses; não importar o relógio/textos/defaults globais. Blur original pode ser excessivo para a prova; priorizar hold nítido|

### Fonte e licença verificáveis

- `biblioteca/hyperframes/facet-morph/facet-morph.html.txt`:
  `ebb10804d82647be0452aa15b4601aa8fb2d4c5c37d9f9cb3092203dad38d53b`.
- `biblioteca/hyperframes/facet-morph/registry-item.json`:
  `d295fcddd250fc920dcad916e91bcafdbf10efd952f47ad2b881d404a10a36e3`.
- `biblioteca/hyperframes/caption-camera-follow/caption-camera-follow.html.txt`:
  `4a0da1ba065882e95274468c8f3e36f1094fc598c3c93be1fc63182e9e42953c`.
- `biblioteca/hyperframes/caption-camera-follow/registry-item.json`:
  `9a231316fbc229723242d30bfda8d74fd32f7d45a7237b2cd67bf0e6986660e6`.

Originais obtidos por`git show` da revisão acima, byte-idênticos; HTML arquivado como
`.html.txt` para não sofrer mutação doStudio. Apache-2.0 do repositório está preservada
em`biblioteca/hyperframes/LICENSE`; esses dois itens não declaram licença substitutiva.
GSAP mantém sua própria licença separada. Essa procedência não concede direitos de
packs nem das mídias das referências. As referências são usadas para estudo, não
como imagem, marca ou áudio da campanha.

### Receitas que oMD pode implementar

**Mesh:** cada forma deve ter os mesmos vértices e a mesma ordem. Para cada índice,
interpolarA→B com um único progresso; a triangulação mantém os mesmos índices. Cada
update escreve`points/fill/stroke` de todas as faces, evitando dependência de uma
CSSvar de cor que possa não repintar corretamente emseek reverso. Fonte original
usa luz(-0,62,-0,78), fasesLCGfixas e pseudonormais; não há simulação em tempo real.
Formas adicionais são uma adaptação autoral documentada, não presets nativos novos.

**Câmera:** para uma caixa fixa(x0,y0,x1,y1),
`s=min(W/((x1-x0)*margin),H/((y1-y0)*margin))`,
`x=W/2-s*(x0+x1)/2`, `y=H/2-s*(y0+y1)/2`.
Com`transform-origin:0 0`, um tween no mundo(x,y,scale) visita regiões enquanto as
palavras conservam posições no desenho. Isso dá continuidade espacial sem fileira
de cartões, fadeemcadafrase ou letra apenas sobreposta à filmagem. O estado de leitura
precisa estar nítido; não usar smear para esconder transições fracas.

## Teste representativo executado

`check-selected-primitives.cjs` montou os dois templates originais emChromium com
GSAP3.14.2 local, retirando oscriptCDN e fornecendo somente variáveis de runtime em
stub isolado. NenhumHTML daV14 foi alterado. Ambos registraram timeline pausado,
preencheram1080×1920 e mudaram estado. Sequência de seek
`0→1,6→4,9→1,6→0` voltou a estadosDOM byte-idênticos:

- facet-morph:36polygons,5s, diferenças reais entre formas efills.
- caption-camera-follow:14palavras,9s, câmera e smear sincronizados nooriginal.

Relatório:`primitive-compatibility-probe.json`; screenshots de inspeção em
`facet-morph-probe.png` e`caption-camera-follow-probe.png`.
Esse teste confirma funcionamento de mecânicasDOM/SVG/GSAP e determinismo no contexto
isolado. **Não substitui o renderHyperFrames finalV14**, não prova naturalidade de
áudio e não declara que as adaptações daV14 já foram implementadas/aprovadas.

## Opções consideradas e não selecionadas

|Candidato|Mecanismo real|Decisão|
|---|---|---|
|vector-editor-rig|Pathdash por comprimento real, âncoras/handles em sequência|MD não precisaUI de ferramenta; linhas/paths já existem no acervo. Não adicionado|
|rubber-band-bumper|Resistência em5passos e releasecomovershoot sobre um painel|A lógica de tensão pode inspirar o ator; não substituir a composição por painéis repetidos|
|ticker-takeover|Reel acelera/desacelera, trava palavra e promove headline|Exige palavras/opções adicionais; não introduzir escolhas ou métricas que não pertencem à narrativa|
|morph-text|Blur complementar de dois textos mais thresholdSVG|Original temFigtree/fontes externas e morph que compromete leitura durante a passagem; câmera/mesh escolhidos oferecem função mais clara aqui|
|segmentation-flood|Regiões de segmentação, scanlinequantizado eHUD|Vocabulário de visão de máquina não comprova campanha e não precisa ser acrescentado ao case|
|stitched-text-draw|Alfabeto single-stroke com dashoffsetattribute eagulha|Fonte nativa limitaA-Z0-9/12caracteres; não combina comDM/acentoportuguês desta direção|

As escolhas técnicas são orientadas pela função na narrativa, não pela dificuldade
de implementação. Não instalarThree/WebGL apenas para anunciar mais complexidade;
SVGfacetado e câmera2D resolvem as aplicações concretas aceitas.

## Dado da nova versão

O briefingV14 declara **20milvisualizações de pessoas de Clevelândia**. Essa informação
vem da confirmação do usuário nesta etapa. Não derivá-la da captura anterior de
20.981impressões/13.064alcance e não converter nomes entre métricas. O screenshot antigo
não é comprovante dessa nova afirmação. Esta auditoria não alterou copy/números na
composição; oMD aplica a instrução nova e registra sua origem correta.
