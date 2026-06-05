content = open('index.html','r',encoding='utf-8').read()
# Remplacer toutes les occurrences problematiques dans les strings JS
import re
# Fix: showPage("home") dans les strings html += "..."
content = content.replace(
    'onclick=\'showPage(\"home\")\' style=\'margin-top:auto',
    'onclick=\'tnBack()\' style=\'margin-top:auto'
)
# Fix: le recap a aussi showPage("home") - le garder mais echapper correctement
# Chercher dans tnShowRecap
old = 'onclick=\'showPage(\"home\")\' style=\'padding:14px'
new = 'onclick=\'showPage(\\x22home\\x22)\' style=\'padding:14px'
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
