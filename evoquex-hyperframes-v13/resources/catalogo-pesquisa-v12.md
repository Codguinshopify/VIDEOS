# V12 — pesquisa técnica de catálogo, sem implementação

Pesquisa de 2026-10-15. Escopo read-only nos projetos/catálogos existentes; somente este relatório foi escrito. Nenhuma instalação, renderização, edição de composição ou modificação do catálogo compartilhado.

## Base verificada

- Instruções lidas: `VIDEOS/AGENTS.md`, `biblioteca/README.md`, `biblioteca/hyperframes/catalogo.json`, `biblioteca/componentes/catalogo.json`, `biblioteca/packs/inventario.json` e direção V11.
- Skill consultada: `hyperframes:hyperframes-registry` (`c0/hyperframes-registry`): componentes são snippets; markup/CSS/JS devem ser integrados, não confundidos com um bloco de vídeo pronto.
- Clone Git sem checkout: `/workspace/referencias-tecnicas/hyperframes`; revisão `08ee1bd5ad59987a7f2525222683e24ca30971f9`. Somente `git show`/`git ls-tree` usados.
- Instalação real V11 verificada: HyperFrames **0.8.162**, GSAP **3.14.2**, iguais ao package.json. GSAP local é suficiente para todos os sete candidatos. Não há necessidade de nova biblioteca para as mecânicas abaixo.
- Os 20 arquivos originais dos 10 itens do catálogo permanente conferem com os SHA-256 declarados. Os sete arquivos de amostras do pack também conferem.
- Lidos os usos anteriores V9/V10/V11: V9 já usou perspective-marquee, máscara de palavra, collage, órbita e tiles; V10 usou motion-path, morph play/check e foco; V11 usou line-swap/underline/focus. Repetir simplesmente os mesmos layouts não constitui uma evolução.
- Licença do clone: Apache-2.0 no `LICENSE`. Os sete `registry-item.json` não declaram licença substitutiva, atribuição externa ou dependências adicionais. Preservar LICENSE e proveniência; GSAP mantém sua licença própria, não vira Apache por estar incluído. A fonte DM Sans e ícones Lucide existentes possuem OFL/ISC, respectivamente.

## Seleção de sete componentes concretos

Todos os caminhos abaixo são relativos à revisão Git fixada. Somente `perspective-marquee` também existe nos originais da V9; os demais seis candidatos não são presumidos instalados na biblioteca permanente: extrair os originais exatos quando a implementação decidir usá-los, guardando HTML como `.html.txt` para não sofrer mutação do Studio. Adotar JS local GSAP, removendo dependência de CDN dos snippets.

### 1. whip-pan-cut — passagem por superfície única e blur direcional

- Fonte: `registry/components/whip-pan-cut/whip-pan-cut.html`
- SHA-256 HTML: `2e21c04b6b72c4c4087b9e926da4f83b95940e798b9e5ad26e4845c41e6df7b7`
- SHA-256 metadata: `d94fc3446d2e150451f7adf66af231663c36dd3318ce8777ba6702c0ed03f591`
- API original: `direction:left|right`, `whip_at`, `accent`, `exit:none|fade|up`; slots `before`/`after`.
- Mecânica real: A e B montadas numa única `.wpc-strip`; B a exatamente uma largura de quadro. Medir largura uma vez e fazer `tl.fromTo(strip,{x:0},{x:sign*width,duration:0.55,ease:'power3.inOut'},at)`. As velocidades dos dois lados da costura são idênticas porque compartilham um único tween.
- Blur real: SVG `feGaussianBlur stdDeviation='X 0'`; proxy `v` sobe 0→16 na primeira metade com `power3.in` e retorna 16→0 com `power3.out`; `onUpdate` escreve o atributo. O filtro está no mover 2D, não no pai de planos 3D, evitando achatamento da perspectiva.
- Uso proposto: hook→cidade perto de 4 s, duração autoral de aproximadamente 0,40–0,48 s, e não em toda passagem. Usar foto real/cidade como slot B. SFX no meio do movimento, onde a velocidade é máxima; evento `hf:sfx` original apenas sinaliza, não produz som.
- Cuidado: filtro necessita margem lateral suficiente para não cortar o smear; não repetir texto legível durante o pico do blur. Não combinar filtro com `preserve-3d` no mesmo nó.

