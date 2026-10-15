# Evoquex V11 — instruções específicas

Leia primeiro ../AGENTS.md e ../biblioteca/README.md. Preservam direção criativa,
pesquisa de recursos, duas referências, fatos do case e preferência de entrega.
As skills HyperFrames, CLI e registry devem ser consultadas antes de alterações.
DESIGN.md é a direção visual desta composição; STORYBOARD.md guarda o texto/cues.

Um timeline raiz pausado em window.__timelines, sem aleatoriedade ou playback manual.
Use versão fixada 0.8.162 e GSAP 3.14.2; npm ci com lockfile. Vídeo mudo, áudio separado.
Toda alteração HTML exige npm run check. Revise avisos; não desative verificações
para forçar aprovação. Asserções automáticas de motion são desabilitadas por padrão;
revise mapa e render exportado. Não declare que esse módulo automático executou.

Preview gerenciado: npm run dev, depois node scripts/hf.mjs preview --status.
Verifique resposta HTTP e snapshots, mantenha durante revisão e encerre com
node scripts/hf.mjs preview --stop. Não dependa de um shell em background que termine.
Se houve edição no aplicativo desktop, execute catch-up antes de alterar fontes.

Nenhuma voz disponível: não reutilize Kokoro rejeitado. Arquivo real é pré-requisito
para prepare-voice.py; ao inseri-lo retime visual/FX e confira inteligibilidade.
Não prometer naturalidade por configuração ou ASR. Não há escuta subjetiva aqui.
Não expor segredos, não comprar assinaturas. Não entregar comparativos.

Arquivos de catálogo .html.txt são originais de arquivo; não renomear para .html
sem necessidade, porque o Studio injeta identificadores em HTML de composição.
