# V13 — atualização das competências reutilizáveis

## Leitura e escopo

O briefing completo foi lido de
`/workspace/attachments/ac4d04ba-add9-4f36-b6c9-29b97d7f4dc5/Texto colado.txt`,
incluindo as regras de preservação do hook, roteiro fixo, auditoria Git, execução,
revisão em movimento e relatório final.

Antes de criar a skill, foram lidos os quatro `SKILL.md` locais existentes,
`AGENTS.md` da raiz e `biblioteca/README.md`. As skills anteriores já cobrem análise
de referências, pesquisa/compatibilidade de packs, criação de assets por IA e QA
visual/sonoro/factual. Criar doze arquivos repetidos não acrescentaria operações.

## Arquivos alterados nesta tarefa

- `.agents/skills/motion-direction/SKILL.md`: nova skill operacional com storyboard,
  decisões de hierarquia e tipografia cinética, passagem por objeto compartilhado,
  máscaras, profundidade, ritmo, sincronização e exemplos GSAP determinísticos.
- `.agents/skills/motion-quality-control/SKILL.md`: ampliação das regras de hook e
  texto protegido; comparação automatizada dos 120 frames iniciais; distinção entre
  igualdade lossless e compressão H.264; sequências consecutivas, trajetórias e
  verificação de sound cues; limites honestos de playback e escuta.
- `AGENTS.md`: somente apêndice V13. Os parágrafos anteriores foram preservados.
- Este registro de auditoria.

Nenhuma composição V12/V13, fonte visual, mídia ou render foi alterado por esta tarefa.
Não foi afirmada execução de QA, reprodução do vídeo ou audição apenas por escrever
as instruções. A implementação e a validação do vídeo pertencem ao fluxo principal.

## Cobertura das doze competências sem duplicação

| Competência solicitada | Recurso operacional responsável |
| --- | --- |
| Análise técnica das referências | `reference-analysis` |
| Storyboard e direção visual | `motion-direction` |
| Tipografia cinética avançada | `motion-direction`, com documentação GSAP instalada |
| Transições | `motion-direction` e exemplos reais do catálogo |
| Composição, profundidade e parallax | `motion-direction` |
| Compatibilidade de bibliotecas e packs | `asset-library-research` |
| Assets por IA | `ai-visual-asset-design` |
| Som e sincronização | Storyboard/cues de `motion-direction` e validação de `motion-quality-control` |
| Implementação HyperFrames | `motion-direction`, código/exemplos e documentação da versão instalada; skills do motor quando acessíveis |
| Qualidade do render | `motion-quality-control` |
| Métricas e prova visual | `motion-quality-control` |
| Ritmo, continuidade e diversidade | `motion-direction` e inspeção em movimento de `motion-quality-control` |

## Decisões verificáveis

O hook V13 é o intervalo `[0,4)` da base aprovada. A 30 fps, isso corresponde aos
frames 0–119. O procedimento exige comparar todos eles e revisar a emenda separadamente.
Métricas perceptuais do MP4 não serão chamadas de igualdade de pixels. Texto invariável
inclui setters e palavras ocultas que entram depois; mover elementos não autoriza
reescrever o roteiro. No restante, os critérios observam gesto, hierarquia e continuidade;
quantidade de tweens ou movimento de grão não demonstram acabamento profissional.

As skills ficam em `.agents/skills/<nome>/SKILL.md` e devem ser lidas diretamente
quando aplicáveis. A sessão informou que não há cloud skills disponíveis no momento;
não houve registro nem teste de descoberta automática. Documentação e exemplos locais
continuam sendo fontes verificáveis, sem presumir acesso a serviços indisponíveis.

As quatro skills anteriores foram reaproveitadas; só `motion-quality-control` foi
ampliada. As outras três permanecem intactas. Não foi acrescentada aprovação extra
para ações já autorizadas pelo briefing.
