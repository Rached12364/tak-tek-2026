content = open('index.html','r',encoding='utf-8').read()
idx = content.find('id="page-home"')
print(content[idx:idx+200])
