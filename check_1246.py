# Lire la sauvegarde propre
old = open('index_save_20260605_1246.html','r',encoding='utf-8').read()
# Vérifier sa structure
tm = old.find('<div id="tn-main"')
right = old.find('<div id="right"')
print("1246 - tn-main at:", tm)
print("1246 - right at:", right)
print("1246 - right INSIDE tn-main?", )
# Trouver fin tn-main
depth = 0
i = tm
while i < len(old):
    if old[i:i+4] == '<div': depth += 1
    elif old[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            tm_end = i + 6
            break
    i += 1
print("tn-main spans:", tm, "->", tm_end)
print("right inside tn-main?", tm < right < tm_end)
print("\ntn-main content (first 400):", repr(old[tm:tm+400]))
