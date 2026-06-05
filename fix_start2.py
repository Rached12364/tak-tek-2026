content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'function startTunisiaXI() { tnStep=0; tnPicks={}; setTimeout(tnRender,50); }',
    '''function startTunisiaXI() {
  tnStep=0; tnPicks={};
  var pg = document.getElementById("page-tunisia");
  if(pg) pg.style.display="flex";
  setTimeout(tnRender, 100);
}'''
)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
