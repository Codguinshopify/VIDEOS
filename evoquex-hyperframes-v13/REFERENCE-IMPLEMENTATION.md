# V13 — referências, implementação e critérios de confirmação

As oito técnicas abaixo foram selecionadas no estudo anterior à composição,
`resources/reference-motion-study-v13.md`. A tabela identifica a adaptação presente
no código e a janela a ser examinada. **As técnicas foram confirmadas por sequências do MP4 final.**
O primeiro render foi criticado e corrigido; a conferência definitiva é descrita abaixo.

As quatro referências únicas permanecem em `../biblioteca/referencias/`: Shard Cloud,
Virgílio Contabilidade, OtoCriativo e Weven. Seus conteúdos, marcas e áudios não foram
reutilizados como mídia da campanha.

| Técnica observada | Referência e tempo de origem | Adaptação no código da V13 | Janela da V13 | Arquivo e elemento | Critério no MP4 final |
| --- | --- | --- | --- | --- | --- |
| 1. Um suporte nasce no conteúdo e passa a ocupar o plano | Shard Cloud, 2,067–3,267 s | A pergunta encontra uma máscara tipográfica preenchida pela foto real; a abertura se amplia. A máscara de letras é uma adaptação nossa do princípio de expansão, não cópia literal da referência. | 4,04–5,83 s | `index.html`: máscara SVG e `#masked-city`; `motion.js`: `#flat-query`, `#city-open`; `style.css`: plano da cidade | As duas leituras se conectam sem imagem prematura, flash ou tela vazia; foto e tipografia resolvem com hierarquia. |
| 2. A borda sobrevive à imagem e assume outra função | Virgílio, 19,267–19,800 s | O contorno da cidade se comprime em linha e conduz a abertura do plano da filmagem. O texto permanece independente da deformação da borda. | 7,12–8,41 s | `#flow-frame`, `#city-open`, `#motion-world`; `EvoquexV13.frame()` | O percurso da borda tem origem e destino reconhecíveis; a câmera chega ao case sem salto de escala ou letras esticadas. |
| 3. Passagem entre planos com movimentos internos em outros eixos | OtoCriativo, 7,900–8,267 s | Uma estação entrega o filme enquanto nome, palavras e mídia chegam com trajetórias e tempos diferentes. A filmagem avança e o texto recua, sem carrossel de celulares. | 7,64–10,20 s | `#motion-world`, `#campaign-rig`, `.client-name`, `#production-type`; `EvoquexV13.letters()` | Mídia e palavras mudam de hierarquia com continuidade; uma única instância real do filme, sem colisão prolongada com o nome. |
| 4. Fragmentos se alinham para reconstruir palavra ou número | OtoCriativo, 14,733–15,233 s | Três fatias recompõem “divulgações.”, “Evoquex.” e “20.981”. O alcance utiliza grupos de dígitos e articulação própria. Aplicar o princípio às métricas é uma adaptação declarada. | 5,86–6,43 s; 10,93–11,54 s; 15,12–15,74 s; 17,98–18,65 s | `.slice`, `#distribution-brand`, `#impression-value`, `.digit-group`; `EvoquexV13.slices()` | As fatias se unem antes da leitura principal; valor e definição permanecem corretos, sem número parcial sugerindo nova métrica. |
| 5. O objeto muda de função sem perder o percurso | Weven, 12,200–13,800 s | O mesmo vídeo passa de retrato a janela horizontal para acompanhar “Só para Clevelândia.”; seu contorno continua até a estação documental. Não reproduzimos cursor, pessoa ou cliente da referência. | 12,75–15,35 s | `#campaign-rig`, `.campaign-viewport`, `#locality-type`, `#flow-frame`; `motion.js` | A mudança de janela conduz à informação local e prepara a prova; sem substituição por mockups repetidos ou material fictício. |
| 6. Uma peça muda de geometria e prepara o próximo campo | Weven, 27,800–29,267 s | A câmera e o contorno entregam a captura original, que abre em três painéis complementares enquanto o numeral se resolve. A fragmentação é feita com CSS, não com um recibo ou dashboard recriado. | 14,63–16,05 s | `#document-rig`, `.paper-piece`, `#proof-metric-a`; `style.css` e `motion.js` | Os painéis recompõem o mesmo documento, sem lacunas persistentes, pausa opaca longa ou ocultação da identificação da prova. |
| 7. Conector e polos reorganizam a frase seguinte | Shard Cloud, 26,067–27,000 s | “Mensagem” e “Público” chegam por lados opostos; curva e ponto os conectam. O diagrama se comprime e entrega visualmente a passagem ao campo do convite. | 21,65–23,95 s | `#message-node`, `#audience-node`, `#link-curve`, `#traveller`, `#diagram-v13`; MotionPathPlugin | O ponto percorre a curva real; os polos participam da transformação, em vez de permanecerem como ícones decorativos estáticos. |
| 8. Fronteira entre campos redistribui texto e CTA | Virgílio, 55,300–57,300 s | O campo azul nasce da linha do diagrama e se expande até o rodapé, reorganizando pergunta, CTA em duas linhas e assinatura; há pequena reação de ida e volta antes do assentamento. Empresa e serviço trocam com o gênero correto no mesmo marco. | 23,85–30 s | `#cta-field`, `#question-v13`, `#cta-type`, `#company-ask`, `#service-ask`, `#closing-drawing`; `motion.js` | Texto não sofre squash; a leitura se resolve; não aparece “E a seu” ou “E o sua”; convite e assinatura têm espaço próprio. |

