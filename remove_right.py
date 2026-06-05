content = open('index.html','r',encoding='utf-8').read()
# Supprimer le bloc #right (dupliqué, inutile)
start = content.find('<div id="right"')
depth = 0
i = start
while i < len(content):
    if content[i:i+4] == '<div':
        depth += 1
    elif content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            end = i + 6
            break
    i += 1
content = content[:start] + content[end:]
open('index.html','w',encoding='utf-8').write(content)
print('done - #right removed')
