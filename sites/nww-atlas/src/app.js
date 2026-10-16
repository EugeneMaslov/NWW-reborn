'use strict';
const $ = id => document.getElementById(id);
const statuses = {full:'Полная переработка',legacy:'Фокусы из Legacy',none:'Без уникальных фокусов NWW',partial:'Новое дерево / в разработке'};
const byTag = new Map(DATA.countries.map(c => [c.tag,c]));
const paths = [...document.querySelectorAll('#countries path')];
const onMap = DATA.countries.filter(c => c.box);
let filter = 'all', selected = null, drag = null, moved = false;
let view = [0,0,DATA.width,DATA.height];
const svg = $('map'), container = $('map-container');
paths.forEach(p => {p.dataset.status = byTag.get(p.dataset.tag).status; const title = document.createElementNS('http://www.w3.org/2000/svg','title'); title.textContent = byTag.get(p.dataset.tag).name; p.append(title);});
// Counts describe actual owners at the selected start date. Successors are searchable separately.
$('count-all').textContent = onMap.length;
for (const s of Object.keys(statuses)) $('count-'+s).textContent = onMap.filter(c=>c.status===s).length;
function renderList(){
  const query = $('search').value.trim().toLocaleLowerCase('ru');
  let countries = DATA.countries.filter(c => (filter==='all' ? query || c.status!=='none' : c.status===filter) && (!query || (c.name+' '+c.tag).toLocaleLowerCase('ru').includes(query)));
  const rank={full:0,legacy:1,partial:2,none:3};
  countries.sort((a,b)=>rank[a.status]-rank[b.status] || Number(!!b.box)-Number(!!a.box) || a.name.localeCompare(b.name,'ru'));
  $('list-title').textContent = query ? 'РЕЗУЛЬТАТЫ ПОИСКА' : filter==='all' ? 'СТРАНЫ С КОНТЕНТОМ' : statuses[filter].toUpperCase();
  $('result-count').textContent=countries.length;
  $('country-list').replaceChildren();
  if(!countries.length){const empty=document.createElement('p');empty.className='empty';empty.textContent='Страна не найдена. Попробуйте название или трёхбуквенный тег.';$('country-list').append(empty);}
  for(const c of countries){
    const button=document.createElement('button');button.className='country-row'+(selected===c.tag?' selected':'');button.dataset.tag=c.tag;
    const swatch=document.createElement('i');swatch.className='swatch '+c.status;
    const label=document.createElement('span');label.className='country-label';label.textContent=c.name;
    if(!c.box){const note=document.createElement('small');note.textContent='Не существует на старте';label.append(note);}
    const tag=document.createElement('code');tag.textContent=c.tag;
    const arrow=document.createElement('span');arrow.className='row-arrow';arrow.textContent='↗';
    button.append(swatch,label,tag,arrow);button.addEventListener('click',()=>selectCountry(c.tag,true));$('country-list').append(button);
  }
}
function setFilter(value){
  filter=value;
  document.querySelectorAll('[data-filter]').forEach(b=>{const active=b.dataset.filter===value;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active));});
  paths.forEach(p=>p.classList.toggle('dim',filter!=='all' && byTag.get(p.dataset.tag).status!==filter));
  renderList();
}
function applyView(){
  const [x,y,w,h]=view;
  view=[Math.min(DATA.width-w*.15,Math.max(-w*.85,x)),Math.min(DATA.height-h*.15,Math.max(-h*.85,y)),w,h];
  svg.setAttribute('viewBox',view.join(' '));
}
function resetView(){view=[0,0,DATA.width,DATA.height];applyView();}
function screenPoint(x,y){const point=svg.createSVGPoint();point.x=x;point.y=y;return point.matrixTransform(svg.getScreenCTM().inverse());}
function zoom(factor,clientX,clientY){
  const r=container.getBoundingClientRect(), point=screenPoint(clientX??r.x+r.width/2,clientY??r.y+r.height/2);
  const oldW=view[2], newW=Math.min(DATA.width*1.25,Math.max(90,oldW*factor)), ratio=newW/oldW;
  view=[point.x-(point.x-view[0])*ratio,point.y-(point.y-view[1])*ratio,newW,view[3]*ratio];applyView();
}
function focusCountry(c){
  if(!c.box)return;
  const [x1,y1,x2,y2]=c.box;
  const r=container.getBoundingClientRect(), aspect=r.width/r.height;
  let w=Math.max(150,(x2-x1)*1.8),h=Math.max(100,(y2-y1)*1.8);
  if(w/h<aspect)w=h*aspect;else h=w/aspect;
  // Leave room for the information card in desktop layouts.
  const desktop=window.innerWidth>760;
  if(desktop){w*=1.4;h*=1.4;}
  view=[(x1+x2)/2-w*(desktop?.37:.5),(y1+y2)/2-h*.5,w,h];applyView();
  if(window.innerWidth<=760)container.scrollIntoView({behavior:'smooth',block:'start'});
}
function selectCountry(tag,focus=false){
  const c=byTag.get(tag);if(!c)return;
  selected=tag;paths.forEach(p=>p.classList.toggle('selected',p.dataset.tag===tag));
  // Move selected geometry above neighbors so its border stays visible.
  const path=$('country-'+tag);if(path)path.parentNode.append(path);
  $('detail-name').textContent=c.name;$('detail-status').textContent=statuses[c.status];
  $('detail-description').textContent=c.description;$('detail-focuses').textContent=c.focuses||'—';
  $('detail-states').textContent=c.states;$('detail-tag').textContent=c.tag;
  $('detail-note').textContent=!c.box?'Страна отсутствует на старте 1936 года. Дерево доступно в моде для её возможного появления.':c.status==='none'?'Белый цвет относится к контенту NWW; у страны может быть стандартное дерево игры или DLC.':c.status==='partial'?'Белая штриховка: новое дерево; полная переработка пока не подтверждена документацией проекта.':'Цвет распространяется на все владения страны, включая колонии.';
  $('detail-sources').replaceChildren();
  for(const source of c.sources){const li=document.createElement('li');li.textContent=source;$('detail-sources').append(li);}
  $('source-details').hidden=!c.sources.length;$('source-details').open=false;
  $('detail').hidden=false;$('tooltip').hidden=true;renderList();
  history.replaceState(null,'','#'+tag);
  if(focus)focusCountry(c);
}
function closeDetail(){selected=null;$('detail').hidden=true;paths.forEach(p=>p.classList.remove('selected'));history.replaceState(null,'',location.pathname+location.search);renderList();}
$('detail-close').addEventListener('click',closeDetail);
document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>setFilter(b.dataset.filter)));
$('search').addEventListener('input',renderList);
$('search').addEventListener('keydown',e=>{if(e.key==='Enter')$('country-list').querySelector('button')?.click();});
$('zoom-in').addEventListener('click',()=>zoom(.72));$('zoom-out').addEventListener('click',()=>zoom(1.4));
$('reset').addEventListener('click',()=>{resetView();closeDetail();});
document.querySelector('.brand').addEventListener('click',e=>{e.preventDefault();$('search').value='';setFilter('all');resetView();closeDetail();});
container.addEventListener('wheel',e=>{e.preventDefault();zoom(Math.exp(e.deltaY*.0012),e.clientX,e.clientY);},{passive:false});
const pointers=new Map();let pinch=null;
container.addEventListener('pointerdown',e=>{
  if(e.pointerType==='mouse'&&e.button!==0)return;
  pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});container.setPointerCapture(e.pointerId);
  if(pointers.size===2){const [a,b]=[...pointers.values()];pinch={distance:Math.hypot(a.x-b.x,a.y-b.y)};drag=null;moved=true;}
  else{drag={id:e.pointerId,x:e.clientX,y:e.clientY,view:[...view]};moved=false;}
});
container.addEventListener('pointermove',e=>{
  if(pointers.has(e.pointerId))pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});
  if(pointers.size===2&&pinch){const [a,b]=[...pointers.values()],distance=Math.hypot(a.x-b.x,a.y-b.y);if(distance>0){zoom(pinch.distance/distance,(a.x+b.x)/2,(a.y+b.y)/2);pinch.distance=distance;}return;}
  if(drag&&drag.id===e.pointerId){
    if(Math.hypot(e.clientX-drag.x,e.clientY-drag.y)>4)moved=true;
    if(moved){const matrix=svg.getScreenCTM();view=[drag.view[0]-(e.clientX-drag.x)/matrix.a,drag.view[1]-(e.clientY-drag.y)/matrix.d,drag.view[2],drag.view[3]];applyView();container.classList.add('dragging');$('tooltip').hidden=true;}return;
  }
  const path=e.target.closest?.('path[data-tag]');
  if(!path){$('tooltip').hidden=true;return;}
  const c=byTag.get(path.dataset.tag),tip=$('tooltip');tip.replaceChildren(document.createTextNode(c.name));
  const small=document.createElement('small');small.textContent=c.tag+' · '+statuses[c.status];tip.append(small);tip.hidden=false;
  tip.style.left=Math.max(8,Math.min(e.clientX+14,innerWidth-tip.offsetWidth-12))+'px';
  tip.style.top=Math.max(8,Math.min(e.clientY+16,innerHeight-tip.offsetHeight-12))+'px';
});
function endPointer(e){
  const wasDrag=!!drag;
  if(!moved&&wasDrag){const element=document.elementFromPoint(e.clientX,e.clientY);const path=element?.closest('path[data-tag]');if(path)selectCountry(path.dataset.tag);else closeDetail();}
  pointers.delete(e.pointerId);drag=null;pinch=null;container.classList.remove('dragging');
}
container.addEventListener('pointerup',endPointer);
container.addEventListener('pointercancel',e=>{pointers.delete(e.pointerId);drag=null;pinch=null;container.classList.remove('dragging');});
container.addEventListener('pointerleave',()=>{$('tooltip').hidden=true;});
container.addEventListener('keydown',e=>{
  if(['+','=','-','ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Home'].includes(e.key))e.preventDefault();
  if(e.key==='+'||e.key==='=')zoom(.75);if(e.key==='-')zoom(1.33);if(e.key==='Home')resetView();
  const step=view[2]*.1;
  if(e.key==='ArrowLeft')view[0]-=step;if(e.key==='ArrowRight')view[0]+=step;
  if(e.key==='ArrowUp')view[1]-=step;if(e.key==='ArrowDown')view[1]+=step;applyView();
});
const dialog=$('about');
for(const id of ['about-open','about-footer'])$(id).addEventListener('click',()=>dialog.showModal());
for(const id of ['about-close','about-done'])$(id).addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.x||e.clientX>r.right||e.clientY<r.y||e.clientY>r.bottom)dialog.close();}});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeDetail();$('tooltip').hidden=true;}if(e.key==='/'&&!dialog.open&&!['INPUT','TEXTAREA'].includes(document.activeElement.tagName)){e.preventDefault();$('search').focus();}});
function downloadSvg(){
  const clone=svg.cloneNode(true);clone.setAttribute('viewBox',`0 0 ${DATA.width} ${DATA.height+180}`);clone.setAttribute('width',DATA.width);clone.setAttribute('height',DATA.height+180);
  clone.querySelectorAll('path[data-tag]').forEach(p=>{const c=byTag.get(p.dataset.tag);p.removeAttribute('class');p.setAttribute('fill',c.status==='full'?'#63ad72':c.status==='legacy'?'#e6a15a':c.status==='partial'?'url(#partial-hatch)':'#fff');p.setAttribute('stroke','#303d2d');p.setAttribute('stroke-width','1');});
  const ns='http://www.w3.org/2000/svg';
  const rect=document.createElementNS(ns,'rect');rect.setAttribute('y',DATA.height);rect.setAttribute('width',DATA.width);rect.setAttribute('height','180');rect.setAttribute('fill','#f6f6f2');clone.append(rect);
  const text=(x,y,label,size=24)=>{const t=document.createElementNS(ns,'text');t.setAttribute('x',x);t.setAttribute('y',y);t.setAttribute('font-family','Arial, sans-serif');t.setAttribute('font-size',size);t.setAttribute('fill','#212820');t.textContent=label;clone.append(t);};
  text(60,DATA.height+55,'NWW REBORN / АТЛАС РАЗРАБОТКИ — 01.01.1936',32);
  const items=[['#63ad72','Полная переработка'],['#e6a15a','Legacy'],['#fff','Без дерева NWW'],['url(#partial-hatch)','Прочие новые деревья']];
  items.forEach(([color,label],i)=>{const r=document.createElementNS(ns,'rect');r.setAttribute('x',60+i*1100);r.setAttribute('y',DATA.height+95);r.setAttribute('width','26');r.setAttribute('height','26');r.setAttribute('fill',color);r.setAttribute('stroke','#303d2d');clone.append(r);text(104+i*1100,DATA.height+117,label);});
  const blob=new Blob([new XMLSerializer().serializeToString(clone)],{type:'image/svg+xml;charset=utf-8'}),url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='NWW-Reborn-content-map-1936.svg';a.click();setTimeout(()=>URL.revokeObjectURL(url),3000);
}
$('export').addEventListener('click',downloadSvg);
setFilter('all');resetView();
const initial=decodeURIComponent(location.hash.slice(1));if(byTag.has(initial))selectCountry(initial,true);
