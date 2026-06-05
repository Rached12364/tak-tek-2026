content = open('index.html','r',encoding='utf-8').read()
# Trouver positions exactes
tm_start = content.find('<div id="tn-main"')
tm_end_search = tm_start
depth = 0
i = tm_start
while i < len(content):
    if content[i:i+4] == '<div':
        depth += 1
    elif content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            tm_end = i + 6
            break
    i += 1
pl_pos = content.find('id="tn-player-list"')
print("tn-main spans:", tm_start, "->", tm_end)
print("tn-player-list at:", pl_pos)
print("Is player-list INSIDE tn-main?", tm_start < pl_pos < tm_end)
print("\nContent just before player-list:")
print(repr(content[pl_pos-300:pl_pos+50]))
