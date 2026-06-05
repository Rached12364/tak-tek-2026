import re
content = open('index.html','r',encoding='utf-8').read()
# Fix pitch div - replace the broken style
content = re.sub(
    r'<div style="width:420px;flex-shrink:0;background:linear-gradient\(180deg,#0b3d1f,#0a3018,#0b3d1f\);position:relative;overflow:hidden;[^"]*">',
    '<div style="width:55%;flex-shrink:0;height:100%;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;">',
    content
)
# Fix right panel
content = re.sub(
    r'<div style="width:33%;flex-shrink:0;overflow-y:auto;[^"]*">',
    '<div style="width:45%;height:100%;overflow-y:auto;padding:24px 20px;background:#111;">',
    content
)
content = re.sub(
    r'<div style="flex:1;overflow-y:auto;[^"]*">',
    '<div style="width:45%;height:100%;overflow-y:auto;padding:24px 20px;background:#111;">',
    content
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
