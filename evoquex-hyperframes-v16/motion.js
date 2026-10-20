/* V16: frame-locked GSAP scene choreography, rebuilt around Oto/Park techniques. */
const tl=window.__timelines['evoquex-v16'];
const M=window.EvoquexV14,V=window.EvoquexV15;
const H=(oldSeconds)=>oldSeconds*.75;
M.glyphs();
const draw=(sel,at,duration)=>V.draw(tl,sel,at,duration,'power3.inOut');
// 1. An immediate living type rig: the bar becomes a mask, then the question opens the city.
tl.from('.sua span',{yPercent:13,rotationX:12,duration:.4,ease:'power3.out'},H(0));
tl.from('.empresa span',{yPercent:12,rotationX:18,duration:.5,ease:'power4.out'},H(0));
tl.from('.hook-signature',{y:25,opacity:.35,duration:.45,ease:'power2.out'},H(0));
tl.from('.company-rule',{scaleX:.1,duration:.5,ease:'expo.out'},H(0));
tl.from('#hook-company',{rotationY:-10,z:90,duration:.5,ease:'power3.out'},H(0));
tl.to('#hook-company',{x:-1050,rotationY:-25,scale:.82,duration:.35,ease:'power3.inOut'},H(.70));
tl.fromTo('#hook-known',{opacity:1,x:1080,rotationY:25},{opacity:1,x:0,rotationY:0,duration:.44,ease:'power4.out',immediateRender:false},H(.74));
tl.from('.known-band',{scale:.62,rotation:10,y:100,duration:.49,ease:'back.out(1.1)'},H(.81));
tl.to('.known-band',{rotation:-5,duration:.4,ease:'power3.out'},H(1.04));
tl.from('.known-prefix',{y:-60,opacity:0,duration:.36,ease:'power2.out'},H(.87));
tl.from('.known-echo',{y:90,opacity:0,rotationX:38,duration:.5,ease:'sine.out'},H(.82));
tl.to('#hook-known',{y:-1100,rotationX:27,scale:.85,duration:.36,ease:'power3.inOut'},H(1.59));
tl.fromTo('#hook-city',{opacity:1,y:1120,rotationX:-25},{opacity:1,y:0,rotationX:0,duration:.42,ease:'power4.out',immediateRender:false},H(1.64));
tl.from('.city-name span',{x:160,rotationY:20,duration:.42,ease:'expo.out'},H(1.70));
tl.from('.city-underline',{scaleX:0,duration:.43,ease:'power2.inOut'},H(1.82));
tl.to('#hook-city',{x:1150,rotation:-8,duration:.38,ease:'power3.inOut'},H(2.47));
tl.fromTo('#hook-question',{opacity:1,x:-1050,rotation:7},{opacity:1,x:0,rotation:0,duration:.43,ease:'power4.out',immediateRender:false},H(2.51));
tl.from('.question-prefix span',{y:100,duration:.35,ease:'power2.out'},H(2.61));
M.letters(tl,'.question-word',H(2.67),{y:90,rx:55,stagger:.023,duration:.42});
V.draw(tl,'#question-curve',H(3.04),.3,'power3.inOut');
tl.to('.hook-orbit',{scale:.8,x:-110,y:-90,duration:3.5,ease:'sine.inOut'},H(0));


// Park circular draft meets Oto's hard dark field and central phrase.
tl.set('#phrase-scene',{opacity:1,clipPath:'inset(0% 0% 100% 0%)'},2.92);
tl.to('#phrase-scene',{clipPath:'inset(0% 0% 0% 0%)',duration:.32,ease:'power4.inOut'},2.92);
tl.fromTo('.small-kicker',{y:100,opacity:0,filter:'blur(15px)'},{y:0,opacity:1,filter:'blur(0px)',duration:.5,ease:'power3.out',immediateRender:false},3.2);
tl.fromTo('.park-orbit',{scale:1.5,opacity:0,rotation:-80},{scale:1,opacity:.7,rotation:0,duration:.85,stagger:.12,ease:'power3.out',immediateRender:false},3.35);
tl.to('.park-orbit',{rotation:45,scale:1.08,duration:4.3,ease:'sine.inOut'},3.9);
tl.fromTo('.phrase-ghost',{x:-130,opacity:0},{x:0,opacity:.45,duration:.6,ease:'power2.out',immediateRender:false},3.48);
tl.fromTo('.phrase-top',{x:-650,skewX:13,opacity:0},{x:0,skewX:0,opacity:1,duration:.49,ease:'power4.out',immediateRender:false},4.2);
tl.fromTo('.phrase-bottom',{y:240,scale:1.3,opacity:0,filter:'blur(13px)'},{y:0,scale:1,opacity:1,filter:'blur(0px)',duration:.65,ease:'power4.out',immediateRender:false},5.15);
draw('.phrase-underline path',5.7,.65);
tl.fromTo('.phrase-index',{y:25,opacity:0},{y:0,opacity:1,duration:.4,immediateRender:false},6.25);
tl.to('.phrase-block',{scale:.92,y:-45,duration:.75,ease:'power2.inOut'},7.1);

