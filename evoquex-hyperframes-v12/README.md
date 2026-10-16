# Evoquex V12 — Ser conhecida. Ser vista.

Composição publicitária vertical de **30 segundos, 1080 × 1920, 30 fps**, em
HyperFrames 0.8.162 e GSAP 3.14.2. A narrativa conecta divulgação local, produção
do vídeo da **Danny’s Presentes**, distribuição pela Evoquex e prova documental,
encerrando com um convite próximo. Não há montagem comparativa.

## Direção e técnicas implementadas

A composição usa DM Sans local, fundo escuro, azul para estrutura e vermelho para a
pergunta do hook. A superfície clara da prova preserva a captura real. As técnicas
adaptam a construção das referências; não reutilizam suas marcas, imagens ou áudio.

| Técnica | Implementação | Janela editorial |
| --- | --- | --- |
| Letras articuladas e profundidade | Letras em rotação e planos, etiqueta diante de cópias discretas; `motion.js` e `vendor/evoquex-v12-effects.js` | 0–4 s |
| Iris ligado à pergunta | Máscara e aro compartilham o mesmo movimento para revelar a cidade | 3,82–4,47 s |
| Whip em trilho compartilhado | Cidade e case deslizam num único trilho, com blur curto que resolve no destino | 7,75–8,30 s |
| Plano de filme em 2.5D | Vídeo real em camada inclinada; o mesmo objeto muda de posição e profundidade enquanto o processo é explicado | 8–15 s |
| Documento como prova | Shutter diagonal revela a captura original em perspectiva; os números aparecem separadamente | 15–21 s |
| Transformação FLIP para o convite | A geometria do documento conduz à moldura do convite; texto permanece em plano separado, sem ser esticado | 20,82–21,61 s |
| Contorno desenhado e CTA cinético | Traço, seta, marca por letras e troca empresa/serviço completam o convite | 25,35–30 s |

`REFERENCE-IMPLEMENTATION.md` registra trechos de origem, decisões e verificações
no MP4 final. `DESIGN.md` e `STORYBOARD.md` descrevem a direção e o timing. O registro
de revisão identifica o hash efetivamente examinado; código sozinho não valida vídeo.

## Materiais, fatos e biblioteca

- `assets/campanha.mp4`: vídeo real, uma reprodução, áudio original zerado.
- `assets/clevelandia.jpg`: registro aéreo original; não foi inventado detalhe novo.
- `assets/resultados.jpg`: captura original da campanha, sem reconstrução de interface.
- `assets/DM-Sans.woff2`: fonte local; licença preservada nos recursos do projeto.
- Vetores Lucide e helpers locais: procedência e licenças mantidas; recursos de
  referência HyperFrames estão catalogados em `../biblioteca/hyperframes`.
- `resources/catalogo-pesquisa-v12.md`: pesquisa dos recursos antes da implementação.
- `resources/scene-manifest.json`: estrutura modular; **Luciane desativada**, sem
  imagem, título, placeholder ou tempo vazio reservado na composição.

O case comprova **13.064 pessoas alcançadas** e **20.981 impressões/exibições do
anúncio**. A Evoquex produziu o vídeo e direcionou os anúncios somente a Clevelândia.
Ir além dos seguidores é descrito como objetivo; não há quantidade comprovada desse
público. Os registros não comprovam vendas, conversões, visualizações ou ROI.

Não foi necessário gerar assets por IA nesta versão: imagens documentais, tipografia
editável, máscaras e vetores existentes resolvem as necessidades. Isso não representa
um teste de geração realizado nem a criação de novos materiais de campanha.

As quatro skills locais ficam em `../.agents/skills/`: `ai-visual-asset-design`,
`reference-analysis`, `asset-library-research` e `motion-quality-control`. Foram
preparadas para consulta direta; sua existência no repositório não comprova registro
ou descoberta automática pelo serviço de skills em nuvem.

## Áudio e locução

