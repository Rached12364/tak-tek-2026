content = open('index.html','r',encoding='utf-8').read()
# Position de #right et #cards
r_pos = content.find('id="right"')
c_pos = content.find('id="cards"')
# Trouver fin de #right
start = content.find('<div id="right"')
depth = 0
i = start
while i < len(content):
    if content[i:i+4] == '<div':
        depth += 1
    elif content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            r_end = i + 6
            break
    i += 1
print("right spans:", start, "->", r_end)
print("cards at:", c_pos)
print("cards INSIDE right?", start < c_pos < r_end)
print("\nContenu de #right:")
print(repr(content[start:r_end]))
