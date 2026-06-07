content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '{ q: "Benzarti est ne en 1950 ce qui lui fait 76 ans en 2026 ?", type:"tf", answer: true }',
    '{ q: "En quelle annee Benzarti est ne ?", type:"mcq", answer: 1950, choices:[1945, 1950, 1955] }'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
