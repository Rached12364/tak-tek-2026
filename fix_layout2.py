import re
content = open('index.html','r',encoding='utf-8').read()
# Fix page-tunisia to be column with flex children
content = re.sub(
    r'<div id="page-tunisia" style="[^"]*"',
    '<div id="page-tunisia" style="display:none;width:100%;height:100vh;background:#111;flex-direction:column;overflow:hidden;"',
    content
)
# Fix tn-main to take remaining height
content = re.sub(
    r'<div id="tn-main" style="[^"]*">',
    '<div id="tn-main" style="display:flex;flex-direction:row;flex:1;overflow:hidden;min-height:0;">',
    content
)
# Pitch: 55% width, full height
content = re.sub(
    r'<!-- LEFT: Pitch -->\s*<div style="[^"]*linear-gradient[^"]*0b3d1f[^"]*">',
    '<!-- LEFT: Pitch -->\n    <div style="width:55%;flex-shrink:0;height:100%;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;">',
    content
)
# Right panel: 45%
content = re.sub(
    r'<!-- RIGHT[^>]*>\s*<div style="[^"]*tn-player-list[^"]*">',
    lambda m: m.group(0),
    content
)
content = re.sub(
    r'(<!-- RIGHT.*?-->)\s*<div style="[^"]*overflow-y:auto[^"]*">',
    r'\1\n    <div style="width:45%;height:100%;overflow-y:auto;padding:24px 20px;background:#111;">',
    content,
    flags=re.DOTALL
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
