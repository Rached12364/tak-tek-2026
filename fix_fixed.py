content = open('index.html','r',encoding='utf-8').read()
# In showPage function, hide/show the fixed home button
content = content.replace(
    'if(page==="tunisia" && typeof startTunisiaXI==="function") { setTimeout(startTunisiaXI, 50); }',
    'if(page==="tunisia" && typeof startTunisiaXI==="function") { setTimeout(startTunisiaXI, 50); }\n  var fixedBtns = document.querySelectorAll(\'div[style*="position:fixed"]\');\n  fixedBtns.forEach(function(b){b.style.display=page==="tunisia"||page==="home"?"none":"block";});'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