`assets/mix-v12.wav` contém instrumental e efeitos reais derivados dos stems próprios
preservados em `resources/audio/`. A mixagem tem seis seções, variações de intensidade
e 18 acentos, com recortes, velocidade de reprodução, reversão, panorâmica e envelopes
documentados em `resources/audio/provenance-v12.json`. A licença integral GeneralUser
GS e suas ressalvas estão incluídas. Não foi utilizado áudio das referências ou a voz
Kokoro rejeitada. A masterização é reproduzível com:

```bash
python scripts/remix-audio.py
```

**A locução feminina brasileira está pendente.** Não há ferramenta ElevenLabs de
geração exposta nesta sessão nem chave disponível; não houve geração, exportação ou
teste autenticado de voz. O plano e seus direitos comerciais não foram validados.
Nenhuma compra ou alteração de plano foi feita.

`resources/voice-cues.json` guarda o roteiro e janelas **estimadas**, não um alinhamento
com gravação. `resources/voice-status.json` distingue o que existe das pendências. A
fala real deverá orientar o retiming de imagem, música, efeitos e ducking; não acelerar
uma locução artificialmente para forçá-la aos 30 segundos. O HTML atual referencia
somente o mix real, sem caminho fictício de voz. O helper `prepare-voice.py` é uma
etapa de preparação para gravação fornecida, não um sintetizador nem troca automática
do áudio final; confirme sua duração e entradas V12 antes de utilizá-lo.

**Não houve escuta subjetiva nesta interface.** Probe, decode, loudness, pico e ausência
de clipping são validações técnicas; não comprovam naturalidade ou inteligibilidade
por audição humana.

## Reproduzir

Execute na raiz desta composição. São necessários Node/npm, Chromium e FFmpeg; os
scripts de análise usam Python, NumPy e Pillow já disponíveis no ambiente de produção.
O lockfile fixa as dependências; `scripts/hf.mjs` usa caches locais e a configuração de
Chromium disponível, evitando depender de escrita no diretório pessoal.

```bash
npm ci --cache /workspace/.npm
npm run dev
node scripts/hf.mjs preview --status
npm run check
npm run render
python scripts/validate-output.py
python scripts/review-output.py
```

O comando de render do pacote grava `renders/evoquex-hyperframes-v12.mp4`, em 30 fps,
qualidade alta, CRF 18 e captura sem GPU. O preview é gerenciado; encerre ao concluir:

```bash
node scripts/hf.mjs preview --stop
```

Para mapa de animações em dimensões verticais explícitas:

```bash
node scripts/animation-map/animation-map.mjs . --out review/animation-map --width 1080 --height 1920 --fps 30
```

Esse helper foi adaptado ao pacote instalado; limites e modificações estão em
`scripts/animation-map/ADAPTATION.md`. O mapa é uma ferramenta de inspeção e não
substitui assistir às sequências exportadas. Asserções automáticas de motion podem
estar desativadas; só declare executadas as verificações presentes nos relatórios.

## Estado da validação

A revisão final está em `review/final-review.md`, vinculada ao MP4 SHA-256
`928b0b271c5144169af4dfe378935af5f8b4ca1b45fa4865bb63b7b1fd2b3361`.
Foram examinados 121 frames consecutivos da abertura, 60 amostras ao longo do vídeo,
63 amostras de transição, 64 estados intermediários e seis enquadramentos de telefone.
Decodificação completa e validação técnica do áudio passaram. Não houve escuta
subjetiva; a locução continua pendente. O check nativo passou com um aviso informativo
de oclusão intencional no shutter aos 15 s; seu módulo automático de motion está
desativado. O mapa separado de animações foi executado em 1080×1920 e revisado.
Relatórios de V11 ou de outro hash não validam esta versão. Em novas alterações,
repita os checks afetados e a inspeção do MP4 real antes de entregar.

O slot Luciane não possui ativação automática: adicionar o componente e os materiais
aprovados e retimar a partir do marcador de convite será uma etapa futura. Nenhuma
cena/voz/imagem provisória é renderizada.
