# V13 — estudo de trajetórias e continuidade das referências

## Escopo e método

O hook V12 de 0–4 s está aprovado. Este estudo não recomenda alterar texto, cores, tipografia, composição ou timing desse intervalo. Todas as aplicações abaixo se destinam a 4–30 s e mantêm literalmente o roteiro existente.

Os quatro arquivos reais e únicos estão acessíveis em `biblioteca/referencias`: Park/Shard Cloud (44,652 s), Park/Virgílio Contabilidade (64,714 s), OtoCriativo (27,767 s) e Park/Weven (42,608 s). São quatro conteúdos, embora o pedido os agrupe como três referências anteriores. Os reenvios idênticos não foram contados como novos exemplos.

A análise completa dessas quatro peças foi realizada e preservada na V12; nesta etapa revisei a duração inteira de Virgílio novamente em 130 amostras ordenadas e extraí **228 quadros novos**, em oito sequências densas, para investigar como o objeto percorre o espaço entre estados. As primeiras cinco sequências têm quadros consecutivos a 30 fps; as três últimas usam um quadro a cada dois, equivalendo a 15 amostras por segundo. Todos foram obtidos por decode sequencial e seleção de `n`, sem busca temporal prévia. Os timestamps nas sheets derivam de `n/30`, não da ordem do diretório.

Evidências: `sequence-sampling.json`, `extract-motion-study.py`, pasta `sequences/`. Arquivos e intervalos:

| Estudo | Referência | Intervalo observado | Amostras |
|---|---|---:|---:|
| `shard-disc` | Shard Cloud | 2,000–3,267 s | 39, consecutivas |
| `shard-plus` | Shard Cloud | 26,067–27,000 s | 29, consecutivas |
| `oto-cards` | OtoCriativo | 7,700–8,500 s | 25, consecutivas |
| `oto-label` | OtoCriativo | 14,667–15,467 s | 25, consecutivas |
| `virgilio-photo` | Virgílio | 18,800–19,800 s | 31, consecutivas |
| `virgilio-cta` | Virgílio | 55,300–57,300 s | 31, intervalo 2 quadros |
| `weven-cursor` | Weven | 12,200–13,800 s | 25, intervalo 2 quadros |
| `weven-band` | Weven | 27,800–29,300 s | 23, intervalo 2 quadros |

Os relatórios V12 sobre o render real, inclusive o MP4 final SHA `928b0b271c5144169af4dfe378935af5f8b4ca1b45fa4865bb63b7b1fd2b3361`, continuam válidos como diagnóstico da base. O ponto fraco após 4 s é o movimento do suporte maior que o movimento da ideia: a imagem fica num cartão e a frase se substitui em outra região, sem uma relação física suficiente entre ambos. O usuário aprovou a intensidade do hook; conservar o vazio final legível não significa conservar esse padrão durante 26 segundos.

## Oito técnicas selecionadas e aplicações propostas

### 1. O suporte nasce dentro do conteúdo, ocupa o plano e retorna com outra função

**Referência e trajetória real:** Shard Cloud, 2,067–3,267 s. Um ponto escuro nasce sobre o telefone (2,067 s); até 2,200 s cresce como disco. Em 2,233 s a palavra aparece comprimida em profundidade; em 2,400 s o plano está quase totalmente ocupado e a palavra assenta. Em 3,100–3,267 s o campo escuro recua, inclina, encolhe e acaba como cápsula. É um objeto contínuo que troca a relação com a câmera. Não é apenas entrar com zoom em um título.

**Por que funciona:** o espectador já acompanha o centro do objeto. A expansão prepara a troca; o recuo mostra que o fundo anterior era uma peça da cena seguinte. A mesma superfície explica os dois espaços e evita corte sem relação.

**Aplicação proposta em 4,000–5,300 s:** o pequeno círculo de saída do hook permanece exatamente como na V12 até o limite aprovado. Depois de 4,000 s ele se amplia para revelar a imagem aérea, ocupando a maior parte do quadro, enquanto `Já viu` chega de cima e `por aqui?` emerge de uma faixa no eixo oposto. A palavra `aqui?` pode ser máscara da foto antes de a foto ganhar contorno amplo. A máscara tipográfica é uma adaptação nossa do princípio observado, não um efeito literal existente na referência.

