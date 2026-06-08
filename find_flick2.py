content = open('index.html','r',encoding='utf-8').read()
idx = content.find('Hansi')
print('Position:', idx)
print(content[idx-50:idx+300])
