content = open('index.html','r',encoding='utf-8').read()
idx = content.find('showPage')
print(repr(content[idx:idx+400]))