**Implementação:** um elemento compartilhado, com máscara SVG/clip-path animada; coordenadas de âncora idênticas na expansão e no recuo. Nada de exibir o próximo plano cedo por trás de uma máscara transparente. O estado plenamente legível deve resolver em no máximo 0,5 s, depois sustentar leitura curta.

### 2. A borda sobrevive à imagem e se torna a próxima palavra

**Referência e trajetória real:** Virgílio, 19,267–19,800 s. A pequena fotografia sai por redução de contraste; a borda se duplica brevemente em perspectiva. Em 19,400 s a fotografia já está quase ausente, mas o contorno quadrado continua. Em 19,433–19,567 s o retângulo comprime em altura, a palavra `IMPOSTOS` desliza para dentro e a forma se transforma numa cápsula. O ponto que acompanha a borda continua para o plano seguinte.

**Por que funciona:** o espectador não troca toda a composição de uma vez. Uma propriedade reconhecível, o contorno, conduz a leitura do conteúdo concreto para o rótulo.

**Aplicação proposta em 6,800–8,200 s:** a moldura da cidade passa a sublinhar `Uma das nossas divulgações.`; depois comprime numa faixa e puxa a entrada de `Danny’s Presentes`. A imagem não precisa girar como um telefone. O contorno da cidade abre uma janela vertical ou uma faixa grande que recebe o vídeo original. Nome e fotografia têm uma passagem em comum, sem tela vazia entre eles.

**Implementação:** animar o mesmo SVG rect ou container por width/height/border-radius, acompanhado de máscara complementar. A captura da cidade permanece no mesmo eixo enquanto a moldura muda. A palavra não deve ficar comprimida junto com o container; texto e borda são camadas diferentes.

### 3. A passagem lateral tem movimentos verticais internos e mudança de foco

**Referência e trajetória real:** OtoCriativo, 7,900–8,267 s. O card do mapa avança para a esquerda, mas o card novo entra primeiro por baixo e à direita (7,933 s); ele sobe, ganha contraste e reduz a distância ao eixo central. O título de cada card se desloca com ele; o marcador embaixo troca de estado só depois. O conteúdo do card novo já começa a mudar antes de o trilho parar. Três ações têm tempos diferentes, preservando hierarquia.

**Por que funciona:** as direções não são todas iguais e as camadas não começam nem terminam juntas. Existe antecipação da próxima informação, impacto do suporte e settle do conteúdo.

**Aplicação proposta em 8,200–10,600 s:** o vídeo original ocupa uma área maior da composição, sem bezel de telefone. `Produzimos` entra de baixo para cima como palavra grande recortada; `o vídeo.` vem da direita e assenta numa faixa ligada à imagem. A filmagem avança diagonalmente para o enquadramento principal; o texto recua para dar espaço. Não imitar o carrossel de três celulares, pois o usuário rejeitou mockups repetidos.

**Implementação:** planos independentes com transforms e delays curtos; pequeno overshoot de 3–5% seguido de settle. O movimento da filmagem deve ser fluido, com uma única instância real, e nunca antecipar cortes internos do arquivo. Usar alinhamento comum como ponto de chegada, sem forçar uma grade de cartões.

### 4. A palavra chega em fragmentos e se reúne antes de ser lida

**Referência e trajetória real:** OtoCriativo, 14,733–15,233 s. O rótulo preto não entra inteiro: chega dividido em aproximadamente três fatias verticais, com alturas e rotações diferentes. As fatias atravessam a área central, alinham-se e se tornam uma única etiqueta em cerca de 0,3 s. Atrás, três cópias tipográficas reduzem contraste para sugerir profundidade; a etiqueta resolve nítida e quase horizontal.

**Por que funciona:** o movimento revela a construção da palavra; a fragmentação termina antes de a leitura principal começar. A forma unida demonstra conclusão. Permanecer fragmentado por muito tempo destruiria a mensagem.

**Aplicação proposta em 10,500–12,700 s:** a palavra existente `E divulgamos pela Evoquex.` articula-se por três grupos, alternando y, rotação e profundidade, enquanto a faixa do vídeo se abre. Para a prova em 15–21 s, o mesmo princípio pode ser adaptado aos dígitos: o valor atual se reparte por grupos de glifos, sai em direções alternadas e o próximo se recompõe. A referência mostra rótulo fragmentado, não uma métrica; a aplicação a dígitos é adaptação explícita.

