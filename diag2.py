content = open('index.html','r',encoding='utf-8').read()
# Chercher page bestxi
idx = content.find('id="page-bestxi"')
print("page-bestxi:", idx)
# Chercher dans js/
import os
for f in os.listdir('js'):
    c = open(f'js/{f}','r',encoding='utf-8').read()
    if 'bestxi' in c.lower() or 'step' in c:
        print(f"\n=== js/{f} (first 300) ===")
        print(c[:300])
# Structure du right panel dans index_save_20260605_1246
old = open('index_save_20260605_1246.html','r',encoding='utf-8').read()
idx2 = old.find('id="page-bestxi"')
print("\npage-bestxi in 1246:", idx2)
idx3 = old.find('id="right"')
print("right panel in 1246:", repr(old[idx3:idx3+200]))
