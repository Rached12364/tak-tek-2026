import re
content = open('index.html','r',encoding='utf-8').read()
# Extraire le bloc #right complet
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
right_block = content[start:end]
# Trouver la fermeture de tn-main (compter les divs depuis tn-main)
tm_start = content.find('<div id="tn-main"')
depth = 0
i = tm_start
while i < len(content):
    if content[i:i+4] == '<div':
        depth += 1
    elif content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            tm_end = i
            break
    i += 1
# Supprimer #right de sa position actuelle
content_new = content[:start] + content[end:]
# Réinsérer #right juste avant la fermeture de tn-main
tm_end_new = content_new.find('</div>', content_new.find('<div id="tn-main"'))
# Recalculer tm_end dans le nouveau contenu
tm_start2 = content_new.find('<div id="tn-main"')
depth = 0
i = tm_start2
while i < len(content_new):
    if content_new[i:i+4] == '<div':
        depth += 1
    elif content_new[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            tm_end2 = i
            break
    i += 1
content_new = content_new[:tm_end2] + '\n' + right_block + '\n' + content_new[tm_end2:]
open('index.html','w',encoding='utf-8').write(content_new)
print('done - right block moved inside tn-main')
