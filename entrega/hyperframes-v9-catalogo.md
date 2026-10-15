# V9 — recursos do catálogo efetivamente adaptados

Origem: heygen-com/hyperframes, commit 08ee1bd5ad59987a7f2525222683e24ca30971f9.
Originais HTML e manifests estão em catalog-originals; catálogo não é um pack de vídeos.
A instalação por hyperframes add não alcançou o host HTTP neste ambiente. Os mesmos
fontes foram obtidos do clone Git existente e incorporados localmente, com provenance.
Não se afirma que o comando add tenha funcionado.

| Recurso novo | Onde aparece | Mecânica preservada | Adaptação real |
|---|---|---|---|
| svg-mask-reveal | Abertura, 0–0,75 s | Palavra SVG como máscara, interseção com faixa que percorre a palavra | Fotografia original substitui fill do demo; VÍDEO em Manrope; bounds e IDs próprios |
| perspective-marquee | Abertura, 0,8–4,5 s | Pílulas duplicadas num plano inclinado, offset único seekable | SUA EMPRESA / SEU SERVIÇO, escala maior, paleta Evoquex |
| paper-collage-reveal | Passagem, 4,5–5,09 s | Mesmo LCG de seed 0x2c6b8f19, polígonos irregulares, deslocamento radial e arco perpendicular | Seis papéis azuis em malha 2×3 vertical, frases do case e transição mais curta |
| locked-nucleus-orbit | Cidade, 11,1–13,3 s | Braços rotacionam e chips contrarrotacionam para permanecer legíveis | Foto real é núcleo fixo; satélites Instagram, Facebook, Público local; sem sugerir mapa geográfico |
| kinetic-center-build | Perguntas, 23,16–25,64 s | Posições calculadas para cada prefixo; cada palavra desloca as anteriores até centralizar | Português, palavras medidas com Manrope 800, uma timeline raiz, entradas comprimidas |
| wordmark-tiles | Encerramento, 28,85–30,46 s | Mesmo LCG 0x57a7c1e e rank column+row×0,68+sin(row×1,7+column×0,42)×2,15; fragmentos da mesma marca em 60 células | Evoquex, recortes em px fixos do canvas vertical, ruído nas cores da marca, onda curta e hold |
| zoom-through-transition | Passagens 10,5 / 28,5 s | Recorte do incoming 100→0%, x 60→0 e scale 1,04→1; compressão/blur outgoing e faixa de acento | 0,52 s, sem strobes RGB do demo; cenas verdadeiras substituem labels genéricas |

As funções de adaptação estão em catalog-motion.js e são chamadas na coreografia motion.js.
HTML/CSS e as seis composições são novos; a V7 e a V8 ficam preservadas. Não se limitou
a copiar os quatro recursos que as versões anteriores já usavam. O conteúdo factual e a
faixa de música/efeitos continuam iguais para permitir comparação honesta. Nenhum áudio
externo ou locução foi retirado do catálogo. Instalação e execução sem CDN no render.
