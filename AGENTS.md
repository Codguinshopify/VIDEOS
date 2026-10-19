# Evoquex — instruções permanentes de produção

Estas instruções abrangem este repositório. Preserve as regras específicas de cada
projeto e os arquivos existentes; não substitua versões anteriores ao criar uma nova.
Leia primeiro `biblioteca/README.md` e o `DESIGN.md` da composição escolhida.

## Direção criativa

Motion minimalista, dinâmico e profissional: uma mensagem principal por momento,
poucas palavras, hierarquia e espaço negativo. Varie enquadramento e composição sem
trocar a identidade a cada frase. Use as referências para estudar timing, máscaras,
continuidade, transformações e acabamento; não copie layout, paleta ou sequência.
Não resolva tudo com frases sobrepostas, círculos repetidos ou ícones com zoom.
O movimento começa no primeiro frame quando o briefing pedir um hook imediato.

## Pesquisar antes de construir

1. Leia as skills e a documentação da versão instalada do HyperFrames.
2. Consulte `biblioteca/hyperframes/catalogo.json`, os exemplos originais e os
   componentes reutilizáveis de produções anteriores catalogados na biblioteca.
3. Consulte `biblioteca/packs/inventario.json`; verifique formatos, integridade,
   dependências e licença. ZIP/RAR é embalagem, não formato de animação.
4. Consulte **todas as** referências em `biblioteca/referencias/catalogo.json` e
   suas análises. Incorpore novos exemplos ao catálogo, sem apagar os anteriores.
5. Só crie um recurso manual quando não houver alternativa adequada; registre a
   decisão e a procedência. Não instale bibliotecas desnecessárias.

## Referências permanentes

- `biblioteca/referencias/park-shard-cloud/Park_Criativo_video_no_watermark (1).mp4`
- `biblioteca/referencias/park-virgilio/Park_Criativo_video_no_watermark.mp4`
- `biblioteca/referencias/oto-criativo/oto_criativo_video_no_watermark.mp4`
- `biblioteca/referencias/park-weven/Park_Criativo_video_no_watermark (1).mp4`

São originais preservados por hash; não renomeie, sobrescreva ou remova sem necessidade.
Uso de estudo: não reutilize sua música, voz, imagens, marcas ou alegações no case.
Leia `biblioteca/referencias/ANALISE.md` para técnicas e trechos relevantes.

## Execução e validação

HyperFrames é o motor atual. Um timeline raiz pausado e registrado, animações
determinísticas, médias locais e versões fixadas. Preserve fontes e licenças.
Sincronize movimento com frases e efeitos; não force mudanças a cada segundo.
Antes de entregar, renderize e inspecione o MP4 real: abertura quadro a quadro,
transições, duração completa, hierarquia, texto, dados e áudio. Compilar não basta.
Separe claramente checagem técnica de áudio de escuta humana indisponível.

## Fatos e voz

**Danny’s Presentes** é a grafia obrigatória. Evoquex produziu o vídeo e direcionou
a campanha somente a Clevelândia. Evidências: 13.064 pessoas alcançadas e 20.981
impressões/exibições do anúncio. Não inferir vendas, conversões, ROI, visualizações
ou distribuição para não seguidores. Métricas são prova, não a narrativa inteira.
Fale também de empresa/serviço. CTA natural: “Conversa com a gente.”

Voz feminina brasileira natural é desejada. Não reutilize a voz Kokoro rejeitada.
Verifique ferramentas e presença de credenciais sem revelar valores. Não compre
planos. Se não houver voz adequada, prepare roteiro/cues e declare a locução pendente;
nunca deixe referências a um arquivo de voz inexistente no HTML.

## Reutilização e entrega

Catalogue recursos, proveniência, dependências, limitações e modo de uso. AEP/MOGRT
não executam diretamente em HyperFrames; considere mídia pré-renderizada e conversão
validada. Não declare analisado um volume ainda não baixado ou um arquivo incompleto.
Entregue somente o vídeo editado, sem montagens comparativas. Preserve fontes e QA no
repositório. O usuário prefere link GitHub `/raw/refs/heads/.../entrega/...mp4`.

## Referências primeiro, execução verificável — diretriz V12

