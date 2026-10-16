---
name: asset-library-research
description: Pesquisa a biblioteca Evoquex e o catálogo do motor antes de criar recursos; inventaria packs, valida volumes e distingue mídia utilizável de projetos dependentes de outros runtimes.
---

# Pesquisa de biblioteca e compatibilidade de packs

Use antes de escolher, converter ou criar um recurso visual/sonoro, ao receber packs
e ao incorporar exemplos do catálogo. ZIP/RAR é embalagem; o formato dos arquivos
internos é que determina compatibilidade e dependências.

## Entradas

- Briefing, função do recurso e motor/versões em uso.
- `biblioteca/README.md` e catálogos de `hyperframes`, `packs`, `componentes` e
  `referencias`, além dos materiais já usados nas produções anteriores.
- Arquivos locais ou links que possam ser acessados pelos meios autorizados.

## Procedimento

1. Consulte os catálogos existentes e abra os candidatos mais relevantes. Compare
   função, estética, formato, dimensões, duração, alpha, dependências e licença. Não
   instale outra biblioteca se o acervo ou o motor atual já resolverem a necessidade.
2. Verifique as ferramentas de listagem/extração realmente instaladas. Para arquivos
   compactados, liste conteúdo, quantidade, tamanho expandido previsto e volumes
   necessários antes de extrair. Verifique caminhos que escapem do destino e não
   execute instaladores, plugins ou scripts desconhecidos presentes nos packs.
3. Em arquivos multipartes, confirme sequência e presença dos volumes e execute o
   teste de integridade disponível. Uma listagem parcial não prova que o pack inteiro
   está utilizável. Arquivos independentes extraídos de um volume incompleto só podem
   ser marcados como utilizáveis após validação individual de integridade e abertura.
4. Inspecione os formatos internos. Para mídia, valide metadados e decodificação; para
   animações e projetos, confira referências externas, fontes, plugins, expressões,
   versão e runtime. Não declare compatibilidade pelo nome comercial do pack.
5. Classifique cada candidato usando a matriz abaixo. Teste uma amostra real no motor
   antes de generalizar a compatibilidade para uma família inteira.

| Categoria | Caminho de integração | Verificação necessária |
| --- | --- | --- |
| PNG/JPEG/WebP/SVG | Mídia ou vetor local | Dimensões, alpha, fontes/recursos externos e renderização |
| MP4/WebM/MOV | Mídia pré-renderizada | Codec, fps, duração, cor e suporte real de alpha no pipeline |
| Sequência de imagens | Frames ou transcodificação | Ordem, fps, frames ausentes, alpha e tamanho final |
| JSON de animação | Runtime específico ou conversão | Schema real, recursos vinculados e dependências; JSON não significa automaticamente Lottie |
| AEP/MOGRT/FFX e plugins | Runtime de origem ou renderização intermediária | Aplicativo, versão, fontes, efeitos e mídia de origem; não executam diretamente em HTML/React |
| PSD/AI/EPS e outros editáveis | Exportação ou conversão validada | Camadas, vetores, fontes, fidelidade e ferramenta disponível |
| WAV/MP3/OGG | Trilha, voz ou efeito local | Decodificação, canais, sample rate, duração e direitos de uso |

6. Se exigir conversão, proponha o caminho concreto disponível: exportar camadas,
   renderizar com alpha em ferramenta compatível, converter uma mídia independente
   ou adaptar o mecanismo de um exemplo licenciado. Preserve o original e compare o
   resultado visual/sonoro. Não substitua automaticamente o recurso por um desenho
   manual simplificado nem alegue ter executado After Effects ausente.
7. Preserve procedência: nome original, caminho, hash, origem, versão/revisão,
   licença/atribuição, integridade, dependências, limitações e exemplo de uso real.
   Download disponível ou compra de acesso ao site não comprova direitos comerciais.
   Não invente licença quando ela não vier com o material.
8. Para exemplos HyperFrames, consulte a skill de registry e a documentação instalada.
   Registre se houve instalação pelo CLI ou cópia manual de uma revisão Git. Arquive
   originais HTML de estudo como `.html.txt` quando o Studio puder alterá-los; mantenha
   as adaptações separadas, com seus créditos e parâmetros de timing.
9. Atualize o catálogo apropriado sem apagar itens anteriores, respeitando seu schema.
   Identifique recursos reutilizáveis, recursos específicos do case e pendências.
   Para novo recurso por IA, aplique `ai-visual-asset-design` após esta pesquisa.

## Saídas e critérios verificáveis

- Inventário com caminho, formato real, integridade, uso possível, licença conhecida
  e categoria: direto, conversão necessária, outro runtime ou pendente.
- Seleção justificada de candidatos e teste representativo de integração.
- Lista explícita de volumes/arquivos faltantes e ferramentas indisponíveis.
- Nenhuma afirmação de pack completo analisado sem todos os volumes necessários;
  nenhum arquivo incompleto incluído no vídeo final.
- Recursos e originais preservados, sem dependência obrigatória de um anexo temporário
  do chat. Use o validador da biblioteca existente quando houver alteração de catálogo.

Continue as partes autorizadas e possíveis sem criar aprovação extra. A ausência de
um runtime ou licença deve ser relatada com precisão, sem fingir que foi resolvida.
