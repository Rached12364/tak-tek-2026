content = open('index.html','r',encoding='utf-8').read()
# Deplacer le slot coach en haut droite
content = content.replace(
    'id="tn-slot-coach" style="position:absolute;top:2%;left:50%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #FFD700;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#FFD700;font-family:\'Barlow Condensed\',sans-serif;font-size:11px;font-weight:700;">COACH</div>',
    'id="tn-slot-coach" style="position:absolute;top:2%;right:2%;width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #FFD700;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#FFD700;font-family:\'Barlow Condensed\',sans-serif;font-size:11px;font-weight:700;">COACH</div>'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
