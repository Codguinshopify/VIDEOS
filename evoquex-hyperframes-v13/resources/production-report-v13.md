# Evoquex V13 — relatório de produção

**Estado: MP4 final renderizado e revisado por sequências consecutivas e análise técnica.**
Os limites de reprodução contínua e escuta permanecem explícitos ao fim. O render
anterior serviu à crítica e foi corrigido antes desta entrega.

| Identificação da entrega | Estado |
| --- | --- |
| Caminho | `renders/evoquex-hyperframes-v13.mp4` |
| Formato | 30 s; 1080 × 1920; 30 fps; 900 frames |
| SHA-256 do MP4 final revisado | `548a550705c835551b4ab2817acec0d92862eb79fee40b6299a18c54c6a81ef2` |
| Confirmação visual por técnica | Confirmada por sequências do arquivo acima |
| Verificação técnica do áudio final | Decode completo; −16,25 LUFS; −1,74 dBTP; zero clipping |
| Reprodução contínua e escuta subjetiva | Indisponíveis nesta interface; não realizadas |

## Principais mudanças implementadas no código

O hook de 0 a 4 segundos e os textos da V12 foram protegidos. A reconstrução se
concentra no restante: a tipografia revela a fotografia da cidade; uma câmera percorre
estações conectadas; texto e filmagem trocam escala e hierarquia; palavras e valores
se reúnem por fragmentos; a captura original participa da composição; os dois dados
ocupam arranjos diferentes; mensagem e público se conectam por curva; o convite final
utiliza uma fronteira móvel e CTA tipográfico, em vez de repetir cartão e botão.

Não houve reescrita do roteiro, criação de métricas, depoimentos ou imagens de clientes.
As mudanças descritas foram conferidas nas sequências extraídas do MP4 final.

## Referências e aplicações

| Princípio técnico | Referência e tempo | Trecho da V13 | Estado de confirmação |
| --- | --- | --- | --- |
| Expansão de suporte a partir do conteúdo | Shard Cloud, 2,067–3,267 s | 4,04–5,83 s: máscara tipográfica e abertura da foto | Confirmado nas sequências do MP4 final |
| Borda que assume outra função | Virgílio, 19,267–19,800 s | 7,12–8,41 s: contorno, linha e abertura do filme | Confirmado nas sequências do MP4 final |
| Planos e trajetórias internas em eixos diferentes | OtoCriativo, 7,900–8,267 s | 7,64–10,20 s: câmera, nome, filmagem e texto | Confirmado nas sequências do MP4 final |
| Fragmentação e recomposição | OtoCriativo, 14,733–15,233 s | 5,86–6,43 s; 10,93–11,54 s; 15,12–15,74 s; 17,98–18,65 s | Confirmado nas sequências do MP4 final |
| Objeto que muda de função durante o percurso | Weven, 12,200–13,800 s | 12,75–15,35 s: vídeo horizontal e passagem à prova | Confirmado nas sequências do MP4 final |
| Mudança de geometria que prepara outro campo | Weven, 27,800–29,267 s | 14,63–16,05 s: documento em painéis e numeral | Confirmado nas sequências do MP4 final |
| Conector que redistribui a composição | Shard Cloud, 26,067–27,000 s | 21,65–23,95 s: mensagem, público, curva e passagem | Confirmado nas sequências do MP4 final |
| Fronteira móvel entre campos do CTA | Virgílio, 55,300–57,300 s | 23,72–30 s: pergunta, convite e assinatura | Confirmado nas sequências do MP4 final |

O detalhamento de seletores, helpers e critérios está em
`REFERENCE-IMPLEMENTATION.md`. Os quatro arquivos únicos de referência permanecem
preservados no repositório, inclusive os reenvios reconhecidos por hash.

## Recursos efetivamente reutilizados

- Vídeo original da Danny’s Presentes: uma reprodução, com áudio zerado.
- Fotografia aérea real de Clevelândia e captura original dos resultados.
- Fonte DM Sans local, vetores Lucide e helper V12 preservado.
- Mecânicas HyperFrames adaptadas: `type-match-cut`, `pan-stations` e
  `text-match-cut`, com código novo separado em `vendor/evoquex-v13-motion.js`.
- MotionPathPlugin, já disponível no pacote GSAP, para o ponto que percorre a curva.
- Instrumental e efeitos próprios existentes, com licença e procedência preservadas;
  nova edição após o segundo 4, totalizando 24 acentos.

O pack 6000 Motion teve os três volumes recuperados e o RAR interno listado. Cinco
amostras pequenas foram preservadas na biblioteca, porém a licença comercial dos
efeitos não foi encontrada: **nenhum novo áudio ou overlay desse pack foi usado na
peça**. Do Glitch, foram inspecionados somente um prefixo e previews de 250 × 141;
não foram tratados como efeitos HD. Não foi gerado asset de IA nesta versão, pois
documentos e vetores existentes resolvem as necessidades sem fabricar evidência.

## Problemas encontrados e corrigidos

