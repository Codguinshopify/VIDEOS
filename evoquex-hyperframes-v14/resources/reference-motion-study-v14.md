# V14 — nova consulta integral das três referências obrigatórias

Relatório interno de direção e verificação. Não acompanha a entrega ao usuário, que deve conter somente o vídeo final.

## 1. Fontes, integridade e consulta realizada nesta etapa

Li integralmente o briefing recebido em `/workspace/attachments/a42cae84-b58f-4789-8dbd-73a74ce3e83b/Texto colado.txt`. A mudança central da V14 é tornar o gráfico protagonista, usando o material real como prova breve. A autorização da V14 permite melhorar o hook sem congelar todos os seus pixels; a restrição de congelamento da V13 deixou de ser aplicável.

Os três anexos atuais foram abertos e decodificados novamente, sem substituir a consulta por memória ou relatórios anteriores. Seus hashes são idênticos às três referências permanentes existentes:

| Referência | SHA256 | Duração | Cópia permanente original |
|---|---|---:|---|
| Park / Shard Cloud | `d3b4dbe47d772e8a54371336ccc9db228166b4936775cea28415edd894d9d93c` |44,651973s|`/workspace/VIDEOS/biblioteca/referencias/park-shard-cloud/Park_Criativo_video_no_watermark (1).mp4`|
| Park / Virgílio Contabilidade | `f21687d6e6c8f224378de5f8ac82056e3e60c9d87554d2cbfb23d750f824bc54` |64,713991s|`/workspace/VIDEOS/biblioteca/referencias/park-virgilio/Park_Criativo_video_no_watermark.mp4`|
| OtoCriativo | `39bc21037a522d3088630fcf79b9da61cc759c31b5386c39759e074283395a8c` |27,766667s|`/workspace/VIDEOS/biblioteca/referencias/oto-criativo/oto_criativo_video_no_watermark.mp4`|

Não renomeei, recomprimi nem sobrescrevi os originais. A identidade das duplicatas foi verificada contra os arquivos anexados, não inferida pelo nome. O manifesto `reference-manifest-v14.json` guarda os caminhos dos anexos, caminhos permanentes, hashes,probe e quantidade de amostras. A quarta referência Weven preservada no projeto não é um dos três anexos obrigatórios desta V14 e não foi usada como substituta deles.

**Consulta visual integral:**276 quadros novos por decode sequencial, selecionando `n=0,15,30…`, explicitamente ordenados:90 Shard,130 Virgílio,56 Oto. Inspecionei as dez sheets completas, não apenas pontos escolhidos. Evidências nesta pasta: `shard-full-{1,2,3}.jpg`, `virgilio-full-{1,2,3,4,5}.jpg`, `oto-full-{1,2}.jpg`. O script `extract-references.py` documenta e reproduz a extração.

**Consulta temporal densa nova:**114 quadros em seis sequências, um quadro a cada dois de uma fonte 30 fps (15 amostras/s), extraídos por seleção do número de quadro durante decode sequencial. Inspecionei todas as seis sheets em `sequences/`; manifesto `sequences/sampling.json`, script `extract-sequences.py`. A resolução temporal é suficiente para acompanhar direção, reparenting aparente e mudança de suporte; não afirmo reprodução contínua em tempo real.

## 2. O que as três peças fazem que a V13 ainda não sustentava

### O gráfico é o sujeito da ação

Em Shard 9,6–11,1s, a palavra/cursor se converte num sistema de curvas e módulos. Em Virgílio 16,3–17,3s, uma cápsula textual vira uma pessoa recortada; o símbolo passa a carregar a ideia. Em Oto 10–10,9s, cápsulas e seu nó branco articulam a composição enquanto o texto ocupa o espaço livre. A fotografia não é o suporte permanente desses trechos.

NaV13 o filme real permanecia em cena aproximadamente8,2–15s, e o nomeDanny’s ocupava o topo durante o mesmo intervalo. A filmagem mudava de enquadramento, porém várias frases ainda eram ditas ao lado do mesmo objeto filmado. O espectador acompanhava principalmente a imagem e a troca de frase, em vez de uma ação gráfica que explicasse produção e divulgação. Esta é uma diferença de protagonismo; adicionar mais rotação na janela não a resolve.

### A forma muda de significado, não apenas de posição

