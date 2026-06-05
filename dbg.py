content = open('index.html','r',encoding='utf-8').read()
idx = content.find('<div id="page-tunisia"')
print(repr(content[idx:idx+800]))
