content = open('index.html','r',encoding='utf-8').read()
idx = content.find('Luis Enrique')
print('Luis Enrique position:', idx)
print(content[idx-50:idx+400])
