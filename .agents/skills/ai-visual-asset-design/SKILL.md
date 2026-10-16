---
name: ai-visual-asset-design
description: Pesquisa, seleciona ou gera recursos visuais de apoio para a Evoquex, com direção de arte, transparência, procedência e separação rigorosa entre ilustração e prova real.
---

# Design de recursos visuais com IA

Use esta skill quando um briefing exigir um novo recurso visual, uma edição de imagem
ou a avaliação de imagens geradas para motion design. Ela complementa as skills do
motor de vídeo; não substitui a documentação do HyperFrames ou do Remotion.

## Entradas

- Briefing vigente, narrativa aprovada, formato de entrega e identidade da composição.
- `AGENTS.md`, `biblioteca/README.md` e `DESIGN.md` do projeto escolhido.
- Catálogos da biblioteca, materiais reais e restrições de uso das referências.
- Função do recurso: plano de fundo, objeto, textura, recorte ou apoio conceitual.

## Procedimento

1. **Pesquise antes de gerar.** Consulte os catálogos de packs, componentes e
   HyperFrames. Examine amostras, formatos e licenças com `asset-library-research`.
   Reaproveite um recurso adequado; registre o motivo concreto se for necessário
   criar outro. Não use geração para substituir automaticamente os packs do usuário.
2. Defina função narrativa, enquadramento, paleta, espaço para texto, escala de uso,
   integração entre camadas e necessidade de transparência. Um objeto bonito sem
   função na cena não é um resultado suficiente.
3. Verifique as ferramentas realmente expostas na sessão. Quando a geração ou a
   edição de imagem for necessária e `image_gen.imagegen` estiver disponível, use
   essa ferramenta. Inspecione a imagem de origem antes de editá-la. Use caminhos
   locais como referências quando disponíveis, ou a menor quantidade necessária de
   imagens recentes da conversa; não misture os dois mecanismos.
4. Escreva um prompt específico que descreva a função, a composição, o material, a
   luz, o estilo, a paleta e o recorte. Prefira gerar objetos ou fundos sem textos
   essenciais: tipografia, números e dados devem continuar editáveis no motor de
   vídeo. Para recorte, remoção de fundo ou fundo transparente, solicite
   `transparent_background: true`; preserve transparência existente nas edições.
5. Não use Python para criar ou editar as imagens no lugar da ferramenta de imagem,
   salvo instrução explícita do usuário. Comandos de metadados podem medir dimensões,
   canais, hash e integridade; não equivalem à inspeção visual.
6. Inspecione o arquivo produzido em tamanho suficiente e na composição prevista.
   Confira silhueta, bordas, recorte, textura, artefatos, luz e área de texto. Se há
   transparência, confira o canal alpha e a composição sobre fundo claro e escuro;
   um padrão quadriculado desenhado na imagem não comprova transparência.
7. Preserve o original e produza derivados somente quando necessários. Registre
   prompt, referência de origem, ferramenta efetivamente utilizada, dimensões,
   alpha, hash e restrições de uso. Não invente licença: registre os termos aplicáveis
   conhecidos ou a pendência. Não copie marcas, áudio ou imagens das referências
   publicitárias para a peça final sem autorização de uso correspondente.
8. Se a ferramenta não estiver disponível, selecione uma alternativa real do acervo
   ou registre exatamente qual recurso está pendente. Não simule uma geração nem
   referencie um arquivo inexistente. Prossiga com o restante do trabalho autorizado,
   sem criar uma nova etapa de aprovação por conta própria.

## Limite entre ilustração e evidência

Imagens geradas podem apoiar uma ideia visual. Nunca devem se passar por filmagem da
Danny’s Presentes, foto documental da campanha, captura do gerenciador de anúncios,
depoimento ou evidência comercial. Preserve os materiais reais e identifique a
procedência dos recursos de apoio no projeto. Não gere métricas, clientes ou vendas.
No case atual, os dados comprovados são 13.064 pessoas alcançadas e 20.981 impressões;
não transformá-los em visualizações, conversões ou retorno financeiro.

## Saídas e critérios verificáveis

- Recurso local existente, aberto e inspecionado; original preservado.
- Registro de procedência com caminho, hash, formato, dimensões, alpha, uso previsto,
  prompt quando houver geração e informação de licença/termos conhecida.
- Exemplo de aplicação ou nota de encaixe na cena, respeitando o espaço de texto.
- Nenhuma evidência de campanha fabricada, nenhuma chave de API registrada e nenhum
  arquivo ausente declarado como pronto.

Mantenha esses registros no projeto ou catálogo correspondente, respeitando o schema
existente e as instruções da produção. Não exponha credenciais em prompts ou logs.
