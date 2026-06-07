content = open('index.html','r',encoding='utf-8').read()
idx = content.find('page-quiz')
print('page-quiz position:', idx)
print(content[idx-50:idx+300])
