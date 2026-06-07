content = open('index.html','r',encoding='utf-8').read()
idx = content.find('fadeInUp')
print(content[idx-200:idx+100])
