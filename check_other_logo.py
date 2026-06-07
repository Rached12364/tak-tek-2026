content = open('index.html','r',encoding='utf-8').read()
idx = content.find('logo-tunisia')
print(content[idx-50:idx+200])
