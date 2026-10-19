# Assets de packs preparados para a produção V15

Esta seleção é material de produção. O manifesto registra a origem, os hashes,
os parâmetros de conversão e as limitações de cada arquivo. Nenhum recurso é
marcado como usado na edição apenas por estar nesta pasta.

O usuário autorizou expressamente o uso dos materiais fornecidos, inclusive
comercialmente. As antigas observações de licença da auditoria V13 descrevem
aquele momento e não devem bloquear genericamente esta produção.

| Arquivo pronto | Origem | Aplicação deliberada |
| --- | --- | --- |
| `ink-11-portrait-mask-atlas.png` | 6000 Motion / `Ink_11.mp4` | Revelação orgânica da cena real da Danny’s Presentes, aproximadamente 6,74–7,36 s. Máscara com borda de tinta verdadeira do pack, controlada pela timeline. |
| `flare-warm-impact.mp4` | 6000 Motion / `TransitionFlare_1.mp4` | Acento curto de luz na passagem para o resultado, aproximadamente 15,72–16,22 s. Screen blend, intensidade controlada e saída gradual. |
| `brush-2-alpha.png` | 6000 Motion / `Brush 2.png` | Sublinhado material, revelado por recorte, para Produzimos ou Estratégia se o acabamento combinar. Não é obrigatório usar. |
| `dots-light-burn.mp4` | Viral Video / `Dots light burn 1.mov` | Feixe azul de pontos para a composição de distribuição; uma alternativa ao flare quente, sem repetir os dois a cada transição. |
| `woven-texture-gray.jpg` | Viral Video / `Background texture.jpg` | Textura discreta para o fundo quente da produção ou para o resultado. Opacidade baixa; a tipografia permanece dominante. |

O sound design também dispõe dos WAV reais `SFX - Fast Swoosh 1.wav` e
`SFX - Impact 1.wav` em `../packs/6000-motion-audit-v13/`. O responsável pelo áudio
selecionará as ocorrências, cortes e níveis conforme os movimentos finais.

## Máscara de tinta

- Atlas RGBA 3240 × 4800: seis colunas, cinco linhas, trinta estados.
- Cada estado mede 540 × 960, adequado ao recorte vertical.
- `mask-size: 600% 500%` e `mask-repeat: no-repeat`.
- Para o estado `i`: posição X `(i % 6) * 20%`, Y `floor(i / 6) * 25%`.
- Estado 0 completamente transparente; estado 29 completamente opaco.
- Os estados intermediários vêm dos primeiros 2,25 s do vídeo, com rotação de
  90° e alpha derivado de `255 - luminância`. Não são manchas recriadas manualmente.
- Interpolar o índice inteiro durante aproximadamente 0,62 s; remover a máscara
  quando completar a abertura. Aumentar a duração requer mais estados para evitar
  repetição excessiva de quadros.

## Vídeos, transparência e reprodução

Os dois MP4 são H.264/yuv420p com `faststart`, silenciosos, 30 fps. **Não possuem
alpha.** O fundo preto exige screen blend ou composição equivalente. O flare dura
0,500 s; a conversão do light burn mantém sua evolução completa de aproximadamente
1,167 s. São recursos de passagem, não fundos permanentes.

A tinta e o brush são PNG com alpha efetivo. O JPEG da textura não tem transparência.
O contraste, a intensidade e o instante de entrada devem ser validados na composição
e no MP4 final. A validação isolada não substitui a revisão da integração.

## Recuperação e escolhas

As amostras preservadas do pack 6000 foram reutilizadas; não houve novo download
de seus volumes. Somente o Viral Video foi recuperado do Git LFS, com 225.406.633
bytes e SHA-256 `bd2e024256780f4de3910c425cf0d956ffca547d673c07cde8a4548bf2bf4c47`.
O `git lfs fetch` encontrou HTTP 503 ao ler uma árvore promisor do GitHub; o resolver
oficial de mídia LFS do GitHub entregou o objeto completo, conferido contra o ponteiro.
O teste integral pelo 7-Zip 26.04 terminou sem erros em todas as trinta entradas
regulares. Apenas cinco entradas relevantes foram extraídas, cerca de 30,5 MB.

O arquivo `scene1- alpha.mov` é uma máscara em preto e branco para pessoas segurando
placas; não contém alpha embutido. O vídeo correspondente mostra personagens que
não pertencem ao case. Ambos foram decodificados e inspecionados temporalmente;
não foram selecionados para esta narrativa. O AEP do template requer After Effects
para executar seu projeto, mas os MOV e o JPEG escolhidos independem desse runtime.

O pack não contém WAVs independentes. A trilha do demo não foi extraída nem reutilizada.
Não houve novo download dos packs de mockups ou glitch: os candidatos já disponíveis
atendem às necessidades identificadas sem recuperar vários gigabytes desnecessários.

Os originais compactados continuam preservados fora da biblioteca normal do Git.
Esta pasta contém somente cinco derivados pequenos, sua documentação e a procedência.
