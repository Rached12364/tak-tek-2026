content = open('index.html','r',encoding='utf-8').read()
lines = content.split('\n')
# Afficher les lignes autour de 742, 1429, 1562 pour confirmer
for i in [741, 742, 743, 1428, 1429, 1430, 1431, 1432, 1561, 1562, 1563, 1612, 1613]:
    if i < len(lines):
        print(f"L{i+1}: {lines[i][:120]}")
