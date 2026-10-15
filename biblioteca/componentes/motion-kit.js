/* Evoquex reusable motion primitives. GSAP must be supplied by the host.
 * Mechanics: HyperFrames line-swap, lt-accent-underline, focus-blur-resolve.
 * See catalogo.json and upstream originals. No media/network/time side effects.
 */
(function(global){
  function draw(tl, selector, at, duration=.5, stagger=0){
    document.querySelectorAll(selector).forEach(el=>{
      el.setAttribute('pathLength','1');
      el.style.strokeDasharray='1';el.style.strokeDashoffset='1';
    });
    tl.to(selector,{strokeDashoffset:0,duration,stagger,ease:'power2.inOut'},at);
  }
  function maskedSwap(tl, selector, height, at, duration=.42){
    // A single shared rail avoids cross-easing glyph collisions between words.
    tl.to(selector,{y:-height,duration,ease:'power3.inOut'},at);
  }
  function focus(tl,selector,at){
    tl.from(selector,{y:24,rotationX:32,opacity:0,filter:'blur(7px)',
      stagger:.05,duration:.55,ease:'power3.out'},at);
  }
  function underline(tl,selector,at,duration=.45){
    tl.from(selector,{scaleX:.02,transformOrigin:'0% 50%',duration,ease:'power4.out'},at);
  }
  global.EvoquexMotion={draw,maskedSwap,focus,underline};
})(window);
