# Envio de packs pelo GitHub Desktop

Esta configuração está na branch `packs-lfs` do repositório `Codguinshopify/VIDEOS`.
O vídeo permanece sem alterações. Arquivos RAR, ZIP e 7Z dentro de `pack/` usam Git LFS.

1. Instale o GitHub Desktop pelo site oficial https://desktop.github.com/ e entre na sua conta.
2. Use **File > Clone repository > URL** com `https://github.com/Codguinshopify/VIDEOS.git`.
3. Em **Current branch**, selecione `packs-lfs`. Use **Repository > Show in Explorer**.
4. Dentro de `pack/`, crie uma pasta para o pacote e copie primeiro um arquivo compactado pequeno de teste.
5. No Desktop, confira se somente o arquivo esperado está em **Changes**, escreva uma descrição e clique em **Commit to packs-lfs**.
6. Clique em **Push origin** e aguarde a conclusão. O commit salva localmente; o push envia ao GitHub.
7. Avise no chat o nome do arquivo. Depois de o download e a extração serem validados, envie o pack completo.

O GitHub Desktop inclui suporte ao Git LFS. Não use o upload do navegador para os arquivos LFS.
Se aparecer aviso de limite, cota, pagamento ou erro de LFS, pare e informe a mensagem; não altere o plano.
Confirme a franquia disponível da conta antes de enviar arquivos grandes. Não há promessa de velocidade para packs de 1 GB.

`teste-lfs.zip` é um arquivo pequeno de diagnóstico, contendo somente `teste.txt`; não é um recurso visual.
