import re
content = open('index.html','r',encoding='utf-8').read()
for m in re.finditer(r'<button[^>]*>.*?HOME.*?</button>', content, re.DOTALL):
    print(repr(m.group()[:200]))
    print('---')
