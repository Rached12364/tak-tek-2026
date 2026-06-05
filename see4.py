content = open('index.html','r',encoding='utf-8').read()
idx = content.find('function showPage')
print(repr(content[idx:idx+600]))