Em todo novo vídeo: auditar arquivos e referências antes de escrever composição;
consultar exemplos/documentação HyperFrames e acervo local; produzir tabela com
referência/timestamp, técnica, função, adaptação, arquivo/função de implementação e
frame de aceitação no MP4. Só marcar implementado depois de ver a técnica renderizada.
Análise sozinha não cumpre produção. Renders devem ser criticados e iterados.
Organização das amostras deve ser ordenada por timestamp/número de quadro; não inferir
cronologia pela ordem de diretório. Proteger legibilidade nos estados intermediários.

Conteúdo mínimo, riqueza na execução: variar escala, eixo, enquadramento e profundidade;
não substituir técnica adequada por fade/zoom genérico apenas por ser mais fácil.
O briefing V12 autoriza nova direção: fundo escuro, branco, azul#54A6FF e vermelho
#F87171 no hook. Leia DESIGN.md da versão atual; não imponha paleta antiga.
O usuário confirmou divulgação pela conta Evoquex e intenção de alcançar quem ainda
não acompanhava a empresa. Isso não prova a quantidade efetiva de não seguidores.
Luciane deve permanecer desativada/modular, sem cena ou dado fabricado, até pedido.

Skills locais, com procedimentos reais em `.agents/skills/`:
- `reference-analysis/SKILL.md`: auditoria temporal e análise aplicada.
- `asset-library-research/SKILL.md`: formatos, licenças, pesquisa e packs.
- `ai-visual-asset-design/SKILL.md`: IA somente quando melhorar necessidade concreta;
  usar ferramenta de imagem disponível e não fabricar prova de campanha.
- `motion-quality-control/SKILL.md`: QA real de imagem/áudio/fatos, com limitações claras.
Essas skills complementam as dos plugins; leia seus arquivos quando aplicáveis.
Não afirmar registro automático em um serviço de skills que não tenha sido testado.

## Execução contínua após o hook — diretriz V13

O hook aprovado de **0 a 4 segundos** é a base protegida desta etapa: preservar sua
composição, cores, tipografia e movimentos. Reconstruir a execução visual **de 4 s até
o encerramento**, com continuidade, tipografia cinética, máscaras, profundidade e
transições escolhidas para cada ideia. Não reescrever o roteiro por iniciativa
própria e não desviar esta etapa para coerência textual. O restante deve alcançar o
acabamento do hook; fade/zoom repetido, screenshots em mockups e cartelas independentes
não cumprem esse objetivo. Minimalismo significa hierarquia; não simplificação do motion.

Antes de implementar, auditar Git e arquivos locais contra o histórico disponível,
incluindo branches relevantes, novos packs, áudio, componentes, scripts e referências.
Preservar alterações existentes e registrar base, caminhos, formatos, integridade,
compatibilidade e recursos realmente escolhidos. Não alegar auditoria completa com
histórico ou volumes faltantes. Usar os recursos úteis descobertos quando adequados,
não apenas listá-los. Não assumir que presets AEP/MOGRT executam em HyperFrames.

Aplicar `motion-direction/SKILL.md` em `.agents/skills/` para storyboard por trecho,
foco, estado inicial, trajetória, curva, saída, conexão, recursos e sound cue. Essa
skill complementa as quatro locais e as skills oficiais do motor. Pesquisar exemplos
da versão instalada antes de decidir uma solução personalizada; só registrar uma
técnica como implementada após confirmá-la no MP4 exportado.

O QA deve comparar automaticamente o hook inteiro `[0,4)` por frames/pixels contra
a base aprovada, distinguindo identidade lossless de diferenças de compressão no MP4.
Verificar também invariância dos textos, frames consecutivos das transições,
trajetórias, leitura e sincronização dos acentos. Não confundir screenshots isolados,
grão animado ou contagem de tweens com revisão do movimento. Se playback/escuta não
estiverem disponíveis, declarar a limitação sem afirmar que assistiu ou ouviu.

Entregar vídeo renderizado e revisado, com o relatório objetivo pedido nesta etapa:
técnica/referência/trecho, recursos reutilizados, problemas corrigidos e limitações.
Não gerar montagem comparativa. A documentação não substitui a execução do vídeo.

## Direção vigente e agente MD — diretriz V14

O briefing V14 é a instrução atual e **prevalece sobre as restrições históricas da
V13 quando houver conflito**. Leia `.agents/agents/md.md` ao assumir a direção de
motion design. É um arquivo de instruções locais persistentes; não alegar registro
ou descoberta automática de agente em nuvem.

