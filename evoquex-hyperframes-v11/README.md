# Evoquex V11 — Uma ideia conduz à próxima

Evolução da V10, preservando DM Sans, paleta, filmagem e provas. Duas referências
orientam técnicas de movimento; originais em ../biblioteca/referencias/, com hashes.
As referências não entram no render nem têm seu áudio reutilizado.

33 s, 1080×1920, 30 fps. HyperFrames 0.8.162 / GSAP 3.14.2 fixados por lockfile.
Sem novas dependências. Todos os recursos necessários ao render estão neste projeto.
Leia ../AGENTS.md, AGENTS.md, DESIGN.md, STORYBOARD.md e resources/SOURCES.json.

## Reproduzir

Node 22+, FFmpeg/ffprobe e Chromium do sistema. Python/numpy/Pillow para QA e remix.

```sh
npm ci --cache /workspace/.npm --no-audit --no-fund
npm run dev
node scripts/hf.mjs preview --status
npm run check
npm run render
python scripts/validate-output.py
python scripts/review-output.py
node scripts/hf.mjs preview --stop
```

O wrapper mantém caches no projeto e seleciona /usr/bin/chromium. O Studio é um
serviço local de trabalho, não um link de entrega. Reinicie após restaurar ambiente.
Mapeamento adicional: HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium node
scripts/animation-map/animation-map.mjs . --width 1080 --height 1920 --out review/animation-map
O check testa lint, runtime, layout e contraste; a verificação automática de movimento
vem desabilitada nesta versão, por isso a coreografia também é inspecionada no MP4.

## Edição e limites

Traço abre moldura; wipe liga o anúncio à cidade. Prova azul com uma métrica de cada
vez; perguntas em substituição mascarada. A assinatura resolve em foco e conduz ao CTA.
Danny’s Presentes; campanha somente Clevelândia; 13.064 pessoas alcançadas e 20.981
impressões. Não inferir vendas/ROI/não seguidores. Material original reproduzido uma
vez, mudo. A foto 600×337 aparece a 660×371, leve ampliação, sem inventar detalhes.

Não há narração gerada. CLI TTS investigado: família Kokoro, previamente rejeitada.
Sem acesso autenticado a serviço profissional. Nenhuma compra ou mudança de plano.
resources/voice-cues.json contém janelas semânticas estimadas; prepare-voice.py mistura
um arquivo real com ducking, sem carregar voz inexistente ou acelerar a gravação.
Ao receber voz, medir/retimar/revisar antes de gerar versão narrada.
Áudio atual: instrumental e efeitos próprios anteriores, retimados em 19 eventos.
A validação de áudio é técnica; não houve escuta subjetiva nesta interface.

Biblioteca permanente no diretório pai: referências originais, fontes de catálogo,
amostras completas de packs e motion-kit reutilizável. AEP não executa aqui;
parte 2 está identificada, não analisada. Não confundir catálogo parcial com extração
do pack inteiro. Confira licenças antes de reutilizar conteúdo comercial de packs.

Entregar somente o vídeo editado. Fontes e QA ficam disponíveis para continuidade,
sem montagens comparativas. O ZIP do projeto não duplica os originais de referência;
a biblioteca permanece ao lado dele no repositório.
