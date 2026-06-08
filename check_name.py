content = open('index.html','r',encoding='utf-8').read()
idx = content.find('slice(-1)[0]')
print(content[idx-200:idx+100])
