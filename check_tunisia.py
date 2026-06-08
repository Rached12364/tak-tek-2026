content = open('index.html','r',encoding='utf-8').read()
idx = content.find('page-tunisia')
print(content[idx:idx+300])