Um círculo pode começar como superfície, depois ser contorno e terminar como ícone. A função muda junto com o movimento. É diferente de um círculo sempre decorativo ou um cartão que apenas desliza. A V14 deve ter pelo menos uma transformação funcional por unidade de sentido, usando os mesmos pontos de origem e chegada.

### Há planos de repouso, mas o repouso conclui uma construção

As três peças não têm alta densidade gráfica em todos os frames. Há palavras curtas nítidas e espaço negativo. O que cria riqueza é alternar palavra, objeto, sistema, campo e imagem, com transições que têm origem visível. O problema não é uma frase ficar legível por um segundo; é um suporte ficar igual durante diversas informações sem evoluir.

### A mídia real é breve e integrada

Em Virgílio a fotografia resolve dentro de uma moldura por cerca de1s em18,8–19,4s e volta em49–50,2s; a moldura se transforma ao sair. Em Shard o telefone aparece por intervalos curtos e depois a peça volta a ser sistema gráfico. Oto é praticamente toda construída com gráficos e representações de interface. Esses intervalos são estimativas visuais da consulta, não classificação automática de mídia.

O plano de filme real por2,1 s em6,9–9s proposto pelo agenteMD é coerente com essa gramática. É mais útil que conservar7s de vídeo e simplesmente animar o seu retângulo.

## 3. Sequências densas verificadas nesta etapa

### Shard Cloud9,600–11,067s — palavra/cursor vira sistema espacial

23amostras. Em9,6s o cursor ocupa a metade inferior e`Conecte` está acima. Por10s a composição recua; em10,067–10,267s a câmera atravessa lateralmente os planos. Em10,4s aparecem caminhos e módulos oblíquos; de10,5 a11,067s o centro de atenção se desloca ao sistema. Os caminhos já têm elementos móveis e posições distintas, não são linhas estáticas acrescentadas depois.

**Por que funciona:** o verbo conduz à representação da ação; movimento de câmera transforma uma palavra em sistema, sem precisar de vídeo de apoio.

**Aplicação4–6,9s:**`Já viu por aqui?` pode conduzir a uma abertura/olho ou marcador local que empurra e revela brevemente a cidade. A foto apenas ocupa parte da transformação; o campo gráfico e a pergunta continuam a conduzir a atenção. Não usar um mapa nacional ou outras cidades.

### Shard Cloud15,500–16,900s — anel vira linha e muda o plano de leitura

22amostras. O aro oblíquo envolve a frase. Em16,3–16,5s ele reduz a espessura aparente até virar quase uma linha; texto/cursor também recuam. Em16,567s nova frase emerge em profundidade; em16,633–16,9s outro trecho de anel se desenha ao redor do novo centro. A transição não é só dissolver duas frases.

**Por que funciona:** a escala do espaço muda antes da informação. A compressão prepara a aceleração; o novo objeto se assenta numa posição relacionada à anterior.

**Aplicação9–14s:** a máscara da filmagem fecha num elemento vetorial que se comprime e vira placa de divulgação; a placa se dobra e vira ponto/marcador deClevelândia. Usar apenas um nó principal e trajetória clara. As palavras`E divulgamos pela Evoquex.` e`Só para Clevelândia.` acompanham fases diferentes da transformação, sem virar cabeçalhos permanentes.

### Virgílio 16,300–17,300s — cápsula textual se recorta em pessoa

16amostras. A cápsula`Profissional` cresce em altura; o texto sai por baixo; a forma arredondada vira disco. Um recorte aparece no topo em16,567s, e espaço negativo desenha a pessoa por16,7s. O anel externo amplia e o personagem recua, enquanto cópias tipográficas assumem o plano de fundo.

**Por que funciona:** um único volume atravessa três significados. O recorte tem papel expressivo e semântico; não é um enfeite.

**Aplicação6,9–9s e14–18s:** símbolo de produção/câmera abre em lamelas para mostrar o material real, depois volta a ser play/placa. Na evidência, a mesma lógica pode separar `20` e `mil`, formar o dado e resolver o rótulo `visualizações de pessoas de Clevelândia`. Pessoas vetoriais, se usadas, são qualitativas; não representar uma equivalência quantitativa inventada.

### Virgílio38,200–39,600s — segmento vira lupa e percorre a informação

22amostras. Um pequeno arco cresce sobre um fundo difuso e ganha moldura por38,467s. Em38,8s se compacta num ponto; por38,867s a lupa começa a se formar. Em39–39,6s o objeto percorre lateralmente o rótulo enquanto cresce/rota levemente. O mesmo centro visual participa da geração, da inspeção e da conclusão.

