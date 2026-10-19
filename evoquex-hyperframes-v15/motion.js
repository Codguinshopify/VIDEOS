/* V15. One shared paused timeline; scenes, media and audio are anchored to timing.js. */
const tl=window.__timelines['evoquex-hf-v15'];
const T=window.EVOQUEX_TIMING,M=window.EvoquexV14,V=window.EvoquexV15;
const S=(id,offset=0)=>T.scenes[id][0]+offset;
M.glyphs();gsap.registerPlugin(MotionPathPlugin);
Object.entries(T.scenes).forEach(([id,p])=>tl.addLabel(id,p[0]));
document.querySelector('#root').dataset.duration=T.duration;
document.querySelector('#soundtrack').dataset.duration=T.duration;
const mesh=M.mesh('#actor-mesh');
// SVG actors share an explicit local origin; the curved path must not change their pivot.
gsap.set('#actor-position,#actor-rotation',{svgOrigin:'0 0',smoothOrigin:false});
// Fine shading leaves the silhouette dominant; no decorative low-poly rock.
document.querySelector('#actor-mesh').style.filter='saturate(.95)';

// 1. An immediate living type rig: the bar becomes a mask, then the question opens the city.
tl.from('.sua span',{yPercent:13,rotationX:12,duration:.4,ease:'power3.out'},0);
tl.from('.empresa span',{yPercent:12,rotationX:18,duration:.5,ease:'power4.out'},0);
tl.from('.hook-signature',{y:25,opacity:.35,duration:.45,ease:'power2.out'},0);
tl.from('.company-rule',{scaleX:.1,duration:.5,ease:'expo.out'},0);
tl.from('#hook-company',{rotationY:-10,z:90,duration:.5,ease:'power3.out'},0);
tl.to('#hook-company',{x:-1050,rotationY:-25,scale:.82,duration:.35,ease:'power3.inOut'},.70);
tl.fromTo('#hook-known',{opacity:1,x:1080,rotationY:25},{opacity:1,x:0,rotationY:0,duration:.44,ease:'power4.out',immediateRender:false},.74);
tl.from('.known-band',{scale:.62,rotation:10,y:100,duration:.49,ease:'back.out(1.1)'},.81);
tl.to('.known-band',{rotation:-5,duration:.4,ease:'power3.out'},1.04);
tl.from('.known-prefix',{y:-60,opacity:0,duration:.36,ease:'power2.out'},.87);
tl.from('.known-echo',{y:90,opacity:0,rotationX:38,duration:.5,ease:'sine.out'},.82);
tl.to('#hook-known',{y:-1100,rotationX:27,scale:.85,duration:.36,ease:'power3.inOut'},1.59);
tl.fromTo('#hook-city',{opacity:1,y:1120,rotationX:-25},{opacity:1,y:0,rotationX:0,duration:.42,ease:'power4.out',immediateRender:false},1.64);
tl.from('.city-name span',{x:160,rotationY:20,duration:.42,ease:'expo.out'},1.70);
tl.from('.city-underline',{scaleX:0,duration:.43,ease:'power2.inOut'},1.82);
tl.to('#hook-city',{x:1150,rotation:-8,duration:.38,ease:'power3.inOut'},2.47);
tl.fromTo('#hook-question',{opacity:1,x:-1050,rotation:7},{opacity:1,x:0,rotation:0,duration:.43,ease:'power4.out',immediateRender:false},2.51);
tl.from('.question-prefix span',{y:100,duration:.35,ease:'power2.out'},2.61);
M.letters(tl,'.question-word',2.67,{y:90,rx:55,stagger:.023,duration:.42});
V.draw(tl,'#question-curve',3.04,.55,'power3.inOut');
tl.to('.hook-orbit',{scale:.8,x:-110,y:-90,duration:3.5,ease:'sine.inOut'},0);

