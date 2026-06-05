content = open('index_backup_v2.html','r',encoding='utf-8').read()
# Trouver où sont les cartes joueurs - chercher la structure du layout bestxi
idx = content.find('id="left"')
print("left at:", idx, repr(content[idx:idx+100]))
idx2 = content.find('id="right"')
print("right at:", idx2, repr(content[idx2:idx2+100]))
# Trouver le conteneur principal bestxi
idx3 = content.find('id="tn-main"')
print("tn-main at:", idx3, repr(content[idx3:idx3+200]))
# Chercher le layout principal (pitch + cards côte à côte)
import re
layouts = re.findall(r'id="([^"]*main[^"]*)"', content)
print("main divs:", layouts)
