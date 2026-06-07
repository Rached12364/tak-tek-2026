content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '<img src="tuns.png" id="quiz-logo-spin" style="width:180px;height:180px;object-fit:contain;">',
    '<img src="tuns.png" class="btn-icon" style="width:160px;height:160px;object-fit:contain;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
