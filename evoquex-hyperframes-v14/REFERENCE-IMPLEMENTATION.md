# V14 — referências, direção e verificação de execução

Este documento relaciona a direção registrada em `DESIGN.md` e `STORYBOARD.md` às
passagens de `resources/scene-timing-v14.json`. As adaptações foram confirmadas
por inspeção de frames do MP4 final, com parecer independente e revisão de direção
em `review/independent-motion-review-final.md` e `review/director-motion-review-final.md`.
Arquivo revisado: `renders/evoquex-hyperframes-v14.mp4`, SHA-256
`a07de6cdbab452fb10e0d65c731710d4f64d14caa94a100730dec78838964417`. A revisão não foi playback contínuo nem escuta subjetiva.

## Acervo e consulta obrigatória

Quatro originais únicos permanecem em `../biblioteca/referencias/`, com hashes e
metadados em `catalogo.json`: Park/Shard Cloud, Park/Virgílio Contabilidade,
OtoCriativo e Park/Weven. Os três primeiros são obrigatórios a cada novo trabalho
ou revisão. Seus reenvios na V14 são cópias idênticas; não alteram o acervo. Weven
continua como referência adicional, sem apagar ou substituir nenhuma das três.

O MD deve registrar internamente a consulta aos MP4 reais, cobertura temporal,
movimentos críticos, método e limites. A análise temporal anotada em `DESIGN.md`
indica cobertura de toda a duração das três referências; as janelas abaixo são as
seleções de execução. Elas não substituem a abertura dos arquivos originais. Não
afirmar playback em tempo real ou escuta quando só houve decodificação e quadros.
Nenhuma música, voz, imagem ou marca dessas referências será incorporada ao case.

## Passagens e critérios para o MP4 V14

| Passagem V14 | Técnica e referência estudada | Adaptação e pontos de implementação | Critério de revisão no render |
| --- | --- | --- | --- |
| 0–4 s: hook | Articulação tipográfica e mudança de eixo, OtoCriativo 3,9–5,1 s; benchmark do hook atual | Rig de palavras do hook, perspectiva e máscara circular. Preservar a ideia das quatro mensagens, melhorando movimento quando útil. | Movimento desde o primeiro frame, hierarquia legível e passagem integrada ao pós-hook. Não exigir identidade com o render V13. |
| 4–6,6 s: reconhecimento | Forma que redefine a composição, Virgílio 16,3–17,3 s; articulação do Oto | `#local-phrase`, `#city-fragment` e `#local-caption`: palavras abrem a paisagem em faixas, depois as faixas conduzem o próximo campo. | Paisagem nasce do gesto, a leitura resolve e a saída tem destino reconhecível; não parecer um título sobre uma foto parada. |
| 6,6–9,2 s: produção | Transformação entre suporte e imagem, Virgílio 16,3–17,3 s; continuidade do conteúdo real | `#production-scene`, `#film-rig`, `#real-film`, `#film-lines`: uma filmagem de 2,56 s (6,9–9,46 s) recortada em três lamelas, nome e mensagem com hierarquia própria. | Uma instância do filme, sem celular ou áudio concorrente; Danny’s Presentes legível; filme não domina a duração. |
| 9,2–11,6 s: divulgação | Formas com função transitiva e percurso, Shard Cloud 9,6–11,1 s | `#facet-layer`, `#distribution-brand`, `#distribution-band`, `#flight-trails`: play facetado muda em seta e entrega a faixa tipográfica. | A mudança play→seta e sua trajetória podem ser acompanhadas em frames consecutivos; texto não é uma cartela independente. |
| 11,6–14 s: localidade | Contorno que assume nova função, Virgílio 38,2–39,6 s | `#facet-layer`, `#target-city`, `#target-art`: seta torna-se marcador, tipografia muda de orientação e a aproximação abre a área da prova. | Marcador e texto têm relação espacial clara; sem deformação sustentada das letras e sem marca-d’água persistente. |
| 14–18 s: dado ativo | Fragmentação e recomposição tipográfica do Oto; expansão de forma da linguagem das três referências | `#proof-number`, `#twenty`, `#thousand`, `#proof-unit`, `#proof-qualifier`: número em fatias, qualificador em seguida e reenquadramento. | Ler “20 mil visualizações de pessoas de Clevelândia” sem converter a unidade. O dado é atestado pelo usuário; nenhuma captura antiga é apresentada como comprovação. |
| 18–20,5 s: relevância | Anel/linha e conexão, Shard Cloud 15,5–16,9 s | `#strategy-one`, `#strategy-two`, `#strategy-graph`, `#graph-path`, `#graph-traveller`: forma vira conversa, polos se aproximam e conexão prepara o sublinhado. | Ponto percorre a curva e os polos participam da transformação, em vez de atuar como ícones decorativos. |
| 20,5–26 s: convite | Câmera que acompanha a frase, OtoCriativo 20,4–21,5 s; campo que reorganiza composição, Virgílio | `#cta-world`, `.cta-station`, `#cta-blue-field`, `#cta-invitation`, `#cta-signature`: câmera visita empresa e serviço, ligação vira fronteira e o convite ganha escala. | Perguntas com gênero correto, CTA natural, continuidade até a assinatura e leitura suficiente. Não manter dois blocos fixos por toda a janela. |

As janelas compõem o arquivo final de 26 s/780 frames. Se o MD retimar a composição,
atualizar timing, áudio, storyboard e esta tabela antes da verificação definitiva.
A confirmação das passagens e as correções estão vinculadas ao hash acima.
Mudanças posteriores exigem nova inspeção, sem reutilizar a aprovação deste arquivo.

## Mecânicas do HyperFrames e limites

A direção adaptou duas mecânicas da biblioteca:
`facet-morph`, para a geometria que muda de função, e `caption-camera-follow`, para
poses de câmera autoradas em torno das palavras. Originais, versões e licenças devem
permanecer separados das adaptações. As mecânicas estão no helper local
`vendor/evoquex-v14-motion.js` e foram conferidas no render; não são execução literal
dos exemplos originais.

O facetamento usa 18 vértices externos, nove internos e 36 triângulos
interpolados entre play, seta, marcador, disco e balão. Trata-se de vetor com
sombreamento por facetas, não CGI físico ou refração. Câmera CSS em 2,5D, máscaras
SVG, traçados por dashoffset e MotionPath são compatíveis com o motor instalado.
Não afirmar execução literal de uma técnica que foi substituída por outra.

## Som, fatos e evidências finais

A música V14 é uma composição inteiramente nova, já produzida e integrada. Os acentos sonoros
seguem os marcos de `scene-timing-v14.json`; não copiar áudio das referências nem
reaplicar o loop rejeitado como se fosse música nova. Verificar o arquivo de mix
realmente integrado, sua procedência, duração, clipping e alinhamento aos gestos.
Não alegar escuta subjetiva sem ferramenta de audição disponível.

Locução feminina permanece pendente e não deve ser simulada com a voz Kokoro
rejeitada. A grafia obrigatória é **Danny’s Presentes**. O dado ativo vem da
declaração explícita do usuário no briefing V14, sem verificação independente;
visualizações não provam pessoas únicas, vendas ou ROI.

O responsável pelo QA deve inspecionar sequências consecutivas dos movimentos,
abertura e duração inteira no MP4, corrigir os problemas e registrar internamente
o hash do arquivo final efetivamente revisado. Uma tabela de intenção ou compilação
sem erros não prova acabamento. A aceitação desta entrega está em
`review/final-approval-v14.json`, com os limites do método de inspeção explícitos.
Ao usuário, entregar somente o MP4, conforme o briefing; manter análises e QA internos.
