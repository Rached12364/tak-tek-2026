content = open('index.html','r',encoding='utf-8').read()
idx = content.find('<!-- LEFT: Pitch -->')
print(repr(content[idx:idx+300]))
