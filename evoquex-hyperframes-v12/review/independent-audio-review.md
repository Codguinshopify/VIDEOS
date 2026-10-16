# Revisão independente do áudio codificado — V12

Arquivo examinado: `renders/evoquex-hyperframes-v12.mp4`.

SHA-256 do MP4 final, confirmado por nova leitura dos bytes: `928b0b271c5144169af4dfe378935af5f8b4ca1b45fa4865bb63b7b1fd2b3361`.

Tamanho do arquivo final: **11.100.580 bytes**. Esta revisão está vinculada à renderização definitiva, substituindo o vínculo anterior da prévia. O WAV permaneceu inalterado.

O SHA e o tamanho coincidem com `review/output-validation.json` atualizado; portanto, os resultados de decodificação completa, loudness, pico e correlação daquele relatório se aplicam ao MP4 final. Conferi novamente os valores: correlação 0,999323873268422, loudness −16,12 LUFS, true peak −1,66 dBTP e zero amostras com clipping. Não repeti a mesma decodificação nem o mesmo processamento de loudness. Li também o validador que produziu o relatório: ele compara PCM decodificado do MP4 e do WAV no mesmo início temporal, sem procurar um deslocamento que melhorasse artificialmente a correlação.

O SHA do WAV também foi confirmado contra `resources/audio/provenance-v12.json`: `cde124ba505d0fe60ab30f239ccf510c2f452e012b59c551419ca9009cd6fdb7`.

## Resultado técnico

| Verificação | Resultado no MP4 |
|---|---|
| Duração do arquivo | 30,000 s |
| Áudio | AAC, estéreo, 48 kHz |
| Decodificação completa | Passou, sem erro fatal |
| Loudness integrado | −16,12 LUFS |
| True peak | −1,66 dBTP |
| Faixa de loudness | 2,20 LU |
| Amostras decodificadas com módulo ≥ 1 | 0 |
| Correlação PCM com o WAV, sem deslocamento aplicado | 0,9993238733 |
| Voz nova | Ausente |
| Áudio original do filme | Mutado no HTML |

O WAV original mede −16,09 LUFS e −1,79 dBTP. A codificação AAC aumentou o true peak em aproximadamente 0,13 dB e alterou o loudness em −0,03 LU. O MP4 continua abaixo de zero, sem clipping. O pico codificado fica 0,14 dB acima do alvo editorial nominal de −1,8 dBTP; isso está registrado, e não foi feita uma remasterização que divergisse dos assets já renderizados. Não é um arquivo com limite de entrega contratual de −1,8 dBTP comprovado no AAC; para um limite estrito seria preciso reduzir a margem no WAV e renderizar novamente.

## Sincronização com a animação efetivamente implementada

Comparei os tempos de `motion.js` com os eventos de `resources/audio/provenance-v12.json`. Para evitar usar apenas o nome do evento, reconstruí os mesmos recortes de efeitos a partir do PCM fonte, com a taxa, reversão e envelope registrados, e medi o centro da janela de 10 ms com maior energia RMS. Isso localiza a ênfase real do efeito isolado; não é uma afirmação de julgamento auditivo.

