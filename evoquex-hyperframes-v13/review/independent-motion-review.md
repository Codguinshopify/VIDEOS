# Revisão independente de movimento — V13 FINAL

MP4 final inspecionado: `renders/evoquex-hyperframes-v13.mp4`.
SHA256 final confirmado pelo arquivo: `548a550705c835551b4ab2817acec0d92862eb79fee40b6299a18c54c6a81ef2`.

## Parecer final

**As cinco correções identificadas no primeiro render foram confirmadas visualmente no MP4 final. Não há recomendação visual pendente a partir dos trechos inspecionados.** A evolução após4s permanece real: a tipografia muda de função, suportes se transformam e as trajetórias passam a conectar as informações. As pausas dos dados são de leitura; não são usadas como justificativa para longos vazios ou repetição de cartões.

Esta conclusão substitui o parecer de “primeiro MP4 não pronto” preservado no histórico abaixo. O histórico continua útil para mostrar o que foi encontrado e corrigido; não descreve defeitos remanescentes do arquivo final.

## Evidência adicional sobre o render final

Inspecionei129quadros consecutivos das sheets atualizadas, vinculadas ao SHA final em `hf-v13-sampling.json`:10,2–11,5s(39quadros),23,3–24,8s(45quadros),26–27,5s(45quadros). Revi também o trecho24–29,5s na sheet de duração inteira. Extraí e inspecionei37quadros próprios do arquivo final:8amostras de9–10,4s,21amostras de27,5–29,5s e8amostras de26,5–29,5s. Confirmei a cedilha num recorte de1080px em27,1s. Evidências próprias em `/workspace/audit-v13/qa-final/`.

### 1. Contraste na produção — corrigido

De9–9,8s a parte superior da filmagem tem véu escuro e o título grande continua distinguível sobre as áreas claras; por10s o título recua para fora da fotografia e a imagem ganha espaço. Em10,2–10,4s não existe mais texto branco assentado sobre o teto branco. Na passagem10,5–10,7s as letras da próxima frase atravessam brevemente a região da imagem, mas resolvem em≈10,8s sobre fundo escuro; isso é uma transição curta, não o antigo problema sustentado.

### 2. Suporte azul vazio — corrigido

O retângulo que antes esperava vazio desde10,4s foi removido desse intervalo. A nova construção começa como traço/peça estreita por10,9s; em11–11,2s o suporte se alarga junto com a chegada das partes do nome. Em11,233–11,267s a etiqueta já está legível. Não há mais a pausa de mais de meio segundo com uma placa azul vazia.

### 3. Linha do diagrama vira fronteira — corrigido

Em23,6–23,9s o diagrama inclina e comprime na mesma região que dá origem à faixa azul. Em23,933–24,067s a linha começa a ganhar altura sem saltar para o rodapé; em24,1–24,5s a área cresce para baixo, enquanto a pergunta se resolve acima dela. Agora se acompanha a origem física da fronteira. Os textos não são esmagados junto com o suporte, e o campo não encobre o título ou a pergunta no assentamento.

### 4. Assinatura e seta — corrigido

De27,5–29,5s a assinatura se articula e assenta à esquerda, abaixo da curva. O traço termina/dobra à direita e não cruza os glifos. A margem permanece suficiente inclusive durante a variação de altura da fronteira perto de28s. Não identifiquei nova colisão entreCTA, assinatura e seta.

### 5. Cedilha de serviço — corrigido

O grupo da pergunta ficou acima da fronteira, com folga inferior. Em26,9–27,5s, no recorte27,1s e durante a variação de28–29,5s, a cedilha aparece integralmente dentro do fundo escuro, sem coincidir com o azul. O estado “serviço?” está claramente legível e não perde o descendente. A troca “E a sua empresa?” para “E o seu serviço?” mantém concordância.

## Limites preservados

A revisão anterior cobriu as393imagens consecutivas das nove janelas e a duração inteira por amostragem; esta conferência final concentra-se nas correções e nos novos limites de máscara/composição. Não afirma inspeção humana de todos os900quadros nem reprodução contínua em tempo real. **Não houve escuta subjetiva.** Não aprovo timbre, narração ou mixagem percebida; a voz feminina continua pendente e não é apresentada como gerada. A aceitação estética final cabe ao usuário; este parecer confirma a execução e a resolução dos achados visuais observáveis.

