# Packs — estado verificado na auditoria V13

O inventário canônico é `inventario.json`. Os originais grandes permanecem em
Git LFS na branch `packs-lfs`, commit `b1e0a83a28f424143601f134d9e1de2570eaf54c`.
Não copiar RARs de gigabytes para Git normal. Não executar instaladores, plugins,
AEP, MOGRT ou HTML de documentação para fazer uma inspeção de formatos.

## 6000+ Motion Graphics Pack V5.1

Os três volumes estão presentes no remoto e foram recuperados no cache LFS.
SHA-256 e tamanho dos três foram conferidos. Sem baixar novamente a parte 1,
a auditoria baixou as partes 2 e 3 e recuperou o RAR interno completo:
3.400.442.578 bytes, SHA-256
`da6b3f82dee8c8dfbaf91f62e5d8fd677fd17161d822a32a6a30563e0ff65952`.
O contêiner externo terminou sem erro; a listagem interna chegou ao fim com
11.829 entradas, aproximadamente 4,98 GB regulares expandidos.

Isso significa que o arquivo completo está disponível nesta auditoria, **não** que
cada projeto ou cada mídia foi executado/decodificado. Foram identificados:

- 206 AEP e 1.354 MOGRT: exigem o aplicativo, fontes e dependências de origem.
- 83 MP4: 13 tintas, 12 flares e 58 partículas/revelações.
- 567 WAV: swooshes, impacts, interface e outras categorias.
- 4.601 GIF e 4.605 PNG: muitos estão em `Atom Preview Assets`; o formato não
  comprova que sejam elementos finais em alta resolução.

As sete amostras antigas de `6000-motion-amostras/` continuam preservadas.
Os relatórios `part1-*` nessa pasta são históricos e corretamente descrevem a
inspeção parcial daquela etapa. O inventário canônico contém o estado atual.

A pasta `6000-motion-audit-v13/` acrescenta somente cinco arquivos, 3.958.157 bytes:
Fast Swoosh 1 e Impact 1 em WAV; TransitionFlare_1 em MP4; Fonts.txt e Fonts.html.
Cada mídia selecionada passou por leitura completa da entrada/CRC, hash, probe e
decode FFmpeg. WAV é PCM16 estéreo 44,1 kHz; flare é H.264 1920×1920, 1,668 s,
yuv420p, **sem alpha**. Um fundo preto não vira transparência automaticamente.

Não foi encontrado arquivo de licença, README, EULA ou termos pelo nome em toda a
árvore. Os dois documentos disponíveis listam fontes e links de download; não
concedem licença do pack. Portanto os candidatos ficam com direitos de uso e
redistribuição pendentes e **não são declarados utilizados no audiovisual V13**.
O som da peça continua usando os stems com procedência/licença já documentadas.
A presença da amostra no acervo técnico não equivale a liberação comercial.

## 650+ Glitch Elements v1.0

Há três pointers LFS no remoto: 1.048.576.000, 1.048.576.000 e 315.397.780 bytes.
Foi baixado somente o intervalo de 8 MiB inicial da parte 1 por HTTP 206, sem
confundir prefixo com volume completo. O RAR contém outro RAR. A inspeção parcial
confirmou previews GIF/PNG de gradientes, 250×141; quatro pares completos foram
extraídos e decodificados na área privada da auditoria. A entrada seguinte estava
truncada no prefixo e não foi incluída como válida. As partes 2 e 3 não foram
baixadas; integridade e conteúdo completos do Glitch permanecem sem validação.

Prefixes, RAR interno de gigabytes e inventários extensos ficam fora do Git normal.
O manifesto compacto registra bytes, hashes, intervalo, condição real e limitações.
Não dizer que o Glitch inteiro foi analisado nem que seus previews são overlays HD.

## Reutilização

Antes de integrar qualquer candidato: verificar licença, formato real, integridade,
alpha, resolução, duração e composição no motor. MP4/WAV independentes podem ser
usados no HyperFrames após validação e direitos; AEP/MOGRT/ATOM não executam em HTML.
Os contadores de formato descrevem caminhos listados, não 11.829 assets prontos.
