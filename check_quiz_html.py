content = open('index.html','r',encoding='utf-8').read()
idx = content.find('page-quiz')
print(content[idx:idx+1500])
