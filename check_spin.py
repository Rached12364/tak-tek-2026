content = open('index.html','r',encoding='utf-8').read()
idx = content.find('quiz-spin')
while idx != -1:
    print('Position:', idx)
    print(content[idx-100:idx+100])
    print('---')
    idx = content.find('quiz-spin', idx+1)
