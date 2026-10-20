/* Evoquex V15: reusable scene envelope / ink atlas / semantic curves.
 * line-swap and caption-camera-follow mechanics adapted from pinned Apache-2.0 HF sources.
 * No clocks or async animation. Host owns media times, scene windows and acceptance. */
(function(){'use strict';
 function enter(tl,selector,at,opt={}){tl.fromTo(selector,{opacity:0,x:opt.x||0,y:opt.y??100,rotation:opt.rotation||0,rotationX:opt.rx||0,scale:opt.scale??1},{opacity:1,x:0,y:0,rotation:0,rotationX:0,scale:1,duration:opt.duration??.43,ease:opt.ease||'power4.out',immediateRender:false},at);}
 function draw(tl,selector,at,duration=.5,ease='power2.inOut'){document.querySelectorAll(selector).forEach(p=>{const n=p.getTotalLength();p.style.strokeDasharray=n;p.style.strokeDashoffset=n;tl.fromTo(p,{strokeDashoffset:n},{strokeDashoffset:0,duration,ease,immediateRender:false},at);});}
 function atlas(tl,selector,at,duration,cols=6,rows=5){const el=document.querySelector(selector),state={frame:0};function paint(){const n=Math.max(0,Math.min(cols*rows-1,Math.floor(state.frame))),pos=`${n%cols/(cols-1)*100}% ${Math.floor(n/cols)/(rows-1)*100}%`;el.style.maskPosition=pos;el.style.webkitMaskPosition=pos;}paint();tl.fromTo(state,{frame:0},{frame:cols*rows-1,duration,ease:'none',onUpdate:paint,immediateRender:false},at);return state;}
 function sceneTime(id,localSeconds){const p=window.EVOQUEX_TIMING.scenes[id];return p[0]+localSeconds;}
 window.EvoquexV15={enter,draw,atlas,sceneTime};
})();
