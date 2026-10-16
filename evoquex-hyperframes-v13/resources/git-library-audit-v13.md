# V13 — auditoria real do Git, packs e catálogo HyperFrames

Escopo: recursos e compatibilidade. Briefing de reconstrução a partir de4s lido;
hook0–4s e roteiro não foram modificados por esta auditoria. Nenhum checkout,
reset ou stage foi executado. O HEAD principal continua unborn e o índice intacto.

## Remoto e diferenças verificadas

Baselines: entrega V12 `ef13b86ed238901ca92564b0ce501bb0b7c1dbee` e packs
`fcf095991ad0ce8b0e10728c8abf927bc4bddfa9`. `git ls-remote --heads`, árvores completas,
metadados e diferenças estão em `git-remote-tree-audit.json`.

| Branch remota | SHA no instante da auditoria | Arquivos |
|---|---|---:|
| comparacao-hyperframes-v8 | bbc544292992ddce2d71edb1c7859e876d05c3e0 |30|
| edicao-v7-bibliotecas |5076ea07a056029006c2a20ce4832fa7f2663876|21|
| entrega-evoquex |b2efd94aed79f11a6cdc0c6b485797848a44c2eb|14|
| hyperframes-v10-direcao-criativa |a68b54a8ed98870623b35325e0f51e423303db7e|43|
| hyperframes-v11-biblioteca-permanente |0ca586233fffe474cf0477cd5e28502dea73ce05|171|
| hyperframes-v12-motion-publicitario |ef13b86ed238901ca92564b0ce501bb0b7c1dbee|293|
| hyperframes-v9-catalogo |e208111f3e21d6382492ac0861ef5a45b8e7dbd6|37|
| packs-lfs |b1e0a83a28f424143601f134d9e1de2570eaf54c|24|

Não há head novo descendente da V12 no instante consultado. Branches históricas
não são tratadas como exclusões/novidades só porque divergem da entrega atual.
Na branch packs, a diferença desde o baseline anterior contém **quatro adições**:

- `pack/6000+Motion Graphics Pack V5.1-002_rar.part3.rar`.
- `pack/650+ Glitch Elements v1.0-009_rar.part1.rar`.
- `pack/650+ Glitch Elements v1.0-009_rar.part2.rar`.
- `pack/650+ Glitch Elements v1.0-009_rar.part3.rar`.

Não há script, SVG, áudio ou preset avulso novo nessa diferença: são contêineres
RAR em LFS, cujo conteúdo foi investigado abaixo. Os ZIPs pequenos já existentes
foram recuperados integralmente e testados por CRC/hash: contêm apenas TXT de teste
LFS, sem efeito, transição ou asset utilizável.

## 6000 Motion: arquivo completo disponível e conteúdo novo confirmado

Reutilizada a parte1 já em cache; baixadas somente partes2+3,1.728.585.440bytes.
Os três volumes estão completos e tiveram SHA-256/tamanho conferidos:

| Parte |Bytes|SHA-256|
|---|---:|---|
|1|1.048.576.000|2600fa0f9f53ab9484f1fb822eeeec4b1e78cb98a03776b56b55275a8cd432fc|
|2|1.048.576.000|f01638e9cd0f52482941d8648bee33f0fe8e98b8ca92306fb4e958c176f15426|
|3|680.009.440|688d8389895c80e7d0870de9b58c441efd6d9da79cc595d33115e3157d6103fb|

Libarchive.so.13, já instalado, abriu a sequência multipartes sem instalar outra
ferramenta. O único item externo é outro RAR, recuperado integralmente:
3.400.442.578bytes, SHA-256
`da6b3f82dee8c8dfbaf91f62e5d8fd677fd17161d822a32a6a30563e0ff65952`.
A leitura externa terminou sem erro/CRC; listagem interna chegou ao EOF com11.829
entradas (11.442 arquivos,387diretórios),4.977.698.862bytes regulares expandidos.
Nenhum caminho absoluto ou `..` foi encontrado. Não há symlinks na árvore listada.

Inventário integral: `6000-complete-inventory.json`. Isso confirma disponibilidade
completa do contêiner e de sua árvore; **não** prova execução de todos os projetos
nem decode/CRC de cada uma das11mil entradas. Apenas selecionados foram extraídos
com leitura integral e decodificados, sem executáveis/instaladores/plugins.