### 2. perspective-marquee — tipografia em plano oblíquo

- Fonte: `registry/components/perspective-marquee/perspective-marquee.html`
- SHA-256 HTML: `14d4544b748881f564ee3a2ffd55b1a630179b47b9d17bc3ee24667baf7c1698`
- SHA-256 metadata: `dd58efc4635d18550ef20d380f2140a63e41c36ef534f804e79bd9f0cca92d39`
- API original: `tilt:flat|standard|steep` (6/18/34°), `travel:short|standard|long` (0.55/1/1.8), `tone`, `words`.
- Mecânica real: plano com `perspective:900px`; faixa inline-flex duplica palavras; translateX controlado por `--hf-marquee-x`, multiplicado por `--hf-marquee-reach`. Receita original: `tl.fromTo(rail,{'--hf-marquee-x':'0px'},{'--hf-marquee-x':'-360px',duration:4.5,ease:'none'},start)`.
- Adaptação proposta: não repetir pílulas da V9. Extrair a mecânica do plano e montar **tipografia de grande escala**, peso alto, sem cards; wrapper tem perspectiva, filho inclina/recua. No hook, palavra parcial já visível no frame 0 entra por escala e translateZ/rotateY e resolve frontal em 0,45–0,65 s. Recuar a palavra anterior no espaço enquanto entra a próxima. Sugestões textuais: `SUA EMPRESA` → `NA SUA CIDADE`; só usar o texto final do roteiro aprovado.
- Cuidado: valores extremos exigem overscan e teste em 1080×1920; manter palavra principal frontal no trecho de leitura. Perspectiva CSS é 2.5D, não malha 3D real. Nenhum CSS animation de relógio é necessário.

### 3. iris-reveal — abertura de máscara com borda acoplada

- Fonte: `registry/components/iris-reveal/iris-reveal.html`
- SHA-256 HTML: `977a7e068ebe7f547006794ee36ef4d30cd36d68edbd05acf60719e294de989e`
- SHA-256 metadata: `fa1700c4e29b98ad6169a8cbe67438a583d9f6797f7d1d82f5aef6ca3ddcab18`
- API: `iris_x`, `iris_y` (0–100%), `open_at`, `register:plain|color`, `accent`, `exit`; slots before/after.
- Mecânica real: medir caixa uma vez; raio final `hypot(max(cx,W-cx),max(cy,H-cy))*1.02+2`. Um proxy de raio alimenta tanto `clip-path:circle(...)` quanto o SVG do contorno. Um tween `radius:0→fullRadius`, `power2.inOut`, mantém máscara e borda alinhadas. Fonte usa 1,1 s; não é duração obrigatória para V12.
- Adaptação proposta: revelar vídeo 8 s a partir de abertura que nasce do marcador da cidade ou do contracampo de uma letra; 0,45–0,55 s. Se a direção pedir gate retangular, preservar o princípio de **uma propriedade de progresso que dirige máscara e contorno**, adaptando geometria para `inset`/polígono de vértices fixos. Isso é adaptação declarada, não API pronta do iris.
- Cuidado: `register:color` original dessatura o estado anterior; escolher `plain` para preservar material real. Não transformar todo o vídeo em círculos; usar o gate apenas onde conduz a história.

### 4. modal-morph — layout que se transforma sem esticar o conteúdo

