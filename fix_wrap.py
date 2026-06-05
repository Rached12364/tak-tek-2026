content = open('index.html','r',encoding='utf-8').read()
# Chercher le wrap div
idx = content.find('id="wrap"')
print("wrap actuel:", repr(content[idx:idx+60]))
# Ajouter flex row au wrap
import re
content = re.sub(
    r'<div id="wrap">',
    '<div id="wrap" style="display:flex;flex-direction:row;width:100%;height:100vh;overflow:hidden;">',
    content
)
# Forcer #left height et #right height via CSS inline
content = content.replace(
    '<div id="left">',
    '<div id="left" style="flex:1;height:100%;overflow:hidden;">'
)
content = content.replace(
    '<div id="right">',
    '<div id="right" style="width:420px;flex-shrink:0;height:100%;overflow-y:auto;background:#111;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
