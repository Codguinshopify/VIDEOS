# V11 — roteiro e tempos de inserção de voz

Texto-base preservado e simplificado; NÃO há locução gerada. Tempos são janelas
editoriais estimadas, não alinhamento medido com áudio de voz.

| Janela | Narração preparada | Texto/ação principal |
|---|---|---|
| 0–4,5 | Para divulgar sua empresa ou serviço, começamos pela mensagem. | Como divulgar / sua empresa / seu serviço. Troca para Começamos / pela mensagem. Traço abre moldura. |
| 4,5–9,5 | Transformamos essa ideia em vídeo. Foi assim com a Danny’s Presentes. | A ideia vira vídeo. Material real, uma única reprodução; crédito Evoquex. |
| 9,5–14,5 | Depois, direcionamos o anúncio para o público de Clevelândia. | Canais, foto e Clevelândia. Só a cidade, sem mapa de cobertura inventado. |
| 14,5–21 | Os registros mostram quantas pessoas foram alcançadas e quantas vezes o anúncio foi exibido. | 13.064 pessoas, depois 20.981 exibições/impressões. Captura original. Voz não repete os números. |
| 21–27 | Para sua empresa ou serviço, duas escolhas: o que dizer e com quem falar. | Uma pergunta de cada vez, depois Mensagem + Público. |
| 27–33 | Quer fazer algo assim para a sua empresa? Conversa com a gente. | Convite e assinatura, espaço para leitura final. |

O número de palavras e a duração devem ser conferidos na leitura: a duração definitiva depende da leitura natural.
Ao receber voz real, medir e retimar as cenas antes de produzir a versão com locução.
Não acelerar áudio para fingir encaixe. `resources/voice-cues.json` registra pontos
semânticos e `scripts/prepare-voice.py` cria mix com ducking somente quando um arquivo
real for fornecido. O vídeo entregue nesta etapa usa trilha e efeitos, sem voz.
