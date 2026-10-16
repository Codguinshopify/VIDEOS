/* Evoquex V13: focused adaptations of pinned HyperFrames registry primitives.
 * Apache-2.0 upstream: text-match-cut E85 bisection, pan-stations shared strip,
 * type-match-cut complementary type aperture. Local implementation stays separate.
 */
(function(){
 function e85(x){let lo=0,hi=1,u=.5;for(let i=0;i<24;i++){u=(lo+hi)/2;const k=1-u;const v=3*k*k*u*.85+3*k*u*u*.15+u*u*u;if(v<x)lo=u;else hi=u}return 3*(1-u)*u*u+u*u*u}
 function glyphs(){document.querySelectorAll('[data-letters]').forEach(el=>{const t=el.textContent;el.setAttribute('aria-label',t);el.innerHTML='';for(const c of t){let s=document.createElement('span');s.className='vchar';s.textContent=c===' '? '\u00a0':c;el.appendChild(s)}})}
 function letters(tl,selector,at,opts={}){const a=gsap.utils.toArray(selector+' .vchar');a.forEach((el,i)=>tl.from(el,{x:(i%2?1:-1)*(opts.x??12),y:opts.y??100,rotationX:(i%2?1:-1)*(opts.rot??65),rotationZ:(i%2?1:-1)*(opts.tilt??3),opacity:0,duration:opts.duration??.46,ease:opts.ease??'power4.out'},at+i*(opts.stagger??.018)))}
 function slices(tl,selector,at,opts={}){const els=gsap.utils.toArray(selector+' .slice');els.forEach((el,i)=>tl.from(el,{x:(i-1)*(opts.distance??130),y:[70,-95,95][i],rotationZ:[-8,5,-4][i],rotationY:[30,-24,38][i],opacity:0,duration:opts.duration??.5,ease:opts.ease??'back.out(1.08)'},at+i*.035))}
 function frame(tl,box,at,duration=.6){tl.to('#flow-frame',{attr:box,duration,ease:e85},at)}
 window.EvoquexV13={e85,glyphs,letters,slices,frame};
})();
