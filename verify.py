content = open('index.html','r',encoding='utf-8').read()
# Vérifier que tn-main, LEFT Pitch, RIGHT, tn-selection sont UNIQUEMENT dans page-tunisia
tn_start = content.find('id="page-tunisia"')
tn_end = content.find('id="page-tunisia"', tn_start+1)  # 2eme occurrence si existe
print("page-tunisia positions:", tn_start, tn_end)
# Vérifier que LEFT: Pitch est dans Tunisia seulement
lp = content.find('<!-- LEFT: Pitch -->')
print("LEFT Pitch at:", lp, "- inside Tunisia?", lp > tn_start)
# Vérifier que #wrap (monde) n'a pas LEFT Pitch
wp = content.find('id="wrap"')
print("wrap at:", wp)
print("LEFT Pitch is AFTER wrap?", lp > wp)
# tn-selection
ts = content.find('id="tn-selection"')
print("tn-selection at:", ts, "- inside Tunisia?", ts > tn_start)
