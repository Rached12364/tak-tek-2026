content = open('index.html','r',encoding='utf-8').read()
idx = content.find('id="home-nav-btn"')
print('Position:', idx)
print(content[idx-20:idx+200])
