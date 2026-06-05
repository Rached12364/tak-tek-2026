import re
content = open('index.html','r',encoding='utf-8').read()
# 1. Supprimer le bouton Tunisia (de <button onclick="showPage('tunisia') jusqu'a </button>)
content = re.sub(r"\s*<button onclick=\"showPage\('tunisia'\).*?</button>", "", content, flags=re.DOTALL)
# 2. Supprimer les 3 lignes Tunisia dans showPage
content = content.replace('\n  var tn=document.getElementById("page-tunisia"); if(tn) tn.style.display=page===\"tunisia\";\"flex\":\"none\";', '')
content = re.sub(r'\n  var tn=document\.getElementById\("page-tunisia"\);[^\n]+', '', content)
content = re.sub(r'\n  if\(page===\"tunisia\"[^\n]+', '', content)
content = re.sub(r'\n  fixedBtns\.forEach\(function\(b\)\{b\.style\.display=page===\"tunisia\"[^\n]+', '', content)
# 3. Supprimer page-tunisia (de </script><div id="page-tunisia" jusqu'a tunisia.js></script></body>)
content = re.sub(r'</script><div id="page-tunisia".*?<script src="tunisia\.js"></script></body>', '</body>', content, flags=re.DOTALL)
open('index.html','w',encoding='utf-8').write(content)
print("OK - lignes restantes:", len(content.split('\n')))
