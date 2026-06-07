content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:20px;"',
    'style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:20px;width:100%;"'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
