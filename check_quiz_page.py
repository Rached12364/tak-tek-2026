content = open('index.html','r',encoding='utf-8').read()
idx = content.find("id=\"quiz\"")
print('Page quiz position:', idx)
print(content[idx:idx+400])
