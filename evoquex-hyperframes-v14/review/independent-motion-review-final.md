# V14 — revisão visual independente final

Documento interno; não acompanha a entrega ao usuário.

## Arquivo e método

Arquivo final: `renders/evoquex-hyperframes-v14.mp4`.
SHA256: `a07de6cdbab452fb10e0d65c731710d4f64d14caa94a100730dec78838964417`.
26 segundos, 780 quadros, 30 fps.

Esta revisão verifica o resultado decodificado do MP4, não apenas as fontes. Na primeira revisão foram examinados 435 quadros consecutivos em nove janelas e 52 amostras distribuídas pelos 26 segundos. O primeiro parecer está preservado em `independent-motion-review.md` e vinculado ao SHA do primeiro arquivo. Nesta revisão foram reabertas as amostras completas, 381 quadros das oito janelas que abrangem as mudanças e 64 quadros próprios do candidato intermediário `904031b398ca48965ca80fb91b336cb06ddc0bb6f6520929b15b538ce044472f`. O último render recebeu nova decodificação sequencial de **97 quadros únicos**, todos inspecionados visualmente. Essa seleção inclui todos os 34 quadros de 6,8–7,367s e 9,0–9,5s, os sete intervalos de correção e estados de prova de nome, métrica, diagrama e CTA. O manifesto `/workspace/audit-v14/final-a07de6cdbab4-QA/frame-map.json` registra o SHA, números reais de quadro, ordem e imagens. O SHA foi confirmado novamente depois da extração.

As três referências foram reconsultadas integralmente nesta etapa por 276 novas amostras de duração completa e 114 quadros de sequências temporais, conforme `/workspace/audit-v14/reference-study.md`. A comparação considera trajetórias, função do objeto, hierarquia, relação entre recortes e texto e mudanças de composição. Não usa quantidade de tweens como critério de qualidade.

Não houve reprodução contínua em tempo real nem escuta subjetiva. Este parecer não certifica naturalidade da narração, mixagem percebida ou impacto sonoro; essas limitações não são substituídas por medições técnicas. Nenhuma fonte visual ou mídia foi alterada por este agente.

## Parecer visual

**Não identifiquei pendência visual concreta nos intervalos e estados examinados do arquivo final. As sete correções solicitadas e as duas correções adicionais de limites do filme estão presentes no MP4 de SHA acima.**

A direção muda substancialmente em relação à V13. O filme real aparece brevemente em três lamelas e participa de uma transição para o gráfico; não é o suporte contínuo para frases sobrepostas. Um ator visual muda de função entre play, seta de divulgação, marcador local, disco de passagem e símbolo de mensagem. As mudanças têm relação com produzir, divulgar, localizar, apresentar a evidência e explicar a estratégia.

O uso de texto claro no escuro, texto escuro no campo branco e métrica sobre azul cria variação sem mudar a identidade a cada frase. As letras têm trajetórias e recortes próprios. O número recebe construção em partes, depois sustenta a leitura. O diagrama Mensagem/Público adiciona uma explicação, e o CTA muda a organização da tela. Isso aproxima a lógica das referências, sobretudo a metamorfose funcional de elementos observada no Park/Virgílio, as mudanças de plano do Shard e a articulação de palavras/objetos do Oto. Não implica reprodução exata nem equivalência subjetiva de acabamento com essas referências.

## Correções verificadas

