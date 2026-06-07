content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'border:2px solid #00C853;border-radius:16px;color:#00C853;font-fam',
    'border:2px solid #00C853;border-radius:16px;color:#00C853;transition:transform 0.2s;font-fam'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
