content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '.home-btn {\n  animation: fadeInUp 0.6s ease both;\n}',
    '.home-btn {\n  animation: fadeInUp 0.6s ease both;\n  transition: transform 0.2s ease;\n}\n.home-btn:hover {\n  transform: scale(1.05);\n}'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