- Fonte: `registry/components/modal-morph/modal-morph.html`
- SHA-256 HTML: `a932a8deece4bbe231f99010e01800e35564a4d59ca4d59bbce09b1f0be942b4`
- SHA-256 metadata: `a0b1a87b24fbd21e8f19863da00ce91cb5861b3c3df77e3703bba7401fb9a6b4`
- API: `from_scale`, `expand_at`, `register:calm|snappy`, `accent`, `exit`; slot `template[data-slot='modal-morph-card']`, pares de filhos `data-morph-key`.
- Mecânica real: layouts final e inicial existem no DOM e são medidos **uma vez**; FLIP por translate/scaleX/scaleY do contêiner, nunca tween de width/height. Filhos interpolam retângulos próprios e aplicam counter-scale para letras/imagens não se deformarem. `applyTime(tl.time())` é função pura; anchor tween cobre a duração inteira. Modo snappy dura 0,6 s e overshoot analítico fica abaixo de1,02.
- Adaptação proposta: a moldura do vídeo se transforma em recorte da captura de resultados aos15s; título/data ficam em posição específica enquanto a janela se amplia. Na saída das métricas, a mesma linha/caixa pode virar estrutura editorial do CTA. Remover mobiliário de dashboard demo; não montar um falso painel.
- Cuidado: aguardar fontes locais antes de medir; tamanhos/reflow devem ser idênticos no frame0 e em seek isolado. Se usar filhos duplicados durante handoff, não duplicar duas vozes/vídeos ou apresentar duplos valores. Elementos decorativos não recebem semântica de dado.

### 5. scan-band — faixa óptica diagonal, localizada

- Fonte: `registry/components/scan-band/scan-band.html`
- SHA-256 HTML: `66e19b727703fa360aca5a9c87b930e71b07b3d1c1649eb8e0befab4e614e83f`
- SHA-256 metadata: `c7e2f1f9e50a36438a034d530e597d1d0c585877bb6a5d4d6be108dc9a295c4e`
- API: `wordmark`, `band_angle` −30…30°.
- Mecânica real: wordmark limpo mais três clones recortados pela **mesma banda**. `clip-path:polygon` calcula posição com `--sb-band-position` e inclinação `tan(angle)*50`; GSAP move posição −60%→160%. Fora da banda, o lettering é sempre nítido.
- Adaptação proposta: uma passagem curta de0,3–0,4s sobre palavra do hook ou assinatura Evoquex, sem strobe. Baixar deslocamentos RGB do original a aproximadamente1–2px e alpha≤0,20 para não remeter a glitch genérico. Pode manter somente clone claro/deslocado se a direção não comportar RGB.
- Cuidado: não aplicar sobre números durante a janela de leitura; não confundir scan-band com overlay scanline permanente. A banda é um evento, não uma textura que treme a peça inteira.

### 6. light-sweep-pass — luz única compartilhada pelos materiais

- Fonte: `registry/components/light-sweep-pass/light-sweep-pass.html`
- SHA-256 HTML: `16f8575923e3deacbbf2a2154bf4ec7c77ae8dd8d588c0ce0b5e25e5eea7376a`
- SHA-256 metadata: `9228f84345f6d0e3b4a3fdf3e0d577589c448d6d333834293d5bcc48c6c7b9f3`
- API: `angle`60…160°, `sweep_at`, `strength:subtle|standard`, `accent`, `exit`; slot scene; opt-in por `data-lit` e posição `--lsp-x`.
- Mecânica real: único proxy `light.x` escreve CSSvar `--light-x`. O valor passa−35→118 (`sine.inOut`) e assenta62 (`power2.out`); sombras, highlight por elemento e a faixa respondem ao mesmo valor. Fonte leva1,6s+0,55s; adaptar a duração conscientemente, não colar o demo inteiro.
- Adaptação proposta: fundo carvão e borda/linha azul Evoquex recebem uma passagem discreta, não filtro sobre a fotografia original. Atingir a métrica no momento em que ela resolve e manter o número quieto durante a leitura. CTA pode receber outra luz de direção compatível, sem confete/iluminação aleatória.
- Cuidado: não clipe o texto abaixo do contraste. Evitar bloom cobrindo captura verdadeira; conservar screenshot sem alteração que prejudique prova. Fonte0,5s stage fade não precisa ser reutilizada.

