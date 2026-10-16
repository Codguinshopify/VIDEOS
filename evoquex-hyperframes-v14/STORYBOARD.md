# V14 — storyboard técnico

|Janela|Ideia|Texto preservado|Movimento e continuidade|
|---|---|---|---|
|0–4s|Hook|SUA EMPRESA → É CONHECIDA → EM CLEVELÂNDIA. → MAS É VISTA?|Rig tipográfico com quatro eixos, profundidade, contraste e máscara. A pergunta entrega a abertura circular.|
|4–6.6s|Reconhecimento|Já viu por aqui? Uma das nossas divulgações.|Letras se articulam, por aqui abre paisagem em faixas; paisagem fecha em lâminas e desloca o campo.|
|6.6–9.2s|Produção|Produzimos o vídeo. Danny’s Presentes|Fundo branco entra pelo espaço entre palavras; filme real único só6.9–9.46,3lamelas. Play facetado nasce da mesma geometria.|
|9.2–11.6s|Divulgação|E divulgamos pela Evoquex. Objetivo: ir além dos seguidores.|Play vira seta com36facetas, rastro emcurva. Palavra e faixa azul ocupam o espaço que o filme devolve.|
|11.6–14s|Localidade|Só para Clevelândia.|Seta dobra em marcador local. Tipografia muda de orientação, pin aproximae abre o campo azul da prova.|
|14–18s|Prova|20 mil visualizações de pessoas de Clevelândia|Numeral recomposto por fatiasemprofundidade. Mil articula, qualificador entra apósassentamento; câmera deslocae reframa, mantendo frase inteira legível.|
|18–20.5s|Relevância|Cada empresa. Uma estratégia. Mensagem → Público.|Ponto do0saiemtrajetória evirabalão, dois polos se aproximam e conexão se torna underline da estratégia.|
|20.5–26s|Convite|E a sua empresa? E o seu serviço? Conversa com a gente. Evoquex|Câmerafazrota por palavras emum mundo2160px. Ligação vira fronteira, campoazul invade, tipoConversa assumeescala e assinatura resolve; não há doisblocosfixospor4s.|

Cada gesto tem antecipação0,1–0,2s, passagem0,25–0,6s, leitura0,7–1,6s; as trocas de plano são feitas pelo ator ou máscara, sem cartela vazia. As trajetórias e facetas são determinísticas e reconstruíveis em seek. A validação final é responsabilidade do root e deve usar o MP4.

## Correções após inspeção do primeiro MP4
No MP4 real,5,8s confirmou protrusão da cunha branca antes da transição e contato do caption com a foto. Cunha agora invisível até6,28s, caption deslocado140px abaixo. Em8,8s a ponta do play encobria Produzimos: centro antecipado340→190px, mesmo destino9,65s. O marcador12,5s parecia balão; contorno agora arco superior240graus+pontainferior e furo circular em11,91–13,64s, preservando malha e anchors de áudio. Verificar essas correções no MP4final.

Segunda revisão do primeiroMP4: a placaazul9,3–9,73estava noestadofinalantesdo tween; estadoCSSagorascaleX0até9,72. A saída da cunha branca foi antecipada6,62→6,57e encurtada0,34→0,27, preservandoo acento6,35. As perguntas da CTA recebem máscara23,02–23,30antesde ficaremforada câmera; evita fragmentobrancoemcima do campofinalem23,5.

QA temporal também detectou elementos de entradas futuras mostrando o estadoCSSfinal antes do fromTo(immediateRender:false). Opacidade inicial0 aplicada ao objetivo, sombra, eco, dois rótulos e partícula; evita flash/reentrada e quarto de círculo no canto superior. Timings/áudio/destinos do movimento permanecem iguais. Verificar especialmente9,5–10,8 e18–19,6 no MP4final.

Terceira revisão do MP4hash904031b398: o frame6,9mostrava filme inteiro antesde abrir aslamelas6,91; retângulosSVG agora têmheight0noHTML, de acordo com fromTo. O vídeo terminava9,1antesde o plano sair9,46, gerando retângulo escuroem passagem. Duração da única mídia aumentada2,2→2,56s(6,9–9,46); permanece breve<3s e acompanha a saída completa do plano. Anchors sonoros e duração total26s intactos.
