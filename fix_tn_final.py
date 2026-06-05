content = open('index.html','r',encoding='utf-8').read()
# Fix panneau droit Tunisia: 33% -> 45%
content = content.replace(
    '<!-- RIGHT: Player selection -->\n    <div style="width:33%;flex-shrink:0;overflow-y:auto;padding:24px 20px;background:#111;">',
    '<!-- RIGHT: Player selection -->\n    <div style="width:45%;height:100%;overflow-y:auto;padding:24px 20px;background:#111;">'
)
# Fix pitch Tunisia: prendre 55%
import re
content = re.sub(
    r'(<!-- LEFT: Pitch -->[\s\S]{0,10}<div style=")[^"]*(")',
    r'\g<1>width:55%;flex-shrink:0;height:100%;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;\g<2>',
    content
)
# Fix tn-main: flex row explicite
content = re.sub(
    r'<div id="tn-main" style="[^"]*">',
    '<div id="tn-main" style="display:flex;flex-direction:row;width:100%;height:calc(100vh - 73px);overflow:hidden;">',
    content
)
# Fix page-tunisia JS (showPage)
content = content.replace(
    'if(page==="tunisia"){tn.style.display="flex";tn.style.flexDirection="column";tn.style.height="100vh";}else{tn.style.display="none";}',
    'if(page==="tunisia"){tn.style.display="flex";tn.style.flexDirection="column";tn.style.height="100vh";var tm=document.getElementById("tn-main");if(tm){tm.style.display="flex";tm.style.flexDirection="row";}}else{tn.style.display="none";}'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
