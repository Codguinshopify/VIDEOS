# Auditoria visual da referência OtoCriativo e da V11 — etapa V12

## Material e método

Arquivo recebido: `/workspace/attachments/81f6c078-c0f5-4c37-bed1-64bbda0ba12d/oto_criativo_video_no_watermark.mp4`.
Probe: 27,766667 s, 833 quadros, 576×1024, H.264 a30fps; AAC estéreo44,1kHz. É uma terceira referência, diferente das duas Park preservadas.

Inspecionados visualmente os56quadros ordenados da duração inteira em `oto-exact-1.jpg` e `oto-exact-2.jpg`, selecionados por número de quadro (`n=0,15,30…825`). Mais72quadros em quatro sheets de detalhe (`details/hook.jpg`, `cards.jpg`, `type.jpg`, `cta.jpg`). Confirmação por decode sequencial dos quadros0,6,30,45,60. A primeira geração de sheets estava fora de ordem por `glob` sem ordenação; foi substituída e não serve como evidência de timing. As sheets `oto-exact-*` são as definitivas.

**Precisão temporal:** os intervalos abaixo são aproximados, refinados pelos detalhes quando necessário. O primeiro quadro real é branco; o texto resolve logo após0,1s. A nossa exigência de ação desde o quadro0 é mais rigorosa que o arquivo de referência e precisa ser atendida diretamente na V12.

Também li o catálogo e a análise conjunta em `/workspace/VIDEOS/biblioteca/referencias/{catalogo.json,ANALISE.md}` e inspecionei as três sheets reais da V11, cobrindo todos os33s, mais o frame de celular da cidade. Não houve escuta subjetiva: estas observações não avaliam timbre, naturalidade ou mix percebido.

## O que a nova referência efetivamente faz

