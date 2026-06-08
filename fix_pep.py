content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    "name:'Pep Guardiola',  club:'Manchester City', country:'Allemagne', flag:'🇩🇪', ini:'HF'",
    "name:'Pep Guardiola',  club:'Manchester City', country:'Espagne', flag:'🇪🇸', ini:'PG'"
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