**Por que funciona:** o gráfico realiza a ação que a frase promete. O texto é consequência da operação, em vez de ser o único elemento que se anima.

**Aplicação14–18s:** o numeral pode ser revelado por uma abertura/recorte que percorre os dígitos e se transforma em suporte do rótulo. Não copiar lupa sobre valor monetário, gráfico de lucro ou captura com outra métrica. O novo dado do briefing é20 mil visualizações, não a métrica antiga de impressões.

### Oto 10,000–10,867s — nós e cápsulas organizam um sistema

14amostras. A cápsula central com círculo branco muda de posição/tamanho; satélites entram com escalas e deslocamentos diferentes. O texto ocupa o vazio entre eles, e as formas ganham foco com tempos levemente escalonados. Em10,8s a composição começa a sair por foco/escala.

**Por que funciona:** o elemento branco indica estado/atividade; a variedade de movimento pertence ao mesmo sistema visual e não cria confete aleatório.

**Aplicação9–14s ou18–20,5s:** o símbolo de anúncio pode produzir dois/três caminhos discretos com pontos móveis, todos convergindo para o marcador local. Na parteMensagem/Público, os polos se afastam e aproximam, a curva responde a esse movimento e depois vira o contorno do CTA. Não usar ícones estáticos apenas como adesivos.

### Oto20,400–21,467s — fragmentos se reúnem e a composição troca de escala

17amostras. O botão começa dividido em partes; contorno e texto se alinham por20,8s. Um cursor se aproxima por baixo, toca por21,0s; o botão contrai e recua, e o próximo objeto lateral ganha enquadramento por21,333–21,467s.

**Por que funciona:** ativação, reação e saída pertencem à mesma ação. O efeito é expressivo mesmo com poucas formas.

**Aplicação20,5–26s:** a linha Mensagem/Público pode reunir os fragmentos do convite, abrir um contorno assimétrico e então fazer a tipografia do CTAocupar outra região. A assinatura conclui a transformação; não reproduzir o mesmo layout título→cartão→botão da V12. O convite atual permanece natural, com empresa/serviço em concordância.

## 4. Proposta de direção aplicável ao alvo26s

| Trecho | Mensagem existente / função | Ação visual que muda o protagonismo | Evidência real | Ponte seguinte |
|---|---|---|---|---|
|4–6,9s|`Já viu por aqui?` / reconhecimento|Palavra e marcador se articulam, forma revela cidade num plano que se dobra; nenhum cabeçalho Evoquex/Clevelândia permanece após5s.|Foto aérea breve, recortada dentro da ação.|Marcador/abertura vira símbolo de produção.|
|6,9–9s|Case Danny’s / produção do vídeo|Câmera ou abertura vetorial se desdobra em3 lamelas; frases acompanham o gesto em eixos distintos.|Filme original total≈2,1 s, sem bezel ou repetição.|Lamelas fecham e a mesma peça vira placa/play.|
|9–11,5s|Divulgação Evoquex|Objeto principal muda de papel e inicia percurso, curvas/nós respondem ao movimento; marca entra como parte do objeto e sai.|Nenhuma filmagem contínua necessária.|Placa se dobra e vira marcador local.|
|11,5–14s|Somente Clevelândia|Marcador e território abstrato ocupam a composição, localidade é função da ação; sem mapa/alcance externo inventado.|Pode usar pequena textura da imagem real, sem voltar à mesma janela do filme.|Trajetória termina nos dígitos.|
|14–18s|20 mil visualizações de pessoas de Clevelândia|Dígitos grandes se separam, giram/comprimem e se reúnem; rótulo muda de alinhamento e assenta; nunca outro cartão de screenshot.|Dado explicitamente atestado pelo usuário no briefing atual.|O zero/contorno vira polo deMensagem/Público.|
|18–20,5s|Cada empresa / mensagem+público|Dois polos móveis em planos diferentes e curva que se adapta às posições, com transformação real de forma.|Gráficos qualitativos, sem novos resultados.|Curva/contorno se transforma no suporte do convite.|
|20,5–26s|Empresa/serviço e convite|Pergunta em arranjo assimétrico; tipo ocupa duas regiões sucessivas, fragmentos se reúnem e contorno reage; leitura final1,5–2s.|AssinaturaEvoquex somente no encerramento.|Conclusão em movimento assentado, sem longo hold.|