// Oto's white field and moving vertical card deck show the actual campaign.
tl.set('#example-scene',{opacity:1,clipPath:'circle(0px at 540px 960px)'},7.75);
tl.to('#example-scene',{clipPath:'circle(1480px at 540px 960px)',duration:.58,ease:'power4.inOut'},7.75);
tl.fromTo('.ex-heading',{y:-170,opacity:0},{y:0,opacity:1,duration:.65,ease:'power4.out',immediateRender:false},8.12);
tl.fromTo('.film-card',{y:840,rotation:-9,scale:.75,opacity:0},{y:0,rotation:0,scale:1,opacity:1,duration:.72,ease:'back.out(1.04)',immediateRender:false},8.43);
tl.fromTo('.side-card.left',{x:-400,rotation:-22,opacity:0},{x:0,rotation:-8,opacity:1,duration:.66,ease:'power3.out',immediateRender:false},8.76);
tl.fromTo('.side-card.right',{x:400,rotation:24,opacity:0},{x:0,rotation:8,opacity:1,duration:.66,ease:'power3.out',immediateRender:false},8.92);
tl.fromTo('.ex-client',{y:90,opacity:0},{y:0,opacity:1,duration:.4,ease:'power3.out',immediateRender:false},9.46);
tl.fromTo('.scribble-arrow',{rotation:-55,scale:.15,opacity:0},{rotation:0,scale:1,opacity:1,duration:.5,ease:'back.out(1.5)',immediateRender:false},10.25);
tl.to('.card-rail',{x:-20,scale:1.04,duration:3.4,ease:'sine.inOut'},10.5);
tl.to('.side-card.left',{x:115,rotation:-2,duration:.65,ease:'power3.inOut'},12.3);
tl.to('.side-card.right',{x:-115,rotation:2,duration:.65,ease:'power3.inOut'},12.3);
tl.to('.film-card',{y:-55,scale:1.08,duration:.65,ease:'power3.inOut'},13.5);
tl.fromTo('#burn-overlay',{opacity:0},{opacity:.28,duration:.35,immediateRender:false},8);
tl.to('#burn-overlay',{opacity:0,duration:.45},8.35);

// Park's expanding circles connect the real film to one geographic audience.
tl.set('#geo-scene',{opacity:1,clipPath:'circle(0px at 540px 1100px)'},14.72);
tl.to('#geo-scene',{clipPath:'circle(1650px at 540px 1100px)',duration:.55,ease:'power4.inOut'},14.72);
tl.fromTo('.geo-head',{x:-650,opacity:0},{x:0,opacity:1,duration:.5,ease:'power4.out',immediateRender:false},15.25);
tl.fromTo('.geo-topline',{y:-65,opacity:0},{y:0,opacity:1,duration:.42,ease:'power3.out',immediateRender:false},15.33);
tl.fromTo('.geo-map-card',{y:790,rotation:11,rotationY:-16,scale:.8,opacity:0},{y:0,rotation:0,rotationY:0,scale:1,opacity:1,duration:.8,ease:'power4.out',immediateRender:false},15.85);
tl.fromTo('.map-target',{scale:.05,opacity:0},{scale:1,opacity:1,duration:.7,ease:'back.out(1.12)',immediateRender:false},16.65);
tl.fromTo('.geo-ticket',{x:-370,opacity:0},{x:0,opacity:1,duration:.55,ease:'power3.out',immediateRender:false},18);
tl.fromTo('.geo-line',{scaleX:0},{scaleX:1,duration:.52,ease:'power4.inOut',immediateRender:false},18.3);
tl.to('.geo-map img',{scale:1.15,x:-30,y:-25,duration:4.1,ease:'sine.inOut'},17.15);
tl.to('.map-target',{scale:1.28,opacity:.68,duration:1.1,ease:'sine.inOut'},20.45);