| Tempo aproximado | Construção observada | O que aproveitar |
|---|---|---|
| 0,10–0,60s | Frase central entra com blur horizontal/escala e resolve rapidamente. | Entrada curta e resolução nítida; nunca deixar blur sustentado sobre mensagem. |
| 0,70–1,15s | Telefone vertical sobe/escala diante de três cópias de “Criativos”; cópias perdem contraste em profundidade. | Tipografia como cenário e objeto como primeiro plano, não título sobre miniatura. |
| 1,20–2,25s | Confirmação Pix no centro, símbolos de dinheiro com tamanhos e focos diferentes na periferia, valor muda. | Planos de profundidade e foco em um dado. NÃO transportar recibo, valores, dinheiro ou prova comercial ao case. |
| 2,40–3,75s | Frase montada por trechos; fundo branco vira preto; curva curta termina o argumento. | Mudança de contraste com função narrativa e traço como conclusão, sem repetir sempre sublinhado. |
| 3,90–5,10s | Letras de “Criativos” começam rotacionadas/desalinhadas e se assentam; enquadramento amplia para revelar preço e elementos periféricos. | Palavra construída por letras e câmera que revela uma composição maior. Não copiar preço. |
| 5,45–6,40s | Retângulos verticais grandes entram em vários planos; texto fica entre eles. | Máscara de vídeo presente antes de mostrar o conteúdo; movimento espacial preparado. |
| 6,80–8,85s | Carrossel2.5D: cards de tamanho fixo atravessam a tela; anterior permanece parcialmente na borda; ponto inferior muda; conteúdo interno também anima. | Três tipos de movimento simultâneos mas hierarquizados: trilho, indicador, conteúdo. O mapa nacional e a contagem de vendas são exclusivos da referência, não do case. |
| 9,00–9,75s | Frase entra por palavras com foco progressivo e depois desaparece em blur. | Direcionar leitura sem trocar o layout para cada sílaba. |
| 10,00–10,95s | Cápsulas azuis de vários tamanhos entram lateralmente; uma tem círculo interno que percorre o trilho; texto ocupa o vazio central. | Formas explicam estado/ação e organizam espaço; não são confete. |
| 11,15–11,70s | Folha de roteiro em perspectiva com faixa passando à frente; blur na entrada resolve a peça. | Documento real como objeto, profundidade por pequena rotação e recorte, com anotações em camada distinta. |
| 11,80–12,80s | Forma de onda vertical anima com dois objetos em planos desfocados e texto secundário abaixo. | Animar uma série de barras por dados reais de áudio, caso a voz esteja disponível; não simular voz inexistente. |
| 13,00–14,60s | Linha curta é revelada de esquerda a direita; fundo vai de branco a cinza mais escuro em etapas enquanto frase se conclui. | Revelação por faixa de palavras e contraste gradual em uma mesma ideia. |
| 14,70–15,45s | “Profissional” se repete em três profundidades; balão preto rotacionado vem da lateral, desacelera e assenta com sombra. | Hierarquia de títulos + objeto que resolve num rótulo. Letras atrás com baixo contraste, sem competir. |
| 16,00–18,10s | Bolhas de conversa entram em sequência; uma bolha de arquivo cresce para aparecer como conteúdo entregue. | Sequência de processo, mas sem criar conversa/depoimento fictício no case. Pode virar sequência de fases factuais com rótulos claros. |
| 18,30–20,20s | Cada palavra-valor é acompanhada por ícone específico; câmera passa por escala grande/blur entre itens. | Ícone semântico conduz a transformação da próxima composição. NÃO transportar “preço acessível”, segurança ou qualidade como promessas sem base. |
| 20,45–21,10s | Botão ganha contorno desenhado em volta e cursor circular aproxima; botão escala para longe na saída. | Contorno por SVG e movimento que leva ao CTA; evitar simular interface clicável se vídeo. |
| 21,40–22,45s | Telefone na esquerda, frase à direita, seta curva desenha até o objeto. | Composição assimétrica e seta como explicação da relação imagem/mensagem. |
| 22,65–23,50s | Frase curta resolve em foco; depois marca ocupa centro. | CTA com uma ideia clara e encerramento breve. |
| 23,65–27,75s | Símbolo e depois wordmark sustentados por vários segundos. | Não imitar a longa espera da marca no nosso Reels. |

A densidade é controlada: a maior parte das frases aparece no centro com espaço negativo; as mudanças de escala, suporte e semântica fazem o movimento parecer mais elaborado. Não é uma tela permanentemente cheia. Os trechos mais ricos (cards, objeto+palavra, documento, conversa) alternam com frases breves.

## Limitações visíveis da V11

1. **A composição central se repete por quase todo o vídeo.** Hook, distribuição, prova, perguntas e CTA usam região central estreita, texto acima e objeto pequeno abaixo. O fundo muda na prova, mas a organização espacial pouco muda.
2. **Abertura4,5s contém essencialmente uma única estrutura.** Troca “sua empresa/seu serviço/pela mensagem” sobre o mesmo sublinhado. Existe animação, mas pouca transformação narrativa ou de escala.
3. **A filmagem vira miniatura por todo o trecho4,5–9,5s.** A escala do conteúdo real poderia alternar entre detalhe e contexto, integrando-se a recortes que revelem a próxima ação. Não é necessário mostrar várias cópias independentes simultâneas.
4. **A imagem da cidade fica como cartão11,25–14,25s.** A cidade é uma informação estratégica confirmada, mas o cartão pequeno não explica a diferença entre conhecer a empresa e receber o anúncio.
5. **As métricas15–21s têm legibilidade e precisão, porém a mesma moldura.** Cada número resolve e fica cerca de3s; número, rótulo, risco e miniatura de evidência nunca mudam de relação. Convém associar alcance a pessoas e impressões à repetição/exibição, sem gráfico fictício.
6. **Perguntas22–27s repetem a estrutura do hook.** Seria melhor levar uma peça visual do resultado à pergunta sobre outra empresa.
7. **CTA quase parado de29–33s.** A pausa facilita leitura, mas quatro segundos da mesma composição podem ser reduzidos/ocupados por uma transformação discreta que conclua a ideia.

