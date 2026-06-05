content = open('index.html', 'r', encoding='utf-8').read()
# Fix showPage for tunisia - it needs to also call startTunisiaXI
old = 'var tn=document.getElementById("page-tunisia"); if(tn) tn.style.display=page==="tunisia"?"flex":"none";'
new = '''var tn=document.getElementById("page-tunisia"); if(tn) tn.style.display=page==="tunisia"?"flex":"none";
  if(page==="tunisia" && typeof startTunisiaXI==="function") { startTunisiaXI(); }'''
content = content.replace(old, new, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
