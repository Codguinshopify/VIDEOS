# Revisão do export V15R1

Arquivo inspecionado: `renders/evoquex-hyperframes-v15-revisado.mp4`, SHA-256
`88bd145d5f8d1a0737db24da200c3866c644e5b20ade38549e83944314d7409f`.
Os 702 quadros do MP4 foram decodificados; a abertura foi extraída em todos os
quadros e as oito transições em janelas consecutivas. Também foram examinadas
amostras de todo o vídeo a cada meio segundo e um quadro em tamanho de telefone
de cada cena. Nenhum quadro vazio ou uniformemente preto/branco foi encontrado.

A abertura já tem composição gráfica no primeiro quadro: tipografia em rig,
linha que cresce, substituição de palavras, cor coral e pergunta concluída antes
da passagem à cidade. A imagem real de Clevelândia se revela no espaço aberto
pelo texto; a máscara orgânica e a textura Brush 2 levam à filmagem da Danny’s
Presentes. Na etapa azul, a borda do filme entrega uma rota e a seta muda para
um pino. O contato do pino abre por círculo o campo verde do dado. O número e seu
qualificador ficam legíveis antes da composição de estratégia; a curva liga
mensagem e público e conduz à chamada. As mudanças são perceptíveis ao longo do
filme, com pausa de leitura deliberada sobre “20 MIL”. A grafia de Danny’s
Presentes está correta nos elementos de texto da composição.

A inspeção dos quadros confirma que o atlas de tinta, o Brush 2, o light burn e
o flare entram nos trechos planejados. Os assets originais continuam preservados
e a referência visual não foi incorporada. O único dado de campanha exibido é
“20 mil visualizações de pessoas de Clevelândia”; ele é a declaração fornecida
pelo usuário e não é tratado como alcance único, vendas ou retorno financeiro.

O MP4 passou na decodificação integral, tem 1080×1920, 30 fps, 23,4 s e uma
faixa AAC estéreo. O áudio codificado mantém correlação alta com o mix de origem,
mede −16,12 LUFS e −2,47 dBTP, sem amostras clipadas. A trilha ocupa todo o
intervalo, com fade final; há sete fontes distintas de efeitos em 17 cues. Não
existe narração nesta etapa. Foi feita verificação técnica de som, **não escuta
subjetiva**; naturalidade e adequação perceptiva devem ser confirmadas na futura
integração da locução e na revisão do cliente.

O lint e a checagem focada da abertura do HyperFrames passaram. As checagens
focadas posteriores executaram o runtime sem erro, mas o verificador de layout
também contou camadas antigas, já ocultas por máscaras, e apontou baixo contraste
e uma sobreposição nesses elementos. O frame real em 14,694 s foi inspecionado:
somente o resultado verde aparece, sem a camada “Danny’s Presentes” indicada
pela advertência. A checagem automática de toda a timeline atingiu seu limite
interno de tempo. A validação do MP4 e das janelas consecutivas é a evidência
direta usada para a decisão de entrega.
