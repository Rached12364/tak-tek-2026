content = open('index.html','r',encoding='utf-8').read()
idx = content.find('Lignes terrain')
print(content[idx:idx+400])
