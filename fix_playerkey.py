content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'html += "<button onclick=\'startQuiz("" + playerKey + "")\'',
    'html += "<button onclick=\'startQuiz(\'" + playerKey + "\')\'"'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
