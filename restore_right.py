# Extraire le bloc #right complet de la sauvegarde 1246
old = open('index_save_20260605_1246.html','r',encoding='utf-8').read()
start = old.find('<div id="right"')
depth = 0
i = start
while i < len(old):
    if old[i:i+4] == '<div':
        depth += 1
    elif old[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            end = i + 6
            break
    i += 1
right_block = old[start:end]
print("Extrait #right, longueur:", len(right_block))
print("Apercu:", repr(right_block[:150]))
# Le réinsérer dans index.html juste avant </div> de tn-main
content = open('index.html','r',encoding='utf-8').read()
# Trouver fin de tn-main
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
content = content[:tm_end] + '\n' + right_block + '\n' + content[tm_end:]
open('index.html','w',encoding='utf-8').write(content)
print('done')