A proposta foi comunicada ao agente `/root/md_v14` antes da implementação. Esse agente informou plano compatível com26s, mídia real6,9–9s e sistema de forma única produção→divulgação→marcador. As sugestões são técnicas de direção, não uma alegação de que aV14jáas implementou; essa comprovação depende do MP4.

## 5. Densidade e legibilidade: critérios úteis para a execução

- No máximo uma ideia principal e um complemento curto por estado legível. As referências têm espaço negativo; densidade não significa três parágrafos simultâneos.
- Tratar mudança de função como unidade de ritmo: palavra→forma, forma→janela, janela→marcador, marcador→número, número→ligação. Um zoom que deixa tudo na mesma relação não conta como nova composição.
- Enquanto o suporte se transforma, outra camada pode antecipar a próxima ideia, mas precisa resolver antes de exigir leitura. Evitar placas totalmente vazias por mais de≈0,15–0,2s.
- O filme não deve ocupar o papel de protagonista por vários segundos enquanto três frases trocam ao lado dele. Se isso reaparecer no render, reconstruir o trecho.
- Dar ao dado real pelo menos1,3–1,6s legível após a construção. Não transformar a métrica continuamente a ponto de ninguém lê-la.
- Não manterEvoquex ou Clevelândia como marca-d’água depois5s. Entradas com função narrativa e assinatura final são permitidas; cabeçalho fixo não.
- `20 mil visualizações de pessoas de Clevelândia` é a informação do briefing atual. Não substituir por20.981 impressões ou13.064 de alcance nem transportar provas/legendas de outra métrica por inércia.
- Fotografias, gráfica da referência e som são material de estudo. Nada deles deve ser copiado para o anúncio final.

## 6. Som: o que foi medido e o que não pode ser afirmado

Decodifiquei integralmente as trilhas dos três anexos para PCM mono 16 kHz e calculei envelopes RMS de100 ms e candidatos de subida de energia em20 ms. Dados em `reference-audio-technical.json`, script `analyze-audio.py`. Durações PCM:Shard 44,6534 s;Virgílio 64,7154 s;Oto 27,7492 s. A pequena diferença entre duração de áudio e vídeo é da codificação/origem.

Candidatos de subida de energia coincidem aproximadamente com algumas mudanças gráficas observadas:Shard2,08s(disconascendo),26,52s(faixa/plus),28,76s(entrada do telefone);Virgílio17,32s(assentamento do símbolo/pessoa),57,32s(revelação de foto);Oto 10,38s(cápsulas),22,64s(frase do convite). **Essas subidas podem ser voz, música ou efeitos misturados. Não classifiquei o evento como impacto/whoosh nem aleguei ter escutado.** Correlação temporal não prova qualidade sonora.

Princípios aplicáveis à nova produção: antecipação sonora curta antes da transformação principal, impacto no assentamento de forma/número, espaço menos denso enquanto o dado é lido e nova atividade na passagem ao convite. Não adicionar som a cada letra nem reaproveitar a faixa repetitiva da V13apenas com novos FX por cima. O compasso e a instrumentação podem mudar por blocos, conservando continuidade, com cuepoints aproximadamente4;6,9;9;11,5;14;18;20,5;23s conforme o timing efetivamente adotado peloMD. Nenhum áudio de referência será usado.

Os níveis das referências não devem ser copiados como alvo: a decodificação AAC de duas delas apresenta amostras float acima0 dBFS. Isso é um dado técnico do arquivo e não uma análise subjetiva de distorção. Para o novo MP4é preciso medir loudness, truepeak, saturação e conferir o alinhamento com os movimentos próprios.

## 7. Limitações e confirmação futura

A consulta foi renovada nestaV14, com imagens novas da duração inteira e114 quadros novos de trajetórias específicas. Não foi reprodução contínua em tempo real e não houve escuta subjetiva. Não afirmo ter avaliado naturalidade de voz, timbre ou impacto percebido. O relatório trata técnicas observadas e propostas de aplicação separadamente.

Na revisão da V14, o critério mais importante será verificar nos frames consecutivos se o gráfico realiza ações entre ideias e se o material real permanece breve. Compilação, número de tweens e quantidade de presets não substituem essa inspeção. Nenhuma alteração visual foi feita por este agente; os originais permanecem preservados.