---

# Histórico do primeiro render — achados resolvidos acima

# Revisão independente de movimento — V13, primeiro MP4

Arquivo efetivamente inspecionado: `review/first-v13.mp4`.
SHA256: `a8357e4481c9aa982e4b62990e218886f00194941dc8e5008822a95c8c1d1627`.

Esta revisão corresponde ao primeiro render. As correções que o executor informou ter feito nas fontes **ainda não estão confirmadas neste MP4**. A aprovação dos trechos corrigidos depende de conferir o arquivo final.

## Método

Li o briefing V13 e o README. Inspecionei as três sheets da duração inteira (60 amostras) e todas as 393 imagens das nove janelas consecutivas, de acordo com `hf-v13-sampling.json`, SHA correspondente ao arquivo acima. As sheets têm número do quadro e timestamp, permitindo acompanhar trajetória e não apenas escolher um hero frame. Janelas:4–6;7,5–8,7;10,2–11,5;12,5–13,8;14,6–15,8;17,6–19;20,5–22,2;23,3–24,8;26–27,5s. Inspecionei também um recorte 1080px do CTA em27,1s, extraído diretamente doMP4 em `/workspace/audit-v13/qa/cta-descender.png`.

Não usei contagem de tweens, compilação ou lista de componentes para aprovar movimento. Não houve reprodução contínua em tempo real nem escuta subjetiva. A inspeção sequencial permite identificar direções, sobreposições, máscaras, hierarquia e continuidade; não permite afirmar impacto sonoro percebido ou equivalência completa à experiência de assistir normalmente.

## Parecer sobre a evolução

A mudança após4s é substancial e visível no arquivo real. Há composição tipográfica que vira imagem, moldura que muda de proporção, mídia em trajetória coordenada, etiqueta que se reconstrói, numeral que se articula, documento recortado em painéis, troca de eixo entre métricas e CTA baseado numa fronteira móvel. Isso já constitui uma linguagem de motion ao longo da peça, em vez de só entradas de texto sobre um vídeo fixo.

O padrão do hook aparece especialmente em4,0–5,6s,10,8–11,2s,12,7–13,3s,15,0–15,7s e18,0–18,4s: palavras se articulam, escalas e direções mudam, a composição se constrói em vez de simplesmente aparecer. As sustentações em16–17,8s e18,5–20,8s são mais discretas; considero adequadas à leitura dos dados, pois as transições de entrada/saída são fortes e a hierarquia não é a mesma nas duas métricas. Não é necessário dar à prova a mesma frequência de troca dohook.

**Não considero este primeiro MP4 pronto para entrega**, devido a contraste prejudicado na produção, suporte azul vazio prolongado e colisão da assinatura, além de dois refinamentos de continuidade/margem identificados abaixo. A direção visual funciona, mas esses problemas específicos afetam o acabamento.

## Achados objetivos e estado das correções

| Prioridade | Tempo no primeiroMP4 | Evidência visual | Ação indicada / estado |
|---|---|---|---|
| Alta | Aproximadamente9,0–10,6s | `Produzimos` branco atravessa o teto branco da filmagem; o texto resolve sobre área clara e perde contraste por tempo legível, não só num frame de transição. | Executor já informou redução de tipo, aumento/reposicionamento do vídeo e veil no início. Ainda precisa ser conferido no render final. |
| Média |10,400–10,967s | Retângulo azul grande ocupa a região central antes de conter a marca. Fica mais de meio segundo como bloco vazio. Fragmentos de `Evoquex.` só aparecem perto11s. | Executor informou que suporte passa a abrir em10,85s e fatias começam10,93s. Conferir se a nova passagem parece construção simultânea, sem espera de placa vazia. |
| Média |23,667–24,067s | Diagrama comprime e sobe para uma linha na região superior; o campo azul seguinte nasce do rodapé, em outro local. Há transformação de forma, mas a trajetória não conserva a âncora física. | Executor informou que conector e nova fronteira compartilharão y1050 e nascerão um do outro. Esse ajuste é material para atender à continuidade solicitada. Ainda não confirmado no arquivo aqui avaliado. |
| Média | Aproximadamente27,8–30s | Curva/seta inferior atravessa a área da assinatura Evoquex. A interseção permanece depois do assentamento da marca. | Executor informou assinatura movida para esquerda/parte inferior. Verificar separação real entre linha e glifos na versão final. |
| Baixa, corrigível |26,9–30s | A cedilha de `serviço?` encosta na fronteira do campo azul; a margem inferior do glifo desaparece contra a área da mesma cor. Confirmado num recorte em27,1s. | Subir o grupo da pergunta em cerca12–20px ou descer um pouco a fronteira; garantir folga após o descendente, sem modificar texto. |

