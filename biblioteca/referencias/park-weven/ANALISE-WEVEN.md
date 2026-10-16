# Quarta referência única encontrada na auditoria — Park / Weven

## Identidade e momento da análise

Arquivo: `/workspace/attachments/4afe9f03-5ee4-48b4-89a4-b344f3484d18/Park_Criativo_video_no_watermark (1).mp4`.
SHA256 informado e confirmado pelo inventário do parent: `55e691627b4c2c44f867184702be323dd885e9f3767a4a9a7223eb4cbe1c6e95`.
Probe realizado nesta auditoria:42,608005s,576×1024,30fps,H264/AAC,781.464bytes.

**A análise deste arquivo específico foi realizada depois da definição da direção principal e do primeiro render da V12.** A descoberta veio da auditoria adicional de anexos. Não alego que esta quarta referência tenha orientado decisões anteriores. O objetivo desta análise é completar o repertório verificável, conferir lacunas e preservar a procedência.

É um anúncio da **Weven**, produto ligado a organização de clientes/CRM e IA, apresentado dentro de um cartão vertical com moldura e publicidade do autor **ParkCriativo** ao redor. O título externo `Quer um criativo assim? Me mande uma mensagem`, o perfil e o pássaro são a assinatura da apresentação do autor, não elementos do anúncio da Evoquex e não recursos reutilizáveis.

Li `/workspace/VIDEOS/evoquex-reel/analise-referencia-park.md`. O texto antigo declara64,70s e descreve uma sequência diferente, com outro padrão de imagens e objetos. Portanto esse documento **não serve como prova de análise anterior deste arquivo42,608s**, ainda que algumas técnicas genéricas coincidam. Não transferi automaticamente a descrição antiga.

## Método e evidência

Decode sequencial de todo o vídeo, selecionando número de quadro (`n=0,15,30…1275`) e salvando em ordem natural explícita. Foram86imagens, cobrindo0–42,5s. Inspecionei visualmente as quatro sheets completas:

- `park-extra-sheet-1.jpg`:0–13,5s.
- `park-extra-sheet-2.jpg`:14–27,5s.
- `park-extra-sheet-3.jpg`:28–41,5s.
- `park-extra-sheet-4.jpg`:42–42,5s.

Frames individuais em `park-extra-frames/`. Não houve escuta subjetiva. Os tempos são aproximados com resolução de amostragem0,5s; a análise identifica construção e encadeamento, não uma medição frame a frame de cada curva de aceleração.

## Sequência e técnicas concretas

