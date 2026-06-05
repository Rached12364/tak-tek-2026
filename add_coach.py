content = open('index.html','r',encoding='utf-8').read()
old_lw = '  { pos:"lw", slot:"tn-slot-lw", label:"11 / 11 — LEFT WING", title:"AILIER GAUCHE", players:['
new_lw = '  { pos:"lw", slot:"tn-slot-lw", label:"11 / 12 — LEFT WING", title:"AILIER GAUCHE", players:['
content = content.replace(old_lw, new_lw)
old_end = '''    {name:"IYED BELWAFI", club:"CS Sfaxien", age:"23 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/4C42SQFG-Eg24ohRo.png"}
  ]}
];'''
new_end = '''    {name:"IYED BELWAFI", club:"CS Sfaxien", age:"23 ans", mv:"N/A", img:"https://static.flashscore.com/res/image/data/4C42SQFG-Eg24ohRo.png"}
  ]},
  { pos:"coach", slot:"tn-slot-gk", label:"12 / 12 — COACH", title:"ENTRAINEUR", players:[
    {name:"FAOUZI BENZARTI", club:"Club Africain", age:"76 ans", mv:"—", img:"https://static.flashscore.com/res/image/data/OzYTtzdM-t8nTEIjj.png"},
    {name:"MOHAMED KOUKI", club:"CS Sfaxien", age:"51 ans", mv:"—", img:"https://tse3.explicit.bing.net/th/id/OIP.OWBL_xCpJFlQsxG0LLkSBwAAAA?pid=Api&P=0&h=180"},
    {name:"MONCEF MCHAREK", club:"Zarzis", age:"—", mv:"—", img:"https://tse2.mm.bing.net/th/id/OIP.pQRiQsrODgQCd8vfikUlWgHaER?pid=Api&P=0&h=180"}
  ]}
];'''
content = content.replace(old_end, new_end)
# Apres le dernier step (coach), afficher recap
old_pick = '''  if(tnStep < tnSteps.length - 1) {
    tnStep++;
    setTimeout(tnRender, 300);
  }'''
new_pick = '''  if(tnStep < tnSteps.length - 1) {
    tnStep++;
    setTimeout(tnRender, 300);
  } else {
    setTimeout(tnShowRecap, 400);
  }'''
content = content.replace(old_pick, new_pick)
# Ajouter fonction recap
old_back = 'function tnBack() {'
new_back = '''function tnShowRecap() {
  var html = "<div style='color:#E70013;font-size:11px;font-weight:700;letter-spacing:4px;'>VOTRE EQUIPE TUNISIA XI</div>";
  html += "<div style='font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:36px;font-weight:900;line-height:1;margin-bottom:8px;'>RECAPITULATIF</div>";
  var labels = {gk:"GK",cb1:"CB",cb2:"CB",rb:"RB",lb:"LB",cdm:"CDM",cm1:"CM",cm2:"CM",rw:"RW",st:"ST",lw:"LW",coach:"COACH"};
  for(var pos in tnPicks) {
    var p = tnPicks[pos];
    html += "<div style='display:flex;align-items:center;gap:12px;background:#1a1a1a;border:1px solid #333;border-radius:10px;padding:8px;'>";
    html += "<div style='background:#E70013;color:#fff;font-size:10px;font-weight:800;padding:3px 8px;border-radius:4px;min-width:40px;text-align:center;'>"+labels[pos]+"</div>";
    html += "<img src='"+p.img+"' style='width:44px;height:55px;object-fit:cover;border-radius:6px;'>";
    html += "<div style='font-family:Barlow Condensed,sans-serif;color:#fff;font-size:15px;font-weight:700;'>"+p.name+"<br><span style='color:#E70013;font-size:12px;font-weight:400;'>"+p.club+"</span></div>";
    html += "</div>";
  }
  html += "<button onclick='startTunisiaXI()' style='margin-top:8px;padding:14px;background:#E70013;border:none;color:#fff;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:700;cursor:pointer;letter-spacing:2px;'>&#8635; RECOMMENCER</button>";
  html += "<button onclick='showPage(\"home\")' style='padding:14px;background:transparent;border:1px solid #444;color:#aaa;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:700;cursor:pointer;letter-spacing:2px;'>&#8592; ACCUEIL</button>";
  document.getElementById("tn-panel").innerHTML = html;
}
function tnBack() {'''
content = content.replace(old_back, new_back)
open('index.html','w',encoding='utf-8').write(content)
print("OK - coach + recap ajoutes")
