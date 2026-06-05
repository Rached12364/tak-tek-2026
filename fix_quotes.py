content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'html += "<button onclick=\'showPage(\"home\")\' style=',
    'html += "<button onclick=\'showPage(\\\"home\\\")\' style='
)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
