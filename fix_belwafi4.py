content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'img:"https://static.flashscore.com/res/image/data/4C42SQFG-Eg24ohRo.png"}',
    'img:"belwafi.png"}'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
