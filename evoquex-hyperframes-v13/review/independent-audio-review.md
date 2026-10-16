# Revisão independente do áudio final — V13

Arquivo: `renders/evoquex-hyperframes-v13.mp4` (**11.388.859 bytes**, 30,000 s).

SHA-256 conferido nos bytes reais: `548a550705c835551b4ab2817acec0d92862eb79fee40b6299a18c54c6a81ef2`. Coincide com `review/output-validation.json`; foram aproveitados os testes completos desse arquivo final, sem repetir desnecessariamente a decodificação e o loudness.

| Verificação | Resultado no MP4 final |
|---|---|
| Codec / canais / taxa | AAC / estéreo / 48 kHz |
| Início e duração do stream de áudio | 0,000 s / 30,000 s |
| Decodificação completa | Passou |
| Loudness integrado | −16,25 LUFS |
| True peak | −1,74 dBTP |
| Faixa de loudness | 2,10 LU |
| Clipping PCM decodificado | 0 amostras |
| Correlação PCM com o WAV, sem deslocamento aplicado | 0,9993028085 |
| Locução | Ausente |
| Fala/ambiente do vídeo original | Mutado no HTML |

O true peak final atende ao limite desta etapa de ≤ −1,5 dBTP. O WAV-fonte mede −16,21 LUFS e −1,79 dBTP; o AAC mede −16,25 LUFS e −1,74 dBTP. A compressão não introduziu clipping. A trilha é `assets/mix-v13.wav`, com início em 0 e duração de 30 s no HTML, e seu SHA coincide com o validador e a proveniência.

## Hook preservado e limites da compressão

Li os primeiros 192.000 frames estéreo dos WAVs V12 e V13 e confirmei igualdade literal: 768.000 bytes PCM, SHA `50d3a486fcc2f64bde3ff7c62e3c35e233a8ddf594bbbf8e537ab4a72514fd09`. Nenhum frame fonte anterior a 4,000 s foi modificado. O crossfade começa em 4,000 s e termina em 4,064 s, conforme a proveniência.

Decodifiquei adicionalmente somente os primeiros 4 s do MP4 para verificar a transferência desse prefixo ao arquivo final. Correlação com o PCM do WAV: **0,9990667012**. O PCM decodificado do AAC não é igual ao PCM original, como esperado em compressão com perdas. **Não há alegação de identidade de bits entre o AAC da V13 e o vídeo V12**, nem de identidade de bits entre AAC e WAV.

## Os 24 acentos e a timeline final

Conferi `motion.js` e o helper de três fatias em `vendor/evoquex-v13-motion.js`. Reconstruí os recortes reais registrados na proveniência e medi o centro da janela de 10 ms com maior energia RMS após taxa/reversão/envelope. A coluna de ênfase é uma medição do efeito-fonte isolado, não uma afirmação de percepção auditiva nem uma extração perfeita do efeito do mix AAC.

