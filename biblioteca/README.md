# Biblioteca permanente Evoquex

Comece pelas instruções do `../AGENTS.md`. Esta pasta acompanha o código no Git;
não depende de anexos temporários do chat ou de caminhos externos à cópia do repositório.

| Recurso | Local | Uso e limite |
|---|---|---|
| Quatro referências originais | `referencias/catalogo.json` | MP4 originais, nomes preservados em diretórios distintos, com hash e metadados. Estudo somente. |
| Análise de técnicas | `referencias/ANALISE.md` | Trechos e decisões de adaptação, sem reproduzir a identidade das peças. |
| Catálogo HyperFrames selecionado | `hyperframes/catalogo.json` | Fontes originais fixadas em revisão Git. HTML arquivado como `.html.txt`, para o Studio não alterar sua integridade. |
| Recursos de packs | `packs/inventario.json` | Amostras completas já extraídas; volumes adicionais apenas identificados. AEP requer outro runtime. |
| Componentes Evoquex | `componentes/catalogo.json` | Funções compartilháveis e caminho da produção que as utiliza. |
| Validador da biblioteca | `scripts/verificar.py` | `python biblioteca/scripts/verificar.py` valida existência, hashes e decodificação da mídia catalogada. |

Para adicionar um pack, preserve o original em `pack/` (LFS se necessário), registre
nome, volumes, formato interno, licença e integridade. Extraia apenas arquivos seguros
e necessários; não execute instaladores ou plugins dos pacotes. Não derive direitos
comerciais apenas do fato de o download estar disponível.

Para adicionar referências: use novo diretório, mantenha nome original, registre hash,
metadados e análise; não substitua as atuais. Para novos componentes: registre origem,
licença, dependências, variáveis de timing e um exemplo de uso real. Evite duplicações.

A V12 mantém o instrumento e os efeitos próprios já utilizados. Os efeitos de tinta
do pack estão disponíveis para outros estilos; não foram forçados numa direção atual.

A análise Oto adicional está em referencias/oto-criativo/ANALISE-OTO.md. Técnicas
implementadas e seus critérios estão em ../evoquex-hyperframes-v12/REFERENCE-IMPLEMENTATION.md.

A referência Park/Weven anterior foi recuperada na auditoria por hash de todos os
anexos, com análise própria. Uploads de conteúdo idêntico não duplicam a biblioteca.
