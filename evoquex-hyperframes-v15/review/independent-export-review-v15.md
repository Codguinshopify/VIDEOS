# Revisão independente do MP4 V15 — candidato final corrigido

**Veredito: a falha identificada foi corrigida no novo MP4; nenhum bloqueio visual permanece nas janelas e amostras examinadas nesta revisão.**

- Arquivo atual: `renders/evoquex-hyperframes-v15.mp4`.
- SHA-256 atual: `b49533215c68181ad225d74de8aa58de6e4ee496e5a330bdec9d62caa1724e1d`.
- Bundle atual: `c2968c97deb6c129d7c87d098da4c27f10e080d6bf28817a98b2e4cfe49138d6`.
- Formato conferido pelo relatório atual: 1080 × 1920, 30 fps, 27,6 s, 828 quadros; 9,923,897 bytes.

## Revisão da substituição

Foram abertas as cinco novas folhas do MP4 corrigido: `review/v15-b49533215c68/critical-04-01.jpg`, `critical-04-02.jpg`, `full-01.jpg`, `full-02.jpg` e `full-03.jpg`. Elas contêm todos os 42 quadros consecutivos da passagem de distribuição para localização (12,467–13,833 s) e 57 amostras da duração inteira até o quadro 827.

A correção está confirmada: Clevelândia permanece oculta até o quadro 400 (13,333 s), começa sua entrada somente no quadro 401 (13,367 s), avança em opacidade/posição e assenta sem o estado anterior de “aparece → esconde → entra”. Só para também entra durante a revelação sem aparição antecipada. O pino conserva o furo, preenchimento e contorno limpo. Os contatos de duração completa mantêm as nove cenas coerentes, Danny’s Presentes corretamente identificada, a métrica completa e correta, ambos os rótulos da estratégia na tela e o encerramento estável.

O novo `review/output-validation-v15.json` corresponde exatamente ao hash e bundle acima: decodificação integral aprovada, áudio AAC estéreo a 48 kHz, loudness −16,22 LUFS, true peak −1,55 dBTP e zero amostras clipadas. A limitação permanece: não houve reprodução audiovisual contínua nem escuta subjetiva. Nesta rodada a inspeção independente repetiu a janela afetada e as amostras de toda a duração; a inspeção densa das outras passagens abaixo pertence ao candidato anterior e está preservada como histórico, sem falsamente reatribuir esses arquivos ao novo hash.

Nenhum arquivo de runtime/recurso foi alterado por esta revisão. O único arquivo escrito por este agente foi este relatório.

---

# Histórico — candidato anterior corrigido

Candidato examinado em 19/10/2026: `renders/evoquex-hyperframes-v15.mp4`, posteriormente preservado em `review/candidate-e69aa4b4fdcb.mp4`. **Candidato substituído; não é a entrega final.** A execução principal aplicou a correção descrita e iniciou novo render com bundle `c2968c97deb6c129d7c87d098da4c27f10e080d6bf28817a98b2e4cfe49138d6`; a verificação desse novo MP4 está registrada no início deste documento.

- SHA-256 do MP4: `e69aa4b4fdcb99395b2707bbca27c59dd67cba64f50347eeb1684a8b630913bc`.
- Bundle congelado: `014ead5abeff35217566d3aaab8de48a8ed9f8bffa2e49982aad432e1233b9d5`.
- 1080 × 1920, 30 fps, 27,6 s, 828 quadros; 9.943.398 bytes.
- Veredito deste candidato: **corrigir a aparição antecipada de Clevelândia na passagem para localização antes da entrega**. O restante da inspeção descrita abaixo não encontrou outra falha visual impeditiva. Este parecer não valida um MP4 de outro hash.

## Método efetivamente realizado

Leitura das instruções raiz e locais, `DESIGN.md`, `STORYBOARD.md`, `resources/reference-study-v15.md`, biblioteca/README e skill local `motion-quality-control`. A consulta nova às referências originais já estava registrada pela execução principal; esta revisão independente não reivindica uma segunda consulta aos originais.

