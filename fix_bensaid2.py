content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '{name:"BECHIR BEN SAID", club:"Esperance Tunis", age:"31 ans", mv:"562k", img:"belwafi.png"}',
    '{name:"BECHIR BEN SAID", club:"Esperance Tunis", age:"31 ans", mv:"562k", img:"https://static.flashscore.com/res/image/data/4C42SQFG-Eg24ohRo.png"}'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
