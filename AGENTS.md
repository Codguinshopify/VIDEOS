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
