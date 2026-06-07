content = open('index.html','r',encoding='utf-8').read()
idx = content.find('home-btn')
print(content[idx-200:idx+50])
