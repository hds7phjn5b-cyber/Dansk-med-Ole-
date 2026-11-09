const CACHE='dansk-ole-course-v15-christel-voice',FILES=["./","./index.html","./manifest.json","./icon.svg","./icon-192.png","./icon-512.png"];
self.addEventListener('install',e=>e.waitUntil((async()=>{
 const c=await caches.open(CACHE);await c.addAll(FILES);
 try{
  const response=await fetch('./audio-manifest.json',{cache:'no-store'});
  if(response.ok){
   const items=await response.json();
   const names=items.filter(x=>x&&typeof x.path==='string'&&x.path.startsWith('audio/')&&x.path.endsWith('.mp3')).map(x=>'./'+x.path);
   for(let i=0;i<names.length;i+=16)await Promise.allSettled(names.slice(i,i+16).map(name=>c.add(name)));
  }
 }catch{}
 await self.skipWaiting();
})()));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('dansk-ole-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
async function respond(request){
 if(request.mode==='navigate'){try{const fresh=await fetch(request);if(fresh.ok)return fresh}catch{}}
 const cache=await caches.open(CACHE);const hit=await cache.match(request,{ignoreSearch:true});
 if(!hit){const fresh=await fetch(request);if(fresh.ok&&new URL(request.url).pathname.endsWith('.mp3'))cache.put(request,fresh.clone()).catch(()=>{});return fresh;}
 const range=request.headers.get('range');
 if(!range||!new URL(request.url).pathname.endsWith('.mp3'))return hit;
 const data=await hit.arrayBuffer();const length=data.byteLength;const m=/^bytes=(\d*)-(\d*)$/.exec(range);
 if(!m||(!m[1]&&!m[2]))return new Response(null,{status:416,headers:{'Content-Range':`bytes */${length}`}});
 const start=m[1]?Number(m[1]):Math.max(0,length-Number(m[2]));const end=m[1]?(m[2]?Math.min(Number(m[2]),length-1):length-1):length-1;
 if(start>=length||end<start)return new Response(null,{status:416,headers:{'Content-Range':`bytes */${length}`}});
 return new Response(data.slice(start,end+1),{status:206,headers:{'Content-Type':'audio/mpeg','Accept-Ranges':'bytes','Content-Length':String(end-start+1),'Content-Range':`bytes ${start}-${end}/${length}`}});
}
self.addEventListener('fetch',e=>{if(e.request.method==='GET'&&new URL(e.request.url).origin===self.location.origin)e.respondWith(respond(e.request));});