// 2. A photographic field opens between words. The source is the user's aerial PHOTO.
tl.fromTo('#local-scene',{opacity:1,clipPath:'circle(0px at 540px 1050px)'},{opacity:1,clipPath:'circle(1500px at 540px 1050px)',duration:.62,ease:'power3.inOut',immediateRender:false},S('local',-.22));
V.enter(tl,'#local-ja',S('local',.02),{y:120,duration:.44,ease:'expo.out'});
V.enter(tl,'#local-aqui',S('local',.17),{y:160,rx:30,duration:.52,ease:'power4.out'});
tl.fromTo('#local-title',{rotation:-5,x:50},{rotation:0,x:0,duration:.57,ease:'power3.inOut',immediateRender:false},S('local',.12));
tl.fromTo('#city-photo',{clipPath:'inset(50% 0% 50% 0%)'},{clipPath:'inset(0% 0% 0% 0%)',duration:.56,ease:'power4.inOut',immediateRender:false},S('local',.45));
tl.fromTo('#city-frame',{rotation:-7,rotationY:12,y:80,scale:.85},{rotation:2,rotationY:0,y:0,scale:1,duration:.72,ease:'back.out(1.04)',immediateRender:false},S('local',.45));
tl.fromTo('#city-photo img',{scale:1.12,x:-18},{scale:1.03,x:8,duration:1.6,ease:'sine.inOut',immediateRender:false},S('local',.7));
V.draw(tl,'#city-frame-line',S('local',.72),.65);
V.draw(tl,'#city-connector',S('local',1.55),.65);
// The picture's right contour anticipates the next filmed plane, under the real ink edge.
tl.to('#city-frame',{rotation:-3,y:-15,scale:1.02,duration:.6,ease:'sine.inOut'},S('production',-.5));

// 3. Real pack ink is the transition matte; one real vertical film occupies the main plane.
tl.set('#production-scene',{opacity:1},S('production',-.26));
V.atlas(tl,'#production-scene',S('production',-.26),.62);
V.enter(tl,'#produzimos',S('production',.02),{y:100,duration:.43,ease:'power3.out'});
V.enter(tl,'#o-video',S('production',.16),{y:160,rx:-25,duration:.48,ease:'expo.out'});
tl.fromTo('#film-shell',{x:-90,y:110,rotation:-10,scale:.9},{x:0,y:0,rotation:-3,scale:1,duration:.64,ease:'power4.out',immediateRender:false},S('production',.05));
tl.fromTo('#film-opening',{attr:{height:0}},{attr:{height:995},duration:.53,ease:'power4.inOut',immediateRender:false},S('production',.05));
V.draw(tl,'#film-frame-line',S('production',.35),.72);
V.enter(tl,'#client-first',S('production',.48),{x:140,y:0,duration:.42,ease:'power3.out'});
V.enter(tl,'#client-last',S('production',.63),{x:110,y:0,duration:.46,ease:'expo.out'});
V.draw(tl,'#production-pointer',S('production',1.03),.6);
tl.to('#film-shell',{rotation:2,x:8,y:-14,duration:1.15,ease:'sine.inOut'},S('production',1.1));
tl.fromTo('#actor-position',{opacity:0,x:865,y:620,scale:.18},{opacity:1,x:865,y:620,scale:.51,duration:.49,ease:'back.out(1.08)',immediateRender:false},S('production',.65));
tl.fromTo('#actor-rotation',{rotation:-15},{rotation:8,duration:1.1,ease:'sine.inOut',immediateRender:false},S('production',.65));

// 4. The filmed plane hands off to an actual arrow; the trail wraps around the brand.
tl.fromTo('#distribution-scene',{opacity:1,clipPath:'polygon(100% 0%,100% 0%,100% 100%,100% 100%)'},{opacity:1,clipPath:'polygon(0% 0%,100% 0%,100% 100%,0% 100%)',duration:.50,ease:'power4.inOut',immediateRender:false},S('distribution',-.26));
mesh.morph(tl,1,S('distribution',-.22),.68);
tl.to('#actor-position',{x:130,y:1370,scale:.62,duration:.68,ease:'power3.inOut'},S('distribution',-.22));
tl.to('#actor-rotation',{rotation:-20,duration:.6,ease:'power3.inOut'},S('distribution',-.22));
V.enter(tl,'#divulgamos',S('distribution',.02),{x:-160,y:0,duration:.46,ease:'expo.out'});
V.enter(tl,'#pela',S('distribution',.22),{y:95,duration:.36,ease:'power2.out'});
M.letters(tl,'#brand-word',S('distribution',.42),{y:95,rx:-45,stagger:.025,duration:.45});
tl.fromTo('#brand-back',{opacity:0,y:80},{opacity:1,y:0,duration:.64,ease:'power3.out',immediateRender:false},S('distribution',.48));
V.draw(tl,'#distribution-path',S('distribution',1),.82,'power3.inOut');
V.draw(tl,'#distribution-trace',S('distribution',1.09),.86,'sine.inOut');
tl.to('#actor-position',{motionPath:{path:'#distribution-path',autoRotate:false},duration:.85,ease:'power3.inOut'},S('distribution',1));
tl.to('#actor-rotation',{rotation:-65,duration:.85,ease:'power3.inOut'},S('distribution',1));
tl.to('#distribution-brand',{rotation:-4,x:20,y:20,duration:.75,ease:'sine.inOut'},S('distribution',1.3));

