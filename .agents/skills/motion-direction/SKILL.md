---
name: motion-direction
description: Transforma roteiro e referências em storyboard técnico, tipografia cinética, continuidade entre cenas, transições e profundidade determinísticas, com critérios de movimento verificáveis no render.
---

# Direção e execução de motion

Use para desenhar e implementar a execução visual de um roteiro existente. Esta
skill cobre decisões de composição e movimento; não duplica análise de referências,
inventário de packs, geração de imagens ou QA final. Combine-a com as quatro skills
locais existentes e com HyperFrames, CLI, registry e GSAP da versão instalada.

## Entradas e limites

- Briefing vigente, roteiro e trechos aprovados que devem permanecer intactos.
- Vídeo anterior real, `DESIGN.md`, storyboard, mídia documental e timeline atual.
- Análises temporais das referências, catálogo HyperFrames e auditoria dos recursos
  novos/modificados no Git, feitos antes de construir a composição.
- Formato, fps e restrições de marca, prova e áudio.

No briefing V13, **preserve integralmente o hook 0–4 s e o conteúdo do roteiro**.
Reconstrua a execução visual de 4 s até o fim; coerência textual será tratada depois.
Não transformar uma tarefa de motion em reescrita ou em lista de sugestões.

## Storyboard técnico obrigatório

Antes do código, preencha uma linha por unidade de ideia; uma unidade pode conter
várias ações e não precisa corresponder a uma cartela ou frase inteira.

| Campo | Pergunta operacional |
| --- | --- |
| Janela e texto fixado | Quando acontece e qual texto deve permanecer? |
| Compreensão e foco | O que precisa ser entendido e qual palavra/objeto domina? |
| Estado de entrada | Qual objeto, alinhamento, eixo e escala vêm da unidade anterior? |
| Movimento principal | Qual transformação explica a ideia? Qual trajetória e easing? |
| Antecipação e settle | Há preparação/impacto úteis? Onde a leitura se estabiliza? |
| Saída e continuidade | O que atravessa, comprime, revela ou se transforma no próximo plano? |
| Recursos | Qual componente real, mídia ou pack validado será efetivamente usado? |
| Som e aceitação | Qual marco visual recebe acento e em quais frames verificá-lo? |

Uma linha como “texto entra com fade, fica e sai” não resolve a direção. Defina
hierarquia, trajetória e passagem entre composições. Um momento calmo pode ser
intencional; não crie movimento decorativo para esconder ausência de narrativa visual.

## Procedimento de decisão

1. **Pesquisar e selecionar.** Use `reference-analysis` para técnica/timestamp/função;
   `asset-library-research` para catálogo, Git e compatibilidade. Abra os exemplos
   escolhidos e confira a versão. Distingua componente instalado, adaptação de fonte
   e implementação personalizada. Não presuma springs, câmera ou shaders nativos.
2. **Definir um verbo de movimento por unidade.** Empurrar, abrir, dobrar, atravessar,
   recuar, revelar ou conectar. Escolha o verbo pelo significado e pela continuidade,
   não para cobrir uma lista de efeitos. Registre o destino do objeto no trecho seguinte.
3. **Construir tipografia como composição.** Separe palavra de foco, palavras de apoio
   e informação documental. Defina baseline, largura, janela/máscara e área segura.
   Uma troca de palavras dentro de uma janela compartilhada é diferente de animar
   duas caixas independentes com curvas conflitantes. Só fragmente letras quando
   o stagger e a articulação reforçarem a mensagem sem destruir sua leitura.
4. **Conectar as cenas.** Prefira um mesmo objeto ou trilho para handoffs cuja velocidade
   deve coincidir. Em match cut, alinhe escala, ponto de apoio e direção antes do corte.
   Em máscara, mova sua borda e o conteúdo como partes da mesma passagem. Evite tela
   inteira em fade como solução padrão e não repita entrada idêntica em todos os trechos.
5. **Desenhar profundidade com parcimônia.** Defina plano próximo, assunto e plano de
   apoio, perspectiva e ponto de fuga. Mova-os em amplitudes diferentes, mantendo
   coerência de direção e sombra. Texto documental permanece legível. Transformação
   CSS/2.5D não é CGI físico; descreva a técnica real, sem prometer refração ou câmera3D
   que não existem no pipeline.
6. **Especificar timing.** Use segundos ou frames no fps fixado. Separe preparação,
   deslocamento, overshoot e settle; intervalos curtos não devem receber back/elastic
   só por aparência. Reserve tempo de leitura após a estabilização. Varie curva,
   direção, escala e alinhamento por função, preservando identidade de cor e tipografia.
