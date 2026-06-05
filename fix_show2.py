import re
content = open('index.html', 'r', encoding='utf-8').read()
# Fix the broken showPage - remove the bad "var home =" line and move TUNISIA_STEPS outside
old = '''  var tp = document.getElementById("page-tunisia"); if(tp) tp.style.display = page==="tunisia" ? "flex" : "none";
  var home =
var TUNISIA_STEPS'''
new = '''  var tp = document.getElementById("page-tunisia"); if(tp) tp.style.display = page==="tunisia" ? "flex" : "none";
  var home = document.getElementById("page-home");
  var wrap = document.getElementById("wrap");
  var tier = document.getElementById("page-tierlist");
  if(home) home.style.display = page==="home" ? "flex" : "none";
  if(wrap) wrap.style.display = page==="bestxi" ? "flex" : "none";
  if(tier) tier.style.display = page==="tierlist" ? "flex" : "none";
  if(page==="tierlist" && document.getElementById("player-pool") && document.getElementById("player-pool").children.length===0) initTierList();
}
var TUNISIA_STEPS'''
content = content.replace(old, new, 1)
# Remove duplicate closing brace if any
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