| Formato real |Quantidade|Integração/limite|
|---|---:|---|
|AEP|206|AfterEffects, fontes/plugins/fontes de mídia; não executa no HyperFrames|
|MOGRT|1.354|Runtime Adobe; não é presetHTML ou GSAP|
|MP4|83|Mídia independente:13Ink,12TransitionFlare,58partículas/reveals|
|WAV|567|Áudio independente em Atom Preview Assets; direitos precisam ser comprovados|
|PNG|4.605|Muitos previews; tamanho/alpha precisam de inspeção individual|
|GIF|4.601|Muitos previews animados; não presumir assetHD ou seek determinístico|
|JPG|20|Guide Images/apoios, não fotografias do case|
|HTML/TXT|1/2|Lista de fontes e relatório de projeto; documentação, não licença|
|JSON/AEGRAPHIC/ATOM|1cada|Metadados/projetos específicos, não assumir Lottie ou plugin executável|

WAV por categoria:60FastSwooshes,42Game,150Glitch,77Hi-Tech,27Impacts,
61Interface,36Magic,40Notifications,29Pops,10Swipes,35Whooshes.

### Amostras pequenas efetivamente extraídas e testadas

18entradas:10WAV,6MP4 e2documentos. Cada uma passou por leitura integral/CRC,
hash e, para mídia, ffprobe+decodecompletoFFmpeg. Detalhes, sinal e hashes:
`6000-selected-inventory.json`.

Somente cinco arquivos (3.958.157bytes, menos de4MB) foram preservados no Git normal,
em `biblioteca/packs/6000-motion-audit-v13/`:

|Arquivo|Qualidade e função técnica|Situação de uso|
|---|---|---|
|SFX - Fast Swoosh 1.wav|PCM16/44,1kHz estéreo,1,2s; pico−7,20dBFS em0,344s; sem samplesfullscale; candidato a pan/reveal|Direitos pendentes; não usado no audiovisual V13|
|SFX - Impact 1.wav|Mesmo formato,4,5s; pico−0,52dBFS em0,0045s; sem samplesfullscale; ataque+cauda|Direitos pendentes; não usado no audiovisual V13|
|TransitionFlare_1.mp4|H.2641920×1920/29,97fps/1,668s; yuv420p, semalpha; flare sobrepreto|Screenblend/conversão possíveis; direitos pendentes e estética cinematográfica não obrigatória|
|Fonts.txt/Fonts.html|Lista real de links de fontes; lidos como documentação; HTML não executado|Não autoriza pack e não determina mudança tipográfica|

As sete amostras antigas permanecem intactas. Ink_15, antes incompleto, agora foi
extraído integralmente e decodificado na auditoria privada; não foi copiado para
ampliar desnecessariamente o acervo normal. Flares1/4/7 e Reveals1/2 têm frame real
inspecionado. Reveals são3840×2160/59,94fps/2,669s, H.264semalpha. Portanto não há
falso anúncio de vídeo transparente pronto.

Nos testes de sinal, Interface1/2 têm um sampleint16 no limite cada; isso não prova
por si só distorção audível, mas não foram escolhidos como os dois exemplos. Não
houve escuta subjetiva: naturalidade/timbre não são certificados porastats.

### Licença: pendência concreta

Busca de nomes em **toda a árvore** porlicense/licence/README/EULA/terms/licen/readme:
nenhum arquivo de licença ou termos. SóDocumentation/Fonts.txt/html, lidos, com
links de fontes e sem concessão de uso dos efeitos. Nenhum direito foi inferido do
nome do site ou da disponibilidade do download. Manter os stems próprios legais
já documentados na peça; não forçarWAV/MP4 do pack por terem sido encontrados.

## Glitch: inspeção parcial eficiente, sem afirmar pack completo

Os três pointers LFS estão presentes no remoto:1.048.576.000 +1.048.576.000 +
315.397.780bytes. Só a parte1 teve byte-range0–8.388.607baixado (HTTP206). O prefixo
contém início de outro RAR;11headers internos foram alcançados. QuatroGIF+quatroPNG
de gradientes foram extraídos completos, CRC-read e decodificados:250×141;GIF84frames,
3,36s. A próxima entrada estava truncada e foi marcada incompleta, sem inclusão.

Isso é preview de baixa resolução, não overlayHD. Parte2/3 e o fim do pack não
foram baixados, portanto não se afirma integridade nem licença da coleção inteira.
Relatórios:`partial-listing-glitch.json`,`glitch-samples.json`; hashes/range compactos
no inventário permanente. Prefixes e amostras de estudo ficam na área privada.

## HyperFrames: alternativas concretas para4–30s

Versões mantidas:HyperFrames0.8.162/GSAP3.14.2. Fonte oficial fixada em
`08ee1bd5ad59987a7f2525222683e24ca30971f9`, sem upgrade e sem alegar sucesso de
`hyperframes add`.17itens prévios foram conferidos; quatro novos originais foram
arquivados comHTML`.html.txt`+registryJSON, total21itens/42arquivosSHA conferidos.
LicençaApache2 preservada; dependências GSAP mantêm sua própria licença.

