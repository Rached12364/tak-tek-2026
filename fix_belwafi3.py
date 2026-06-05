content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'https://i.ytimg.com/vi/fefKdTsX8UI/maxresdefault.jpg',
    'belwafi.png'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