Preservar da V11: exatidão das duas métricas, nome correto, uso do material original, subordinação do azul, espaço negativo e tamanho de texto. A evolução deve aparecer em escala, encadeamento entre objetos e distribuição da atenção, e não somente em mais ocorrências de blur.

## Nove técnicas diferentes e implementação concreta

1. **Construção por letras e substituição de palavra em recorte.** `span.char` por letra, `gsap.fromTo` com `yPercent:105`, rotações pequenas alternadas e stagger0,018–0,028s; um ancestral `overflow:hidden` impede vazamento. Duração da formação0,32–0,45s, mantendo o estado legível0,65–1s. Palavras subsequentes substituem o grupo por eixo diferente, em vez de repetir fade.
2. **Câmera sobre planos2.5D.** Um wrapper `perspective:1300px` + filhos em `translateZ`, `rotationY` e escala; GSAP move wrapper. Limitar rotação da filmagem5–7graus para não atrapalhar leitura. Camadas têm blur apenas na passagem, nunca como efeito contínuo.
3. **Carrossel sem reiniciar cena.** Trilho com cards posicionados em x e diferença de Z; deslocamento comum e foco individual do card ativo; retângulos têm `clip-path:inset` e conteúdo ancorado. Um ponto/linha muda juntamente. Usar como processo “vídeo produzido → anúncio → público local”, não como catálogo de efeitos.
4. **Imagem compartilhada transformada em máscara.** Mesma fotografia em duas camadas bit-identical com máscaras complementares, ou um único elemento cujo container anima posição/raio/tamanho. Troca de contêiner de faixa larga para janela vertical em0,35–0,55s; não cortar abruptamente a cidade para um cartão vazio.
5. **Traço SVG como ponte semântica.** Curva com `pathLength=1`, strokeDashoffset1→0 em0,3s, seta apontando do vídeo para “Clevelândia”; depois o mesmo traço serve de divisor da prova. Não usar curva aleatória em todas as cenas.
6. **Tipografia com profundidade e rótulo em primeiro plano.** Duas cópias decorativas do título com opacidade0,12/0,06 e deslocamentosy30/60; título real intacto e rótulo entrou por rotação/escala. Cópias `aria-hidden`; mascarar e retirar quando troca frase. Só um momento de ênfase, nunca em todos os títulos.
7. **Contadores sem gráfico inventado.** Animar os dígitos reais em um `data-value`, `Intl.NumberFormat('pt-BR')`; numeral cresce em0,6–0,8s e resolve no valor exato. Alcance pode ter3–5pictogramas qualitativos sem equivalência quantitativa; impressões pode ter uma ficha repetida em3camadas, rotulada “exibições do anúncio”, evitando “visualizações”. Número no mínimo1,3s após resolver.
8. **Foco seletivo e ponte de zoom.** Durante0,2–0,35s de deslocamento, blur0→5→0px e escala0,92→1; `filter` é caro, aplicar em um pequeno wrapper, não a viewport inteira. A cena resolve, depois fica nítida. Evitar segurar o blur como substituto de leitura.
9. **Contorno de CTA e resposta do objeto.** SVG rect com comprimento normalizado1, `strokeDashoffset` e arrow draw; o suporte do objeto da etapa anterior vira o contorno, enquanto a frase aparece. Resposta de escala1→1,025→1 pode ocorrer uma vez, não loop infinito.

Todas são viáveis com GSAP, CSS, SVG e HyperFrames existentes. Não há necessidade de uma nova biblioteca nem de AEP, animação3D real ou asset externo não confirmado. O roteiro pode receber locução depois pelo mesmo mapa de eventos; ondas de áudio só devem ser incluídas após ter arquivo real.

