content = open('index.html','r',encoding='utf-8').read()
# Force tn-main to be flex-row with proper height
content = content.replace(
    '<div id="tn-main" style="display:flex;height:calc(100vh - 73px);overflow:hidden;">',
    '<div id="tn-main" style="display:flex;flex-direction:row;height:calc(100vh - 73px);overflow:hidden;width:100%;">'
)
# Pitch: fixed width, full height
content = content.replace(
    'width:65%;flex-shrink:0;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;',
    'width:55%;flex-shrink:0;height:100%;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;'
)
# Right panel: 45%, scrollable
content = content.replace(
    '<div style="width:35%;overflow-y:auto;padding:24px 20px;background:#111;">',
    '<div style="width:45%;height:100%;overflow-y:auto;padding:24px 20px;background:#111;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
