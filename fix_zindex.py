content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '<div style="position:absolute;top:12px;right:12px;z-index:100;display:flex;gap:8px;">',
    '<div style="position:fixed;top:12px;right:12px;z-index:9999;display:flex;gap:8px;pointer-events:auto;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
