content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '<div style="perspective:400px;"><img src="tuns.png" style="width:160px;height:160px;object-fit:contain;animation:quiz-spin 4s linear infinite;"></div>',
    '<img src="tuns.png" class="btn-icon" style="width:160px;height:160px;object-fit:contain;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
