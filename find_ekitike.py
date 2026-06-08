content = open('index.html','r',encoding='utf-8').read()
idx = content.find('Ekitike')
print('Position:', idx)
print(content[idx-50:idx+200])
