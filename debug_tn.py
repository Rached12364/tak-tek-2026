content = open('index.html','r',encoding='utf-8').read()
# 1. Vérifier la structure actuelle de tn-main
import re
# Trouver le bloc tn-main complet
start = content.find('<div id="tn-main"')
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
tn_main_block = content[start:end]
print("=== STRUCTURE TN-MAIN ACTUELLE ===")
print(tn_main_block[:1500])
# 2. Vérifier où est le panneau droit
right_pos = tn_main_block.find('RIGHT: Player selection')
print(f"\nPanneau droit trouvé à la position: {right_pos}")
# 3. Vérifier que le panneau droit est bien un frère du pitch (pas à l'intérieur)
pitch_end = tn_main_block.find('</div>', tn_main_block.find('LEFT: Pitch'))
print(f"Fin du pitch: {pitch_end}")
print(f"Début du panneau droit: {right_pos}")
