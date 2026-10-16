/* V12 — reference-led kinetic advertising, deterministic HyperFrames/GSAP.
 * Concrete origins and rendered acceptance frames: REFERENCE-IMPLEMENTATION.md.
 * Each phase is a different composition, connected by actual moving objects.
 */
const tl=window.__timelines['evoquex-hf-v12'];
const FX=window.EvoquexFX;
tl.addLabel('hook',0).addLabel('local',4).addLabel('case',8).addLabel('proof',15).addLabel('invitation',21);

// HOOK: articulated glyphs, depth-stack label, oblique locality, red doubt.
// Frame zero is visibly populated; the first title starts partially articulated.
tl.from('.suaword .char',{yPercent:10,rotationX:12,opacity:1,stagger:.025,duration:.42,ease:'power4.out'},0);
tl.from('.companyword .char',{yPercent:12,rotationX:18,opacity:1,stagger:.022,duration:.48,ease:'power4.out'},0);
tl.from('.hook-kicker',{y:25,opacity:.3,duration:.5,ease:'power2.out'},0);
tl.from('.company-rule',{scaleX:.12,duration:.5,ease:'expo.out'},0);
tl.from('#hook-company',{rotationY:-12,z:90,duration:.6,ease:'power3.out'},0);
// One continuous handoff: the title recedes as the known-label takes its plane.
tl.to('#hook-company',{x:-900,rotationY:-35,z:-220,scale:.72,filter:'blur(7px)',duration:.34,ease:'power3.inOut'},.76);
tl.set('#hook-company',{opacity:0},1.1);
tl.fromTo('#hook-known',{opacity:1,x:980,rotationY:30,z:180},{opacity:1,x:0,rotationY:0,z:0,duration:.42,ease:'power4.out',immediateRender:false},.8);
tl.from('.known-top',{y:45,opacity:0,duration:.3,ease:'power2.out'},.88);
tl.from('.known-tag',{rotation:13,scale:.62,y:100,duration:.5,ease:'back.out(1.12)'},.85);
tl.to('.known-tag',{rotation:-6,duration:.4,ease:'power3.out'},1.05);
tl.from('.known-echo',{y:70,rotationX:40,opacity:0,duration:.5,ease:'power3.out'},.8);
tl.to('#hook-known',{y:-800,rotationX:45,scale:.8,duration:.33,ease:'power3.inOut'},1.63);
tl.set('#hook-known',{opacity:0},1.96);
tl.fromTo('#hook-city',{opacity:1,y:820,rotationX:-25},{opacity:1,y:0,rotationX:0,duration:.38,ease:'power4.out',immediateRender:false},1.66);
tl.from('.local-type',{x:140,rotationY:20,scaleX:.85,duration:.42,ease:'power3.out'},1.69);
tl.from('.local-bars i',{scaleX:0,transformOrigin:'0% 50%',stagger:.04,duration:.35,ease:'power4.out'},1.8);
tl.to('#hook-city',{x:900,rotation:-10,scale:1.12,duration:.32,ease:'power3.inOut'},2.48);
tl.set('#hook-city',{opacity:0},2.8);
tl.fromTo('#hook-question',{opacity:1,x:-950,rotation:8},{opacity:1,x:0,rotation:0,duration:.38,ease:'power4.out',immediateRender:false},2.52);
tl.from('.question-top',{x:60,opacity:0,duration:.3,ease:'power2.out'},2.58);
FX.letters(tl,'.vista-word .char',2.65,{duration:.38,stagger:.025});
tl.from('.scan-corners b',{scaleX:.2,opacity:0,stagger:.03,duration:.35,ease:'power3.out'},2.85);
tl.to('.vista-sheen',{'--light-x':'130%',duration:.5,ease:'power2.inOut'},3.03);
tl.to('.red-light',{opacity:1,duration:.45,ease:'power2.out'},2.6);

// LOCAL: the question opens an iris into the real place. Mask and rim share a proxy.
FX.iris(tl,'#middle-mask',3.82,{duration:.65,cx:540,cy:1040,borderSelector:'#iris-ring'});
tl.set('#hook',{opacity:0},4.47);
tl.to('#iris-border',{opacity:0,duration:.18,ease:'power2.out'},4.35);
tl.from('.local-overline',{x:-45,opacity:0,duration:.45,ease:'power2.out'},4.02);
tl.from('#recognition h1',{x:-100,rotationY:12,opacity:0,duration:.65,ease:'power4.out'},4.08);
tl.from('.city-stack',{y:130,rotationY:-18,scale:.72,opacity:0,duration:.75,ease:'power3.out'},4.12);
tl.from('.city-backplate',{x:-40,y:-40,stagger:.07,duration:.7,ease:'power2.out'},4.25);
tl.to('.city-photo',{rotationY:5,rotationX:0,rotation:1,y:-10,duration:2.3,ease:'sine.inOut'},5.1);
tl.from('.recognition-caption',{x:80,opacity:0,duration:.45,ease:'power3.out'},5.3);
FX.draw(tl,'.local-arrow path',5.75,.65);
tl.to('.red-light',{opacity:0,duration:.6,ease:'power2.out'},4.1);

