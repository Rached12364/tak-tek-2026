content = open('index.html','r',encoding='utf-8').read()
import re
matches = [(m.start(), m.group()) for m in re.finditer(r'@keyframes spin[^3]', content)]
for pos, match in matches:
    print('Position:', pos)
    print(content[pos:pos+150])
    print('---')
