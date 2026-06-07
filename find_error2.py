content = open('index.html','r',encoding='utf-8').read()
start = content.find('var quizData')
script = content[start:start+3000]
lines = script.split('\n')
for i,line in enumerate(lines):
    # Chercher apostrophes non fermees dans les strings
    if line.count("'") % 2 != 0 and '"//' not in line:
        print('Possible erreur ligne', i+1, ':', line[:150])