**Implementação:** spans por grupo de letras/dígitos, máscara externa e transform-origin consistente. Não transformar 20.981 em outro número intermediário ilegível mantendo o rótulo antigo. Antes de trocar o significado, retirar o rótulo anterior; o valor final deve ficar integralmente legível por pelo menos 1,3–1,6 s. Os dois números reais e suas definições permanecem intactos.

### 5. O objeto muda de categoria enquanto continua o percurso

**Referência e trajetória real:** Weven, 12,200–13,800 s. Cursor chega de cima e toca a cápsula `Centralize`; a cápsula cresce em altura (12,400 s), muda de contorno e vira uma pessoa (12,533 s). Depois a pessoa se afasta, perde contraste e é substituída pelo item `cliente`, que entra de baixo, sobe ao centro e serve à próxima operação. A mão acompanha a ação, em vez de estar isolada como decoração.

**Por que funciona:** uma intenção tem um percurso físico claro. Cada novo estado recebe a atenção do movimento anterior. Não se trata de trocar um ícone por outro com fade no mesmo local.

**Aplicação proposta em 12,700–15,100 s:** o fragmento real do anúncio se transforma em peça de divulgação, percorre uma curva e encontra a palavra `Clevelândia.`. O texto `Só para Clevelândia.` se monta em duas direções, com a preposição ancorada e o nome da cidade ocupando o território visual. O objeto do vídeo pode se converter em tira de evidência, preparando a captura real da prova. Não acrescentar cliente, funil, intenção de compra ou interface fictícia.

**Implementação:** MotionPath ou caminho paramétrico determinístico com âncoras compartilhadas; duas representações do mesmo objeto podem usar máscaras complementares. A passagem precisa mostrar o que o objeto era e o que virou, sem sumir em blur total por 0,5 s.

### 6. A mesma peça muda de altura, texto e papel de fundo

**Referência e trajetória real:** Weven, 27,800–29,267 s. Um comprovante verde fica azul e comprime em altura até virar a cápsula `cobranças` (28,000 s). A cápsula perde foco enquanto um campo azul nasce de cima e desce; a frase branca é revelada dentro dele. Em 28,800 s a peça já domina o telefone. É uma cadeia de deformação e mudança de escala, não um wipe sem origem.

**Por que funciona:** a troca de cor/forma nasce numa peça visível, e o novo fundo tem direção e velocidade. O texto entra quando já há suporte suficiente, antes de o fundo terminar a viagem.

**Aplicação proposta na entrada da prova, 14,700–15,500 s:** a tira do anúncio/cidade abre em vários recortes da captura real; um desses recortes alarga e serve como plano de fundo do numeral. A expansão deve acontecer simultaneamente à entrada dos dígitos, evitando o intervalo azul totalmente vazio que existiu na primeira V12. Manter as palavras exatas `Nos registros da campanha`, `impressões`, `exibições do anúncio`, `pessoas alcançadas` e `alcance` nos seus estados corretos.

**Implementação:** clip-path de faixas e escala de suporte, com texto independente. Não usar o comprovante Pix ou dados da referência. Se for preciso fazer breve wipe opaco, cobertura total abaixo de aproximadamente 0,15 s e conteúdo começando a resolver antes do fim.

### 7. Um conector vira suporte de frase enquanto as palavras se reorganizam

**Referência e trajetória real:** Shard Cloud, 26,067–27,000 s. O ícone plus começa relativamente grande; encolhe verticalmente e desloca-se, depois o suporte arredondado expande só na horizontal. O plus continua minúsculo por alguns quadros enquanto as letras começam a aparecer dentro da faixa. A frase percorre o eixo em pequenos grupos até resolver. O objeto não é descartado quando a palavra aparece.

**Por que funciona:** a redução de um elemento abre espaço para texto sem cortar para outra composição. O traço horizontal oferece direção e segura a leitura durante a transformação.

**Aplicação proposta em 21,000–24,300 s:** a separação dos números deixa dois alinhamentos no espaço; eles tornam-se os suportes de `Mensagem` e `Público`. Os ícones chegam em trajetórias opostas e um conector de fato os une. A união vira uma linha maior, empurrando `Cada empresa.` para um lado e `Uma estratégia.` para outro, antes de resolver a nova hierarquia. O conteúdo textual permanece exatamente o atual; não introduzir novas frases.

**Implementação:** um único grupo SVG com coordenadas compartilhadas; translação oposta dos dois polos, curva que desenha entre posições reais e depois retifica. A mudança deve produzir uma composição nova, não outro painel central contendo dois ícones estáticos.