Foram abertas e examinadas todas as 30 folhas listadas em `review/v15-e69aa4b4fdcb/sampling.json`: 57 amostras a 2 fps incluindo o último quadro, os 120 quadros consecutivos da abertura, oito janelas de transição de 42 quadros cada e seis janelas de limite de mídia de nove quadros cada. Foram também abertas as nove imagens de telefone (360 × 640), os quadros 510 e 514–528 para a entrada completa do complemento da métrica, e os quadros 783, 789, 795, 801, 807, 813, 819, 825 e 827 para o encerramento.

As imagens são extrações do MP4 real, não capturas de preview HTML. As folhas têm miniaturas de 216 × 384; as imagens de telefone ampliam a avaliação da leitura. Não houve playback audiovisual contínuo nem escuta subjetiva. A validação técnica de áudio abaixo é leitura do relatório produzido pela execução principal, não aprovação por audição.

## Correção necessária

**13,133–13,433 s, quadros 394–403: o nome Clevelândia aparece antes de sua entrada e depois reinicia.** Em `critical-04-01.jpg`, Clevelândia já é azul, legível e praticamente assentada nos quadros 394–397. Em `critical-04-02.jpg`, mantém esse estado até o quadro 400, desaparece/quase desaparece no 401 e retorna escura e deslocada nos 402–403 antes de concluir a entrada. É uma descontinuidade perceptível na sequência consecutiva e corresponde ao padrão “aparece → esconde → entra”.

Diagnóstico de apoio em fonte, sem edição nesta revisão: `motion.js` agenda `V.enter('#clevelandia', 13.34)` e `V.enter('#so-para', 13.1)`; o seletor de estados inicialmente ocultos em `style.css` não inclui esses dois IDs. A correção sugerida é definir seus estados inativos antes do reveal da cena, congelar novo bundle, renderizar novamente e conferir os quadros da mesma passagem. Não basta aprovar o estado estável em 13,7 s.

## Observações por trecho

| Trecho | Observação no MP4 |
|---|---|
| 0–4 s | Texto já composto no quadro zero e linha em avanço nos primeiros quadros. Trocas de câmera/tipografia legíveis após o movimento. O arco coral permanece abaixo de VISTA?; não cruza a palavra. A íris clara entra somente no handoff final. |
| 4–6,74 s | A foto aérea cresce a partir de recorte horizontal e permanece reconhecível; não há alegação visual de filmagem aérea. A foto tem peso útil no quadro e texto livre. |
| 6,74–7,85 s | A tinta real é visível, cobre progressivamente a cidade e prepara o campo quente. Não há flash do vídeo em tela cheia nem quadro inteiramente vazio. Há, porém, um suporte pêssego sem filmagem aproximadamente em 6,867–7,167 s (quadros 206–215), durante a passagem e antes da revelação vertical da filmagem; isso deve ser descrito como estado intermediário de suporte, não como “nenhum painel vazio”. A filmagem abre a partir de 7,20 s e a identificação entra em seguida. |
| 7,85–10,3 s | Danny’s Presentes está correta, separada da moldura e legível em telefone. A pessoa e a loja aparecem no vídeo vertical. A transição interna para produtos por volta de 9,6–9,73 s é contínua, com blur do material, e a saída para azul cobre o vídeo antes do fim da mídia. Nenhum salto para poster/placa escura no fim. |
| 10–13 s | Letras Evoquex recompõem sem quadro vazio, incluindo 10,60–10,63 s. O acento de dots aparece no campo azul e sai sem corte preto. O ator passa brevemente sobre as últimas letras de Evoquex por volta de 11,433–11,467 s; são cerca de dois quadros, com leitura longa antes/depois, e não foi tratado como impeditivo. |
| 13–16 s | O pino resolve com silhouette lisa, furo central, preenchimento contínuo e contato no chão; esses reparos estão confirmados no MP4. A entrada do texto Clevelândia apresenta o defeito descrito acima. Após aproximadamente 13,5 s, o estado estável é limpo. |
| 15,72–16,85 s | Flare real acompanha a expansão do pino; não há poster inesperado nem flash de preto em seu início/fim. O campo azul do ator cobre o quadro por dois quadros antes de entregar o campo lima; é parte da transição, não falha de mídia. As fatias do 20 ficam visíveis durante sua recomposição e desaparecem no estado sólido a partir de 16,7 s. |
| 16,85–19,6 s | A métrica lê “20 MIL VISUALIZAÇÕES DE PESSOAS DE CLEVELÂNDIA”, com complemento já legível por volta de 17,3 s e leitura completa sustentada até a próxima expansão por volta de 19,5 s. Não há linha de emenda persistente no número, contador, gráfico inventado nem troca da unidade por alcance/impressões. A procedência do dado é a declaração do usuário. |
| 19,6–22,8 s | Título e ícones entram em estágios, a linha conecta mensagem e público; ambos os rótulos estão dentro da tela e legíveis, inclusive em telefone. A palavra estratégia mantém margem direita. |
| 22,8–25,1 s | CTA limpa, com hierarquia clara e curva abaixo da palavra gente. A entrada por máscara mantém conteúdo anterior/seguinte nos estados de passagem examinados. |
| 25,1–27,6 s | Passagem lateral para a marca contínua, incluindo os quadros 760–761 que cercam 25,352 s. Evoquex resolve antes de 26,1 s; os nove quadros inspecionados de 26,1 s até o último mostram o mesmo fechamento. As estatísticas dos últimos 45 quadros têm mudança média global máxima de 0,144/255, coerente com hold estável e pequenas variações de codificação/textura. |

