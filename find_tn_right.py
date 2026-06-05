content = open('index.html','r',encoding='utf-8').read()
# Tout ce qui est dans page-tunisia
tn_start = content.find('id="page-tunisia"')
# Chercher le panneau droit après LEFT Pitch
lp = content.find('<!-- LEFT: Pitch -->', tn_start)
print("Après LEFT Pitch, chercher RIGHT:")
right_comment = content.find('<!-- RIGHT', tn_start)
print("RIGHT comment at:", right_comment)
print(repr(content[right_comment:right_comment+200]))
# Chercher tn-player-list
pl = content.find('id="tn-player-list"')
print("\ntn-player-list at:", pl)
print(repr(content[pl-150:pl+50]))