// CASE: a shared 2160px strip guarantees equal velocity across the seam.
FX.whip(tl,'#middle-track',7.75,{duration:.55,width:1080,blurSelector:'#whip-blur'});
tl.from('.case-kicker',{x:-35,opacity:0,duration:.45,ease:'power2.out'},8.02);
tl.from('.case-title span',{y:65,rotationX:25,opacity:0,stagger:.08,duration:.55,ease:'power3.out'},8.02);
tl.from('#film-shell',{rotationY:24,rotation:-7,scale:.85,x:70,y:45,duration:.75,ease:'power4.out'},8.02);
tl.fromTo('.film-face',{clipPath:'inset(0 0 100% 0 round 35px)'},{clipPath:'inset(0% 0% 0% 0% round 35px)',duration:.65,ease:'power3.inOut',immediateRender:false},8.1);
tl.from('.process-column',{x:-80,opacity:0,duration:.6,ease:'power3.out'},8.15);
tl.from('.film-tag',{y:20,opacity:0,duration:.4,ease:'power2.out'},8.65);
tl.to('.film-sweep',{'--light-x':'145%',duration:.8,ease:'power2.inOut'},8.7);
tl.to('#film-shell',{rotationY:-7,rotation:2,y:-10,duration:1.4,ease:'sine.inOut'},9.1);
// Same film object recedes; process text becomes the dominant plane.
tl.to('#process-rail',{y:-290,duration:.48,ease:'power3.inOut'},10.45);
tl.to('#film-shell',{scale:.87,x:20,rotationY:12,rotation:-3,duration:.65,ease:'power3.inOut'},10.45);
tl.to('.process-marker i:nth-child(1)',{backgroundColor:'#26344A',duration:.2},10.45);
tl.to('.process-marker i:nth-child(2)',{backgroundColor:'#54A6FF',duration:.2},10.45);
tl.to('.objective-note',{opacity:1,duration:.45,ease:'power2.out'},10.65);
tl.to('#process-rail',{y:-580,duration:.48,ease:'power3.inOut'},12.78);
tl.to('.process-marker i:nth-child(2)',{backgroundColor:'#26344A',duration:.2},12.78);
tl.to('.process-marker i:nth-child(3)',{backgroundColor:'#54A6FF',duration:.2},12.78);
tl.to('#film-shell',{rotationY:0,rotation:0,x:5,y:0,duration:.65,ease:'power3.out'},12.78);

// PROOF: diagonal shutter deliberately hides the change of material/frame.
// It is an authored transition, not a fade of a whole dark canvas.
tl.to('.gate-two',{x:0,duration:.28,ease:'power3.inOut'},14.7);
tl.to('.gate-one',{x:0,duration:.28,ease:'power3.inOut'},14.75);
tl.set('#results',{opacity:1},14.99);
tl.set('#middle-mask',{opacity:0},14.99);
tl.to('.gate-two',{x:2800,duration:.28,ease:'power3.inOut'},15.01);
tl.to('.gate-one',{x:2800,duration:.28,ease:'power3.inOut'},15.06);
tl.from('.results-kicker',{y:40,opacity:0,duration:.4,ease:'power2.out'},14.95);
tl.from('#proof-paper',{rotationY:65,rotation:-8,scale:1.45,x:-200,y:-120,opacity:0,duration:.65,ease:'power3.out'},14.96);
tl.to('#proof-paper',{rotation:3,rotationY:-5,duration:2,ease:'sine.inOut'},16);
tl.from('.proof-copy',{x:-60,opacity:0,duration:.45,ease:'power3.out'},15.12);
FX.draw(tl,'.proof-mark path,.proof-mark polygon',15.5,.55);
tl.from('.metrics-window',{y:45,opacity:0,duration:.5,ease:'power3.out'},15.3);
function count(selector,value,at,duration=.6){
  const frames=Math.round(duration*30);tl.set(selector,{textContent:'0'},at);
  for(let f=0;f<=frames;f++)tl.set(selector,{textContent:Math.round(value*(1-Math.pow(1-f/frames,3))).toLocaleString('pt-BR')},at+f/30);
}
count('#impression-value',20981,15.3,.6);
tl.from('#impression-value',{scale:.94,transformOrigin:'0% 50%',duration:.6,ease:'power4.out'},15.3);
tl.to('#metric-rail',{y:-415,duration:.48,ease:'power3.inOut'},18.05);
count('#reach-value',13064,18.2,.6);
tl.to('#proof-paper',{rotation:-3,y:-12,duration:.6,ease:'power3.inOut'},18.05);