7. **Sincronizar som.** Escolha poucos marcos: mudança de direção, impacto tipográfico,
   abertura de máscara ou assentamento de número. Registre cue, tempo e evento visual;
   efeitos reais e licenciados devem apoiar o gesto. Remixe quando o timing mudar.
   Um sound effect por letra não é requisito de complexidade.
8. **Implementar determinismo.** Um timeline raiz pausado/registrado, animações relativas
   a ele, dados e mídias locais. Sem `Math.random`, relógio de parede, autoplay externo,
   `requestAnimationFrame` ou timers para movimentação. Defina estados iniciais e evite
   `from()` distante que altere prematuramente outro trecho por immediateRender.
9. **Validar em movimento.** Rode os checks do motor e renderize. Aplique
   `motion-quality-control` com frames consecutivos e trajetórias, não apenas capturas
   isoladas. Corrija a execução que ainda pareça cartelas independentes. Declare uma
   técnica implementada somente após confirmá-la no arquivo exportado.

## Exemplos GSAP determinísticos

São padrões de construção para adaptar ao DOM real, não presets que devem aparecer
em toda cena. Use seletores locais e dimensões explícitas; consulte a documentação da
versão instalada antes de adotar recursos além desses exemplos.

```js
// HyperFrames: o motor controla a posição deste único timeline pausado.
window.__timelines = window.__timelines || {};
const tl = window.__timelines['composition-id'] = gsap.timeline({ paused: true });

// Continuidade: dois painéis adjacentes de 1080 px sob a mesma máscara.
// O movimento de um trilho único mantém velocidade e easing iguais na emenda.
tl.to('#shared-track', {
  x: -1080, duration: 0.48, ease: 'power3.inOut'
}, 7.8);

// Tipografia: duas linhas de 130 px dentro de uma janela com overflow:hidden.
// A máscara fica parada; o mesmo trilho desloca a frase e sua substituta.
tl.to('#word-track', {
  y: -130, duration: 0.42, ease: 'power3.inOut'
}, 10.2);

// Letras: articulação curta termina num estado estável e legível.
tl.fromTo('#focus-word .char', {
  yPercent: 70, rotationX: 55, opacity: 0
}, {
  yPercent: 0, rotationX: 0, opacity: 1,
  stagger: 0.025, duration: 0.42, ease: 'power4.out', immediateRender: false
}, 12.0);

// Parallax: amplitudes distintas, mesmo intervalo e direção, perspectiva no pai.
tl.to('#near-plane', { x: -80, z: 90, duration: 0.7, ease: 'power3.inOut' }, 14);
tl.to('#far-plane', { x: -24, z: -90, duration: 0.7, ease: 'power3.inOut' }, 14);
```

Antes do trecho, o CSS ou um `tl.set` deve posicionar e esconder corretamente os
elementos ainda inativos. Não anime a mesma propriedade do mesmo elemento em tweens
simultâneos conflitantes; use wrappers diferentes para câmera, conteúdo e articulação.

Armadilha confirmada na revisão V14: `fromTo(..., {opacity: 0}, {opacity: 1,
immediateRender: false}, at)` **não aplica o estado inicial antes de `at`**. Se o CSS
deixar o elemento visível, ele pode aparecer cedo, sumir no começo do tween e entrar
de novo. Defina o estado inativo em CSS ou em `tl.set(..., 0)` e o destino visível
explicitamente no tween. Faça o mesmo para placas em `scaleX`, partículas SVG,
clips e rótulos futuros; não esconda apenas seus filhos enquanto o suporte fica vazio.
Inspecione também os frames imediatamente anteriores ao anchor, não só a entrada.

Não distorça letras ao transformar a geometria de uma moldura: mantenha texto em plano
separado ou aplique compensação verificada. Respeite `prefers-reduced-motion` apenas
quando fizer parte da entrega interativa; não altere o render temporal por ambiente.

## Critérios de aceitação e saídas

- Storyboard técnico com todos os campos, recursos reais e transição de saída definida.
- Matriz referência/técnica/trecho/função/arquivo/evidência do render, preservada no projeto.
- Sequências consecutivas mostram trajetória contínua, mudança de hierarquia e
  estado final legível; não basta contar tweens ou detectar pixels diferentes.
- Pausas são justificadas por leitura/prova; ruído animado de fundo não mascara uma
  composição principal parada. Analise duração e função de cada hold antes de corrigi-lo.
- O hook e os textos protegidos passam nas verificações específicas; fontes e dados
  reais continuam corretos. Os movimentos começam e terminam onde o storyboard prevê.
- Vídeo completo renderizado e revisado; limitações de reprodução/escuta documentadas.
  Não gere comparativos para o usuário. Nesta V13, entregue também o relatório objetivo
  solicitado, sem substituir o vídeo por documentação.
