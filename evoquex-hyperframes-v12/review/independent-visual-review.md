# Revisão visual independente — V12 FINAL

MP4 final: `renders/evoquex-hyperframes-v12.mp4`.
SHA256 final confirmado: `928b0b271c5144169af4dfe378935af5f8b4ca1b45fa4865bb63b7b1fd2b3361`.

## Conferência das correções no MP4 final

Extraí e inspecionei visualmente 32 novos quadros diretamente do arquivo final:16quadros entre14,80–15,55s em intervalos de0,05s;12quadros entre20,80–21,90s em intervalos de0,1s;4quadros da pergunta em2,9/3,1/3,3/3,6s. Evidências em `/workspace/reference-review-v12/qa-final/{proof,strategy,question}.jpg` e PNGs individuais. Nenhuma alteração foi feita nas fontes ou noMP4 por este agente.

**Correções confirmadas:**

- A cobertura azul antes da prova ficou mais curta. Em14,85s ainda existe parte da filmagem;14,90s só uma ponta da cena anterior;14,95–15,05s cobertura total;15,10s já se vê a cunha escura da revelação;15,15s a captura/texto começam a reaparecer;15,20s a prova está exposta. A cobertura total está agora próxima de0,13–0,17s, dentro do intervalo recomendado. A longa pausa vazia do primeiro render foi resolvida.
- O painel final começa a preencher antes: em21,50s rótulos e primeiros traços são visíveis;21,70s os desenhos estão claramente em formação;21,90s já se reconhecem os dois ícones. O vazio do painel foi reduzido sem competir com a entrada do título.
- Na saída da prova,20,8–21,2s, números e rótulos antigos perdem opacidade/foco antes da substituição. Não permanece retalho de métrica nítida atrás do título novo.
- A pergunta inteira `MAS É VISTA?` está em vermelho, incluindo `MAS É`, nos quatro estados revisados. Contraste e leitura permanecem adequados.

**Parecer final:** os achados objetivos do primeiro render foram corrigidos ou reduzidos conforme recomendado. Não identifiquei novo problema visual nos trechos alterados. Os trechos não alterados mantêm a revisão completa anterior descrita abaixo. Nome e valores finais, concordância doCTA e ausência de colisões persistentes já foram verificados nessa revisão. Não há correção visual adicional necessária a partir das amostras inspecionadas.

**Limitações preservadas:** não houve escuta subjetiva, avaliação de timbre ou reprodução contínua em tempo real nesta interface. A locução feminina continua pendente e não está aprovada nem apresentada como existente. Este parecer valida imagem e evolução dos trechos corrigidos; mixagem percebida e naturalidade de voz exigem escuta humana. Não constitui aprovação artística absoluta, pois o estilo continua uma escolha criativa.

---

## Histórico de QA do primeiro render — achados resolvidos acima

# Revisão visual independente — V12, primeiro render

MP4 inspecionado: `renders/evoquex-hyperframes-v12.mp4`.
SHA256: `26b7fb93f93ed62c7c338b8907a3007e4ded2f19789cc1d5ece8d4f5fde51bca`.

Método: inspeção das três sheets da duração inteira (60amostras,30s),121quadros da abertura em seis sheets, passagens em `hf-v12-cuts-02.jpg` e `cuts-03.jpg`. Adicionalmente36quadros extraídos diretamente desteMP4, cobrindo7,75–8,85s,14,6–15,7s e20,8–21,9s, em `/workspace/reference-review-v12/qa/{cut-city,cut-proof,cut-strategy}.jpg`. Sem análise baseada apenas no código. Nenhuma escuta subjetiva realizada.

## Parecer

A V12 tem evolução visual real sobre a V11: abertura tipográfica escura com troca de escala, palavra em etiqueta e rastro, pergunta vermelha; fotografia em planos; produção com composição assimétrica e revela da filmagem; prova com documento em perspectiva; painel final que transforma mensagem/público em convite. Não é apenas aV11 com outra ferramenta. Não identifiquei cortes de texto persistentes, superposição persistente, erro de grafia do cliente ou erro nos valores finais.

**Ajuste recomendado antes da entrega:** reduzir a cobertura azul completamente vazia em15,0–15,3s. A soma cobertura+revelação leva de14,9 a15,5s, visivelmente mais longa que as outras passagens. Antecipar a revelação para manter no máximo0,12–0,18s de quadro totalmente coberto. Esse é o principal achado de ritmo do render atual.

Ajuste menor: os ícones do painel final só começam a aparecer por21,7–21,9s; o painel já está presente desde21,0s. Antecipar traçados/rótulos em0,2–0,3s reduz a sensação de suporte vazio, preservando a leitura do título.

## Observação por composição

