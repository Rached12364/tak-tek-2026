import re
content = open('index.html','r',encoding='utf-8').read()
# 1. Fix page-tunisia display
content = re.sub(
    r'<div id="page-tunisia" style="display:none;[^"]*"',
    '<div id="page-tunisia" style="display:none;width:100%;height:100vh;background:#111;flex-direction:column;overflow:hidden;"',
    content
)
# 2. Fix tn-main
content = re.sub(
    r'<div id="tn-main" style="[^"]*">',
    '<div id="tn-main" style="display:flex;flex-direction:row;flex:1;min-height:0;overflow:hidden;">',
    content
)
# 3. Fix pitch width only - keep everything else intact
content = re.sub(
    r'(<!-- LEFT: Pitch -->[^<]*<div style=")([^"]*)(">)',
    r'\g<1>width:55%;flex-shrink:0;height:100%;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;\g<3>',
    content
)
# 4. Fix right panel
content = re.sub(
    r'(<!-- RIGHT[^\-]*-->)[^<]*<div style="[^"]*">(\s*<div id="tn-player-list")',
    r'\1\n    <div style="width:45%;height:100%;overflow-y:auto;padding:24px 20px;background:#111;">\2',
    content,
    flags=re.DOTALL
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
