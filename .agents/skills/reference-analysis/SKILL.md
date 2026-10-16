---
name: reference-analysis
description: Analisa referências audiovisuais por trechos e frames, extrai técnicas concretas de composição, movimento e som e as converte em decisões originais verificáveis.
---

# Análise de referências para motion design

Use quando receber uma nova referência, planejar uma direção criativa ou avaliar se
uma edição alcança as técnicas pedidas. A análise orienta a execução; não autoriza
copiar a identidade, o conteúdo ou o áudio de outra peça.

## Entradas

- Referências originais disponíveis e `biblioteca/referencias/catalogo.json`.
- `biblioteca/referencias/ANALISE.md`, briefing vigente e materiais reais do case.
- Composição atual e documentação do motor e das versões efetivamente instaladas.

## Procedimento

1. Localize todas as referências solicitadas. Preserve nomes e arquivos originais;
   registre hash, tamanho, duração, resolução, fps, streams e localização. Arquivos
   diferentes com o mesmo nome devem ficar em diretórios diferentes. Não substitua
   a referência anterior ao receber outra.
2. Confira integridade e decodificação. Extraia uma sequência que cubra a duração
   inteira e frames adicionais nas mudanças de cena e nos momentos importantes.
   Uma folha de contato ajuda a encontrar trechos, mas não comprova continuidade de
   movimento nem sincronização sonora. Examine sequências consecutivas nas passagens
   relevantes; use reprodução audiovisual quando houver ferramenta disponível.
3. Monte uma tabela de observações com tempo inicial/final, conteúdo, composição,
   ação, transformação, timing aproximado, hierarquia e função narrativa. Identifique
   o objeto que conecta uma cena à próxima e o que muda em cada passagem. Diferencie
   observação direta, inferência e hipótese técnica.
4. Analise tipografia, quantidade de palavras, leitura, máscaras, recortes, planos,
   profundidade, câmera, curvas de aceleração e mudanças de layout. Estime a duração
   das transições por frames e fps quando possível. Uma alternância de cores, por si
   só, não explica a linguagem de motion graphics.
5. Inspecione o áudio com os recursos realmente disponíveis. Registre presença de
   voz, música, acentos e relações temporais apenas quando verificáveis. Detecção de
   picos/RMS ou transcrição automática não comprova timbre, naturalidade, mixagem ou
   escuta humana. Indique a limitação se não houver reprodução sonora acessível.
6. Converta observações em técnicas implementáveis: por exemplo, máscara SVG com
   continuidade entre cenas, palavra substituída dentro da mesma janela, objeto que
   muda de escala para conduzir um corte, trilha por caminho ou revelação de mídia.
   Consulte as skills do motor e o catálogo antes de decidir criar componentes.
7. Para cada técnica escolhida, registre: trecho de origem, efeito observado,
   mecanismo compatível com a versão instalada, recurso existente candidato,
   adaptação ao conteúdo real e critério visual de sucesso. Declare aproximações
   quando não houver runtime, recurso ou ferramenta equivalente.
8. Escreva uma direção original e coerente. Use nível de acabamento, hierarquia e
   construção da referência; não replique sua sequência, paleta, marca ou alegações.
   A densidade visual deve servir à mensagem e à legibilidade, sem uma mudança
   obrigatória a cada segundo.

## Saídas

- Análise com trechos e técnicas concretas, evidência visual de apoio e distinção
  entre o que foi visto, medido ou apenas inferido.
- Direção de arte e lista priorizada de adaptações com objetivo e critério de sucesso.
- Registro de origem e restrição de estudo para as referências preservadas.

## Critérios de conclusão

- A duração completa está representada na análise; movimentos críticos têm frames
  consecutivos ou reprodução, além de frames isolados.
- A abertura, transições, trechos de prova e encerramento foram examinados.
- Cada recomendação importante aponta uma técnica e sua função narrativa.
- Não há alegação de escuta ou reprodução integral se apenas amostras foram vistas.
- Materiais da referência não foram introduzidos como prova ou mídia licenciada do
  case. Análises e estudos ficam no repositório; não entregue comparativos ao usuário
  sem pedido explícito.
