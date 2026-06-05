lines = open('index.html','r',encoding='utf-8').read().split('\n')
result = []
i = 0
while i < len(lines):
    l = lines[i]
    # Supprimer bouton Tunisia (ligne 742) - le bouton fait 3 lignes (742,743,744)
    if i == 741:
        # Sauter jusqu'au </button> fermant
        while i < len(lines) and '</button>' not in lines[i]:
            i += 1
        i += 1  # sauter la ligne </button>
        continue
    # Supprimer lignes Tunisia dans showPage (1429, 1430, 1432)
    if i in [1428, 1429, 1431]:
        i += 1
        continue
    # Supprimer page-tunisia (ligne 1562) jusqu'a tunisia.js (ligne 1613)
    if i == 1561:
        while i < len(lines) and 'tunisia.js' not in lines[i]:
            i += 1
        i += 1  # sauter la ligne tunisia.js
        continue
    result.append(l)
    i += 1
open('index.html','w',encoding='utf-8').write('\n'.join(result))
print("OK lignes supprimees:", 1614 - len(result))
