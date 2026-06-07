content = open('index.html','r',encoding='utf-8').read()
idx = content.find('onmouseover')
print(content[idx-300:idx+100])