Antes de cada novo trabalho ou revisão da Evoquex, consultar novamente **os três
MP4 reais** de Shard Cloud, Virgílio e OtoCriativo, nos caminhos permanentes e com os
hashes de `biblioteca/referencias/catalogo.json`. Não substituir a consulta por memória,
descrições ou análises antigas. Os três anexos reenviados na V14 foram deduplicados
por hash e correspondem às cópias já preservadas. A referência adicional Weven continua
disponível. Registrar a consulta efetiva internamente e não alegar playback/escuta
quando só houver decodificação e análise de quadros.

O hook é benchmark de qualidade e **pode ser aprimorado**: não exigir igualdade de
cada frame com a V13. Preservar a ideia do gancho, fundo escuro, branco, azul `#54A6FF`
e vermelho `#F87171`. Reconstruir substancialmente o pós-hook, com motion como
protagonista, composições conectadas e filmagem real breve. Não manter “Evoquex” ou
“Clevelândia” como marca-d’água persistente depois dos primeiros cinco segundos.
As mensagens e a estrutura narrativa permanecem; só ajustar texto minimamente
quando indispensável ao ritmo, à leitura ou à transição. A duração pode ser ajustada.

**Dado ativo da V14:** “20 mil visualizações de pessoas de Clevelândia”, atestado
pelo usuário no novo briefing. Essa é sua procedência; não afirmar verificação
documental independente. Na nova edição, substituir a apresentação das métricas
antigas por esse dado, sem convertê-lo em impressões, alcance ou 20 mil pessoas únicas.
Não usar a captura de 20.981 impressões/13.064 de alcance como prova das novas views.
Preservar os arquivos e as informações históricas da V13, sem reescrevê-los retroativamente.
Danny’s Presentes continua sendo a grafia correta; não inventar vendas ou resultados.

A trilha anterior foi rejeitada por repetição: substituí-la ou reconstruir a música
e sincronizar o sound design às transformações. Consultar acervo, Git e biblioteca
HyperFrames atualizados, não apenas o inventário de uma execução anterior. Usar os
recursos úteis de fato, mantendo procedência e compatibilidade verificáveis.

**Entrega V14: somente o MP4 final**, sem relatório, resumo das mudanças, inventário,
lista de skills, código ou descrição do processo. Fontes, auditorias e QA permanecem
internos ao repositório. Se um bloqueio real impedir a conclusão, informar apenas o
impedimento específico. As decisões criativas já estão autorizadas; não pedir
aprovação a cada transição ou escolha técnica.

## Direção vigente V15 — 19/10/2026

O pedido completo está em `evoquex-hyperframes-v15/resources/briefing-v15.txt` e
prevalece sobre restrições históricas conflitantes. A V15 permite reconstruir o
hook e o restante, variar a paleta com função narrativa e retimar as nove cenas
para leitura. Não limitar a edição a azul, branco e preto. Preserve versões anteriores.

As duas bibliotecas são fontes efetivas de produção: componentes do HyperFrames e
assets dos packs. O usuário autorizou o uso comercial dos materiais que forneceu;
não bloquear por dúvidas genéricas de licença. Verificar compatibilidade, origem,
integridade e uso real na composição. Consultar seleções existentes antes de baixar
packs inteiros. AEP/MOGRT não passam a ser executáveis apenas por terem sido extraídos.

Nesta fase, música e efeitos, **sem geração de voz ou configuração de TTS**. A voz
do ElevenLabs será fornecida pelo usuário depois. Manter cenas, marcadores sonoros
e stems editáveis para sincronizar esse áudio sem reconstruir a composição.

Dado ativo: “20 mil visualizações de pessoas de Clevelândia”, informado pelo usuário.
Não transformar em alcance, pessoas únicas, vendas ou contadores. A imagem aérea
disponível é fotografia; não afirmar que existe filmagem aérea. Danny’s Presentes é
a grafia obrigatória. Preservar registro histórico das outras métricas.

Estudar os três MP4 reais antes da execução e revisar o MP4 final por toda a duração,
com sequências densas de abertura e transições. Registrar exatamente os métodos
disponíveis de revisão; decodificação/medição de áudio não equivale a escuta humana.
Entrega: MP4 com link direto, caminho, dimensões, fps, duração e revisão realizada;
informar apenas limitações relevantes. Sem montagem comparativa.
