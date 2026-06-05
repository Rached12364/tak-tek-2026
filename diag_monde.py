content = open('index.html','r',encoding='utf-8').read()
# Trouver page-bestxi ou page-monde
import re
pages = re.findall(r'id="(page-[^"]+)"', content)
print("Toutes les pages:", pages)
# Chercher le panneau de sélection joueurs monde
for keyword in ['player-list', 'bestxi', 'step-num', 'step-head']:
    idx = content.find(keyword)
    if idx > 0:
        print(f"\n{keyword} at {idx}:", repr(content[idx-100:idx+100]))
