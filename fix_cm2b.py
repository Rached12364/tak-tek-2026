content = open('index.html','r',encoding='utf-8').read()
old = '''pos:"cm2", slot:"tn-slot-cm2", label:"8 / 11 — CM", title:"MILIEU CENTRAL", players:[
    {name:"HAMZA RAFIA", club:"Esperance Tunis", age:"27 ans", mv:"993k", img:"https://static.flashscore.com/res/image/data/vqAEVLjl-O2Ow4Qc6.png"},
    {name:"HOUSSEM TKA", club:"Esperance Tunis", age:"25 ans", mv:"950k", img:"https://static.flashscore.com/res/image/data/SnPIIKeM-MFqZE5YG.png"},
    {name:"OUSSAMA SHILI", club:"Club Africain", age:"29 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/2gV8z9Ca-4WYdb6yU.png"}'''
new = '''pos:"cm2", slot:"tn-slot-cm2", label:"8 / 11 — CM", title:"MILIEU CENTRAL", players:[
    {name:"HAMZA RAFIA", club:"Esperance Tunis", age:"27 ans", mv:"993k", img:"https://static.flashscore.com/res/image/data/vqAEVLjl-O2Ow4Qc6.png"},
    {name:"HOUSSEM TKA", club:"Esperance Tunis", age:"25 ans", mv:"950k", img:"https://static.flashscore.com/res/image/data/SnPIIKeM-MFqZE5YG.png"},
    {name:"AMATH NDAW", club:"Stade Tunisien", age:"24 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/2B6RYwXg-0bhGkmbt.png"}'''
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
