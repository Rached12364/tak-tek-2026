content = open('index.html','r',encoding='utf-8').read()
# 1. Ajouter la classe home-btn home-btn-red au bouton tunisia
content = content.replace(
    'onclick="showPage(\'tunisia\');startTunisiaXI();" style="width:250px;height:380px;background:linear-gradient(135deg,rgba(26,26,26,0.9),rgba(34,34,34,0.9));border:2px solid #E70013;border-radius:16px;color:#E70013;font-family:Barlow Condensed,sans-serif;font-size:24px;font-weight:900;letter-spacing:3px;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;transition:transform 0.2s;backdrop-filter:blur(4px);"',
    'onclick="showPage(\'tunisia\');startTunisiaXI();" class="home-btn home-btn-red" style="width:250px;height:380px;background:linear-gradient(135deg,rgba(26,26,26,0.9),rgba(34,34,34,0.9));border:2px solid #E70013;border-radius:16px;color:#E70013;font-family:Barlow Condensed,sans-serif;font-size:24px;font-weight:900;letter-spacing:3px;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;transition:transform 0.2s;backdrop-filter:blur(4px);"'
)
# 2. Enlever fond blanc du logo - changer mix-blend-mode:screen par multiply + filter
content = content.replace(
    'style="width:110px;height:110px;object-fit:contain;mix-blend-mode:screen;"',
    'style="width:110px;height:110px;object-fit:contain;mix-blend-mode:multiply;filter:contrast(1.1);"'
)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
