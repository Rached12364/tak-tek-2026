files = [
    'index_backup_20260605_0210.html',
    'index_backup_fixed.html', 
    'index_backup_v2.html',
    'index_save_20260605_1138.html',
    'index_save_20260605_1232.html',
    'index_save_20260605_1246.html',
    'index.html'
]
for f in files:
    try:
        c = open(f,'r',encoding='utf-8').read()
        has_tm = 'id="tn-main"' in c
        has_right = 'id="right"' in c
        has_cards = 'id="cards"' in c
        has_tunisia = 'id="page-tunisia"' in c
        has_tnlist = 'id="tn-player-list"' in c
        print(f"{f}: tn-main={has_tm} right={has_right} cards={has_cards} tunisia={has_tunisia} tn-list={has_tnlist} size={len(c)}")
    except:
        print(f"{f}: ERREUR")
