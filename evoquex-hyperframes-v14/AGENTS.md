# Evoquex V14 — instruções da composição

Leia `../AGENTS.md`, `../.agents/agents/md.md`, `../biblioteca/README.md`,
`resources/briefing-v14.txt`, `resources/case-facts-v14.json`,
`resources/scene-timing-v14.json`, `DESIGN.md`, `STORYBOARD.md` e
`REFERENCE-IMPLEMENTATION.md`. O briefing V14 prevalece sobre restrições históricas
da V13 quando houver conflito. Não modificar versões anteriores para alinhar fatos.

## Referências permanentes e pesquisa

Antes de cada produção ou revisão, abrir novamente os MP4 reais de Park/Shard Cloud,
Park/Virgílio e OtoCriativo, nos caminhos permanentes e hashes registrados em
`../biblioteca/referencias/catalogo.json`. Examinar toda a duração e movimentos
críticos; uma análise antiga, memória ou catálogo não substitui essa consulta. A
quarta referência, Park/Weven, continua preservada como estudo adicional. Não
reutilizar música, voz, imagens, marcas ou alegações das referências na campanha.

Registrar internamente arquivo, hash, método de análise e técnicas escolhidas.
Se não houver playback/escuta disponíveis, usar decodificação e sequências de frames
sem afirmar audição ou reprodução em tempo real. Nunca declarar aberto um arquivo
ausente. Não alterar ou remover os originais da biblioteca.

Consultar as cinco skills locais pertinentes e a documentação do motor disponível.
Auditar recursos atuais, catálogos, exemplos e branches de packs; não presumir que
o acervo é igual ao da V13. Usar mecanismos compatíveis que contribuam para a peça,
conservando fontes e licenças. AEP, MOGRT e plugins Adobe não executam diretamente
em HyperFrames. Um recurso só conta como implementado após confirmação no render.

## Direção e implementação

HyperFrames 0.8.162 e GSAP 3.14.2 são o motor principal. O alvo atual é **26 s,
780 frames, 1080 × 1920, 30 fps**, conforme `scene-timing-v14.json`. Registrar um
único timeline raiz pausado `evoquex-hf-v14`, usar mídia local e animações
determinísticas. O tempo final deve ser validado no MP4; a documentação não o prova.

O hook de 0–4 s é benchmark e **pode melhorar**. Preservar sua ideia, contraste,
fundo escuro, branco, azul `#54A6FF` e vermelho `#F87171`. Não exigir igualdade de
pixels ou áudio com a V13. Reconstruir substancialmente o pós-hook, ligando frases
por atores, máscaras, transformações, câmera e mudança de hierarquia. Evitar cartelas,
mockups repetidos, marca-d’água e a mesma entrada/fade/zoom como solução dominante.

Preservar mensagens e estrutura narrativa; só ajustar texto minimamente quando
indispensável ao ritmo, à leitura ou à transição. A filmagem real da Danny’s Presentes
é breve, integrada a recortes, com áudio zerado; o plano atual prevê 6,9–9,46 s (2,56 segundos).
Não manter Evoquex ou Clevelândia como marca-d’água após cinco segundos. Fotos com
baixa resolução não devem sugerir detalhe inexistente. Uma mensagem domina cada estado.

## Fatos, música e voz

Usar a grafia **Danny’s Presentes**. Evoquex produziu o vídeo; a campanha foi
direcionada somente a Clevelândia. O dado ativo, **“20 mil visualizações de pessoas
de Clevelândia”**, é uma declaração explícita do usuário no briefing V14, sem
verificação documental independente. Não transformar visualizações em alcance,
impressões, pessoas únicas, vendas, clientes ou ROI. Não usar a captura de 20.981
impressões/13.064 de alcance como prova das novas visualizações, nem fabricar evidência.
Ir além dos seguidores continua sendo objetivo, não resultado quantificado comprovado.

A música deve ser uma composição nova ou reconstrução substancial, pois a trilha
anterior foi rejeitada. Os materiais musicais novos estão em produção em
`resources/audio/`; a saída é `assets/mix-v14.wav`. Conferir procedência, licença,
duração e sincronização do arquivo realmente integrado, com variações e pausas
intencionais. Não copiar áudio das referências nem preservar o loop antigo por padrão.

Locução feminina natural permanece pendente. Não reutilizar Kokoro, não simular voz
humana, não comprar ou alterar plano e não apontar para arquivo inexistente. Verificar
ferramentas e autenticação sem divulgar credenciais antes de eventual geração. Luciane
permanece desativada, sem cena ou dado fictício.

## QA e entrega

Executar os checks e render V14; inspecionar o MP4 real, não só fonte ou timeline.
Revisar abertura quadro a quadro, sequências consecutivas das transições, texto,
marca, métrica ativa, hierarquia, movimento ao longo de toda a duração e áudio.
Separar validação técnica, leitura de frames, playback e escuta. Ausência de erros
do compilador, contagem de tweens ou fluxo óptico não prova qualidade criativa.

A aprovação técnica e visual por sequências desta entrega está registrada em
`review/final-approval-v14.json`. Não herdar essa aprovação para outra versão. Vincular
cada revisão ao MP4 efetivo e corrigir problemas antes de concluir. Não editar as
fontes durante um render ativo. Encerrar o preview gerenciado ao entregar.

**Entrega V14: somente o MP4 final**, pronto para assistir. Não enviar relatório,
inventário, comparativo, resumo das mudanças, código ou lista de skills. Fontes e QA
permanecem internos. Se houver bloqueio real, comunicar apenas o impedimento específico.
As escolhas criativas estão autorizadas; não pedir aprovação para cada técnica.
Preferir link GitHub direto `/raw/refs/heads/.../entrega/...mp4`.