## Proposta específica ao roteiro0–30s informado

### 0–4s: hook escuro

Frame0 já com fragmentos grandes de `SUA EMPRESA` e filete azul avançado, câmera ligeiramente aproximada. Nada de tela vazia. Texto organiza-se entre0–0,35s.0,85s: `É CONHECIDA` substitui parte de “SUA EMPRESA” por máscara vertical.1,65s: `EM CLEVELÂNDIA.` entra como uma faixa territorial; contorno da cidade/foto permanece apenas num recorte de letras.2,65s: `MAS É VISTA?` ocupa90%da largura em quebra intencional, fundo escuro, azul sobre “VISTA?”. O ponto de interrogação/linha torna-se a curva do próximo plano. É uma pergunta, não afirmar que empresários não são vistos.

### 4–8s: reconhecimento vs exposição

Revelar imagem aérea ampla por máscara que acompanha a curva. Em frente, dois estados qualitativos: “Quem já conhece” como rótulo pequeno à esquerda; “Receber seu anúncio” como foco à direita. Não quantificar não seguidores nem declarar que o alcance foi além deles. Câmera transfere foco de nome/empresa para peça/anúncio. No final, janela de vídeo já está posicionada para receber o material Danny’s.

### 8–15s: ação do case

O original real deve ser importante na composição: janela vertical maior e título lateral `Danny’s Presentes`. Bloco8–10,5s apresenta “Produzimos o vídeo”;10,5–12s puxa a mesma janela para card de campanha;12–15s fotografia local+seta mostram “Anúncios só para Clevelândia”. Pode usar carrossel2.5D em apenas uma passagem, com a janela de vídeo como objeto compartilhado. Não inventar tela de gerenciador da campanha; usar a captura real se precisar mostrar prova.

### 15–21s: evidência, sem virar relatório

15–17,8s o card resolve em `13.064 pessoas alcançadas`. ícones qualitativos periféricos; nada que pareça contabilizar pessoas exatas desenhadas.17,8–20,6s o mesmo card se desdobra em camadas para `20.981 exibições do anúncio` / rótulo técnico `impressões`.17,8transição orientada pela troca de significado, não outrowipegenérico.20,6–21s snapshot real da evidência fica legível o suficiente para reconhecer fonte; manter o limite de resolução, sem redigitar tela como se fosse captura.

### 21–30s: relevância e CTA

A ficha de campanha se afasta e deixa uma composição assimétrica com “E a sua empresa?” / “Seu serviço?”. Elemento principal passa à esquerda; o convite ocupa a direita e depois centraliza. A seta desenha a ligação para “Conversa com a gente.”. Usar21–24,5s para relevância,24,5–28s convite,28–30s leitura/assinatura. Não repetir o vídeo original mais uma vez como fundo do CTA; encerrar com uma forma derivada do card e um único movimento de contorno.

## Validação que a proposta exige

- Checar literalmente o quadro0 e os quadros3,6,9,12,15,30,45,60,75,90,105,120 do MP4 exportado.
- Três estados diferentes de composição precisam ser discerníveis até4s: letra/empresa, contexto local, pergunta dominante.
- Uma ação muda a relação entre elementos a cada informação, sem retirar tempo final de leitura das métricas.
- Diferenciar layouts: hook tipográfico full-width; cidade ampla; produção assimétrica; prova dominante; CTA com transformação. Se todos voltarem ao centrocomminiaturaabaixo, falhou a evolução.
- Comparar timings no código e imagens reais do MP4; inspeção nativa não garante ausência de problemas em composição animada.
- Conferir `Danny’s Presentes`,13.064alcance,20.981impressões. Não usar dado de Pix, preço, vendas, mapa Brasil ou depoimento da referência.
- Nenhuma afirmação de qualidade de voz/mix percebida sem escuta subjetiva. O áudio do OtoCriativo não entra na produção.
