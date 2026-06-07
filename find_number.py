content = open('index.html','r',encoding='utf-8').read()
import re
matches = re.finditer(r'type:"number"', content)
for m in matches:
    print('Position:', m.start())
    print(content[m.start()-50:m.start()+100])
    print('---')