### 7. grain-overlay — textura leve com atualização determinística

- Fonte: `registry/components/grain-overlay/grain-overlay.html`
- SHA-256 HTML: `97a0da8f26feca9574abcf08b8186cef10ea4819b2aeabc30547ae16ed9ae80d`
- SHA-256 metadata: `bd0c8976bc2cf7c6ed6aae3a64023c73e61505b604dfba97220ed27bbca0e897`
- Mecânica real: textura SVG local embutida, `feTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'`; plano com overscan200%; tabela de deslocamentos em10passos.
- **Não usar sem adaptação:** original contém `animation: hf-grain-noise .5s steps(1) infinite`, controlada pelo relógio CSS, e alpha0,15 excessivo para esta peça. Desativar animation, fixar seed do turbulence e controlar índice de offset como função de tempo do timeline (`floor(t*12)%10`), ou usar segmentos GSAP `steps(1)`, com repetição finita. Mesma imagem em seek fora de ordem.
- Uso proposto: alpha0,018–0,035, camada nos fundos gráficos escuros; intensidade ainda menor sobre dados e filmagem. A sutileza é essencial. Textura não substitui composição/movimento principal e não merece um SFX próprio.

## Recurso complexo adicional investigado: shutter-slam

Fonte `registry/components/shutter-slam/shutter-slam.html`, SHA-256 `b5c28857acbd57d0b7c14b029b9a7de1ee0900bbfa7b84a261bd89c85537aec7`; metadataSHA `b586b7428be4d8e710261122511a5bd584430755beeaad4b8f0969a0ce89cd52`.

Há um sistema verdadeiro de shutter temporal incluído: `attachMotionBlur(selector,tl,{shutterAngle,shutterPhase,samplesPerFrame,fps,sharp})`, limite2…64amostras, defaults720°,−360°,16. Clona estilos resolvidos, avalia matrizes de transformação e soma amostras; suporta targets2D/3D, mas recusa targets aninhados entre si. Posição do blur acompanha seek da timeline, não só playback. A amostragem aplica-se ao target e seu conteúdo, sendo cara para grandes árvores DOM.

Não foi descartado por ser trabalhoso. Pode ser útil para **uma única palavra curta de hook**, com8amostras/180° e fps30, depois de teste visual/performance em frame isolado. Evitar aplicar ao vídeo real, telas inteiras ou ao mesmo pai que contém outro alvo blur. Não é necessário usar os seis slams/giros do demo; o motor pode acompanhar uma aproximação curta. A alternativa2D direcional do whip é barata e adequada a pan, mas não equivale a shutter físico temporal. Se o time optar pelo shutter, incluir o helper completo e testar seek0/meio/depois/volta; não fingir motion blur real usando somente CSS blur.

## Aplicação sugerida ao roteiro real (timings como janela, não implementação)

| Janela | Conteúdo factual / função | Movimento recomendado | Estabilidade necessária |
|---|---|---|---|
|0–4s hook|Divulgar sua empresa/serviço; curiosidade clara|Tipografia em perspectiva de escala grande desdeframe0, mudança de palavra por oclusão; 1scan-band ou shutter curto; whip conduz à cidade|Primeira ideia legível até~0,7s; não iniciar com tela vazia|
|4–8s cidade|Campanha direcionada somente a Clevelândia|Foto aérea real em recorte grande com overscan; marcador conduz à abertura/gate|Nome Clevelândia retido; sem mapa de público inventado ou alegação sobre não seguidores|
|8–15s produção|Vídeo da Danny’s Presentes produzido pela Evoquex|Gate revela a filmagem; moldura/layer amplia-se por FLIP; original dura~5,06s e não deve ser repetido para preencher7s|Manter uma reprodução completa sem efeitos que escondam a ação; tempo restante pode ser still identificado ou composição da moldura, não loop|
|15–21s prova|13.064 pessoas alcançadas;20.981impressões/exibições do anúncio|FLIP conduz à captura real; cada métrica recebe destaque separado, rápido assentamento e hold; luz discreta|Rótulos inequívocos; evitar contagem longa, gráfico de vendas, porcentagem ou “visualizações”|
|21–30s conclusão/convite|Pensar mensagem+público para sua empresa/serviço; “Quer fazer algo assim? Conversa com a gente.”|Objeto editorial do resultado vira composição do CTA; mudança de escala e foco, com assinatura limpa|No máximo uma pergunta/ideia por momento; CTA lê sem necessidade de pausar|

