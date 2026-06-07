content = open('index.html','r',encoding='utf-8').read()
start = content.find('var quizData')
end = content.find('function backToList')
script = content[start:end]
# Chercher les apostrophes problematiques
lines = script.split('\n')
for i,line in enumerate(lines):
    if "style=color" in line or "style= color" in line:
        print('PROBLEME ligne', i+1, ':', line[:150])