|Exemplo real|Mecânica efetivamente existente|Adaptação proposta ao conteúdo atual|
|---|---|---|
|type-match-cut|Headline divide em grupos superior/inferior,±20cqh; slot nasce scale.02→.46/.14 e depois1; saídas em2segmentos com arco|“Já viu / por aqui?” abre recorte real da cidade; elemento conduz à filmagem. Não apenas texto comfade|
|pan-stations|Um strip, índiceCSS de estação e dwells; pans0,25s; sem spring genérico|Adaptar eixoX→Y e estações para palavra/foto/filmagem. Continuidade de espaço durante mudança7,7–8,3s|
|text-match-cut|Uma única curvaBezier(.85,0,.15,1), resolvida porbisseção; A→B hardcut no pico u=.5; variaçõestracking/slide/scale|Handoff entre frases do processo ou métricas com número+rótulo atômicos; empresa→serviço muda gênero no mesmo ponto. Não usar duas animações independentes|
|slit-scan-reveal|Canvas96faixas; cada faixa amostra funçãofechada pos(t−offset); jitter seed0x51175c4e; offsets colapsam numa resolução0,6s|Modelo para fragmentação/recomposição de tipografia/documento em faixas. Três bandas diagonaisDOM são uma adaptação declarada desse princípio, não execução literal doCanvas original|
|camera-rig-depth-stack (já catalogado)|UM painelCSSperspective900px, rotateX/Y/Z viaCSSvars; source não implementa stack real nemThreeJS|Cada palavra/filmagem pode ocupar plano próprio num rig autoral; camadas adicionais precisam ser construídas. Não afirmar “3planos nativos” pelo nome|

Fontes reais em `biblioteca/hyperframes/<nome>/`. SHA-256 dosHTML:

- type-match-cut:`403c1a3200f795809bbf37bc6eb1f7659969dfcd2948a2c88c1308c843ad0b21`
- text-match-cut:`9bc1cc08bf75b56aa20b911d706e88755b1a6b39220f5ed5f7e70318ae184186`
- pan-stations:`3d3b32584a7b969025e13a5586a6f7f66cadca311758ce6f735e523a170d6ed3`
- slit-scan-reveal:`896d30e1162029a6f6085d3deb08da22a2b9ef717b1ac0597b09953ec0b1aae7`
- camera-rig-depth-stack:`d0ab77610390dd1e30ac53347b06e3d6aa432ac972989c18df8593d2a2b6b19e`

Foram também examinadosscreen-flow-carousel,spring-stack-shuffle,morph-swap,
pull-back-reveal e kinetic-center-build. Não priorizarcarousel de mockups para esta
V13. Spring-stack tem redireçãoHermite e massa, mas o conteúdo atual não precisa
virar pilha de cartões. Kinetic-center-build tem autoriaMITRemocn e exigeCustomEase
(arquivo local já disponível no pacoteGSAP, não presumir vendor incluído).

### Dois helpers úteis, sustentados por exemplos

1. `splitAperture(tl,upper,lower,media,at,opts)`: preservar a separação/oposição
   top/bottom e o painel que ocupa o espaço negativo de type-match-cut; rects e
   overscan definidos. Pode começar com “por aqui?” e terminar com imagem real,
   mantendo o vídeo e os textos congelados do roteiro.
2. `curveSwap(tl,a,b,at,{duration,mode})`: compartilhar um proxyprogresso eBezier85%
   de text-match-cut; fazer troca deopacity no meio e continuar o mesmo movimento.
   Rótulos/valores trocam como um grupo, sem reconstrução deUI ou nova métrica.

Não foram implementados helpers novos por este agente. Essas são propostas
operacionais; só marcar técnica implementada após inspeção do render final V13.
Snippets originais contêm domíniosCDN e timelines próprios: incorporar mecânicas no
timeline raiz e GSAP local; não importarvários clocks. Manter deterministicseek e
mesma quantidade de vértices em polígonosinterpolados. Não usar CSSanimationinfinite.

## Mudanças realizadas no acervo

- Quatro diretórios de originaisHyperFrames e atualização de `hyperframes/catalogo.json`.
- `packs/inventario.json`schema2: preservadas7amostras; novosvolumes/SHA/listagem;
  cinco candidatos pequenos; Glitchpartialrange; licença explícita pendente.
- `packs/README.md`novo e atualização pontual de `biblioteca/README.md`.
- `biblioteca/scripts/verificar.py`:WAV incluído no decode verificável; schema de
  itens continua compatível. Validador passou:18arquivosmídia/componentes,21fontes.
- Nenhum arquivo visual daV12/V13 alterado; nenhum helperV12 sobrescrito.
- Nenhum RAR gigante, prefixo ou dump integral de milhares de imagens copiado ao
  Git normal. Originais em LFS/cache e área privada da auditoria.