### 8. A fronteira entre campos carrega o texto e muda o alinhamento do CTA

**Referência e trajetória real:** Virgílio, 55,300–57,300 s. Um campo colorido sobe do rodapé; a frase branca está presa à borda superior e sobe junto. O título preto fica acima, criando dois campos complementares. Perto de 56,900 s a fronteira passa a descer, e os dois textos acompanham o plano; a área abre para a fotografia seguinte. A passagem tem ida e volta, sem exigir rotação ou blur.

**Por que funciona:** o movimento nasce da relação entre duas regiões da tela. A hierarquia muda porque o espaço disponível muda; a frase não apenas ganha escala no mesmo ponto.

**Aplicação proposta em 24,300–30,000 s:** o conector anterior vira fronteira oblíqua ou horizontal entre dois campos Evoquex. `E a sua empresa?` ocupa uma região ampla e lateral; a fronteira sobe, revela `Conversa com a gente.` e redistribui a composição. `E o seu serviço?` substitui a pergunta com outro sentido de entrada, mantendo concordância e texto atual. A assinatura fica em região própria, sem repetir título acima de cartão e botão abaixo. Últimos 1,5–2 s podem assentar para leitura.

**Implementação:** dois wrappers com máscaras complementares animados pelo mesmo parâmetro. O texto acompanha a fronteira por coordenada comum, mas não sofre squash. A alteração de `empresa` para `serviço` precisa remover o gênero anterior no mesmo instante; não exibir temporariamente `E a seu` ou `E o sua`.

## Progressão recomendada de direção

- 4–6,8 s: expansão de dentro para fora, depois percurso amplo da cidade e articulação das duas linhas do título.
- 6,8–8,2 s: contorno comprime; texto puxa a transição na diagonal.
- 8,2–10,6 s: filmagem entra por cima/diagonal e palavras chegam pelo eixo contrário.
- 10,6–12,7 s: grupos tipográficos se abrem e fecham; vídeo ganha outra posição.
- 12,7–15,1 s: movimento se curva e termina na informação local; suporte real muda de função.
- 15,1–18,2 s: primeira métrica ocupa o campo com alinhamento expressivo, captura em faixa e depois contexto.
- 18,2–21 s: fragmentos/dígitos saem em eixos alternados; segunda métrica se reúne e assenta. Nada de trocar só o número num cartão idêntico.
- 21–24,3 s: duas direções opostas se ligam; a conexão conduz ao próximo plano.
- 24,3–30 s: fronteira de campos redistribui hierarquia, pergunta troca eixo e CTA conclui com espaço de leitura.

## Regras concretas para confirmar que houve implementação

1. Uma troca de informação deve mudar a relação entre ao menos dois elementos, não só a opacidade da frase nova.
2. Cada trecho deve ter uma trajetória identificável com início, máximo deslocamento, pequena reação e ponto de assentamento. Overshoot só quando a massa/semântica pedir, não em todas as palavras.
3. Não repetir esquerda→direita em cenas consecutivas. Alternar eixo, mas manter a atenção ancorada num objeto conhecido.
4. No render, pausar em intervalos de 2–3 quadros de cada passagem e observar a continuidade dos pontos de origem/destino. Um objeto que some e reaparece longe não virou outro; foi substituído.
5. Verificar visualmente as letras/dígitos nas extremidades das máscaras, inclusive durante overshoot. Nenhuma leitura principal pode acontecer com metade da palavra ausente.
6. A captura original é prova, não textura decorativa sem identificação. Mostrar fonte e contexto reais depois da passagem com recortes.
7. Conservar dados e roteiro literalmente. Não aproveitar preço, faturamento, retorno, Pix, venda, funil ou depoimento das referências.
8. Preservar 0–4 s do render aprovado. O novo movimento deve herdar a saída já existente a partir do corte, sem adicionar antecipações que vazem antes de 4,000 s.

## Limitações da análise

As sequências consecutivas permitem examinar trajetórias, mudança de direção, escalonamento entre camadas e assentamento em detalhe. Elas não equivalem a reprodução contínua em tempo real. Esta interface não oferece escuta subjetiva nem reprodução audiovisual percebida como por um espectador humano. Não afirmo ter avaliado timbre, naturalidade, impacto sonoro percebido ou retenção real. O relatório distingue técnicas observadas de adaptações propostas; não afirma que estas já foram implementadas no render V13. A confirmação cabe à revisão do MP4 novo.
