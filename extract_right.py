import re
content = open('index.html','r',encoding='utf-8').read()
# Trouver la structure exacte
tn_main_start = content.find('<div id="tn-main"')
tn_main_end = content.find('</div>', tn_main_start)
depth = 0
i = tn_main_start
while i < len(content):
    if content[i:i+4] == '<div':
        depth += 1
    elif content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            tn_main_end = i + 6
            break
    i += 1
tn_main = content[tn_main_start:tn_main_end]
# Trouver le pitch et son contenu
pitch_start = tn_main.find('<!-- LEFT: Pitch -->')
pitch_div_start = tn_main.find('<div style="width:55%', pitch_start)
pitch_div_end = tn_main.find('</div>', pitch_div_start)
depth = 0
i = pitch_div_start
while i < len(tn_main):
    if tn_main[i:i+4] == '<div':
        depth += 1
    elif tn_main[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            pitch_div_end = i + 6
            break
    i += 1
# Trouver le panneau droit (qui est malencontreusement DANS le pitch)
right_start = tn_main.find('<!-- RIGHT: Player selection -->')
right_div_start = tn_main.find('<div style="width:45%', right_start)
right_div_end = tn_main.find('</div>', right_div_start)
depth = 0
i = right_div_start
while i < len(tn_main):
    if tn_main[i:i+4] == '<div':
        depth += 1
    elif tn_main[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            right_div_end = i + 6
            break
    i += 1
print(f"Pitch: {pitch_div_start} -> {pitch_div_end}")
print(f"Panneau droit: {right_div_start} -> {right_div_end}")
print(f"Le panneau droit est DANS le pitch ? {right_div_start > pitch_div_start and right_div_end < pitch_div_end}")
# Créer un nouveau tn-main avec la structure correcte
pitch_content = tn_main[pitch_div_start:pitch_div_end]
right_content = tn_main[right_div_start:right_div_end]
# Extraire le reste (dots etc)
before_pitch = tn_main[:pitch_div_start]
after_pitch = tn_main[pitch_div_end:]
# Reconstruire : pitch (sans le panneau dedans) + panneau droit à côté
new_tn_main = before_pitch + pitch_content + '</div>' + right_content + after_pitch
# Remplacer dans le fichier
new_content = content[:tn_main_start] + new_tn_main + content[tn_main_end:]
open('index.html','w',encoding='utf-8').write(new_content)
print("✅ Structure corrigée : panneau droit extrait du pitch")