| Movimento real no código | Áudio real / ênfase medida | Avaliação de timing |
|---|---|---|
| Título articulado desde 0,000 s | Impacto 0,000–0,242 s; maior energia em 0,012 s | Energia já no primeiro quadro; sem introdução sonora vazia |
| Troca de palavra iniciada em 0,760–0,800 s | Sweep 0,700–0,867 s; maior energia em 0,781 s | Movimento e ênfase coincidem |
| Deslocamento vertical 1,630–2,040 s | Sweep 1,530–1,737 s; maior energia em 1,629 s | Acentua o disparo da transição |
| Letras de “VISTA?” iniciadas em 2,650 s | Impacto 2,650–3,004 s; maior energia em 2,659 s | Acompanha a entrada das letras |
| Iris 3,820–4,470 s | Sweep reverso 3,680–3,953 s; maior energia em 3,821 s | Coincidência praticamente exata com a abertura da iris |
| Seta local desenhada em 5,750–6,400 s | Tick em 5,800 s; maior energia em 5,806 s | Acento durante o início do traçado |
| Whip 7,750–8,300 s e filme revelado a partir de 8,100 s | Sweep 7,530–7,830 s, maior energia em 7,681 s; impacto com maior energia em 8,108 s | O sweep antecipa o whip por cerca de 69 ms, seguido do impacto no reveal do filme |
| Troca de plano iniciada em 10,450 s | Sweep 10,270–10,484 s, maior energia em 10,372 s | Preparação curta, cerca de 78 ms antes da mudança |
| Rail de processo muda a partir de 12,780 s | Tick em 12,800 s, maior energia em 12,806 s | Acento no início da mudança |
| Shutter fecha em 14,620–15,170 s; conteúdo troca em 15,120 s; reabre em 15,170–15,680 s | Sweep reverso 14,750–14,926 s, maior energia em 14,843 s | Acompanha o fechamento e antecipa a troca oculta; não foi colocado equivocadamente depois da transição |
| Contador de impressões 15,300–15,900 s | Impacto 15,350–15,640 s, maior energia em 15,358 s | Marca a entrada do contador, não a chegada ao valor final |
| Rail das métricas muda em 18,050–18,530 s; contador de alcance 18,200–18,800 s | Impacto 18,200–18,415 s, maior energia em 18,211 s | Marca a entrada do alcance durante a mudança do rail |
| Área do convite cresce a partir de 20,820 s; frame muda em 20,860–21,610 s | Sweep 20,680–20,980 s, maior energia em 20,829 s | Ênfase no início da transformação |
| Pergunta em foco a partir de 23,400 s | Tick em 23,400 s, maior energia em 23,406 s | Coincide com a nova ênfase tipográfica |
| CTA expande em 25,350–26,000 s; texto entra 25,750–26,150 s | Sweep reverso 25,290–25,623 s, maior energia em 25,462 s; impacto com maior energia em 25,509 s | Ambos acompanham a expansão, antes do texto terminar de entrar |
| Seta desloca em 28,050–28,810 s | Sweep 28,000–28,167 s, maior energia em 28,081 s | Acompanha o primeiro deslocamento da seta |

Existem 18 eventos de efeitos, distribuídos em 30 segundos, sem som em cada letra. Os dois eventos de 25,5 s são camadas intencionais de uma única expansão, não dois impactos em cenas diferentes.

## Achados e limites

- Os nomes descritivos dos eventos de métricas no arquivo de proveniência usam “settles”. O código e o áudio demonstram **ênfase de entrada**: os valores terminam de contar em 15,9 s e 18,8 s, enquanto os impactos ocorrem em 15,35 s e 18,2 s. A revisão registra a diferença sem presumir que o impacto marca a conclusão. Não alterei o arquivo de proveniência nem o mix.
- A correlação alta sem deslocamento aplicado confirma que o MP4 preserva o novo mix e seus pontos de início, dentro das mudanças esperadas da compressão AAC. Não substitui uma avaliação por audição de percepção, equilíbrio subjetivo ou caráter dos efeitos.
- A trilha e os efeitos são reais e rastreáveis aos stems preservados. Não há nova narração, áudio das referências ou reuso da voz rejeitada. Portanto, não há validação de naturalidade de voz ou inteligibilidade de locução a declarar.
- A sincronização acima compara os tempos da animação que gerou a renderização com os efeitos registrados e com o mix de alta correlação. A revisão visual dos quadros exportados pertence à verificação visual do projeto; este documento não apresenta uma escuta audiovisual subjetiva que a interface não permite.
- Não alterei assets, fontes, código visual ou mix durante esta revisão.