// 5. Arrow→pin: top-heavy composition reverses the prior type hierarchy.
tl.fromTo('#target-scene',{opacity:1,clipPath:'polygon(0% 0%,100% 0%,100% 0%,0% 0%)'},{opacity:1,clipPath:'polygon(0% 0%,100% 0%,100% 100%,0% 100%)',duration:.6,ease:'power3.inOut',immediateRender:false},S('target',-.24));
mesh.morph(tl,2,S('target',-.22),.63);
tl.to('#actor-position',{x:540,y:790,xPercent:0,yPercent:0,scale:1.32,duration:.66,ease:'power3.inOut'},S('target',-.22));
tl.to('#actor-rotation',{rotation:0,duration:.6,ease:'power3.inOut'},S('target',-.22));
// Registry topology completes the transition, then resolves to a smooth final contour.
tl.to('#actor-smooth-pin',{opacity:1,duration:.18,ease:'power2.out'},S('target',.42));
tl.to('#actor-mesh',{opacity:0,duration:.18,ease:'power2.out'},S('target',.42));
tl.fromTo('#actor-hole',{opacity:0,scale:.1,transformOrigin:'0px -43px'},{opacity:1,scale:1,duration:.33,ease:'back.out(1.12)',immediateRender:false},S('target',.26));
V.enter(tl,'#so-para',S('target',.1),{x:-120,y:0,duration:.44,ease:'expo.out'});
V.enter(tl,'#clevelandia',S('target',.34),{y:150,rx:30,duration:.52,ease:'power4.out'});
tl.fromTo('#pin-shadow',{opacity:0,scaleX:.4,transformOrigin:'540px 1060px'},{opacity:.8,scaleX:1,duration:.5,ease:'power3.out',immediateRender:false},S('target',.35));
tl.fromTo('#pin-contact',{opacity:0,scale:.4,transformOrigin:'540px 1050px'},{opacity:1,scale:1,duration:.68,ease:'power3.out',immediateRender:false},S('target',1.1));
tl.fromTo('#pin-contact-outer',{opacity:0,scale:.5,transformOrigin:'540px 1050px'},{opacity:.5,scale:1,duration:.82,ease:'sine.out',immediateRender:false},S('target',1.22));
tl.to('#actor-position',{y:775,scale:1.27,duration:.85,ease:'sine.inOut'},S('target',1.1));

// 6. The pin's contact area becomes a luminous proof field. No invented chart or counter.
tl.fromTo('#proof-scene',{opacity:1,clipPath:'circle(0px at 540px 1050px)'},{opacity:1,clipPath:'circle(1500px at 540px 1050px)',duration:.57,ease:'power3.in',immediateRender:false},S('proof',-.27));
tl.to('#pin-contact',{scale:6,opacity:.2,duration:.57,ease:'power3.in'},S('proof',-.27));
tl.to('#actor-hole',{scale:.1,opacity:0,duration:.2,ease:'power2.in'},S('proof',-.25));
tl.to('#actor-smooth-pin',{opacity:0,duration:.12,ease:'power2.in'},S('proof',-.25));
tl.to('#actor-mesh',{opacity:1,duration:.12,ease:'power2.in'},S('proof',-.25));
mesh.morph(tl,3,S('proof',-.25),.42);
tl.to('#actor-position',{x:540,y:1050,scale:8,duration:.48,ease:'power3.in'},S('proof',-.22));
tl.set('#actor-position',{opacity:0},S('proof',.27));
tl.set('#flare-wrapper',{opacity:.5},S('proof',-.28));
tl.to('#flare-wrapper',{opacity:0,duration:.16,ease:'power2.out'},S('proof',.07));
tl.fromTo('.number-slice',{x:i=>[220,-130,90][i],y:i=>[-90,70,110][i],rotationY:i=>[30,-25,15][i],opacity:0},{x:0,y:0,rotationY:0,opacity:1,duration:.48,stagger:.035,ease:'power4.out',immediateRender:false},S('proof',.08));
// The three moving slices resolve to one identical uncut numeral, avoiding subpixel seams.
tl.set('.number-slice',{opacity:0},S('proof',.68));
tl.set('.number-solid',{opacity:1},S('proof',.68));
V.enter(tl,'#mil span',S('proof',.22),{y:130,rx:-50,duration:.47,ease:'expo.out'});
V.enter(tl,'#proof-unit',S('proof',.7),{y:110,duration:.42,ease:'power3.out'});
V.enter(tl,'#de-pessoas',S('proof',1.03),{x:-60,y:0,duration:.36,ease:'power2.out'});
V.enter(tl,'#proof-city',S('proof',1.15),{y:100,duration:.42,ease:'power4.out'});
V.draw(tl,'#proof-frame-a',S('proof',.45),.9,'power2.inOut');
V.draw(tl,'#proof-frame-b',S('proof',.7),.75,'sine.inOut');
tl.fromTo('#proof-dot',{opacity:0,scale:0,transformOrigin:'995px 1450px'},{opacity:1,scale:1,duration:.38,ease:'back.out(1.15)',immediateRender:false},S('proof',1.2));
// A single fitted camera adjustment changes the hierarchy without erasing reading time.
M.camera(tl,'#proof-camera',[-20,35,1100,1955],S('proof',1.75),.72,1);
tl.to('#proof-art',{rotation:-3,scale:1.03,transformOrigin:'540px 960px',duration:.72,ease:'sine.inOut'},S('proof',1.75));

