content = open('index.html','r',encoding='utf-8').read()
idx = content.find('HOME')
print(content[idx-100:idx+200])
