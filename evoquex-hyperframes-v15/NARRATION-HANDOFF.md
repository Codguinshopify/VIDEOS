# Integração posterior da narração

Esta versão usa timing editorial provisório e música/efeitos. O usuário vai solicitar
o texto após avaliar a edição e fornecer uma gravação externa do ElevenLabs. Não gerar
voz local, não reutilizar Kokoro e não simular uma gravação que ainda não existe.

Quando o áudio chegar:

1. Preserve o original, registre hash, duração, sample rate/canais e decodifique-o.
   Faça escuta quando houver uma ferramenta disponível; não inferir naturalidade por
   metadados. Confirme a pronúncia de Danny’s Presentes, Evoquex e Clevelândia.
2. Marque o início e o fim de cada frase no áudio real. Use as nove unidades narrativas
   de `resources/scene-timing-v15.json` como âncoras sem modificar o significado da fala.
3. Ajuste os limites das cenas e os rótulos da timeline aos marcadores da voz. Preserve
   as entradas rápidas e os movimentos de ligação; alongue preferencialmente holds de
   leitura e estados estáveis. Não multiplicar indiscriminadamente todos os tempos.
4. Quando um limite mudar, retime também a janela da mídia, os recortes, a trilha e os
   cues de sound design. Mídia deve continuar presente durante toda a saída de seu suporte.
   Não esticar WAVs de impacto; mova seus pontos de ataque e preserve as caudas.
5. Adicione a voz como stem separado. Faça ducking da música e dos efeitos durante a fala,
   com ataque/retorno suaves e automação por frase. O áudio original da filmagem permanece
   controlado para não criar uma segunda voz simultânea.
6. Refaça mixagem e normalização a partir dos stems, sem normalizar isoladamente cada
   camada ao mesmo nível. Meça loudness, picos verdadeiros e clipping no MP4 real.
7. Atualize timing, procedência, hashes e QA; renderize e revise as emendas afetadas, a
   inteligibilidade da voz e o vídeo inteiro. O render sem voz não valida automaticamente
   a nova versão com locução.

Esse processo reutiliza as composições e os movimentos. Uma locução muito maior que o
espaço previsto pode exigir novos holds ou reorganização pontual; não há promessa de
encaixar qualquer duração sem ajustes editoriais.