## Packs disponíveis e limites que importam

Inventário permanente real: `VIDEOS/biblioteca/packs/inventario.json`; branch previamente inspecionada `packs-lfs`, commit `fcf095991ad0ce8b0e10728c8abf927bc4bddfa9`.

- Part1 de1.048.576.000bytes foi baixada e conferida anteriormente. O pacote completo não está disponível no ambiente.
- Part2 de1.048.576.000bytes tem pointerLFS identificado, mas conteúdo **não foi baixado nem analisado**. Não declare parte2/3 extraídas. Volumes posteriores não aparecem na árvore remota previamente inspecionada.
- Amostras completas de fato presentes e com hash conferido: `Brush 2.png`3517×989; `Ink_1.mp4`1920×1080/10,01s; `Ink_10.mp4`1920×1080/14,748s; `Ink_11.mp4`,`Ink_12.mp4`,`Ink_13.mp4`,`Ink_14.mp4`1920×1080/4,84s cada.
- Brush éPNG; transparência precisa ser inspecionada se virar alpha-mask. InkMP4 é vídeo, não alpha pronto; luma-mask pode exigir threshold/conversão e validação de bordas. Os arquivos correspondem ao hash do catálogo; não revalidei pixels/decodificação nesta pesquisa.
- Licença comercial específica/redistribuição desses packs não consta do inventário. Material fornecido pelo usuário não prova licença; conservar procedência. Nenhum áudio de referência foi selecionado.
- A árvore parcial mostra numerosos `.aep` (AtomAfterEffects/backgrounds etc.). Não existe AfterEffects executável aqui; nenhum AEP foi carregado/executado. Necessitam render/export no AE, dependências e fontes/plugins próprios. Pre-renderalphaPNG/MOV pode ser aproveitado **quando presente e validado**, não supor que o AEP ou MOGRT rode no HyperFrames.
- Para a nova direção escura/cinética, um wipe de tinta pode funcionar como única ruptura editorial, mas não é obrigatório. Os componentes vetoriais com licença verificável já resolvem os movimentos principais sem instalar plugins de origem desconhecida.

## Condições de integração/validação para o implementador

1. Um timeline raiz pausado e registrado. Incorporar mecânicas aos helpers do projeto e chamar a partir desse timeline, em vez de deixar múltiplos clocks/CSSanimations soltos.
2. Medir caixa/fontes uma vez com dimensões fixas1080×1920; não medir DOM a cadaframe. As fontes locais precisam estar prontas antes de construir FLIP.
3. Prefixar IDs/classes de filtros e máscaras; estado inicial explícito; clip e outline sempre derivados do mesmo proxy. Nenhum callback essencial depende de playthrough.
4. Eventos `hf:sfx` dos snippets não contêm áudios e não geram sons. Usar WAV existentes e cues reais, mixar para a nova coreografia. A voz feminina continua condicionada à integração autenticada; não alegar sincronização com locução ausente.
5. Snapshot em seek0→meio→fim→volta; inspecionar renderexportado no pico do pan e entre layouts. Conferir que blur some e números ficam nítidos no hold. Só então considerar o padrão utilizável.