| Intervalo | Resultado observado no MP4 |
|---|---|
|4,2–6,2s|Não há ponta branca antecipada no lado esquerdo. A forma de transição surge a partir de aproximadamente 6,3s e passa a conduzir a troca de fundo.|
|5,8–6,2s|A legenda da cidade fica abaixo da foto com separação visível, sem interseção com sua borda durante o estado final e o início da saída.|
|6,4–7,0s|A cobertura branca integral dura poucos quadros: aproximadamente 6,6–6,7s; os primeiros glifos entram por volta de 6,73s. A passagem não sustenta o intervalo branco antigo.|
|8,3–9,0s|O play permanece acima de `Produzimos o vídeo.` com folga; não colide com o título.|
|9,3–10,2s|A placa azul não aparece inteira e vazia desde 9,3s. Ela cresce aproximadamente 9,73–9,87s enquanto o rótulo começa a entrar; `Evoquex.` está completo por volta de 10,1s.|
|11,9–13,6s|O ator vira marcador local com ponta e furo escuro. A silhueta está reconhecível em 12,2–13,4s. O furo some durante a metamorfose seguinte, em vez de se manter como recorte solto sobre o disco.|
|23,2–23,9s|O bloco da pergunta se retira no recorte; a partir de aproximadamente 23,3s não permanece `E o seu` como fragmento claro no topo do campo azul.|
|Estados iniciais|Nas amostras de 0, 1, 3, 4,5, 7,5, 9,5, 12,5, 15,5, 18,5, 21,5 e 24,5s, não aparecem prematuramente os títulos, placas, marcador ou dado de fases futuras. A conclusão se refere ao que se vê, sem atribuir uma conferência individual a seletores de código.|
|6,9–7,3s|Corrigido: em 6,900s a filmagem ainda está inteiramente ocultada; a primeira lamela aparece em 6,933s e as outras se abrem progressivamente, sem abrir–fechar–reabrir. Conferidos todos os quadros de 6,8 a 7,367s.|
|9,0–9,5s|Corrigido: o filme continua visível na parte do plano que sai entre 9,1 e 9,3s. O recorte do plano desaparece antes de aparecer qualquer painel escuro; não resta placa vazia. Conferidos todos os quadros de 9,0 a 9,5s.|

Os dois últimos pontos foram encontrados em revisão posterior do candidato intermediário. O MD informou que inicializou as três máscaras fechadas e prolongou o único trecho de filme até o fim da saída do plano. A confirmação acima veio da nova decodificação do MP4 final. O primeiro relatório não detectou o vazamento de um quadro na entrada; esta revisão posterior corrige essa avaliação e documenta o teste mais denso no limite exato.

## Legibilidade, conteúdo e continuidade

- `Danny’s Presentes` aparece com dois N e apóstrofo antes do S no rótulo real visível sob o filme.
- O dado final é `20 mil visualizações de pessoas de Clevelândia`, conforme a confirmação do briefing atual. A revisão não o converte em alcance, impressões, vendas ou pessoas únicas.
- A métrica completa permanece nítida aproximadamente de 16 a 17,7s. A tipografia de fundo é menos contrastante e se move discretamente, preservando a prioridade do dado principal.
- O marcador e o disco mantêm posição e massa durante a passagem local → evidência. A troca para o diagrama inclui a retirada da tela azul, o pequeno símbolo de mensagem e a entrada do título; não há um retorno prolongado ao filme.
- O diagrama tem rótulos legíveis, linha de ligação e ponto em movimento. Não há colisão persistente ao entrar a pergunta seguinte.
- `E a sua empresa?` e `E o seu serviço?` assentam com concordância correta. As letras parciais no percurso são fases de entrada/saída, não estados mantidos como frases finais.
- `Conversa com a gente.` termina legível sobre azul, com assinatura Evoquex separada do traço/curva. Não há marca-d'água persistente Evoquex/Clevelândia depois de 5s; essas palavras reaparecem em composições com função narrativa ou de assinatura.

## Pendências e limites

Não há correção visual adicional recomendada a partir do material examinado. A sustentação do dado e do CTA tem menos deslocamento que as transformações intermediárias, com propósito de leitura. Não se recomenda adicionar movimento aleatório para eliminar essas pausas.

Este é um parecer visual por amostragem ampla e sequências consecutivas, com conferência dos limites alterados quadro a quadro. Não certifica uma experiência audiovisual reproduzida e ouvida em tempo real. A validação de áudio permanece separada, a cargo do responsável pela mixagem; não houve escuta subjetiva por este agente.
