content = open('index.html', 'r', encoding='utf-8').read()
content = content.replace('TUNISIE', 'MONDE')
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
