content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'background:linear-gradient(135deg,#0a0a1a 0%,#0d1b2a 40%,#0a0a1a 100%)',
    'background:url(backround.jpg) center/cover no-repeat fixed'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
