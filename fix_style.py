content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    "style=color:#FFD700;>",
    "style='color:#FFD700;'>"
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
