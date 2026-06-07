content = open('index.html','r',encoding='utf-8').read()
idx = content.find('tuns.png')
print(content[idx-20:idx+150])
