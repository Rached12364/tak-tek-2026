content = open('index.html','r',encoding='utf-8').read()
idx = content.find('id="right"')
print(repr(content[idx:idx+200]))
