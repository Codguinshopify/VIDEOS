---
name: motion-quality-control
description: Revisa o MP4 exportado com evidências visuais, técnicas e sonoras honestas, valida narrativa, marca e métricas e impede entrega baseada apenas em compilação.
---

# Controle de qualidade audiovisual

Use antes de concluir uma produção ou revisão. Compilar, passar no lint e renderizar
não comprovam qualidade audiovisual. Esta skill complementa os validadores do motor
e exige examinar o arquivo efetivamente entregue.

## Entradas

- Briefing vigente, roteiro/timing, `DESIGN.md`, análise das referências e fontes.
- Arquivo final exportado, fontes reais da campanha e documentação dos áudios.
- Relatórios de lint, layout, render e validação disponíveis na versão instalada.

## Procedimento

1. Identifique o arquivo candidato por caminho, tamanho e hash. Rode os checks
   apropriados do motor, verifique mídias/fontes locais e erros de console. Não
   confunda o preview HTML com a imagem do MP4 exportado.
2. Faça probe e decodificação completa do MP4. Confira duração, resolução, fps,
   número de frames, codecs, pixel format, canais, sample rate e streams esperados.
   Investigue frames ausentes, falhas de decode, preto acidental e áudio ausente.
3. Extraia frames ao longo da duração inteira e sequências consecutivas na abertura,
   nas transições, nos destaques e no encerramento. Se o hook deve começar no primeiro
   frame, confira que ele já contém uma composição intencional e que o movimento
   começa imediatamente, sem espera ou tela vazia. Não confunda um frame estático
   bem composto com uma animação verificada.
4. Examine a continuidade dos objetos, máscaras, entradas/saídas, easing, cortes e
   mudanças de composição. Procure sobreposição de palavras, elementos parcialmente
   cortados, fonte substituída, contadores duplicados, flashes de poster, saltos de
   enquadramento e recursos genéricos repetidos sem função. Teste a legibilidade em
   tamanho de telefone e confira o tempo real de leitura.
5. Compare a construção e o acabamento com as técnicas documentadas nas referências,
   sem gerar ou entregar vídeos comparativos. Verifique a narrativa completa: cada
   frase acrescenta informação, as métricas funcionam como prova e o CTA soa próximo.
   A densidade de movimento deve servir à clareza, sem checklist de efeitos aleatórios.
6. Revise os textos tanto no código quanto nos frames. Neste case, a grafia é
   **Danny’s Presentes**. Evoquex produziu o vídeo; a campanha foi direcionada somente
   a Clevelândia. Confira os dados contra a captura real: **13.064 pessoas alcançadas**
   e **20.981 impressões/exibições do anúncio**. Não converter em visualizações,
   vendas, conversões, ROI, alcance de não seguidores ou crescimento fictício. Não
   usar gráficos que sugiram evolução temporal não documentada.
7. Valide o áudio efetivamente presente no MP4: decodificação, duração, clipping,
   loudness e pico verdadeiro quando as ferramentas permitirem. Verifique os cues
   contra os frames reais e o alinhamento das frases/acentos. Números de loudness e
   correlação não comprovam naturalidade da voz nem qualidade da mixagem.
8. Quando houver ferramenta de reprodução sonora acessível, escute a edição inteira
   e revise pronúncia, pausas, naturalidade, transições, ducking e competição entre
   vozes. Quando não houver, registre **validação técnica sem escuta subjetiva** e
   não escreva “escutei”, “voz natural confirmada” ou “mixagem aprovada por audição”.
   Transcrição automática ajuda a localizar frases, mas não substitui essa escuta.
9. A voz desejada é feminina brasileira natural. Não reutilize a voz Kokoro rejeitada,
   não invente locução pronta e não deixe referência a arquivo inexistente. Verifique
   ferramentas e autenticação sem expor credenciais. Respeite a autorização vigente
   de uso gratuito; não compre nem altere planos. Se a locução estiver pendente,
   informe isso e preserve roteiro/cues para inserção posterior.
10. Garanta que trilha, efeitos, voz e materiais tenham origem registrada e uso
    permitido. O áudio original deve estar mutado ou reduzido durante a narração
    quando competir com ela; não sobrepor vozes por acidente. Música e efeitos devem
    ter relação com a narrativa, sem mascarar a fala ou distorcer.
11. Corrija os problemas encontrados e renderize novamente. Repita os checks afetados
    e confirme que frames/áudio revisados pertencem ao hash da versão final. Relatórios
    de um render anterior não validam um MP4 alterado depois.

## Saídas

- MP4 final existente, decodificável e identificado por hash.
- Registro de QA com comandos/versões, amostragem visual, erros encontrados/corrigidos,
  checagens de marca/dados e limites reais da avaliação sonora.
- Fontes e registros preservados no repositório para continuidade.

## Trechos e textos protegidos — regra operacional V13

O briefing V13 congela o hook **0–4 s** e o conteúdo atual do roteiro. Primeiro fixe
qual arquivo/código é a base aprovada, sua duração, fps e hash. Guarde uma lista dos
textos por unidade narrativa e dos setters que alteram texto durante o timeline.
Compare esse conteúdo antes/depois, incluindo palavras em máscaras, CTA e textos
ocultos que se tornam visíveis. É permitido reorganizar a composição; não é permitido
reescrever frases para resolver coerência nesta etapa. Contadores intermediários
devem ser tratados como animação de um mesmo dado, não como novas alegações.

