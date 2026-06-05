import re
content = open('index.html','r',encoding='utf-8').read()
# Supprimer bouton Tunisia
content = re.sub(r"\s*<button onclick=\"showPage\('tunisia'\).*?</button>", "", content, flags=re.DOTALL)
# Supprimer lignes Tunisia dans showPage
content = re.sub(r'\n  var tn=document\.getElementById\("page-tunisia"\);[^\n]+', '', content)
content = re.sub(r'\n  if\(page===\"tunisia\"[^\n]+', '', content)
content = re.sub(r'\n  fixedBtns\.forEach\(function\(b\)\{b\.style\.display=page===\"tunisia\"[^\n]+', '', content)
# Supprimer page-tunisia jusqu'a tunisia.js
content = re.sub(r'</script><div id="page-tunisia".*?<script src="tunisia\.js"></script></body>', '</body>', content, flags=re.DOTALL)
open('index.html','w',encoding='utf-8').write(content)
print("OK - lignes:", len(content.split('\n')))
