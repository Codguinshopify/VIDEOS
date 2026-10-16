/** V14 native DOM trajectory/watermark audit; does not claim pixel OCR or playback. */
import {createRequire} from 'node:module';
import {dirname,join,resolve} from 'node:path';
import {existsSync,mkdirSync,readdirSync,readFileSync,writeFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {bundleCompositionForCapture,initializeSessionWithRetry} from './animation-map/package-loader.mjs';
const project=resolve('.');
const config=JSON.parse(readFileSync(join(project,'resources/qa-contract-v14.json'),'utf8'));
const review=join(project,'review');mkdirSync(review,{recursive:true});
process.env.HYPERFRAMES_NO_TELEMETRY='1';
process.env.XDG_CACHE_HOME=join(project,'.hyperframes/runtime-cache');mkdirSync(process.env.XDG_CACHE_HOME,{recursive:true});
process.env.XDG_STATE_HOME=join(project,'.hyperframes/runtime-state');
if(!process.env.HYPERFRAMES_BROWSER_PATH&&existsSync('/usr/bin/chromium'))process.env.HYPERFRAMES_BROWSER_PATH='/usr/bin/chromium';
const require=createRequire(import.meta.url);
const dist=join(dirname(require.resolve('hyperframes/package.json')),'dist');
const producerModule=await import(pathToFileURL(join(dist,readdirSync(dist).find(n=>/^producer-.*\.js$/.test(n)))).href);
const producer=await producerModule.loadProducer();
const compiler=await import(pathToFileURL(join(dist,readdirSync(dist).find(n=>/^compiler-.*\.js$/.test(n)))).href);
const bundle=await bundleCompositionForCapture(compiler,project);
let server,session;
const sampled=[];
const selectors=['#facet-position','#film-rig','#proof-camera','#cta-world','#city-fragment','#target-city'];
try{
 server=await producer.createFileServer({projectDir:project,compiledDir:bundle.compiledDir,port:0});
 session=await initializeSessionWithRetry(producer,()=>producer.createCaptureSession(server.url,review,{width:1080,height:1920,fps:30,format:'png'},null));
 await session.page.evaluate(()=>{
  const norm=s=>String(s||'').replace(/\s+/g,' ').trim();
  let index=0;
  for(const el of document.querySelectorAll('*')){
   const label=norm(el.getAttribute('aria-label')||el.textContent);
   if(/^(?:Evoquex[.]?|Clevelândia[.]?)$/i.test(label))el.dataset.qaBrandAudit=String(++index);
  }
 });
 for(let frame=0;frame<config.expected_frames;frame+=3){
  const time=frame/config.fps;
  await session.page.evaluate(t=>{
   if(window.__hf&&typeof window.__hf.seek==='function')window.__hf.seek(t);
   else for(const tl of Object.values(window.__timelines||{}))if(typeof tl.seek==='function')tl.seek(t);
  },time);
  const state=await session.page.evaluate(({time,selectors})=>{
   const intersect=(a,b)=>({left:Math.max(a.left,b.left),top:Math.max(a.top,b.top),right:Math.min(a.right,b.right),bottom:Math.min(a.bottom,b.bottom)});
   const inspect=el=>{
    if(!el)return null;
    const rect=el.getBoundingClientRect();let box={left:rect.left,top:rect.top,right:rect.right,bottom:rect.bottom};
    let opacity=1,displayed=true;
    for(let ancestor=el;ancestor;ancestor=ancestor.parentElement){
     const style=getComputedStyle(ancestor);
     opacity*=Number(style.opacity||1);
     if(style.display==='none'||style.visibility==='hidden')displayed=false;
     if(/hidden|clip|scroll|auto/.test(style.overflow+style.overflowX+style.overflowY))box=intersect(box,ancestor.getBoundingClientRect());
    }
    box=intersect(box,{left:0,top:0,right:1080,bottom:1920});
    const style=getComputedStyle(el);
    let visible=displayed&&opacity>.025&&box.right-box.left>1&&box.bottom-box.top>1;
    const glyphs=[...el.querySelectorAll('.vchar,.char')];
    if(glyphs.length&&!glyphs.some(char=>Number(getComputedStyle(char).opacity)>.025))visible=false;
    if(visible){
     // Approximate opaque scene occlusion using native paint-order hit testing.
     // Transparent wrappers are skipped; this remains a DOM proxy, not pixel OCR.
     const points=[.25,.5,.75].map(f=>[box.left+(box.right-box.left)*f,box.top+(box.bottom-box.top)*.5]);
     visible=points.some(([x,y])=>{
      for(const hit of document.elementsFromPoint(x,y)){
       const hs=getComputedStyle(hit);let alpha=1;
       for(let a=hit;a;a=a.parentElement)alpha*=Number(getComputedStyle(a).opacity||1);
       if(alpha<.025)continue;
       if(hit===el||el.contains(hit))return true;
       if(hit.contains(el))continue;
       const color=hs.backgroundColor.match(/^rgba?\(([^)]+)\)$/);
       if(color){const channels=color[1].split(',').map(Number);const fill=channels.length===4?channels[3]:1;if(fill*alpha>.98)return false;}
      }
      return false;
     });
    }
    return {visible_estimate:visible,
     opacity,x:rect.x,y:rect.y,width:rect.width,height:rect.height,font_size:Number.parseFloat(style.fontSize)||null,
     transform:style.transform,clip_path:style.clipPath};
   };
   const brands=[...document.querySelectorAll('[data-qa-brand-audit]')].map(el=>({key:el.dataset.qaBrandAudit,id:el.id||null,
    label:String(el.getAttribute('aria-label')||el.textContent).replace(/\s+/g,' ').trim(),...inspect(el)}));
   const actors=Object.fromEntries(selectors.map(selector=>[selector,inspect(document.querySelector(selector))]));
   return {time_seconds:time,brands,actors};
  },{time,selectors});
  sampled.push({frame,...state});
 }
}finally{
 if(session)await producer.closeCaptureSession(session).catch(()=>{});
 server?.close();bundle.cleanup();
}
const keys=[...new Set(sampled.flatMap(state=>state.brands.map(x=>x.key)))];
const brandSpans=[];
for(const key of keys){
 let run=[];
 const finish=()=>{
  if(!run.length)return;
  const xs=run.map(x=>x.node.x),ys=run.map(x=>x.node.y);
  const first=run[0],last=run.at(-1);
  const duration=+(last.time-first.time+.1).toFixed(3);
  const stationary=Math.max(...xs)-Math.min(...xs)<20&&Math.max(...ys)-Math.min(...ys)<20;
  brandSpans.push({key,label:first.node.label,id:first.node.id,start:first.time,end_exclusive:+(last.time+.1).toFixed(3),duration,
   stationary,small_label:Math.max(...run.map(x=>x.node.font_size||0))<65,
   persistent_watermark_candidate:duration>=config.watermark_stationary_candidate_minimum_seconds&&stationary&&Math.max(...run.map(x=>x.node.font_size||0))<65});
  run=[];
 };
 for(const sample of sampled){
  if(sample.time_seconds<config.watermark_disallowed_after_seconds)continue;
  const node=sample.brands.find(x=>x.key===key);
  if(node?.visible_estimate)run.push({time:sample.time_seconds,node});else finish();
 }
 finish();
}
const hashFile=relative=>createHash('sha256').update(readFileSync(join(project,relative))).digest('hex');
const result={version:'V14',ok:!brandSpans.some(x=>x.persistent_watermark_candidate),
 source_sha256:Object.fromEntries(['index.html','style.css','motion.js'].map(path=>[path,hashFile(path)])),
 sample_rate_hz:10,samples:sampled.length,dimensions:[1080,1920],
 brand_visible_spans_after_5_seconds:brandSpans,stationary_persistent_watermark_candidates:brandSpans.filter(x=>x.persistent_watermark_candidate),
 actor_selectors:selectors,trajectory_samples:sampled,
 hook_pixel_identity_required:false,continuous_playback_performed:false,subjective_listening_performed:false,
 limitations:['Computed DOM visibility uses styles, rectangular clipping and native hit-testing of opaque backgrounds, not OCR of encoded pixels.','Animated glyph children, SVG masks, filters, nonrectangular clipping and complex occlusion still require exported-MP4 frame review.','Finite narrative mentions and the final signature are allowed; only persistent small stationary labels are flagged.','No final visual-quality approval is inferred from this runtime audit.']};
writeFileSync(join(review,'runtime-inspection-v14.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({ok:result.ok,samples:result.samples,persistent_watermark_candidates:result.stationary_persistent_watermark_candidates.length}));
