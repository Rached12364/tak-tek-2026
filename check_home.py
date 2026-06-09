content = open('index.html','r',encoding='utf-8').read()
idx = content.find('page-home')
print(content[idx:idx+300])