Não encontrei erro de nome ou valor final, fala inventada, métrica trocada nem concordância incorreta na troca de empresa para serviço. As palavras parcialmente recortadas durante entradas e saídas, quando resolvem em≈0,2–0,4s, foram tratadas como movimento intencional, não automaticamente como falha de layout.

## O que foi efetivamente visto nas sequências

### 4,000–6,000s — círculo, palavra e máscara fotográfica

O círculo do limite dohook cresce de120 a126frames, mantendo a âncora e retirando a pergunta. `por` entra inclinado e atravessa a região enquanto `Já viu` se articula de cima. A frase assenta em≈4,5s. Em5,067–5,267s a foto passa a preencher os glifos; em5,3–5,567s o recorte abre numa faixa fotográfica ampla. As letras não são uma legenda que fica sobre imagem: o suporte muda a função da tipografia. Em5,6–6s a frase inferior chega em grupos com rotações e sentidos distintos. Não vi vazamento da foto fora da máscara antes do momento planejado.

A principal força aqui é o encadeamento: círculo → tipografia → foto. Esse trecho se aproxima claramente da intensidade dohook.

### 7,500–8,700s — faixa fotográfica vira contorno e janela do case

A cidade recolhe para os glifos de `por aqui?` enquanto a borda inferior vira um contorno estreito. O contorno se desloca, aumenta a altura e fica vertical, preparando a janela de filme. Textos antigos sobem, o nome do case entra em grupos e o vídeo revela de baixo para cima. O contorno não surge isolado sem procedência.

O intervalo com moldura sem mídia é curto e coincide com a entrada do nome/produção; não constitui uma pausa global vazia. A legibilidade principal do nome é boa ao assentar. Existe pequena sobreposição temporal entre texto antigo e novo, em planos separados, resolvida sem colisão persistente.

### 10,200–11,500s — mudança de hierarquia e etiqueta em fragmentos

A filmagem grande recua e inclina para a direita, os textos mudam de direção e a faixa azul começa a organizar o nome da Evoquex. Nas imagens11,000–11,200s, fragmentos do nome chegam em alturas diferentes e se alinham dentro da etiqueta. É uma aplicação real da fragmentação/reunião vista na referência OtoCriativo.

Contudo, os dois problemas já descritos ficam nítidos nesta sequência: texto branco sobre teto e suporte azul vazio antes dos fragmentos. O trecho precisa das correções informadas pelo executor; não basta dizer que há muitas animações.

### 12,500–13,800s — etiqueta sai, cidade se articula, mídia muda de proporção

A etiqueta comEvoquex recua e sobe, comprimindo altura antes de sumir. `Só para` e `Clevelândia.` aparecem em grupos de letras com trajetórias diferentes, resolvendo por≈13,2s. A filmagem vertical muda de escala/proporção na mesma passagem e vira uma janela horizontal maior. A mídia já conhecida continua presente; não há uma nova imagem arbitrária para anunciar a cidade. O texto assenta com boa margem; o nomeDanny’s permanece reconhecível.

A imagem final disponível fica sustentada por pouco mais de um segundo. Isso é uma limitação do material original curto, não um novo conteúdo inventado. A transformação anterior cria intenção suficiente para essehold.