// INVITATION: the source-document footprint expands into the invitation support.
// Supplied rectangles avoid font-time measurements; typography is a separate plane.
tl.fromTo('#invitation',{opacity:1,clipPath:'polygon(54% 49%,91% 49%,91% 86%,54% 86%)'},{opacity:1,clipPath:'polygon(0% 0%,100% 0%,100% 100%,0% 100%)',duration:.68,ease:'power3.inOut',immediateRender:false},20.82);
tl.to('#results',{opacity:0,scale:.94,rotationY:-8,filter:'blur(5px)',duration:.48,ease:'power3.inOut'},20.82);
tl.set('#results',{opacity:0},21.5);
FX.flipBox(tl,'#cta-frame',20.86,{from:{x:600,y:1000,width:360,height:642},to:{x:90,y:800,width:900,height:555},duration:.75,innerSelector:'.frame-light'});
tl.from('#relevance-a',{x:-140,rotationY:20,opacity:0,duration:.6,ease:'power4.out'},21.15);
tl.from('#relevance-b',{x:180,rotationY:-15,opacity:0,duration:.65,ease:'power3.out'},21.45);
tl.to('.frame-light',{'--light-x':'140%',duration:.8,ease:'power2.inOut'},22);
tl.from('.strategy-diagram',{y:45,opacity:0,duration:.4,ease:'power3.out'},21.4);
FX.draw(tl,'.strategy-icon path,.strategy-icon circle',21.5,.55);
FX.draw(tl,'.strategy-link path',21.8,.5);
tl.to('.strategy-diagram',{opacity:0,y:-45,duration:.35,ease:'power3.inOut'},23.1);
tl.to('.relevance',{scale:.75,x:-45,y:-50,transformOrigin:'0% 0%',duration:.65,ease:'power3.inOut'},23.15);
FX.focus(tl,'.invite-question',23.4,.55);
// Staggered semantic shift: empresa -> serviço. Top line follows grammatical gender.
tl.to('#invite-word-rail',{y:-126,duration:.42,ease:'power3.inOut'},26.25);
tl.set('.invite-top',{textContent:'E o seu'},26.46);
tl.from('#cta-button',{scaleX:.14,scaleY:.7,opacity:0,transformOrigin:'0% 50%',duration:.65,ease:'power4.out'},25.35);
tl.from('#cta-button>span',{y:25,opacity:0,duration:.4,ease:'power2.out'},25.75);
FX.draw(tl,'#cta-outline rect',25.55,.85);
FX.draw(tl,'.cta-arrow path',26.1,.55);
tl.from('.cta-arrow',{x:-20,y:20,opacity:0,duration:.45,ease:'power3.out'},26.05);
tl.to('#cta-button',{scale:1.025,duration:.25,ease:'sine.out',yoyo:true,repeat:1},27.75);
FX.letters(tl,'.end-wordmark .char',26.75,{duration:.5,stagger:.04});
tl.from('.end-wordmark',{x:75,opacity:0,duration:.55,ease:'power3.out'},26.75);
tl.to('.cta-arrow',{x:7,y:-7,duration:.38,ease:'sine.inOut',yoyo:true,repeat:1},28.05);
// Deterministic texture offset, not CSS animation or a timer.
tl.to('.blue-light',{x:-100,y:100,scale:1.1,duration:15,ease:'sine.inOut'},0);
tl.to('.blue-light',{x:80,y:-20,scale:1,duration:15,ease:'sine.inOut'},15);
for(let i=0;i<60;i++)tl.set('.grain',{x:(i*17%23)-11,y:(i*13%19)-9},i*.5);
window.EVOQUEX_AUDIT={version:'V12',engine:'HyperFrames 0.8.162',duration:30,business:'Danny’s Presentes',reach:13064,impressions:20981,view_count_claimed:false,non_follower_count_claimed:false,original_video_playbacks:1,original_audio_gain:0,voice:false,luciane_rendered:false,reference_audio_used:false};
tl.seek(0);
