/* V12 — reference-led kinetic advertising, deterministic HyperFrames/GSAP.
 * Concrete origins and rendered acceptance frames: REFERENCE-IMPLEMENTATION.md.
 * Each phase is a different composition, connected by actual moving objects.
 */
const tl=window.__timelines['evoquex-hf-v14'];
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



// V14: semantic matter and camera choreography, authored after fresh reference audit.
const M=window.EvoquexV14;M.glyphs();gsap.registerPlugin(MotionPathPlugin);
const mass=M.mesh('#facet-mesh');
FX.iris(tl,'#continuum',3.82,{duration:.62,cx:540,cy:1040,borderSelector:'#iris-ring'});
tl.set('#hook',{opacity:0},4.45);tl.to('#iris-border',{opacity:0,duration:.16,ease:'power2.out'},4.3);
tl.to('.red-light',{opacity:0,duration:.4,ease:'power2.out'},4.1);
//4–6.6: letters open a real landscape; the landscape becomes the next film aperture.
M.letters(tl,'.local-ja',3.97,{y:-75,x:16,rx:-35,stagger:.022,duration:.38});
M.letters(tl,'.local-aqui',4.22,{y:100,x:18,rx:70,stagger:.023,duration:.43});
tl.fromTo('#local-phrase',{rotation:-8,x:55},{rotation:0,x:0,duration:.55,ease:'back.out(1.08)',immediateRender:false},4.08);
tl.to('#local-phrase',{y:-90,scale:.88,transformOrigin:'0% 0%',duration:.55,ease:'power3.inOut'},4.85);
tl.set('#city-fragment',{opacity:1},4.9);
tl.fromTo('.city-stripe',{x:(i)=>i%2?-1100:1100,rotationY:(i)=>i%2?-25:25},{x:0,rotationY:0,duration:.53,stagger:.075,ease:'power4.out',immediateRender:false},4.9);
M.draw(tl,'#city-trace',5.2,.55);
tl.fromTo('#city-fragment',{rotation:-7,rotationX:16,scale:.94},{rotation:3,rotationX:-4,scale:1,duration:.9,ease:'power3.inOut',immediateRender:false},5.25);
M.letters(tl,'#local-caption span',5.35,{y:65,rx:0,stagger:.013,duration:.35});
M.letters(tl,'#local-caption strong',5.57,{y:80,rx:45,stagger:.012,duration:.39});
//The transition is a white wedge travelling through the existing photographic strata.
tl.set('#transition-ribbon',{opacity:1},6.28);
tl.fromTo('#transition-ribbon',{x:0,rotation:-14},{x:1750,rotation:-8,duration:.34,ease:'power4.inOut',immediateRender:false},6.28);
tl.set('#production-scene',{opacity:1},6.57);
tl.to('#transition-ribbon',{x:3700,rotation:-3,duration:.27,ease:'power3.in'},6.57);
tl.to('#city-fragment',{rotationX:65,y:100,scaleY:.45,duration:.38,ease:'power3.inOut'},6.29);
tl.set('#local-scene',{opacity:0},6.96);
//6.6–9.2: a short real film in three lamellae; the brief is motion, never a phone mockup.
M.letters(tl,'#production-heading span',6.61,{y:100,rx:55,stagger:.016,duration:.41});
M.letters(tl,'#production-heading strong',6.8,{y:85,rx:-45,stagger:.023,duration:.43});
tl.set('#film-rig',{opacity:1},6.9);
tl.fromTo('#film-rig',{rotation:-9,x:50,y:100,scale:.85},{rotation:-5,x:0,y:0,scale:1,duration:.53,ease:'back.out(1.08)',immediateRender:false},6.88);
tl.fromTo('#slit-a,#slit-b,#slit-c',{attr:{height:0}},{attr:{height:190},duration:.39,stagger:.055,ease:'power4.out',immediateRender:false},6.91);
tl.fromTo('#film-lines',{opacity:0,x:250},{opacity:1,x:0,duration:.44,ease:'power3.out',immediateRender:false},7.03);
M.letters(tl,'#client-name span',7.35,{y:70,rx:45,stagger:.018,duration:.4});
M.letters(tl,'#client-name strong',7.52,{y:80,rx:-35,stagger:.016,duration:.43});
tl.to('#production-heading',{x:30,y:-55,rotation:-3,scale:.93,transformOrigin:'0% 0%',duration:.65,ease:'power3.inOut'},8.12);
tl.to('#film-rig',{rotation:5,scale:1.06,x:-20,duration:.67,ease:'sine.inOut'},8.25);
tl.fromTo('#facet-position',{opacity:0,x:850,y:190,scale:.18},{opacity:1,x:850,y:190,scale:.65,duration:.48,ease:'back.out(1.1)',immediateRender:false},7.65);
tl.to('#facet-rotation',{rotation:12,duration:.9,ease:'sine.inOut'},7.65);
//9.0: the white filming plane folds aside while the play object becomes a distribution arrow.
tl.set('#distribution-scene',{opacity:1},8.98);
tl.to('#production-scene',{x:-1200,rotation:-5,duration:.46,ease:'power3.inOut'},9.0);
tl.to('#film-lines',{x:1300,duration:.38,ease:'power4.in'},9.0);
tl.to('#facet-position',{x:580,y:1230,scale:1.1,duration:.65,ease:'power3.inOut'},9.0);
mass.morph(tl,1,9.0,.62);tl.to('#facet-rotation',{rotation:-17,duration:.6,ease:'power3.inOut'},9.0);
tl.set('#production-scene',{opacity:0},9.47);
M.letters(tl,'#distribution-heading',9.19,{y:110,rx:-60,stagger:.014,duration:.4});
M.letters(tl,'#distribution-by',9.53,{y:75,rx:35,stagger:.03,duration:.32});
tl.fromTo('#distribution-band',{scaleX:.05,rotation:11},{scaleX:1,rotation:-5,duration:.48,ease:'back.out(1.12)',immediateRender:false},9.72);
M.letters(tl,'#distribution-brand span',9.82,{y:85,rx:65,stagger:.024,duration:.43});
M.draw(tl,'#flight-a',9.7,.8);M.draw(tl,'#flight-b',9.83,.78);M.draw(tl,'#flight-c',9.94,.76);
tl.to('#facet-position',{x:790,y:1160,scale:.9,duration:.8,ease:'power2.inOut'},10.1);
tl.to('#facet-rotation',{rotation:12,duration:.8,ease:'sine.inOut'},10.1);
tl.fromTo('#distribution-objective',{x:-80,opacity:0},{x:0,opacity:1,duration:.4,ease:'power2.out',immediateRender:false},10.36);
tl.to('#distribution-brand',{x:30,rotation:-3,duration:.65,ease:'sine.inOut'},10.47);
//11.35: arrow folds into a pin, while the locality plane is revealed by its direction.
tl.fromTo('#target-scene',{opacity:1,clipPath:'polygon(100% 0%,100% 0%,100% 100%,100% 100%)'},{opacity:1,clipPath:'polygon(0% 0%,100% 0%,100% 100%,0% 100%)',duration:.51,ease:'power4.inOut',immediateRender:false},11.32);
mass.morph(tl,2,11.35,.65);
tl.to('#facet-position',{x:540,y:1120,scale:1.22,duration:.66,ease:'power3.inOut'},11.35);
tl.to('#facet-rotation',{rotation:-4,duration:.66,ease:'power3.inOut'},11.35);
tl.fromTo('#facet-pin-hole',{opacity:0,scale:.1,transformOrigin:'0px -43px'},{opacity:1,scale:1,duration:.3,ease:'back.out(1.1)',immediateRender:false},11.91);
M.letters(tl,'#target-small',11.62,{y:-80,rx:-40,stagger:.025,duration:.4});
M.letters(tl,'#target-city',11.9,{y:100,rx:65,stagger:.014,duration:.45});
tl.fromTo('#target-city',{rotation:7,x:35},{rotation:0,x:0,duration:.55,ease:'power3.inOut',immediateRender:false},11.92);
M.draw(tl,'#target-ray-a,#target-ray-b',12.25,.72);
tl.fromTo('#target-shadow',{scaleX:.2,opacity:0,transformOrigin:'50% 50%'},{scaleX:1,opacity:1,duration:.55,ease:'power3.out',immediateRender:false},12.0);
tl.to('#facet-position',{y:1060,scale:1.15,duration:.9,ease:'sine.inOut'},12.4);
tl.to('#facet-rotation',{rotation:9,duration:.9,ease:'sine.inOut'},12.4);
//13.6: the actual pin grows into the blue proof field, preserving spatial identity.
tl.to('#facet-pin-hole',{opacity:0,scale:.2,duration:.18,ease:'power2.in'},13.46);
mass.morph(tl,3,13.55,.47);
tl.to('#facet-position',{x:540,y:1080,scale:8,duration:.59,ease:'power3.in'},13.59);
tl.fromTo('#proof-scene',{opacity:1,clipPath:'circle(0px at 540px 1080px)'},{opacity:1,clipPath:'circle(1500px at 540px 1080px)',duration:.55,ease:'power3.in',immediateRender:false},13.62);
tl.set('#facet-position',{opacity:0},14.16);
//14–18: one precise metric; no reinterpretation of the older screenshot.
tl.fromTo('#twenty .slice',{x:(i)=>[260,-170,100][i],y:(i)=>[-90,80,140][i],rotationY:(i)=>[45,-35,20][i],opacity:0},{x:0,y:0,rotationY:0,opacity:1,duration:.52,stagger:.045,ease:'power4.out',immediateRender:false},14.12);
M.letters(tl,'#thousand',14.38,{y:95,rx:-75,stagger:.035,duration:.5});
M.letters(tl,'#proof-unit',14.72,{y:80,rx:55,stagger:.012,duration:.43});
tl.fromTo('#proof-echo',{x:250,rotation:12,opacity:0},{x:-40,rotation:-7,opacity:.55,duration:1.1,ease:'power3.inOut',immediateRender:false},14.4);
M.letters(tl,'#proof-qualifier span',15.3,{y:75,rx:0,stagger:.012,duration:.4});
M.letters(tl,'#proof-qualifier strong',15.54,{y:100,rx:-45,stagger:.014,duration:.43});
//Camera follow: explicit fitted box carries all words together, rather than changing a card.
M.camera(tl,'#proof-camera',[-20,80,1100,1800],15.9,.72,1);
tl.to('#proof-echo',{x:-150,y:-50,rotation:-12,duration:1.4,ease:'sine.inOut'},15.6);
//17.6: the proof field peels to the next thought; the zero's point continues as a message.
tl.fromTo('#strategy-scene',{opacity:1,clipPath:'polygon(0% 100%,100% 100%,100% 100%,0% 100%)'},{opacity:1,clipPath:'polygon(0% 0%,100% 0%,100% 100%,0% 100%)',duration:.6,ease:'power3.inOut',immediateRender:false},17.57);
tl.to('#proof-camera',{rotation:-7,scale:.82,x:-85,y:-100,duration:.6,ease:'power3.inOut'},17.58);
tl.set('#facet-layer',{zIndex:12},17.58);
tl.fromTo('#facet-position',{opacity:0,x:360,y:880,scale:.12},{opacity:1,x:260,y:1230,scale:.48,duration:.75,ease:'power3.inOut',immediateRender:false},17.65);
mass.morph(tl,4,17.85,.55);tl.to('#facet-rotation',{rotation:0,duration:.5,ease:'power3.inOut'},17.85);
M.letters(tl,'#strategy-one',18.0,{y:-110,rx:-50,stagger:.012,duration:.4});
M.letters(tl,'#strategy-two span',18.47,{y:75,rx:40,stagger:.025,duration:.35});
M.letters(tl,'#strategy-two strong',18.66,{y:90,rx:60,stagger:.017,duration:.44});
tl.set('#graph-message .graph-icon',{opacity:0},0);
tl.fromTo('#graph-message text',{opacity:0,y:45},{opacity:1,y:0,duration:.4,ease:'power2.out',immediateRender:false},18.6);
M.draw(tl,'#graph-audience circle',18.7,.62);
tl.fromTo('#graph-audience text',{opacity:0,y:35},{opacity:1,y:0,duration:.4,ease:'power2.out',immediateRender:false},18.95);
M.draw(tl,'#graph-path',19.05,.62);
tl.fromTo('#graph-traveller',{opacity:0},{opacity:1,duration:.1,ease:'none',immediateRender:false},19.1);
tl.to('#graph-traveller',{motionPath:{path:'#graph-path',align:'#graph-path',alignOrigin:[.5,.5],autoRotate:false},duration:.7,ease:'power2.inOut'},19.1);
tl.to('#strategy-graph',{y:-60,rotation:-8,scale:1.05,transformOrigin:'540px 1230px',duration:.68,ease:'power3.inOut'},19.7);
tl.to('#facet-position',{x:255,y:1175,scale:.47,duration:.68,ease:'power3.inOut'},19.7);
tl.to('#strategy-two',{x:12,y:25,rotation:-3,duration:.65,ease:'power3.inOut'},19.7);
//20.45–26: a continuous route through company, service and the human invitation.
tl.fromTo('#cta-scene',{opacity:1,clipPath:'polygon(0% 100%,100% 100%,100% 100%,0% 100%)'},{opacity:1,clipPath:'polygon(0% 0%,100% 0%,100% 100%,0% 100%)',duration:.56,ease:'power4.inOut',immediateRender:false},20.4);
tl.set('#facet-position',{opacity:0},20.97);
M.letters(tl,'.cta-station-a .cta-lead',20.63,{y:70,rx:-40,stagger:.025,duration:.35});
M.letters(tl,'.cta-station-a .cta-focus',20.86,{y:110,rx:65,stagger:.024,duration:.45});
//The words have fixed stations. The camera travels; the layout does not crossfade.
M.camera(tl,'#cta-world',[1080,0,2160,1920],21.67,.64,1);
M.letters(tl,'.cta-station-b .cta-lead',21.93,{y:-75,rx:-40,stagger:.022,duration:.35});
M.letters(tl,'.cta-station-b .cta-focus',22.08,{y:100,rx:70,stagger:.026,duration:.42});
M.camera(tl,'#cta-world',[1080,525,2160,2445],22.8,.65,1);
tl.to('#cta-blue-field',{clipPath:'polygon(0% 0%,100% 0%,100% 100%,0% 100%)',duration:.64,ease:'power3.inOut'},22.81);
M.letters(tl,'#cta-conversa',23.0,{y:110,rx:-55,stagger:.025,duration:.47});
M.letters(tl,'#cta-gente',23.55,{y:95,rx:45,stagger:.018,duration:.42});
M.draw(tl,'#cta-curve',23.8,.6);
tl.to('.cta-station-a,.cta-station-b',{clipPath:'inset(0% 0% 100% 0%)',duration:.28,ease:'power3.inOut'},23.02);
tl.set('.cta-station-a,.cta-station-b',{opacity:0},23.31);
M.camera(tl,'#cta-world',[1080,300,2160,2220],24.05,.85,1);
M.letters(tl,'#cta-signature',24.45,{y:70,rx:-40,stagger:.025,duration:.43});
M.draw(tl,'#cta-arrow',24.35,.7);
