# Avaliação do check nativo — V15

Ferramenta examinada: HyperFrames **0.8.162**, instalada neste projeto. Esta nota
interpreta os relatórios existentes; não modifica fontes nem executa novo check.

`hyperframes-check-preflight.json` e `hyperframes-check-final.json` terminaram com
`Check did not finish within its deadline`. O check completo **não foi concluído**:
seções vazias de layout, motion e contraste nesses relatórios não são aprovações.

Na implementação instalada, `check-IRETF27J.js` define `CHECK_DEADLINE_MS = 120000`.
A opção `--timeout` controla a prontidão inicial e a navegação; não aumenta esse
deadline global. Após as amostras de layout solicitadas, `collectGridSamples` chama
incondicionalmente `collectMotionOverlapSamples`. Essa etapa usa uma grade a 8 Hz
pela duração inteira, limitada a 600 pontos: cerca de 222 posições para 27,6 s.
Portanto, diminuir `--samples` ou desativar contraste não elimina essa varredura.
`--range início,fim` restringe sua duração, permitindo checks menores por trecho
sem modificar a composição nem o pacote instalado.

`hyperframes-check-focused.json` concluiu a sessão de navegador e informa:

- Lint: zero erros e avisos.
- Runtime: zero erros e avisos.
- Layout: 11 erros de `text_occluded`, três avisos de `content_overlap` e sete
  informações de `canvas_overflow`.
- Motion e contraste: desativados; não foram validados nesse comando.

Os 11 registros de oclusão em 13,7 s são `MAS É`, os caracteres de `VISTA?`,
`Produzimos`, `o vídeo.`, `Danny’s` e `Presentes`, todos pertencentes a cenas
anteriores cobertas pela cena opaca `#target-scene`. Essa conservação de cenas
anteriores sob a atual é intencional na composição. As sete informações de
overflow também se referem a textos antigos do hook já deslocados para fora.
Esses registros não justificam alterar a edição apenas para remover conteúdo que
já não aparece no quadro final.

Os avisos restantes apontam `#client-first`/`#client-last` contra uma letra de
`#brand-word` em **10,615 s**, e `#gente` contra uma letra de `#brand-signature` em
**25,352 s**. A classificação visual dessas duas emendas permanece **pendente de
inspeção dos quadros consecutivos do MP4 efetivamente renderizado**. A geometria do
DOM, isoladamente, não confirma uma sobreposição visível depois de máscaras e
oclusões. Esta nota não atribui aprovação visual ao vídeo nem ao check completo.

Não foi iniciado navegador, render ou teste adicional nesta investigação; somente
os relatórios, a composição e a implementação instalada foram lidos.

## Fechamento após inspeção do MP4

As emendas de10,615s e25,352s foram examinadas em quadros consecutivos do primeiro MP4 completo e não apresentaram a sobreposição problemática sugerida pelo DOM. A revisão encontrou outro problema real em13,133–13,433s (Clevelândia aparecia antes de sua entrada), corrigido no CSS e reexportado. O MP4 final `b49533215c68181ad225d74de8aa58de6e4ee496e5a330bdec9d62caa1724e1d` foi reinspecionado nas folhas de duração completa, abertura e transição corrigida. Consulte `independent-export-review-v15.md` e `final-approval-v15.json`. O check nativo completo continua registrado como não concluído, não como aprovado.
