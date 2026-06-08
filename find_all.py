content = open('index.html','r',encoding='utf-8').read()
import re
for m in re.finditer(r'[Hh]ansi|HANSI|[Ff]lick|FLICK|Barcelona', content):
    print('Position:', m.start(), ':', content[m.start():m.start()+50])
    print('---')
