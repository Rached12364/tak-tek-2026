content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '<img src="tuns.png" style="width:120px;height:120px;object-fit:contain;animation:quiz-spin 3s linear infinite;">',
    '<img src="tuns.png" style="width:180px;height:180px;object-fit:contain;animation:quiz-spin 4s linear infinite;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