### 14,600–15,800s — filmagem sai, numeral e prova se constroem

O bloco de case sobe enquanto a borda inferior permanece, reduzindo e preparando a janela da prova. `20.` e `981` chegam separadamente com diferença de altura/escala, depois se alinham. A captura original surge em três fatias com profundidade e offsets, que se reúnem ao longo de15,2–15,7s. O rótulo de impressões também se articula e resolve.

Não existe a longa pausa azul da primeiraV12. O numeral final é20.981, e a imagem é o registro real. Durante a construção aparecem barras/reflexos estreitos dos recortes que depois desaparecem; não interpretei esses fragmentos transitórios como dígitos extras, pois o estado assentado é inequívoco.

### 17,600–19,000s — troca de eixo entre métricas

20.981impressões sai para a esquerda; o documento atravessa a composição e sobe para o lado oposto.13.064 entra pela direita/baixo e termina abaixo do documento. Texto de fonte/descrição acompanha a troca espacial, resolve à direita do documento e não encosta no número final. O rótulo `pessoas alcançadas` entra separadamente e fica nítido.

A hierarquia da segunda métrica é diferente da primeira, corrigindo a repetição do mesmo layout daV12. Há interseção breve do documento com a descrição em18,1–18,3s durante deslocamento; ela resolve até≈18,4s e não prejudica uma leitura que precise ocorrer nesse instante.

### 20,500–22,200s — prova entrega o contorno ao diagrama

Documento e número saem pela esquerda; o contorno do documento continua e se comprime em linha. O título `Cada empresa. Uma estratégia.` chega com letras/grupos em direções diferentes. A linha perde altura enquanto os dois ícones e seus rótulos começam a surgir. Não vi número de alcance permanecer legível depois da conclusão do título.

A construção é melhor que o painel pronto daV12, pois o suporte tem origem visível. A frequência de mudança diminui enquanto os ícones completam os traços; essa pausa é motivada pela leitura da combinaçãoMensagem/Público.

### 23,300–24,800s — diagrama inclina, campo azul cresce

Os dois ícones permanecem ligados por curva; um ponto percorre o caminho. O grupo inclina em perspectiva e comprime em altura até ficar linha. A nova pergunta começa a entrar e a região azul cresce a partir debaixo. A divisão de campos é uma solução visivelmente diferente dos cartões anteriores.

No primeiroMP4 a âncora da linha final e a origem do campo não coincidem. Por isso a solução ainda parecia duas ações sucessivas, apesar de ter boa intenção. O ajuste para uma mesma coordenada y1050 deve resolver; é necessário observar a nova trajetória no final.

### 26,000–27,500s — troca de pergunta com concordância e direções opostas

`empresa?` se divide em grupos e sobe/sai pela direção contrária; `serviço?` cresce de baixo e resolve. `E a sua` passa para `E o seu` sem estado legível de concordância errada. OCTApreto no azul permanece estável para leitura. Há movimento da fronteira e desenho da curva inferior, sem necessidade de nova tela.

O problema da cedilha ocorre no estado final, por estar colada à fronteira, e merece ajuste de margem. A grande forma azul e o texto preto têm bom contraste; depois de deslocar assinatura/curva não deve haver competição no encerramento.

## O que precisa ser confirmado no arquivo final

- Contraste efetivo de `Produzimos o vídeo.` ao longo de9–10,7s, após redução/troca de posição e veil.
- Duração curta do suporte azul vazio em10,4–11,2s; etiqueta e suporte devem ser construídos juntos.
- Âncora compartilhada entre linha e campo azul em23,6–24,5s.
- Nenhuma interseção persistente entre seta e assinatura em27,5–30s.
- Cedilha integral e margem inferior em`serviço?`, sobretudo26,9–30s.
- Nome, métricas e rótulos nos estados assentados; hook preservado por comparação técnica própria.

A ausência de outro defeito nas amostras não é prova de perfeição em todos os900quadros. O relatório deve receber apêndice com SHA do render final e evidência dos trechos corrigidos antes de afirmar conclusão.
