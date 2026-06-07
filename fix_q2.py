content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '{ q: "Dans quel club Chaouat jouait avant Club Africain ?", type:"tf", answer: false, diff:3, hint:"ES Sahel - VRAI ou Club Sfaxien - FAUX" }',
    '{ q: "Chaouat jouait a ES Sahel avant de rejoindre Club Africain ?", type:"tf", answer: true, diff:3 }'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
