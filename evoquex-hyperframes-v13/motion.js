/* V12 — reference-led kinetic advertising, deterministic HyperFrames/GSAP.
 * Concrete origins and rendered acceptance frames: REFERENCE-IMPLEMENTATION.md.
 * Each phase is a different composition, connected by actual moving objects.
 */
const tl=window.__timelines['evoquex-hf-v13'];
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


// V13: exact approved hook above; new world choreography only from t=4.
const M=window.EvoquexV13;M.glyphs();gsap.registerPlugin(MotionPathPlugin);
FX.iris(tl,'#middle-mask',3.82,{duration:.65,cx:540,cy:1040,borderSelector:'#iris-ring'});
tl.set('#hook',{opacity:0},4.47);tl.to('#iris-border',{opacity:0,duration:.18,ease:'power2.out'},4.35);
tl.to('.red-light',{opacity:0,duration:.6,ease:'power2.out'},4.1);
tl.set('#recognition-plane',{opacity:1},4);
// LOCAL: type itself is the photographic aperture; the image expands in its place.
tl.from('.place-overline',{x:-125,rotation:-6,opacity:0,duration:.42,ease:'power2.out'},4.02);
M.letters(tl,'.recognition-javiu',4.04,{y:-160,x:22,rot:58,stagger:.025,duration:.44});
tl.from('#flat-query',{x:780,y:80,rotation:-10,transformOrigin:'540px 800px',duration:.5,ease:'back.out(1.08)'},4.35);
tl.from('#masked-city',{opacity:0,duration:.15,ease:'none'},5.04);
tl.to('#flat-query',{opacity:0,duration:.15,ease:'none'},5.04);
tl.to('.recognition-javiu',{y:-70,x:0,scale:.85,transformOrigin:'0 0',duration:.55,ease:'power3.inOut'},5.08);
tl.to('#city-open',{attr:{y:600,height:607},duration:.68,ease:M.e85},5.15);
tl.from('#masked-city',{x:-80,duration:.85,ease:'power2.out'},5.1);
tl.fromTo('#flow-outline',{opacity:0},{opacity:1,duration:.25,ease:'power2.out',immediateRender:false},5.55);
tl.set('#flow-outline',{opacity:1},5.8);
M.letters(tl,'.recog-small',5.62,{y:80,rot:-40,stagger:.01,duration:.42});
M.slices(tl,'#recog-divulgacoes',5.86,{distance:100,duration:.5});
tl.to('#masked-city',{x:18,duration:1.05,ease:'sine.inOut'},6.15);
// The photographic border compresses to a line and becomes the next film aperture.
M.frame(tl,{x:80,y:1480,width:920,height:8,rx:0},7.12,.45);
tl.to('#city-open',{attr:{y:1135,height:0},duration:.5,ease:'power3.inOut'},7.15);
tl.to('#motion-world',{y:-1920,duration:.62,ease:M.e85},7.64);
M.frame(tl,{x:425,y:625,width:560,height:995,rx:0},7.66,.75);
// CASE: one film object; typography and media trade foreground, never a phone mockup.
tl.from('.case-overline-v13',{x:120,opacity:0,duration:.4,ease:'power2.out'},7.93);
M.letters(tl,'.client-name',7.96,{y:90,rot:35,stagger:.016,duration:.48});
tl.from('#campaign-rig',{x:90,y:200,rotationY:-28,rotationZ:8,duration:.67,ease:'back.out(1.05)'},8.02);
tl.to('.campaign-viewport',{clipPath:'inset(0% 0% 0% 0%)',duration:.65,ease:M.e85},8.1);
tl.from('.campaign-tag',{y:45,opacity:0,duration:.45,ease:'power3.out'},8.55);
M.letters(tl,'.produzimos',8.22,{y:170,x:0,rot:45,stagger:.017,duration:.5});
M.letters(tl,'.ovideo',8.5,{y:0,x:100,rot:-30,stagger:.024,duration:.48});
tl.to('#production-type',{x:-20,y:-45,rotationY:-9,scale:.42,transformOrigin:'0% 0%',duration:.65,ease:'power3.inOut'},9.5);
tl.to('#campaign-rig',{left:390,top:590,width:600,height:1066,rotationZ:-2,rotationY:0,duration:.7,ease:'power3.inOut'},9.5);
M.frame(tl,{x:390,y:590,width:600,height:1066},9.5,.7);
tl.to('.campaign-tag',{opacity:0,duration:.22,ease:'power2.out'},10.4);
// The previous phrase is carried around a hinge as the next one enters its plane.
tl.to('#production-type',{x:-1100,rotationY:65,y:-40,duration:.52,ease:M.e85},10.35);
tl.set('#distribution-type',{opacity:0},0);tl.set('#distribution-type',{opacity:1},10.4);
M.letters(tl,'.divulgamos',10.42,{y:-130,x:24,rot:80,stagger:.012,duration:.5});
tl.from('.pela',{x:180,rotationY:65,opacity:0,duration:.5,ease:'power4.out'},10.72);
tl.to('.label-field',{scaleX:1,duration:.55,ease:M.e85},10.85);
M.slices(tl,'#distribution-brand',10.93,{distance:170,duration:.54});
tl.to('#campaign-rig',{left:655,top:1090,width:320,height:568,rotationZ:6,rotationY:-10,duration:.7,ease:M.e85},10.4);
M.frame(tl,{x:655,y:1090,width:320,height:568},10.4,.7);
tl.from('.objective-v13',{x:-180,rotationX:30,opacity:0,duration:.5,ease:'power3.out'},11.23);
tl.to('#distribution-type',{rotationZ:-3,x:-10,duration:.45,ease:'power2.inOut'},11.65);
// Locality is a wide typographic field, with the same film re-cut into a wide window.
tl.to('#distribution-type',{y:-1100,x:180,rotationX:55,duration:.58,ease:M.e85},12.48);
M.letters(tl,'.sopara',12.74,{y:-85,x:40,rot:50,stagger:.025,duration:.4});
M.letters(tl,'.clevelandia-word',12.85,{y:150,x:0,rot:-65,stagger:.018,duration:.5});
tl.to('#campaign-rig',{left:140,top:1030,width:800,height:520,rotationZ:0,rotationY:0,duration:.7,ease:M.e85},12.75);
M.frame(tl,{x:140,y:1030,width:800,height:520},12.75,.7);
// PROOF: the frame survives the travelling scene; there is no empty colour pause.
tl.to('#motion-world',{y:-3840,duration:.65,ease:M.e85},14.63);
M.frame(tl,{x:605,y:900,width:370,height:660},14.65,.7);
tl.from('.proof-overline-v13',{x:-100,rotationX:35,opacity:0,duration:.45,ease:'power2.out'},15.02);
M.slices(tl,'#impression-value',15.12,{distance:240,duration:.55});
M.letters(tl,'#proof-metric-a .metric-title',15.34,{y:100,x:0,rot:65,stagger:.015,duration:.43});
tl.from('#proof-metric-a .metric-definition',{x:95,opacity:0,duration:.4,ease:'power3.out'},15.52);
// Documentary image unfolds as complementary panels, not a fabricated dashboard.
for(let i=0;i<3;i++)tl.from('.paper-'+i,{x:(i-1)*180,y:[80,-100,50][i],rotationY:[65,-65,65][i],opacity:0,duration:.65,ease:'power3.out'},15.2+i*.1);
tl.from('#proof-description',{y:120,opacity:0,duration:.5,ease:'power2.out'},15.7);
FX.draw(tl,'.proof-pointer path',16.02,.65);
tl.to('#proof-metric-a',{y:-45,rotationZ:-3,transformOrigin:'0 50%',duration:.6,ease:'sine.inOut'},16.55);
// Direction / hierarchy swap: old metric and label travel together, new ones together.
tl.to('#proof-metric-a',{x:-1130,y:70,rotationZ:-8,duration:.58,ease:M.e85},17.8);
tl.from('#proof-metric-b',{x:1150,rotationZ:7,duration:.58,ease:M.e85},17.88);
tl.from('#proof-metric-b .digit-group',{y:(i)=>i?140:-140,rotationX:(i)=>i?-75:75,stagger:.055,duration:.48,ease:'back.out(1.06)'},17.98);
M.letters(tl,'.reach-title',18.16,{y:70,x:0,rot:-45,stagger:.008,duration:.38});
tl.from('#proof-metric-b .metric-definition',{x:75,opacity:0,duration:.38,ease:'power3.out'},18.35);
tl.to('#document-rig',{left:115,top:420,width:380,height:676,rotationZ:-6,rotationY:8,duration:.65,ease:M.e85},17.82);
M.frame(tl,{x:115,y:420,width:380,height:676},17.82,.65);
tl.to('#proof-description',{x:500,y:-380,scale:.8,transformOrigin:'0 0',duration:.65,ease:'power3.inOut'},17.82);
// INVITATION: lateral station, the shared outline collapses into a live connector.
tl.to('#motion-world',{x:-1080,duration:.65,ease:M.e85},20.7);
M.frame(tl,{x:250,y:1060,width:580,height:5,rx:0},20.72,.68);
tl.to('#flow-outline',{opacity:0,duration:.2,ease:'power2.out'},21.45);
M.letters(tl,'#relevance-one',21.04,{y:-135,x:14,rot:-55,stagger:.016,duration:.48});
M.letters(tl,'#relevance-two',21.24,{y:150,x:-14,rot:55,stagger:.016,duration:.5});
tl.from('#relevance-two',{rotationZ:5,x:80,duration:.55,ease:'back.out(1.1)'},21.24);
tl.from('#message-node',{x:-220,y:95,rotationY:70,opacity:0,duration:.6,ease:'power4.out'},21.65);
tl.from('#audience-node',{x:220,y:-95,rotationY:-70,opacity:0,duration:.6,ease:'power3.out'},21.8);
FX.draw(tl,'.diagram-icon path,.diagram-icon circle',21.85,.65);
FX.draw(tl,'#link-curve',22.1,.7);
tl.from('#traveller',{opacity:0,duration:.08,ease:'none'},22.15);
tl.to('#traveller',{motionPath:{path:'#link-curve',align:'#link-curve',alignOrigin:[.5,.5]},duration:.7,ease:'power2.inOut'},22.15);
tl.to('#audience-node',{scale:1.12,duration:.16,ease:'power2.out',repeat:1,yoyo:true},22.77);
// Connector becomes the boundary; the wording remains fixed while space redistributes.
tl.to('#diagram-v13',{y:0,scaleY:.1,scaleX:1.6,transformOrigin:'50% 1050px',duration:.6,ease:M.e85},23.35);
tl.to('#diagram-v13',{opacity:0,duration:.12,ease:'none'},23.95);
tl.to('#relevance-one',{y:-65,scale:.72,transformOrigin:'0 0',duration:.55,ease:'power3.inOut'},23.4);
tl.to('#relevance-two',{y:-100,scale:.72,rotationZ:0,x:0,transformOrigin:'0 0',duration:.55,ease:'power3.inOut'},23.4);
tl.set('#cta-field',{opacity:1},23.85);tl.to('#cta-field',{top:1030,height:890,duration:.7,ease:M.e85},23.85);
tl.from('.question-lead',{x:-160,y:-30,rotationZ:-7,opacity:0,duration:.46,ease:'power3.out'},23.94);
M.letters(tl,'#company-ask',24.03,{y:180,x:8,rot:75,stagger:.02,duration:.48});
M.letters(tl,'.cta-conversa',25.05,{y:-120,x:-35,rot:-65,stagger:.022,duration:.5});
M.letters(tl,'.cta-gente',25.28,{y:110,x:25,rot:55,stagger:.016,duration:.5});
FX.draw(tl,'#cta-underline',25.5,.65);
// Matched-speed type replacement at26.4: word and grammatical lead change together.
tl.to('#company-ask .vchar',{y:-230,rotationX:75,stagger:.014,duration:.2,ease:M.e85},26.24);
M.letters(tl,'#service-ask',26.48,{y:230,x:-22,rot:-75,stagger:.014,duration:.44,ease:M.e85});
tl.set('#company-ask',{opacity:0},26.48);tl.set('.question-lead',{textContent:'E o seu'},26.48);
FX.draw(tl,'#cta-flight',26.95,.95);
M.letters(tl,'.end-signature-v13',27.35,{y:110,x:12,rot:45,stagger:.025,duration:.5});
tl.to('#cta-field',{top:985,height:935,duration:.34,ease:'power2.out'},27.8);
tl.to('#cta-field',{top:1015,height:905,duration:.4,ease:'sine.inOut'},28.14);
// Approved ambient/texture choreography is unchanged, including first120frames.
tl.to('.blue-light',{x:-100,y:100,scale:1.1,duration:15,ease:'sine.inOut'},0);
tl.to('.blue-light',{x:80,y:-20,scale:1,duration:15,ease:'sine.inOut'},15);
for(let i=0;i<60;i++)tl.set('.grain',{x:(i*17%23)-11,y:(i*13%19)-9},i*.5);
window.EVOQUEX_AUDIT={version:'V13',engine:'HyperFrames 0.8.162',duration:30,business:'Danny’s Presentes',reach:13064,impressions:20981,original_video_playbacks:1,original_audio_gain:0,voice:false,luciane_rendered:false,reference_audio_used:false,protected_hook_seconds:4};
tl.seek(0);
