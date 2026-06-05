content = open('index.html','r',encoding='utf-8').read()
tm_start = content.find('<div id="tn-main"')
# Trouver le 1er enfant direct (pitch) et sa fermeture
pitch_start = content.find('<!-- LEFT: Pitch -->', tm_start)
# Compter les divs du pitch
i = content.find('<div style="width:55%', pitch_start)
depth = 0
while i < len(content):
    if content[i:i+4] == '<div':
        depth += 1
    elif content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            pitch_end = i + 6
            break
    i += 1
print("Pitch ends at:", pitch_end)
print("Right panel starts at:", content.find('<!-- RIGHT', tm_start))
print("Gap between pitch end and right panel:")
print(repr(content[pitch_end:pitch_end+200]))