- **0–4s / hook:** há conteúdo no quadro0 e movimento imediato no risco e no assentamento. `SUA EMPRESA` → `É CONHECIDA` → `EM CLEVELÂNDIA.` → `MAS É VISTA?` são quatro estados diferentes em4s. A mudança para vermelho só na pergunta cria hierarquia. Na entrada da etiqueta em0,85–0,98s e da pergunta em2,6–2,8s há interseção momentânea de planos; ela resolve em cerca de0,15s, sem texto mal formado sustentado. O mesmo vale à saída da etiqueta por cima em1,8s. Não classifiquei essas passagens como colisão, pois são transições deliberadas e breves.
- **4–8s / reconhecimento:** título grande à esquerda, cidade em três planos e seta curva embaixo. Bem mais espacial que o cartão central daV11. A foto tem deformação de perspectiva pequena, sem prejudicar identificação. O texto `Uma das nossas divulgações.` entra depois do foco principal, sem competir. Composição estabilizada por alguns segundos; o movimento é discreto, não uma imagem estática única.
- **7,75–8,85s / troca para case:** a cidade sai enquanto surge o nome do case. Suporte vertical vazio apenas em8,15–8,25s; imagem já começa a revelar em8,35s e preenche em8,55s. É uma revelação breve com função, aceitável, não considero necessário alterar. A filmagem não dá flash indevido antes da máscara.
- **8–15s / produção e divulgação:** `Danny’s Presentes` tem doisN e apóstrofo correto. Vídeo original aparece uma vez; composição assimétrica com texto à esquerda e filmagem maior à direita. Os textos se substituem com mudança de palavra e pequeno deslocamento, mantendo tempo de leitura. Em10,75s aparece texto intermediário parcialmente mascarado; ele resolve em11,25s e não encosta na filmagem. O objetivo sobre seguidores é explicitamente rotulado `Objetivo`, não apresentado como resultado comprovado.
- **14,6–15,7s / entrada da prova:** precisa do ajuste de ritmo acima. Não há vazamento entre as cenas: o wipe cobre corretamente, mas permanece completamente fechado por tempo perceptível.
- **15,5–21s / resultados:** valores finais corretos:20.981impressões,13.064pessoas alcançadas. Rótulos distinguem impressão de alcance; não se fala em vendas ou retorno. Contagem tem valores transitórios até resolver; isso é animação, não outra métrica. Documento real aparece em perspectiva, porém a captura original tem resolução e legibilidade limitadas, então não deve ser anunciada como comprovante integralmente legível no celular. A mudança vertical entre as métricas em18,2–18,6s passa por recortes parciais intencionais e resolve; não encontrei duas métricas sobrepostas permanentemente. Os dois valores ainda usam organização parecida, mas a troca semântica fica clara pelos rótulos.
- **20,8–21,9s / prova vira painel:** fotografia faz pequena rotação/fecha, suporte escuro atravessa e amplia para painel. Máscaras retiram os textos antigos no mesmo avanço do novo. Não vi vazamento persistente nem um número de alcance aparecendo depois do título. Antecipar ícones é opcional, conforme descrito.
- **21–24s / relevância:** painel com Mensagem + Público tem ícones e ligação animados; é uma composição diferente da prova e da produção, mantendo paleta. Título `Cada empresa. Uma estratégia.` é uma formulação geral, não promessa de resultado.
- **24–30s / CTA:** concordância correta na substituição: `E a sua empresa?` → `E o seu serviço?`. Convite `Conversa com a gente.` próximo e natural. Contorno do botão e seta se resolvem antes da sustentação. Últimos≈3s são estáveis para leitura/assinatura; não há longas repetições de material original. O centro do botão fica nítido, com contraste e espaço interno suficientes.

## Relação concreta com as referências

As técnicas observadas foram adaptadas em conteúdo próprio: etiqueta com cópias em profundidade (Oto14,7–15,45s), objeto e texto em planos (Oto0,7–1,15s/6,8–8,85s), troca com foco seletivo, suporte de mídia revelado, documento em perspectiva (Oto11,15–11,7s), composição assimétrica com seta (Oto21,4–22,45s), CTA com contorno (Oto20,45–21,1s). Não vi reprodução de reciboPix, preço, vendas, mapaBrasil, conversa, símbolo ou cores de marca da referência.

A densidade continua moderada, com pausas nítidas para leitura. Isso está alinhado ao pedido clean/profissional e se diferencia do excesso de objetos. Não seria preciso adicionar efeitos aleatórios para demonstrar densidade. O ajuste da pausa azul é mais útil do que adicionar outro ícone.

## Limites

Esta é uma revisão visual amostrada do arquivo real, com abertura e passagens mais densamente inspecionadas; não equivale a reprodução contínua em tempo real nem a escuta. Não aprova naturalidade de locução ou mixagem percebida. O parecer é específico ao SHA acima; correções exigem conferir os trechos no novoMP4 e atualizar o vínculo do relatório.
