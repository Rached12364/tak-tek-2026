content = open('index.html','r',encoding='utf-8').read()
old_steps = '''var tnSteps = [
  { pos:"gk", slot:"tn-slot-gk", label:"1 / 11 — GOALKEEPER", title:"GARDIEN DE BUT", players:[
    {name:"AYMEN DAHMEN", club:"CS Sfaxien", age:"29 ans", img:"https://static.flashscore.com/res/image/data/QmUS6OCa-lSbL00eG.png"},
    {name:"ABDELMOUHIB CHAMAKH", club:"Club Africain", age:"24 ans", img:"https://static.flashscore.com/res/image/data/K0bbVQDa-WnKvWss7.png"},
    {name:"BECHIR BEN SAID", club:"Esperance Tunis", age:"31 ans", img:"https://static.flashscore.com/res/image/data/4C42SQFG-Eg24ohRo.png"}
  ]},
  { pos:"lb", slot:"tn-slot-lb", label:"2 / 11 — LEFT BACK", title:"DEFENSEUR GAUCHE", players:[
    {name:"GHAITH ZAALOUNI", club:"Club Africain", age:"24 ans", img:"https://static.flashscore.com/res/image/data/n5ogLP9r-0AzSJQvl.png"},
    {name:"MOHAMED BEN HAMIDA", club:"Esperance Tunis", age:"30 ans", img:"https://static.flashscore.com/res/image/data/vcy34QHG-Cp6u72PF.png"},
    {name:"ALI MAALOUL", club:"CS Sfaxien", age:"36 ans", img:"https://static.flashscore.com/res/image/data/6V19PoCr-C8EFM7WN.png"}
  ]}
];'''
new_steps = '''var tnSteps = [
  { pos:"gk", slot:"tn-slot-gk", label:"1 / 11 — GOALKEEPER", title:"GARDIEN DE BUT", players:[
    {name:"AYMEN DAHMEN", club:"CS Sfaxien", age:"29 ans", mv:"715k", img:"https://static.flashscore.com/res/image/data/QmUS6OCa-lSbL00eG.png"},
    {name:"ABDELMOUHIB CHAMAKH", club:"Club Africain", age:"24 ans", mv:"851k", img:"https://static.flashscore.com/res/image/data/K0bbVQDa-WnKvWss7.png"},
    {name:"BECHIR BEN SAID", club:"Esperance Tunis", age:"31 ans", mv:"562k", img:"https://static.flashscore.com/res/image/data/4C42SQFG-Eg24ohRo.png"}
  ]},
  { pos:"cb1", slot:"tn-slot-cb1", label:"2 / 11 — CENTER BACK", title:"DEFENSEUR CENTRAL", players:[
    {name:"HAMZA BEN ABDA", club:"Club Africain", age:"31 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/Wf8JhtwS-WWu2CRtL.png"},
    {name:"HAMZA JELASSI", club:"Esperance Tunis", age:"34 ans", mv:"343k", img:"https://static.flashscore.com/res/image/data/GflDaQWg-tK0qtuln.png"},
    {name:"HICHEM BACCAR", club:"CS Sfaxien", age:"25 ans", mv:"691k", img:"https://static.flashscore.com/res/image/data/29HfkjDa-WIOovKDQ.png"}
  ]},
  { pos:"cb2", slot:"tn-slot-cb2", label:"3 / 11 — CENTER BACK", title:"DEFENSEUR CENTRAL", players:[
    {name:"TAOUFIK CHERIFI", club:"Club Africain", age:"24 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/0r8UG8Ca-vs1m1pCj.png"},
    {name:"MOHAMED TOUGAI", club:"Esperance Tunis", age:"26 ans", mv:"1.3m", img:"https://static.flashscore.com/res/image/data/S4vlg0FG-r9jkPGua.png"},
    {name:"HAMZA BEN ABDA", club:"Club Africain", age:"31 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/Wf8JhtwS-WWu2CRtL.png"}
  ]},
  { pos:"lb", slot:"tn-slot-lb", label:"4 / 11 — LEFT BACK", title:"DEFENSEUR GAUCHE", players:[
    {name:"OUSSAMA SHILI", club:"Club Africain", age:"29 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/2gV8z9Ca-4WYdb6yU.png"},
    {name:"MOHAMED BEN ALI", club:"Esperance Tunis", age:"31 ans", mv:"482k", img:"https://static.flashscore.com/res/image/data/fDo2nOil-C4II6KaD.png"},
    {name:"KEVIN MONDEKO ZATU", club:"CS Sfaxien", age:"30 ans", mv:"511k", img:"https://static.flashscore.com/res/image/data/84J5FQzB-xfQTxQp6.png"}
  ]},
  { pos:"rb", slot:"tn-slot-rb", label:"5 / 11 — RIGHT BACK", title:"DEFENSEUR DROIT", players:[
    {name:"GHAITH ZAALOUNI", club:"Club Africain", age:"24 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/n5ogLP9r-0AzSJQvl.png"},
    {name:"MOHAMED BEN HAMIDA", club:"Esperance Tunis", age:"30 ans", mv:"950k", img:"https://static.flashscore.com/res/image/data/vcy34QHG-Cp6u72PF.png"},
    {name:"ALI MAALOUL", club:"CS Sfaxien", age:"36 ans", mv:"181k", img:"https://static.flashscore.com/res/image/data/6V19PoCr-C8EFM7WN.png"}
  ]},
  { pos:"cdm", slot:"tn-slot-cdm", label:"6 / 11 — CDM", title:"MILIEU DEFENSIF", players:[
    {name:"ONUCHE OGBELU", club:"Esperance Tunis", age:"23 ans", mv:"1.1m", img:"https://static.flashscore.com/res/image/data/WIjGOmzB-022o47ar.png"},
    {name:"SAIDOU KHAN", club:"Club Africain", age:"30 ans", mv:"238k", img:"https://static.flashscore.com/res/image/data/jLQgpff5-dC60tYQc.png"},
    {name:"TRAVIS MUTYABA", club:"CS Sfaxien", age:"20 ans", mv:"421k", img:"https://static.flashscore.com/res/image/data/AFdAvYh5-IZYDgL5g.png"}
  ]},
  { pos:"cm1", slot:"tn-slot-cm1", label:"7 / 11 — CM", title:"MILIEU CENTRAL", players:[
    {name:"ABDRAMANE KONATE", club:"Esperance Tunis", age:"19 ans", mv:"784k", img:"https://static.flashscore.com/res/image/data/nu2f0DyB-IuruetYK.png"},
    {name:"MOATAZ ZEMZEMI", club:"Club Africain", age:"26 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/hxiFbAWg-dlKkqbYG.png"},
    {name:"RAYANE ANANE", club:"Etoile Sahel", age:"19 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/dMmqPWfM-0UW9EpZA.png"}
  ]},
  { pos:"cm2", slot:"tn-slot-cm2", label:"8 / 11 — CM", title:"MILIEU CENTRAL", players:[
    {name:"HAMZA RAFIA", club:"Esperance Tunis", age:"27 ans", mv:"993k", img:"https://static.flashscore.com/res/image/data/vqAEVLjl-O2Ow4Qc6.png"},
    {name:"HOUSSEM TKA", club:"Esperance Tunis", age:"25 ans", mv:"950k", img:"https://static.flashscore.com/res/image/data/SnPIIKeM-MFqZE5YG.png"},
    {name:"OUSSAMA SHILI", club:"Club Africain", age:"29 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/2gV8z9Ca-4WYdb6yU.png"}
  ]},
  { pos:"rw", slot:"tn-slot-rw", label:"9 / 11 — RIGHT WING", title:"AILIER DROIT", players:[
    {name:"BILEL AIT MALEK", club:"Club Africain", age:"29 ans", mv:"830k", img:"https://static.flashscore.com/res/image/data/ji33gowS-IXXhJSnH.png"},
    {name:"EMMANUEL OGBOLE", club:"CS Sfaxien", age:"23 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/G8s2koFa-KETzKlnh.png"},
    {name:"YAN SASSE", club:"Esperance Tunis", age:"28 ans", mv:"1.3m", img:"https://static.flashscore.com/res/image/data/dt2cgPYg-n3Qx4ylf.png"}
  ]},
  { pos:"st", slot:"tn-slot-st", label:"10 / 11 — STRIKER", title:"ATTAQUANT", players:[
    {name:"FLORIAN DANHO", club:"Esperance Tunis", age:"25 ans", mv:"635k", img:"https://static.flashscore.com/res/image/data/65n9DRyS-IDmUYnZ3.png"},
    {name:"FIRAS CHAOUAT", club:"Club Africain", age:"30 ans", mv:"1.1m", img:"https://static.flashscore.com/res/image/data/EL8CsfBr-2X9WEIyE.png"},
    {name:"OMAR BEN ALI", club:"CS Sfaxien", age:"21 ans", mv:"787k", img:"https://static.flashscore.com/res/image/data/ziFqV5hl-lABaXzzC.png"}
  ]},
  { pos:"lw", slot:"tn-slot-lw", label:"11 / 11 — LEFT WING", title:"AILIER GAUCHE", players:[
    {name:"KOUCEILA BOUALIA", club:"Esperance Tunis", age:"25 ans", mv:"749k", img:"https://static.flashscore.com/res/image/data/KUNSE9dM-hr83Inic.png"},
    {name:"HAMZA KHADHRAOUI", club:"Club Africain", age:"27 ans", mv:"957k", img:"https://static.flashscore.com/res/image/data/vTetqTAr-YVrigF7l.png"},
    {name:"IYED BELWAFI", club:"CS Sfaxien", age:"23 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/4C42SQFG-Eg24ohRo.png"}
  ]}
];'''
content = content.replace(old_steps, new_steps)
# Mettre a jour tnRender pour afficher market value
old_render_line = '    html += "<div style=\'color:#888;font-size:12px;\'>Tunisie · "+p.age+"</div></div></div>";'
new_render_line = '    html += "<div style=\'color:#888;font-size:12px;\'>"+p.age+" · <span style=\'color:#FFD700;\'>"+p.mv+"</span></div></div></div>";'
content = content.replace(old_render_line, new_render_line)
open('index.html','w',encoding='utf-8').write(content)
print("OK - tous les postes ajoutes")
