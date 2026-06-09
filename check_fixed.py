content = open('index.html','r',encoding='utf-8').read()
idx = content.find('position:fixed')
print(content[idx-20:idx+300])
