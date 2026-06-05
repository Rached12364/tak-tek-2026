content = open('index.html','r',encoding='utf-8').read()
# 1. Corriger le slot du coach
content = content.replace(
    '{ pos:"coach", slot:"tn-slot-gk"',
    '{ pos:"coach", slot:"tn-slot-coach"'
)
# 2. Ajouter le slot coach sur le terrain (sous le GK)
old_slot = '<div id="tn-slot-gk"'
new_slot = '''<div id="tn-slot-coach" style="position:absolute;top:2%;left:50%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #FFD700;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#FFD700;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">COACH</div>
  <div id="tn-slot-gk"'''
content = content.replace(old_slot, new_slot)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