As alterações abaixo foram reconferidas no arquivo definitivo:

| Ponto tratado | Ajuste presente | Confirmação final |
| --- | --- | --- |
| Posicionamento de artwork absoluto dentro da grade | Rigs de filmagem, documento, diagrama e campo usam o canvas completo, sem herdar o inset da célula | Confirmado no MP4 final |
| Encontro entre frases do processo | Janela de clipping específica para a tipografia de produção/divulgação | Confirmado no MP4 final |
| Contraste no cruzamento entre texto e filme | Gradiente na região superior da filmagem e sombra localizada na tipografia | Confirmado no MP4 final |
| Descoberta duplicada da mídia da prova | Três painéis complementares com o mesmo background real, em vez de três tags de imagem | Confirmado no MP4 final |
| Distribuição da assinatura no encerramento | Alinhamento e distância revistos no campo final | Confirmado no MP4 final |

Também corrigidos e confirmados pelo parecer independente:

- 10,4–10,9 s: eliminada a espera com placa azul vazia; suporte abre junto às fatias.
- 23,35–24,55 s: o conector permanece no eixo y=1050 e origina o campo azul; retirada
  a separação espacial entre linha e nova superfície.
- 26,9–30 s: pergunta elevada em 60 px; cedilha de “serviço?” mantém folga, inclusive
  durante a reação da fronteira. Assinatura passou à esquerda, separada da curva.

O primeiro render foi inspecionado em 393 frames consecutivos e 60 amostras da duração.
A revisão final repetiu as nove sequências e amostras; o parecer independente examinou
129 frames alterados mais 37 amostras próprias e um recorte em resolução integral.
Não foi encontrada falha visual adicional nos trechos examinados.

## Verificações realizadas

- Contrato de fontes e texto passou. Hook HTML/CSS/GSAP preservado; todos os 120 frames
  exportados comparados: SSIM médio 0,9997497, mínimo 0,998027. Isso representa alta
  similaridade dos exports H.264, não identidade lossless de pixels.
- Prefixo PCM de quatro segundos idêntico à V12: 192.000 frames estéreo. AAC é compressão
  com perdas; não foi alegada igualdade de bits no áudio codificado.
- MP4: 30 s, 900 frames, 1080×1920, H.264/BT.709, AAC estéreo 48 kHz; decode completo.
- Áudio final: −16,25 LUFS, −1,74 dBTP, zero clipping, correlação 0,9993028 com o WAV.
  Os 24 acentos foram associados à timeline; um sweep antecede a janela por cerca de
  1 ms, com sua janela RMS sobrepondo o movimento. Não foi constatado problema material.
- Check nativo: lint/runtime/layout/contraste sem erros ou avisos; 104 amostras de texto
  passaram no contraste. Motion automático nativo desativado; mapa separado executado
  e revisado em 1080×1920. O único conflito de rotação é o hook aprovado preservado.
- Reprodução isolada do ZIP passou: CRC, instalação offline das 80 dependências fixadas,
  lint e oito snapshots solicitados, todos em 1080×1920 (CLI adicionou um nono ao fim).
  As 26 entradas essenciais de render e mídia coincidem por hash. A ausência da V12
  isolada limita apenas a comparação com a versão anterior; não impede o render nativo.
- Fluxo temporal estimado em todos os 900 frames; leitura semântica feita por sequências.
  Fontes originais conferidas por hash, Studio respondeu HTTP200, biblioteca passou em
  19 arquivos e 21 fontes de catálogo. Relatórios vinculados ao SHA final.

Os valores reais são **20.981 impressões/exibições do anúncio** e **13.064 pessoas
alcançadas**. A Evoquex produziu o vídeo e direcionou a campanha somente a Clevelândia.
Ir além dos seguidores é objetivo, sem quantidade medida desse público. Não há prova
de vendas, conversões, visualizações ou retorno financeiro. Luciane continua fora do
render, sem placeholder ou dados inventados.

## Limitações reais

- Locução feminina natural pendente: não houve geração autenticada, compra ou voz
  fictícia. Os cues são estimativas editoriais, não alinhamento com gravação.
- A interface não permite playback contínuo nem escuta subjetiva. A revisão utiliza
  sequências consecutivas e checks técnicos; não equivale a ouvir ou assistir em tempo real.
- Fluxo óptico e deslocamentos acumulados são estimativas de imagem, sem identificação
  semântica garantida do objeto. Cortes, blur, grão e oclusões podem afetá-los.
- SSIM do MP4 não prova identidade lossless; compressão pode produzir diferenças.
- Profundidade CSS/2.5D não é CGI físico. A foto aérea original tem resolução de 600 × 337.
- Packs auditados exigem comprovação de licença ou outra ferramenta para formatos
  nativos Adobe; não se presume execução direta no HyperFrames.

Entrega: vídeo editado e relatório objetivo; nenhum render comparativo produzido.
Fontes, origens, skills e QA ficam preservados para a continuidade do trabalho.
