content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '<div style="position:absolute;width:75%;height:88%;border:2px solid rgba(255,255,255,0.25);border-radius:4px;"></div>',
    '<div style="position:absolute;width:75%;height:88%;border:2px solid rgba(255,255,255,0.25);border-radius:4px;animation:tn-glow-lines 3s ease-in-out infinite;"></div>'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
