import re
content = open('index.html','r',encoding='utf-8').read()
idx = content.find('id="tn-main"')
print(repr(content[idx-200:idx+300]))
