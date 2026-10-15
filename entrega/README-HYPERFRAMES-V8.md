# Evoquex — comparação nativa HyperFrames V8

[Baixar vídeo V8](evoquex-hyperframes-v8.mp4) · [Comparar lado a lado](comparacao-remotion-hyperframes.mp4) · [Projeto completo](evoquex-hyperframes-v8-projeto.zip)

Nova versão produzida e exportada nativamente com HyperFrames 0.8.162, HTML/CSS e GSAP 3.14.2. Não é uma exportação Remotion reembalada. A V7 permanece preservada.

**34,5 segundos · 1080 × 1920 · 30 fps · H.264 + AAC estéreo.** O comparativo identifica Remotion V7 à esquerda e HyperFrames V8 à direita; contém uma única faixa de áudio para evitar duplicação.

## O que mudou

- Abertura com tipografia cinética, composição em profundidade e planos fotográficos.
- Passagens com recortes e continuidade entre camadas, coreografadas em uma timeline GSAP determinística.
- Composição azul para os resultados, contadores e captura original integrada.
- Perguntas conectadas e encerramento claro com convite natural.
- Correção do retorno ao poster na primeira passagem, de espaçamento dos números e de contraste do rodapé após revisão do MP4.

A mesma narrativa, duração, filmagem original, foto aérea, registro da campanha e master de música/efeitos da V7 foram mantidos para facilitar a comparação. Danny’s Presentes conserva a grafia correta; os únicos resultados apresentados são 13.064 pessoas alcançadas e 20.981 impressões, sem inferir vendas ou retorno financeiro.

## Verificação realizada

Decodificação integral de imagem/áudio; duração, dimensões, 1.035 frames e codecs confirmados; amostragem de toda a duração, 31 quadros iniciais, 35 amostras de transição, estados internos e legibilidade em telas pequenas. O check nativo passou sem erros de runtime, layout ou contraste. Dois avisos de repetição de fotos correspondem a reutilização intencional. As assertions automáticas de movimento não foram habilitadas; o movimento foi inspecionado nos quadros exportados e no mapa de animação.

O ZIP inclui fontes editáveis, assets locais, dependências fixadas, instruções e relatórios. A reprodução foi verificada em pasta independente com npm ci e quatro snapshots reais, sem depender do projeto Remotion. Relatórios JSON acompanham a entrega e contêm os hashes dos arquivos.

## Limitações

Esta versão continua **sem nova locução**, assim como a V7. Não reutiliza a voz rejeitada, não utiliza serviço pago e não simula gravação humana. A faixa sonora foi validada tecnicamente, sem escuta subjetiva nesta interface. Não foi executado nenhum projeto AEP. A filmagem de origem tem aproximadamente 5 segundos e a foto aérea tem 600 × 337 pixels; esses limites permanecem. A adaptação não demonstra que um motor é universalmente superior ao outro.

Para abrir o projeto: extraia o ZIP, execute npm ci e npm run dev. Os comandos de validação e renderização estão no README do projeto.