| Tempo aproximado | Técnica observada | Adaptação possível para Evoquex |
|---|---|---|
| 0,5–1,5s | Ícone de pessoa dentro de círculo cresce; a frase muda de `Seu cliente` para `Demonstra interesse`; sublinhado se curva para baixo. | Ícone e verbo compartilham a mesma posição; transformação semântica em vez de exibir dois layouts independentes. Não transportar intenção de compra ao nosso case. |
| 2–3,5s | Cartão claro escurece; floco de neve/ícone vira metáfora de interesse que esfria. | Troca de luminância com função narrativa. A pergunta inicial daV12 já usa contraste sem assumir que alguém perdeu interesse. |
| 4–6,5s | Texto se monta por palavras; curva inclinada conduz um ícone de moeda; palavras se alinham e resolvem. | RiscoSVG como trilha de leitura e assentamento rápido. Moeda/dinheiro não se aplica ao nosso case sem dados de receita. |
| 7,5–9s | Bloco escuro com marca passa a campo claro colorido com `Foi criada!`. | Mudança de suporte e contraste marcando introdução da solução, não paleta aleatória. Não copiar identidadeWeven. |
| 9,5–11s | Retângulo simples ganha escala e se transforma em painel; linhas de clientes aparecem uma a uma. Depois surge carimbo `PERDIDA` em vermelho. | Componente construído por etapas. NaV12 o painel que vira estratégia/CTA desempenha papel comparável sem criar CRM fictício. |
| 12–15s | Palavra em pill `Centralize`; pessoa cresce; cursor pega item `cliente`, move-o para um funil que se monta em três níveis. A câmera recua e mostra a operação completa. | É a técnica mais forte desta peça: **interação representada visualmente**, o objeto conserva identidade ao mudar de contexto. Em Evoquex pode ser `vídeo → anúncio → público local`, com objeto compartilhado e seta, nunca um funil de vendas não comprovado. |
| 15,5–17,5s | Círculo rotuladoIA vira frase e destaque `follow-up`, com sublinhado. | Forma simples abre/fecha para revelar palavra e manter continuidade. Não adicionarIAà narrativa se não foi usada. |
| 18,5–20s | Ícone de planilha acompanha verbo/texto; depois a composição reduz para próxima frase. | Ícone semântico para contextualizar documento de campanha, não decoração. Captura real daV12 já garante a evidência. |
| 20,5–22,5s | Glow suave atrás da palavra; texto muda de tamanho; pill envolve palavra crítica, cursor aparece, plus surge e traço termina frase. | Hierarquia por foco e rótulo; em nosso vídeo a palavraVISTAcom cor e colchetes faz função equivalente sem copiar a sucessão de formas. |
| 23,5–24,5s | Plano azul superior e branco inferior, `Tenha humano`/`EIA`; cruz branca atravessa a fronteira. | Diagrama visual de combinação com duas regiões e conector. Adaptação adequada é `Mensagem + Público`, já presente no painelV12. Não usar humano/IA como alegação da produção. |
| 25–26,5s | Círculos concêntricos desenham o contorno enquanto frase aumenta de `Trabalhando` para `Trabalhando juntos!`; saída é zoom/círculo se expandindo. | `strokeDashoffset` emSVG+escala de grupo; seria útil para um segundo projeto mais baseado em processo, sem necessidade de acrescentar anéis em todaV12. |
| 27–29s | ConfirmaçãoPix vira palavra `cobranças`; faixa azul horizontal ocupa progressivamente todo o cartão com frase `Em um só lugar!!`. | **Transformação de faixa em fundo**, viável com retângulo que animaaltura e preserva texto na mesma coordenada. Pode tornar um rótulo em novo plano. Não copiarPix,cobrança,receita. |
| 30–33s | Círculo cresce pelo canto inferior esquerdo como máscara; palavras `operação` e `receita` trocam dentro de pill com glow. | Máscara circular de canto e troca de conteúdo num suporte comum. Boa alternativa a wipes retangulares em futuros vídeos; receita não pertence a esse case. |
| 33,5–35s | Círculo desenhado reduz/expande e tipografia passa de pequena a grande, com duas linhas e corpontual. | Controle de câmera e hierarquia por escala, sem novoasset. |
| 37–39,5s | Alternância preto/azul para frase comercial; CTApillcomcursor cresce;URL fecha. | Contraste e CTAencadeado. Evitar copiar promessa `Transforme oportunidades em receita`; nossa conclusão deve permanecer convite natural. |

## Como se relaciona às outras três referências

- **Weven:** mais didática e próxima de uma demonstração de operação. Um símbolo representa uma entidade, e essa entidade muda de estado. A complexidade está na continuidade semântica, não em3Dou grande densidade de objetos.
- **OtoCriativo:** composição mais variada, objetos de mídia/documento, cards em perspectiva, foco seletivo eCTAassimétrico. Foi a principal referência nova daV12.
- **Park/ShardCloud:** formas ópticas, palavras, conexões etransformação de suporte; maior presença de objetos/lentes.
- **Park/Virgílio:** perguntas, verbos, frasescurtas e ícones que ajudam a explicar umserviço.

Esta análise complementar reforça a decisão de manter cada elemento com função. Não há recomendação de transformar aV12numdemonstrativo deCRM, criar funil, conversa, intenção de compra ou qualquer prova de receita.

## O que mais e menos se aplica

**Mais adequado:** objeto compartilhado entre etapas, painel que se constrói, ícone com verbo, forma que muda de escala para abrir próxima cena, combinação de dois conceitos por conector, CTArevelado de um suportejáexistente. A adaptação pode ser realizada integralmente comCSS,SVG,GSAPeHyperFramesexistentes.

**Menos adequado:** moldura permanente de telefone, excesso de subtítulo miúdo, lista deCRM, arrastedeclientepara funil, dinheiro/Pix, marca/URL, carimboPERDIDA, promessa de receita. São elementos específicos da história da referência ou alegações inadequadas para os dados disponíveis.

## Há algo essencial ausente na V12?

Não identifiquei um requisito técnico ou narrativo essencial que exija reabrir a direção daV12 por causa deste arquivo. A V12járealiza transformação do suporte real em painel, palavra-etiqueta, íconescombinados, seta e objeto com movimento emprofundidade; essas soluções cobrem a função das técnicas desta quarta referência.

Uma futura evolução poderia aprofundar a continuidade `vídeo → anúncio → público` com o mesmo objeto atravessando três estados emvezdeuma simples troca de frase. Isso é uma possibilidade criativa, não umdefeito que invalide o render atual e tampouco exige adicionar todososrecursos de todasasreferências.

A prioridade imediata continua sendo o ajusteQA já identificado no primeiro render: reduzir a pausa totalmente azul antes da métrica e antecipar o preenchimento do painel, preservando os dados e a legibilidade.