Para preservar o hook de um vídeo 30fps, verifique **todos os frames 0–119**,
intervalo `[0,4)`, e examine a emenda em 4 s separadamente. Mudanças globais de CSS,
fontes, filtros, GSAP e composição podem alterar o hook mesmo sem editar seu bloco de
código. Faça comparação automatizada por frame/pixel, não só igualdade de strings.

1. Capture baseline e candidato em condições idênticas: resolução, fps, fontes,
   navegador, renderer, seek e estado inicial. Prefira frames lossless do mesmo
   pipeline para verificar identidade visual. Hash por frame igual comprova pixels
   iguais naquele domínio de captura; registre os 120 resultados e os dois hashes-fonte.
2. Compare também os primeiros 4 s dos MP4 exportados. Registre contagem e alinhamento,
   erro absoluto médio/máximo e/ou PSNR/SSIM. Não escolha tolerância depois de ver os
   resultados só para aprovar. Diferenças precisam ser localizadas e explicadas.
3. H.264 de um render completo pode mudar pixels por compressão ou decisões de GOP.
   Uma boa métrica perceptual não prova igualdade de pixels. Separe “fontes/capturas
   lossless idênticas” de “MP4 perceptualmente semelhante”. Se houver diferença de
   layout, timing, máscara, cor ou letra, investigue a causa e corrija o hook protegido.

Exemplo técnico, executado com os arquivos reais e ambos em 30 fps/mesmas dimensões:

```bash
ffmpeg -v error -i baseline.mp4 -vf "trim=start=0:end=4,setpts=PTS-STARTPTS,format=rgb24" -an -f framemd5 baseline-hook.framemd5
ffmpeg -v error -i candidate.mp4 -vf "trim=start=0:end=4,setpts=PTS-STARTPTS,format=rgb24" -an -f framemd5 candidate-hook.framemd5
ffmpeg -i baseline.mp4 -i candidate.mp4 -filter_complex "[0:v]trim=start=0:end=4,setpts=PTS-STARTPTS[b];[1:v]trim=start=0:end=4,setpts=PTS-STARTPTS[n];[b][n]psnr=stats_file=hook-psnr.log" -an -f null -
```

Compare os hashes de conteúdo de cada frame, não apenas os arquivos `framemd5`
inteiros, cujos cabeçalhos/metadados podem variar. Esses comandos não geram vídeo
comparativo e seus logs ficam no projeto, não como material de comparação ao usuário.

## Revisão real do movimento e dos sound cues

- Use reprodução audiovisual do MP4 completo quando a interface oferecer uma
  ferramenta realmente acessível. Se só for possível decodificar/extrair quadros,
  **não declare que assistiu ao vídeo em playback**. Registre a limitação e examine
  sequências consecutivas suficientes para cada gesto, além das amostras do vídeo
  inteiro. Screenshots isolados não validam ritmo, settle ou continuidade.
- Na faixa 4 s–fim, selecione cada transição e movimento principal no storyboard.
  Extraia todos os quadros de janelas curtas que incluam antecipação, passagem e
  assentamento. Numere-os por frame/timestamp. Procure saltos, inversão inesperada,
  esticamento de letras, oclusões e intervalos ilegíveis nos estados intermediários.
- Quando puder inspecionar o runtime, registre trajetórias em intervalos regulares:
  centro/bounding box, escala, rotação, opacidade e clip do objeto de continuidade.
  Compare posição/velocidade na emenda com a intenção do storyboard. Trajetória de
  DOM é apoio técnico; confirme a aparência correspondente no MP4.
- Conteúdo principal estático com grão ou glow em movimento não comprova motion
  elaborado. Inspecione objeto e hierarquia por região/trecho. Quantidade de tweens,
  optical flow ou ausência de dead zones não são, isoladamente, critérios de qualidade.
  Preserve holds úteis para leitura, prova e conclusão.
- Prepare uma tabela `cue → gesto → tempo planejado → frame/tempo observado →
  arquivo de som → resultado`. Verifique acento e antecipação intencionais no áudio
  real decodificado e nos frames do render, não apenas no nome do evento no código.
  Defina tolerância de sincronização conforme o gesto/fps antes da revisão; um sweep
  pode preceder o impacto por intenção, sem ser erro. Registre a diferença observada.
- Meça clipping, loudness, true peak, canais e ducking quando aplicável. RMS/picos
  ajudam a localizar eventos, mas não demonstram que o efeito “soa bem” ou que uma
  voz é natural. Sem ferramenta de escuta, declare validação técnica e limite sonoro.
- Relacione técnicas às janelas verificadas e marque pendências reais. Uma passagem
  não examinada não recebe status “aprovada” apenas porque o render terminou.

## Critério de entrega

Entregue somente o vídeo editado, sem comparativos ou pacotes extras, salvo pedido
explícito. O usuário prefere link direto GitHub
`/raw/refs/heads/<branch>/entrega/<arquivo>.mp4`. Confirme que o arquivo publicado
corresponde ao validado. Resuma melhorias efetivas e limitações materiais, com voz
pendente quando aplicável; não declare aprovada uma dimensão que não pôde verificar.
