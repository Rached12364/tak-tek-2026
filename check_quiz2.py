content = open('index.html','r',encoding='utf-8').read()
idx = content.find('function startQuiz')
print(content[idx:idx+200])
