content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    "'>??? RETOUR</button>",
    "'>&#8592; RETOUR</button>"
)
# Remplacer showPage("home") par tnBack()
content = content.replace(
    "onclick='showPage(\\\"home\\\")' style='margin-top:auto;",
    "onclick='tnBack()' style='margin-top:auto;"
)
# Ajouter fonction tnBack
old_func = 'function tnPick(stepIdx, playerIdx) {'
new_func = '''function tnBack() {
  if(tnStep > 0) { tnStep--; tnRender(); }
  else { showPage("home"); }
}
function tnPick(stepIdx, playerIdx) {'''
content = content.replace(old_func, new_func)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