| Acento | Ênfase RMS | Movimento efetivo | Janela visual |
|---|---|---|---|
| 1 · impact @0.00 s | 0.012 s | Hook articulado desde o primeiro frame | 0.000–0.900 s |
| 2 · sweep @0.80 s | 0.781 s | Título recua e etiqueta ocupa seu plano | 0.760–1.220 s |
| 3 · sweep @1.65 s | 1.629 s | Troca vertical para a localidade | 1.630–2.040 s |
| 4 · impact @2.65 s | 2.659 s | Letras de VISTA? e cantos de enquadramento | 2.650–3.250 s |
| 5 · sweep @3.85 s | 3.821 s | Iris para a localidade real | 3.820–4.470 s |
| 6 · tick @4.05 s | 4.056 s | Já viu articulado em eixos opostos | 4.040–4.700 s |
| 7 · sweep @5.15 s | 5.145 s | Tipo vira abertura da imagem, city-open 5,15–5,83 s | 5.040–5.950 s |
| 8 · sweep @7.70 s | 7.701 s | Câmera vertical e contorno da mídia | 7.640–8.410 s |
| 9 · impact @8.10 s | 8.108 s | Vídeo real chega e sua janela se abre | 8.020–8.750 s |
| 10 · sweep @9.60 s | 9.603 s | Mídia avança, tipografia recua | 9.500–10.200 s |
| 11 · sweep @10.45 s | 10.455 s | Dobradiça da produção para distribuição | 10.350–11.100 s |
| 12 · tick @11.15 s | 11.156 s | Etiqueta Evoquex em três fatias | 10.930–11.540 s |
| 13 · sweep @12.75 s | 12.752 s | Clevelândia e janela horizontal da mesma mídia | 12.740–13.550 s |
| 14 · sweep @14.70 s | 14.701 s | Câmera e contorno conduzem à prova | 14.630–15.350 s |
| 15 · impact @15.65 s | 15.658 s | 20.981 se reúne em três fatias | 15.120–15.740 s |
| 16 · tick @16.30 s | 16.306 s | Seta documental desenhada junto à captura | 16.020–16.670 s |
| 17 · sweep @17.85 s | 17.848 s | Troca de direção das métricas e reposição do documento | 17.800–18.730 s |
| 18 · impact @18.45 s | 18.460 s | Dígitos e rótulo de 13.064 se recompõem | 17.980–18.730 s |
| 19 · sweep @20.85 s | 20.859 s | Câmera lateral e contorno para estratégia | 20.700–21.400 s |
| 20 · tick @22.25 s | 22.256 s | Linha Mensagem/Público e viajante percorrem a curva | 22.100–22.850 s |
| 21 · sweep @23.65 s | 23.655 s | Diagrama comprime; fronteira/CTA redistribui o espaço | 23.350–24.550 s |
| 22 · impact @25.35 s | 25.358 s | Conversa/com a gente em duas linhas articuladas | 25.050–25.980 s |
| 23 · sweep @26.40 s | 26.399 s | Empresa sai, serviço e concordância entram | 26.240–27.020 s |
| 24 · tick @28.40 s | 28.407 s | Último assentamento do campo de CTA | 28.140–28.540 s |

Os 24 acentos acompanham movimento visual efetivo: cinco no hook aprovado e 19 novos após 4 s. Em 23 eventos, o centro da janela RMS está dentro da janela visual; no sweep preservado de 1,65 s, antecede o movimento em apenas 1,021 ms, e sua janela de 10 ms sobrepõe o início visual. Isso equivale a menos de 0,04 frame em 30 fps. Não há som em cada letra. Os impactos numéricos 15,65/18,45 s agora acompanham o assentamento das fatias/grupos, em vez de depender dos contadores anteriores.

## Precisões e limites

- O tick de 16,3 s foi originalmente descrito no planejamento como abertura de painéis. No código final, os painéis entram em 15,2–16,05 s; o tick acompanha a seta documental desenhada em 16,02–16,67 s. É uma associação com o ponteiro, não com o começo da abertura dos painéis.
- O tick de 28,4 s coincide com o assentamento final do campo de CTA em 28,14–28,54 s. A assinatura e a seta já completaram seu desenho; não foi tratado como início desses elementos.
- O sweep de 26,4 s acompanha a saída de “empresa” e o ponto de troca; “serviço” começa em 26,48 s. A nova frase não está assentada nesse momento.
- Os sons provêm dos stems reais já preservados e licenciados, sem áudio das referências, voz nova ou reuso da voz rejeitada. A licença e as qualificações do autor continuam disponíveis no projeto.
- **Não houve escuta subjetiva nem reprodução audiovisual contínua nesta interface.** Os resultados são checagens técnicas de sinal, código e temporização. Não comprovam naturalidade de voz, pois não há locução, nem substituem uma avaliação auditiva de gosto, equilíbrio percebido e impacto.
- Somente estes relatórios foram escritos nesta revisão; mídia, fontes e HTML permaneceram inalterados.

Detalhes verificáveis por evento, hashes e método: `review/audio-cue-validation-v13.json`.
