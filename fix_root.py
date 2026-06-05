content = open('index.html','r',encoding='utf-8').read()
# 1. page-tunisia: enlever flex-direction du style statique (inutile quand display:none)
content = content.replace(
    'id="page-tunisia" style="display:none;width:100%;height:100vh;background:#111;overflow:hidden;flex-direction:column;"',
    'id="page-tunisia" style="display:none;width:100%;height:100vh;background:#111;overflow:hidden;"'
)
# 2. JS showPage: quand on affiche tunisia, forcer flex + column + height
content = content.replace(
    'tn.style.display=page==="tunisia"?"flex":"none";if(page==="tunisia"){tn.style.height="100vh";}',
    'if(page==="tunisia"){tn.style.display="flex";tn.style.flexDirection="column";tn.style.height="100vh";}else{tn.style.display="none";}'
)
# 3. RIGHT panel: lui donner width:45% et height:100%
content = content.replace(
    '<div id="right">',
    '<div id="right" style="width:45%;height:100%;overflow-y:auto;padding:24px 20px;background:#111;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
