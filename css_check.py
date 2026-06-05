import os
# Lire les CSS
for f in os.listdir('css'):
    content = open(f'css/{f}','r',encoding='utf-8').read()
    if 'tn-main' in content or 'tunisia' in content or 'page-tunisia' in content:
        print(f"=== {f} ===")
        print(content[:1000])
# Aussi: état initial de page-tunisia dans le HTML
html = open('index.html','r',encoding='utf-8').read()
idx = html.find('id="page-tunisia"')
print("\nPAGE-TUNISIA TAG:", repr(html[idx:idx+150]))
# Et tn-main display actuel
idx2 = html.find('id="tn-main"')
print("TN-MAIN TAG:", repr(html[idx2:idx2+120]))
