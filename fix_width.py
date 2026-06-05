content = open('index.html','r',encoding='utf-8').read()
# Make right panel (player list) take 1/3 width, pitch takes 2/3
content = content.replace(
    '<div style="flex:1;overflow-y:auto;padding:24px 32px;background:#111;">',
    '<div style="width:33%;flex-shrink:0;overflow-y:auto;padding:24px 20px;background:#111;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
