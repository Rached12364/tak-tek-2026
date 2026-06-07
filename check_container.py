content = open('index.html','r',encoding='utf-8').read()
idx = content.find('quiz-question-container')
print('Position:', idx)
print(content[idx-200:idx+100])
