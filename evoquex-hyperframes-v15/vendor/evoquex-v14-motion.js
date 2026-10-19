/* Evoquex V14. Adapted mechanisms: HyperFrames facet-morph + caption-camera-follow,
 * revision08ee1bd5ad59987a7f2525222683e24ca30971f9 (Apache-2.0).
 * Original forms, framing, narrative and timing. SVG2.5D; no physical3D claim. */
(function(){'use strict';
const N=18,NS='http://www.w3.org/2000/svg';
function glyphs(){document.querySelectorAll('[data-letters]').forEach(el=>{const t=el.textContent;el.setAttribute('aria-label',t);el.textContent='';for(const ch of [...t]){const s=document.createElement('span');s.className='vchar';s.setAttribute('aria-hidden','true');s.textContent=ch===' '?'\u00a0':ch;el.append(s);}});}
function letters(tl,s,t,o={}){const els=document.querySelectorAll(s+' .vchar');tl.fromTo(els,{yPercent:o.y??90,x:o.x??0,rotationX:o.rx??55,rotationZ:o.rz??0,opacity:o.opacity??0},{yPercent:0,x:0,rotationX:0,rotationZ:0,opacity:1,duration:o.duration??.4,stagger:o.stagger??.018,ease:o.ease??'power4.out',immediateRender:false},t);}
function draw(tl,selector,t,d=.55){document.querySelectorAll(selector).forEach(p=>{const n=p.getTotalLength();p.style.strokeDasharray=n;p.style.strokeDashoffset=n;tl.fromTo(p,{strokeDashoffset:n},{strokeDashoffset:0,duration:d,ease:'power2.inOut',immediateRender:false},t);});}
// This is the registry poseFor algorithm, using explicit authored bounding boxes.
function poseFor(b,margin=1){const s=Math.min(1080/((b[2]-b[0])*margin),1920/((b[3]-b[1])*margin));return{scale:s,x:540-s*(b[0]+b[2])/2,y:960-s*(b[1]+b[3])/2};}
function camera(tl,node,b,t,d=.6,margin=1){tl.to(node,{...poseFor(b,margin),duration:d,ease:'power3.inOut'},t);}
function sample(poly,n){const lens=poly.map((a,i)=>Math.hypot(poly[(i+1)%poly.length][0]-a[0],poly[(i+1)%poly.length][1]-a[1]));const total=lens.reduce((a,b)=>a+b,0);return Array.from({length:n},(_,i)=>{let s=i/n*total,k=0;while(s>lens[k]&&k<lens.length-1){s-=lens[k];k++;}const a=poly[k],b=poly[(k+1)%poly.length],f=s/lens[k];return[a[0]+(b[0]-a[0])*f,a[1]+(b[1]-a[1])*f];});}
function mesh(selector){const root=document.querySelector(selector);const pin=[[0,1.18]];for(let i=0;i<17;i++){const a=(150+i/16*240)*Math.PI/180;pin.push([Math.cos(a)*.85,Math.sin(a)*.85-.25]);}
const circle=Array.from({length:18},(_,i)=>[Math.cos(i/N*Math.PI*2),Math.sin(i/N*Math.PI*2)]);
const bubble=Array.from({length:15},(_,i)=>{const a=-Math.PI*.7+i/14*Math.PI*1.76;return[Math.cos(a),Math.sin(a)*.77];});bubble.push([-.85,.95],[-.7,.32]);
const forms=[sample([[-.7,-1],[1,0],[-.7,1]],N),sample([[-1,-.3],[.05,-.3],[.05,-.8],[1.1,0],[.05,.8],[.05,.3],[-1,.3]],N),sample(pin,N),circle,sample(bubble,N)];
const triangles=[];for(let k=0;k<9;k++){const a=2*k,b=2*k+1,c=(2*k+2)%18;triangles.push([['o',a],['o',b],['i',k]],[['o',b],['o',c],['i',k]],[['o',c],['i',k],['i',(k+1)%9]]);}for(let k=0;k<9;k++)triangles.push([['i',k],['i',(k+1)%9],['c',0]]);
const polys=triangles.map(()=>{const p=document.createElementNS(NS,'polygon');root.append(p);return p;});const state={phase:0,light:0};
function render(){const k=Math.min(3,Math.floor(Math.max(0,state.phase))),f=Math.min(1,Math.max(0,state.phase-k));const outer=forms[k].map((a,i)=>[a[0]+(forms[k+1][i][0]-a[0])*f,a[1]+(forms[k+1][i][1]-a[1])*f]);const inner=Array.from({length:9},(_,i)=>{const a=outer[2*i],b=outer[(2*i+1)%18];return[(a[0]+b[0])*.225,(a[1]+b[1])*.225];});const points={o:outer,i:inner,c:[[0,0]]};triangles.forEach((tri,i)=>{const p=tri.map(([r,j])=>points[r][j]);polys[i].setAttribute('points',p.map(([x,y])=>`${(x*185).toFixed(3)},${(y*185).toFixed(3)}`).join(' '));const cx=p.reduce((n,a)=>n+a[0],0)/3,cy=p.reduce((n,a)=>n+a[1],0)/3;const l=1.0-cx*.18-cy*.14+Math.sin(i*1.72+state.light)*.06;const rgb=[84,166,255].map(v=>Math.max(0,Math.min(255,Math.round(v*l))));polys[i].setAttribute('fill',`rgb(${rgb})`);polys[i].setAttribute('stroke',`rgb(${rgb})`);polys[i].setAttribute('stroke-width','1');});}
render();return{state,render,morph(tl,phase,t,d=.5){tl.to(state,{phase,duration:d,ease:'power3.inOut',onUpdate:render},t);}};}
window.EvoquexV14={glyphs,letters,draw,poseFor,camera,mesh};
})();