// Park's dark number field, circular lens and signal bars display only the verified metric.
tl.set('#metric-scene',{opacity:1,clipPath:'circle(0px at 540px 1120px)'},21.72);
tl.to('#metric-scene',{clipPath:'circle(1650px at 540px 1120px)',duration:.48,ease:'power4.inOut'},21.72);
tl.fromTo('#transition-flare',{opacity:0},{opacity:.55,duration:.22,immediateRender:false},21.78);
tl.to('#transition-flare',{opacity:0,duration:.37},22.08);
tl.fromTo('.metric-ring',{scale:.24,opacity:0},{scale:1,opacity:.6,duration:.85,stagger:.09,ease:'power3.out',immediateRender:false},22.04);
tl.fromTo('.metric-prefix',{x:-180,opacity:0},{x:0,opacity:1,duration:.5,ease:'power3.out',immediateRender:false},22.42);
tl.fromTo('.num-two',{y:400,scale:1.6,opacity:0,filter:'blur(15px)'},{y:0,scale:1,opacity:1,filter:'blur(0px)',duration:.64,ease:'power4.out',immediateRender:false},22.65);
tl.fromTo('.num-mil',{x:180,rotation:18,opacity:0},{x:0,rotation:0,opacity:1,duration:.51,ease:'power4.out',immediateRender:false},23.09);
tl.fromTo('.metric-unit',{y:160,opacity:0},{y:0,opacity:1,duration:.45,ease:'power3.out',immediateRender:false},23.48);
tl.fromTo('.metric-foot',{y:110,opacity:0},{y:0,opacity:1,duration:.55,ease:'power3.out',immediateRender:false},24.7);
tl.fromTo('.metric-signal i',{scaleY:.08,transformOrigin:'50% 100%',opacity:0},{scaleY:1,opacity:1,duration:.58,stagger:.048,ease:'power3.out',immediateRender:false},25.05);
tl.to('.metric-lens',{scale:1.32,rotation:15,duration:3.1,ease:'sine.inOut'},25.7);
tl.to('.metric-wrap',{scale:1.05,y:-36,duration:1.2,ease:'power2.inOut'},27.2);

// The original Blender phone/arrow/target scene, with a synchronized ring at impact.
tl.set('#strategy-scene',{opacity:1,clipPath:'circle(0px at 540px 960px)'},28.75);
tl.to('#strategy-scene',{clipPath:'circle(1650px at 540px 960px)',duration:.6,ease:'power4.inOut'},28.75);
tl.fromTo('.strategy-heading',{x:-220,y:-65,opacity:0},{x:0,y:0,opacity:1,duration:.57,ease:'power4.out',immediateRender:false},29.45);
tl.fromTo('.strategy-label',{y:-80,opacity:0},{y:0,opacity:1,duration:.45,ease:'power3.out',immediateRender:false},29.15);
tl.fromTo('.strategy-bottom',{y:170,opacity:0},{y:0,opacity:1,duration:.55,ease:'power4.out',immediateRender:false},32.35);
tl.fromTo('.pulse-a',{scale:.1,opacity:.75},{scale:14,opacity:0,duration:1,ease:'power3.out',immediateRender:false},34.35);
tl.fromTo('.pulse-b',{scale:.1,opacity:.8},{scale:10,opacity:0,duration:.83,ease:'power3.out',immediateRender:false},34.46);
tl.to('.strategy-bottom b',{color:'#fff',duration:.25},34.38);

// Oto's minimal pale endcard and Park's circle carry the CTA to the brand.
tl.set('#cta-scene',{opacity:1,clipPath:'circle(0px at 540px 960px)'},36.72);
tl.to('#cta-scene',{clipPath:'circle(1600px at 540px 960px)',duration:.65,ease:'power4.inOut'},36.72);
tl.fromTo('.cta-orbit',{scale:.5,rotation:-70,opacity:0},{scale:1,rotation:0,opacity:1,duration:.9,ease:'power3.out',immediateRender:false},37.1);
tl.fromTo('.cta-small',{y:-100,opacity:0},{y:0,opacity:1,duration:.46,ease:'power3.out',immediateRender:false},37.2);
tl.fromTo('.cta-text',{y:180,rotationX:-25,opacity:0},{y:0,rotationX:0,opacity:1,duration:.64,ease:'power4.out',immediateRender:false},37.66);
tl.fromTo('.cta-final',{x:-700,rotation:-6,opacity:0},{x:0,rotation:0,opacity:1,duration:.59,ease:'power4.out',immediateRender:false},39.55);
tl.to('.cta-orbit',{scale:1.4,x:-150,y:150,duration:3.3,ease:'sine.inOut'},39.6);
tl.to('.logo-finish',{opacity:1,duration:.52,ease:'power3.inOut'},41.45);
tl.fromTo('.logo-finish img',{scale:.66,rotation:-12,opacity:0},{scale:1,rotation:0,opacity:1,duration:.68,ease:'back.out(1.1)',immediateRender:false},41.6);
tl.fromTo('.logo-caption',{y:70,opacity:0},{y:0,opacity:1,duration:.52,ease:'power3.out',immediateRender:false},42.15);
