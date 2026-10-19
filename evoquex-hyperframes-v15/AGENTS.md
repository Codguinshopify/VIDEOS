# Instruções locais — V15

Leia o briefing vigente em `resources/briefing-v15.txt`. Ele prevalece sobre regras
históricas da V13/V14 em caso de conflito. Preserve versões e arquivos originais.

- HyperFrames é o motor. Dependências fixadas; recursos locais; animações determinísticas.
- Consulte novamente os três MP4 de referência reais e as duas bibliotecas. Use recursos
  compatíveis dos packs na produção quando melhorarem a cena; registre origem e função.
- O usuário autorizou uso comercial dos packs fornecidos. Diferencie limitações técnicas
  verificadas de suposições genéricas sobre licença.
- Nome obrigatório: **Danny’s Presentes**. Métrica ativa: **20 mil visualizações de pessoas
  de Clevelândia**, declaração explícita do usuário; não converter em alcance, impressões,
  pessoas únicas, vendas ou retorno. Produção pela Evoquex, direcionamento somente local.
- A paleta pode evoluir com intenção. Não impor a paleta restrita histórica a toda a peça.
- O hook pode evoluir, sem obrigação de igualdade de pixels com versões anteriores.
- Nesta etapa, não gerar narração, não usar Kokoro, não configurar serviços de voz e não
  referenciar áudio de voz inexistente. Preserve possibilidade de retimar por cena depois.
- Reutilize recursos HyperFrames e packs de forma visível/audível, sem efeitos decorativos
  aleatórios ou contagens artificiais de assets.
- `resources/scene-timing-v15.json` é o contrato temporal ativo. Derive duração e QA dele.
- Antes do render, congele hashes com `scripts/qa-v15.py --freeze`. Depois, use o mesmo
  bundle para validar o MP4. Alteração de inputs exige novo bundle e novo render.
- Inspecione quadros consecutivos nas emendas, início/fim de mídias, abertura inteira e
  amostras de toda a duração. Números de loudness não substituem escuta subjetiva.
- Não alegue assistir em playback contínuo ou escutar se a interface só permitir extração
  de quadros e checagens técnicas. Registre a limitação honestamente.
- Entrega vigente: MP4 final, caminho/link, resolução, fps, duração e informação honesta
  da revisão. Mencione somente limitações relevantes. Não criar montagem comparativa.

O arquivo `NARRATION-HANDOFF.md` descreve a integração posterior da voz do ElevenLabs.
