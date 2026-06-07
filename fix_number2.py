content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '{ q: "Combien de fois Benzarti a ete selectionneur de la Tunisie ?", type:"number", answer: 3, diff:3 }',
    '{ q: "Combien de fois Benzarti a ete selectionneur de la Tunisie ?", type:"mcq", answer: 3, choices:[1, 3, 5] }'
)
content = content.replace(
    '{ q: "En quelle annee Benzarti est ne ?", type:"number", answer: 1950, diff:3 }',
    '{ q: "En quelle annee Benzarti est ne ?", type:"mcq", answer: 1950, choices:[1945, 1950, 1955] }'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
