content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '.home-btn:hover {\n  transform: scale(1.05);\n}',
    '.home-btn:hover {\n  transform: scale(1.05) !important;\n}'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
