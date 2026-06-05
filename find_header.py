content = open('index.html','r',encoding='utf-8').read()
# Find any fixed/absolute positioned header
import re
for m in re.finditer(r'<div[^>]*position:(fixed|sticky)[^>]*>', content):
    print(repr(m.group()[:150]))
    print('---')