## Evidência técnica consultada

`review/output-validation-v15.json` registra o mesmo hash, bundle e dimensões, decodificação integral aprovada, H.264/yuv420p/BT.709 e áudio AAC estéreo a 48 kHz. Loudness integrado −16,22 LUFS, true peak −1,55 dBTP, zero amostras decodificadas clipadas e correlação 0,99969 com o mix de entrada. Não há narração nesta etapa; a revisão não gerou nem configurou voz. `frame-statistics.json` não contém candidatos quase uniformes, mas essa estatística sozinha não prova ausência de falhas visuais.

## Arquivos de imagem efetivamente inspecionados

Todos os caminhos abaixo têm prefixo `review/v15-e69aa4b4fdcb/`:

- `full-01.jpg`, `full-02.jpg`, `full-03.jpg`.
- `opening-01.jpg`, `opening-02.jpg`, `opening-03.jpg`, `opening-04.jpg`, `opening-05.jpg`.
- `critical-01-01.jpg`, `critical-01-02.jpg`; `critical-02-01.jpg`, `critical-02-02.jpg`; `critical-03-01.jpg`, `critical-03-02.jpg`; `critical-04-01.jpg`, `critical-04-02.jpg`.
- `critical-05-01.jpg`, `critical-05-02.jpg`; `critical-06-01.jpg`, `critical-06-02.jpg`; `critical-07-01.jpg`, `critical-07-02.jpg`; `critical-08-01.jpg`, `critical-08-02.jpg`.
- `critical-09-01.jpg`, `critical-10-01.jpg`, `critical-11-01.jpg`, `critical-12-01.jpg`, `critical-13-01.jpg`, `critical-14-01.jpg`.
- `phone-hook.png`, `phone-local.png`, `phone-production.png`, `phone-distribution.png`, `phone-target.png`, `phone-proof.png`, `phone-strategy.png`, `phone-cta.png`, `phone-brand.png`.
- `all-frames/frame-0510.png`, todos `all-frames/frame-0514.png` a `frame-0528.png`, `all-frames/frame-0783.png`, `frame-0789.png`, `frame-0795.png`, `frame-0801.png`, `frame-0807.png`, `frame-0813.png`, `frame-0819.png`, `frame-0825.png`, `frame-0827.png`.

Nenhum arquivo de composição, recurso ou runtime foi alterado por esta revisão.
