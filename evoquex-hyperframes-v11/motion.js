/* V11: evolution of V10. Shared geometry carries the meaning, not repeated rings.
 * Adapted catalog mechanisms are recorded in resources/SOURCES.json. */
const tl=window.__timelines['evoquex-hf-v11'];
const M=window.EvoquexMotion;
// Same SVG command topology throughout: deterministic round-rectangle morph.
function rectPath(x,y,w,h,r){return `M${x+r} ${y} L${x+w-r} ${y} Q${x+w} ${y} ${x+w} ${y+r} L${x+w} ${y+h-r} Q${x+w} ${y+h} ${x+w-r} ${y+h} L${x+r} ${y+h} Q${x} ${y+h} ${x} ${y+h-r} L${x} ${y+r} Q${x} ${y} ${x+r} ${y}`;}
document.querySelector('#thread').setAttribute('d',rectPath(190,1065,700,3,1));
function shape(at,x,y,w,h,r,d=.65){tl.to('#thread',{attr:{d:rectPath(x,y,w,h,r)},duration:d,ease:'power3.inOut'},at);}
function transition(from,to,at,kind='vertical'){
  // Both full scenes remain in place throughout the shared mask transition.
  const start=kind==='horizontal'?'inset(0 100% 0 0)':'inset(100% 0 0 0)';
  const complement=kind==='horizontal'?'inset(0% 0% 0% 100%)':'inset(0% 0% 100% 0%)';
  tl.fromTo(to,{opacity:1,clipPath:start},{opacity:1,clipPath:'inset(0% 0% 0% 0%)',duration:.5,ease:'power3.inOut',immediateRender:false},at);
  // Incoming scenes are transparent paper over a shared light field. Trim the
  // outgoing scene with the exact complementary mask: no double exposed titles,
  // and the blue proof surface genuinely wipes away instead of vanishing at end.
  tl.to(from,{clipPath:complement,duration:.5,ease:'power3.inOut'},at);
  tl.set(from,{opacity:0},at+.5);
}
function count(id,value,at,duration=.5){
  tl.set(id,{textContent:'0'},at);
  const n=Math.round(duration*30);
  for(let f=0;f<=n;f++)tl.set(id,{textContent:Math.round(value*(1-Math.pow(1-f/n,3))).toLocaleString('pt-BR')},at+f/30);
}
// Frame zero contains a clear message and a partially drawn line. Movement begins immediately.
tl.from('.small-intro',{y:32,scale:.96,duration:.52,ease:'power3.out'},0);
tl.from('#word-track',{y:40,filter:'blur(4px)',duration:.55,ease:'expo.out'},0);
tl.from('.brand-tiny',{opacity:.2,y:20,duration:.6,ease:'power2.out'},0);
M.draw(tl,'#thread',0,.55);
tl.from('#message-note',{y:24,opacity:0,duration:.5,ease:'power2.out'},.35);
M.maskedSwap(tl,'#word-track',135,1.2,.36);
M.maskedSwap(tl,'#word-track',270,2.45,.4);
tl.set('.small-intro',{textContent:'Começamos'},2.45);
tl.to('.fog-one',{x:60,y:-40,scale:1.05,duration:16,ease:'sine.inOut'},0);
tl.to('.fog-two',{x:-65,y:35,scale:1.08,duration:16,ease:'sine.inOut'},0);
shape(2.85,140,1065,800,3,1,.6);
// The message underline unfolds into the portrait film boundary.
transition('#message','#production',4.18);
shape(4.18,295,590,490,770,35,.72);
tl.from('#production h1',{y:42,opacity:0,duration:.55,ease:'power3.out'},4.35);
M.draw(tl,'.camera-drawing path,.camera-drawing circle',4.3,.6,.04);
tl.from('.camera-drawing',{scale:.7,rotationY:-20,duration:.6,ease:'power2.out'},4.3);
tl.fromTo('.film-plane',{clipPath:'inset(0 0 100% 0 round 30px)',rotationY:25,rotation:-5,scale:.9},{clipPath:'inset(0% 0% 0% 0% round 30px)',rotationY:-6,rotation:2,scale:1,duration:.7,ease:'power4.out',immediateRender:false},4.5);
tl.to('.film-plane',{rotationY:4,rotation:-2,y:-5,duration:3.5,ease:'sine.inOut'},5.5);
tl.from('.case-name',{y:26,opacity:0,duration:.45,ease:'power3.out'},5.1);
tl.from('.production-credit',{y:20,opacity:0,duration:.4,ease:'power2.out'},5.3);
tl.to('#thread',{stroke:'#7BA9DF',strokeWidth:2,opacity:.45,duration:.4,ease:'power2.out'},5.1);
// Single directional thought: an ad, its channels, then one verified city.
transition('#production','#distribution',9.4,'horizontal');
shape(9.4,150,730,780,3,1,.65);
tl.to('#thread',{stroke:'#355CE8',strokeWidth:5,opacity:1,duration:.4,ease:'power2.out'},9.5);
tl.from('.distribution-lead',{y:30,opacity:0,duration:.5,ease:'power2.out'},9.6);
tl.from('#distribution h2',{y:40,opacity:0,duration:.6,ease:'power3.out'},9.75);
tl.from('.channel-line',{x:-25,opacity:0,duration:.5,ease:'power2.out'},10.1);
tl.fromTo('.city-mask',{clipPath:'inset(0 100% 0 0 round 26px)'},{clipPath:'inset(0% 0% 0% 0% round 26px)',duration:.7,ease:'power3.inOut',immediateRender:false},10.55);
tl.from('.city-mask img',{scale:1.08,x:-15,duration:1.5,ease:'sine.out'},10.55);
shape(10.55,198,855,684,395,32,.7);
tl.to('#thread',{strokeWidth:2,opacity:.5,duration:.4,ease:'power2.out'},11.3);
tl.from('.city-label',{y:45,filter:'blur(5px)',opacity:0,duration:.6,ease:'power3.out'},11.65);
tl.from('.distribution-note',{y:25,opacity:0,duration:.5,ease:'power2.out'},12.2);
// Evidence is a single number at a time. Blue mask crosses the existing image.
transition('#distribution','#evidence',14.4,'horizontal');
shape(14.4,190,1102,700,3,1,.65);
tl.to('#thread',{stroke:'#FDFEFF',opacity:.5,strokeWidth:3,duration:.5,ease:'power2.out'},14.4);
tl.from('.evidence-intro',{y:30,opacity:0,duration:.5,ease:'power3.out'},14.65);
tl.from('.evidence-brand',{y:20,opacity:0,duration:.45,ease:'power2.out'},14.85);
tl.fromTo('#reach-mode',{opacity:1,y:100},{opacity:1,y:0,duration:.5,ease:'power3.out',immediateRender:false},14.9);
count('#reach-number',13064,14.95,.55);
tl.from('.source-doc',{rotation:6,y:50,scale:.9,opacity:0,duration:.6,ease:'power3.out'},15.15);
tl.from('.proof-copy',{x:25,opacity:0,duration:.5,ease:'power2.out'},15.35);
// A coupled masked handoff; no two readable values occupying the same focus.
tl.to('#reach-mode',{yPercent:-120,duration:.42,ease:'power3.inOut'},17.65);
tl.fromTo('#impressions-mode',{opacity:1,yPercent:120},{opacity:1,yPercent:0,duration:.42,ease:'power3.inOut',immediateRender:false},17.65);
count('#impressions-number',20981,17.85,.55);
shape(18.05,205,1102,670,3,1,.45);
// The same emphasis becomes one question window, rather than two competing cards.
transition('#evidence','#strategy',21,'vertical');
shape(21,155,1105,770,3,1,.65);
tl.to('#thread',{stroke:'#355CE8',opacity:1,duration:.5,ease:'power2.out'},21.05);
tl.from('.strategy-intro',{y:25,opacity:0,duration:.5,ease:'power2.out'},21.2);
tl.from('#strategy h2',{y:35,opacity:0,duration:.55,ease:'power3.out'},21.35);
tl.from('#question-track',{y:180,duration:.6,ease:'power4.out'},21.75);
M.draw(tl,'#question-message path',21.8,.55);
M.maskedSwap(tl,'#question-track',180,23.9,.48);
M.draw(tl,'#question-audience circle',24.05,.55,.04);
tl.from('.strategy-join',{scaleX:.1,scaleY:.7,opacity:0,duration:.5,ease:'power4.out'},25.55);
// The persistent line bends to point at the invitation. No ring around every scene.
transition('#strategy','#invitation',27,'horizontal');
shape(27,190,1120,700,3,1,.7);
M.focus(tl,'.end-wordmark span',27.25);
tl.from('#invitation h2',{y:35,opacity:0,duration:.55,ease:'power3.out'},27.8);
tl.from('.end-note',{y:20,opacity:0,duration:.5,ease:'power2.out'},28.2);
tl.from('.cta-pill',{scaleX:.05,scaleY:.7,opacity:0,duration:.65,ease:'power4.out'},28.65);
tl.from('.cta-pill span',{y:20,opacity:0,duration:.4,ease:'power2.out'},29);
tl.from('.cta-arrow',{x:-18,y:18,opacity:0,duration:.45,ease:'power3.out'},29.15);
M.draw(tl,'.cta-arrow path',29.15,.45,.03);
shape(28.8,865,1235,30,3,1,.6);
tl.to('#thread',{opacity:0,duration:.3,ease:'power2.out'},29.35);
tl.to('.cta-arrow',{x:6,y:-6,duration:.45,ease:'sine.inOut',yoyo:true,repeat:1},30.3);
tl.to('.fog-one',{x:-15,y:15,scale:1.02,duration:16,ease:'sine.inOut'},16);
tl.to('.fog-two',{x:15,y:0,scale:1,duration:16,ease:'sine.inOut'},16);
window.EVOQUEX_AUDIT={engine:'HyperFrames 0.8.162',version:'V11',duration:33,case:'Danny’s Presentes',reach:13064,impressions:20981,originalAudioGain:0,voice:false,originalFootagePlaybackCount:1,referenceAudioUsed:false};
tl.seek(0);
