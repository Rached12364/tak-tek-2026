content = open('index.html','r',encoding='utf-8').read()
# Trouver le bloc tn-main
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
tn_main = content[start:end]
# Afficher le milieu (entre pitch et panneau droit)
print("=== CE QU'IL Y A ENTRE LE PITCH ET LE PANNEAU DROIT ===\n")
print(tn_main[2051:9727])
print("\n=== FIN DE L'EXTRAIT ===")
# Vérifier si le panneau droit est DANS le pitch (mal fermé)
pitch_start = tn_main.find('LEFT: Pitch')
pitch_div_start = tn_main.find('<div style="width:55%', pitch_start)
# Compter les divs ouvertes/fermées dans le pitch
open_divs = 0
for j in range(pitch_div_start, min(pitch_div_start + 8000, len(tn_main))):
    if tn_main[j:j+4] == '<div':
        open_divs += 1
    elif tn_main[j:j+6] == '</div>':
        open_divs -= 1
        if open_divs == 0:
            print(f"\nLe pitch se ferme correctement à la position {j}")
            print(f"Le panneau droit est à {9727} - {'DANS' if j > 9727 else 'APRES'} le pitch")
            break