// 7. A proof point moves into the message→audience connection; the composition is explanatory.
tl.fromTo('#strategy-scene',{opacity:1,clipPath:'circle(0px at 820px 1180px)'},{opacity:1,clipPath:'circle(1700px at 820px 1180px)',duration:.59,ease:'power3.inOut',immediateRender:false},S('strategy',-.28));
V.enter(tl,'#cada-empresa',S('strategy',.02),{y:-130,duration:.47,ease:'power3.out'});
V.enter(tl,'#uma',S('strategy',.35),{x:-100,y:0,duration:.36,ease:'power2.out'});
M.letters(tl,'#estrategia',S('strategy',.75),{y:110,rx:35,stagger:.018,duration:.46});
tl.fromTo('#strategy-underline',{opacity:1,scaleX:0},{opacity:1,scaleX:1,duration:.51,ease:'power3.inOut',immediateRender:false},S('strategy',.97));
V.draw(tl,'#message-outline',S('strategy',.4),.64);
V.draw(tl,'.message-line',S('strategy',.67),.45,'power3.out');
V.draw(tl,'#audience-head',S('strategy',.72),.43,'power3.out');
V.draw(tl,'#audience-body',S('strategy',.85),.52,'power3.inOut');
V.draw(tl,'#audience-halo',S('strategy',1),.59,'sine.inOut');
V.draw(tl,'#strategy-link',S('strategy',1.5),.66,'power3.inOut');
V.enter(tl,'#message-label',S('strategy',1.1),{y:25,duration:.35,ease:'power2.out'});
V.enter(tl,'#audience-label',S('strategy',1.26),{y:25,duration:.35,ease:'sine.out'});
tl.fromTo('#strategy-dot',{opacity:0},{opacity:1,duration:.1,ease:'none',immediateRender:false},S('strategy',1.5));
tl.to('#strategy-dot',{motionPath:{path:'#strategy-link',align:'#strategy-link',alignOrigin:[.5,.5],autoRotate:false},duration:.66,ease:'power3.inOut'},S('strategy',1.5));
tl.to('#strategy-graph',{rotation:-3,y:-20,transformOrigin:'540px 1180px',duration:.7,ease:'sine.inOut'},S('strategy',2.15));

// 8. The same path opens the conversation. A large, legible editorial invitation.
tl.fromTo('#cta-scene',{opacity:1,clipPath:'polygon(0% 100%,100% 100%,100% 100%,0% 100%)'},{opacity:1,clipPath:'polygon(0% 0%,100% 0%,100% 100%,0% 100%)',duration:.54,ease:'power4.inOut',immediateRender:false},S('cta',-.24));
V.enter(tl,'#conversa',S('cta',.16),{y:160,rx:-22,duration:.45,ease:'expo.out'});
V.enter(tl,'#com-a',S('cta',.47),{x:-150,y:0,duration:.36,ease:'power3.out'});
V.enter(tl,'#gente',S('cta',.72),{y:150,rx:22,duration:.48,ease:'power4.out'});
V.draw(tl,'#cta-path',S('cta',.9),.7,'power3.inOut');
M.camera(tl,'#cta-camera',[-8,-12,1108,1972],S('cta',1.37),.61,1);

// 9. The underline resolves into an unambiguous brand signature; settle before the final frame.
tl.fromTo('#brand-scene',{opacity:1,clipPath:'polygon(100% 0%,100% 0%,100% 100%,100% 100%)'},{opacity:1,clipPath:'polygon(0% 0%,100% 0%,100% 100%,0% 100%)',duration:.52,ease:'power3.inOut',immediateRender:false},S('brand',-.08));
M.letters(tl,'#brand-signature',S('brand',.2),{y:85,rx:-25,stagger:.024,duration:.45});
tl.from('#brand-rule',{scaleX:0,duration:.52,ease:'power3.inOut'},S('brand',.48));
tl.from('.brand-content',{rotation:-3,scale:.95,duration:.72,ease:'power3.out'},S('brand',.2));