## Mecânicas HyperFrames efetivamente adaptadas

O helper local `vendor/evoquex-v13-motion.js` registra a origem das mecânicas:
`text-match-cut` para a curva Bézier resolvida por bisseção, `pan-stations` para o
mundo contínuo e `type-match-cut` para o princípio da abertura tipográfica. O resultado
é uma adaptação ao timeline único da composição, não execução direta dos snippets com
CDN e clocks independentes. Originais e licenças continuam na biblioteca.

Fragmentação por faixas e planos em perspectiva são soluções compatíveis com DOM,
SVG, CSS e GSAP instalados. Não se afirma execução literal de Canvas slit-scan, springs
não utilizadas, câmera 3D física ou refração. O helper V12 foi preservado; o novo helper
mantém suas adaptações separadas.

## Hook e texto protegidos

O intervalo `[0,4)` conserva a base aprovada. `resources/copy-contract.json` contém o
contrato de textos e os hashes dos prefixos de HTML, CSS e GSAP usados para conferir
as fontes. Comparar fonte não comprova pixels: os 120 frames devem ser examinados,
separando igualdade lossless de semelhança do MP4 após compressão H.264.

A iris iniciada em 3,82 s vem da V12. A V13 não deve acrescentar antecipações que
alterem o hook antes do segundo 4. A textura e a luz ambiente aprovadas também foram
mantidas. Os primeiros quatro segundos do WAV têm sua própria checagem PCM.

## Evidências do arquivo definitivo

MP4 final SHA-256 `548a550705c835551b4ab2817acec0d92862eb79fee40b6299a18c54c6a81ef2`.
Inspeção: 120 frames do hook, 393 frames consecutivos em nove janelas, 60 amostras da
duração inteira e seis frames de telefone. Registros em `review/hf-v13-sampling.json`,
`review/independent-motion-review.md` e `review/motion-review-v13.json`.
A revisão adicional confirmou as cinco correções nos trechos alterados. Cada critério
da tabela acima foi examinado nas sequências correspondentes, não apenas no código. Os números finais são **20.981 impressões** e **13.064 pessoas
alcançadas**, conferidos contra a captura verdadeira da **Danny’s Presentes**.

Não reaproveitar o hash, a aprovação, os nomes de sheets ou as conclusões do render
V12 como aceitação desta versão. Não chamar de playback contínuo a leitura de frames;
não alegar escuta subjetiva. Esses recursos não estão acessíveis nesta interface.
