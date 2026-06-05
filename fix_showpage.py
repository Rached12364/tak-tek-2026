content = open('index.html','r',encoding='utf-8').read()
# Ajouter la gestion de page-tunisia dans showPage
content = content.replace(
    'var tn=document.getElementById("page-tunisia"); if(tn) tn.style.display=page==="tunisia"?"flex":"none";',
    ''
)
# Chercher showPage et ajouter tunisia
old = 'var home = document.getElementById("page-home");'
new = '''var tn=document.getElementById("page-tunisia"); if(tn) tn.style.display=page==="tunisia"?"flex":"none";
  var home = document.getElementById("page-home");'''
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
