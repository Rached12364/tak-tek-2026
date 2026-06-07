content = open('index.html','r',encoding='utf-8').read()
content = content.replace('raki_aouani.jpg', 'raki_aouani2.png')
open('index.html','w',encoding='utf-8').write(content)
print('OK')
