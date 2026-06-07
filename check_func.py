content = open('index.html','r',encoding='utf-8').read()
idx = content.find('function startQuiz')
print('startQuiz fonction position:', idx)
print(content[idx:idx+200])
