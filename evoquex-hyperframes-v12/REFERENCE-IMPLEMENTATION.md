# Referências → tarefas verificáveis V12

Tabela criada antes da composição e conferida no MP4 final. Estado: técnicas abaixo
implementadas e verificadas por amostragem visual real. Detalhe auditado: biblioteca/referencias/oto-criativo/ANALISE-OTO.md.

|Referência / tempo|Técnica / função|Adaptação Evoquex|Local de implementação|Verificação no MP4|
|---|---|---|---|---|
|Oto3,9–5,1s|Letras rotacionadas que assentam; câmera revela hierarquia|SUA EMPRESA e VISTA? por letras em profundidade|motion.js hook; vendor/evoquex-v12-effects.js letters|quadros0–120: letra, eixo e escala mudam, leitura final clara|
|Oto14,7–15,45s|Cópias de palavra em profundidade + etiqueta em primeiro plano|É CONHECIDA com rótulo azul e cópias discretas|index.html .known-stack; motion.js|0,8–1,6s: etiqueta cruza ecos, sem competir com frase|
|ParkShard2,1–4,8s|Objeto amplia e se transforma, conduzindo mudança|Abertura da pergunta revela cidade por iris acoplado à borda|EvoquexFX.iris; #middle-track|3,8–4,5s: mesma abertura e contorno chegam juntos|
|Oto6,8–8,85s|Trilho2.5D com objeto e foco que mudam juntos|Cidade→case num único trilho; filme desloca para fases reais|#middle-track; FX.whip; #film-shell|7,7–8,3s: deslocamento contínuo e blur curto resolvido|
|Oto11,15–11,7s|Documento em perspectiva como objeto|Captura original ganha plano e rota para métrica|#proof-paper; #results|14,8–16,2s: prova verdadeira presente sem UI reconstruída|
|Oto1,2–2,25s|Número principal e planos periféricos; profundidade|Dados verdadeiros, sem preço/recibo/gráfico inventado|#impression-value;#reach-value|15–21s:20.981impressões e13.064pessoas, cada valor legível|
|ParkVirgílio18,5–22,5s|Foto vira recorte e depois forma/palavra|Superfície se comprime e vira suporte do convite|FX.flipBox; #cta-frame|20,8–21,5s: transformação de geometria sem esticar letras|
|Oto20,45–21,1s|Contorno desenha CTA; resposta discreta|Conversa com a gente com traço e seta licenciada|#cta-outline;#cta-button|25,5–29s: desenho e seta efetivamente visíveis|
|Oto21,4–22,45s|Objeto à esquerda, frase à direita e seta explicativa|Case e encerramento alternam alinhamento real|style.css case/invitation; motion.js|8–15/21–30s: não repetir a estrutura centro+miniatura|

Limites:2.5D/CSS não é CGI3D físico. Não há waveform de voz inexistente. Não copiar
marcas/mídia/áudio de referências. Nova locução ainda não existe; som próprio real
acompanha os movimentos. 


## Aceitação no arquivo final

MP4: `renders/evoquex-hyperframes-v12.mp4`, SHA-256
`928b0b271c5144169af4dfe378935af5f8b4ca1b45fa4865bb63b7b1fd2b3361`.

- Letras articuladas: abertura frames0–120, inspecionada consecutivamente em
  `review/hf-v12-hook-01.jpg` até `06.jpg`. Frame0 tem conteúdo e entrada em movimento;
  etiqueta/profundidade resolvem em0,98–1,2s e pergunta inteira vermelha em2,9–3,6s.
- Iris: frames114–130 em `review/hf-v12-cuts-01.jpg`; raio e aro coincidem, cidade
  é revelada sem flash de outra mídia. Movimento3,82–4,47s.
- Trilho/whip: frames231–247 em `review/hf-v12-cuts-02.jpg`; cidade sai à esquerda,
  título/filme entram no mesmo avanço7,75–8,30s. Plano do filme legível em8,8–13,1s.
- Prova: shutter14,70–15,34s, cobertura total≈0,13–0,17s após correção; documento
  reaparece15,15s. `review/hf-v12-cuts-02.jpg`, folhas completas01/02 e phone-proof.
- Dados:20.981 estabiliza15,9s;13.064 estabiliza18,8s. Rótulos corretos,≈2s de
  sustentação por valor, sem confundir impressões/pessoas. Conferidos na captura real.
- FLIP:20,82–21,61s, amostrasframes624–640 emcuts-02; geometria da superfície muda,
  texto antigo perde foco/opacidade antes do convite e letras não são esticadas.
- Ícones Mensagem/Público em formação21,5–21,9s, completos22,2s. CTA tem traço, seta,
  troca empresa/serviço25,35–27s e sustentação final. Phone-strategy ephone-cta.
- Assimetria: quadros8,8/10/13,5/16,7/22,5/28,5s mostram arranjos realmente distintos.

Todos esses frames foram extraídos do MP4, não são apenas screenshots de HTML.
O parecer independente está em `review/independent-visual-review.md`. O mapa em
`review/animation-map/animation-map.json` tem viewport1080×1920; seus avisos heurísticos
não substituem esta revisão. O check nativo tem motion automático desativado.

## Quarta referência recuperada na auditoria

Park/Weven,42,61s, hash55e691627b4c…: análise completa arquivada na biblioteca em
`park-weven/ANALISE-WEVEN.md`, com86amostras ordenadas. Este original foi identificado
por hash durante a auditoria final dos anexos, depois da implementação principal;
não atribuímos retroativamente a ele a origem do código. Seus exemplos de continuidade
objeto→diagrama12–15s, componentes vetoriais23,5–26,5s e máscaras30s serviram para
conferir a solução final e ficam disponíveis às próximas produções. Não copiar suas
alegações de CRM/IA/vendas. As quatro referências únicas continuam preservadas.
