content = open('index.html','r',encoding='utf-8').read()
# Remplacer le panneau droit statique + ancien script
old_panel = '''  <!-- PANNEAU DROITE -->
  <div style="width:420px;background:#111;display:flex;flex-direction:column;padding:24px;gap:16px;overflow-y:auto;">
    <div style="color:#E70013;font-size:11px;font-weight:700;letter-spacing:4px;">1 / 11 — GOALKEEPER</div>
    <div style="font-family:\'Barlow Condensed\',sans-serif;color:#FFD700;font-size:48px;font-weight:900;letter-spacing:2px;line-height:1;">GARDIEN DE BUT</div>'''
new_panel = '''  <!-- PANNEAU DROITE DYNAMIQUE -->
  <div id="tn-panel" style="width:420px;background:#111;display:flex;flex-direction:column;padding:24px;gap:14px;overflow-y:auto;">'''
content = content.replace(old_panel, new_panel)
# Supprimer les 3 cartes statiques GK + bouton retour statique jusqu'au </div> fermant le panneau
# On cherche depuis la carte Dahmen jusqu'au bouton retour inclus
old_cards_start = '''    <!-- Carte GK 1 - Dahmen -->'''
old_cards_end = '''    <button onclick="showPage(\'home\')" style="margin-top:auto;padding:14px;background:transparent;border:1px solid #444;color:#aaa;border-radius:8px;font-family:\'Barlow Condensed\',sans-serif;font-size:16px;font-weight:700;cursor:pointer;letter-spacing:2px;">← RETOUR</button>
  </div>
</div>'''
idx_start = content.find(old_cards_start)
idx_end = content.find(old_cards_end) + len(old_cards_end)
content = content[:idx_start] + '''  </div>
</div>''' + content[idx_end:]
# Remplacer l'ancien script
old_script = '''<script>
var tnPicks = {};
function tnPick(pos, name, img, club, slotId) {
  tnPicks[pos] = {name:name, img:img, club:club};
  var slot = document.getElementById(slotId);
  if(slot) {
    slot.style.border = "2px solid #E70013";
    slot.innerHTML = "<img src=\'"+img+"\' style=\'width:66px;height:88px;object-fit:cover;border-radius:8px;\'>";
  }
}
function startTunisiaXI() {}
</script>'''
new_script = '''<script>
var tnStep = 0;
var tnPicks = {};
var tnSteps = [
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
];
function startTunisiaXI() { tnStep=0; tnPicks={}; tnRender(); }
function tnRender() {
  var s = tnSteps[tnStep];
  var html = "<div style='color:#E70013;font-size:11px;font-weight:700;letter-spacing:4px;'>"+s.label+"</div>";
  html += "<div style='font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:42px;font-weight:900;letter-spacing:2px;line-height:1;'>"+s.title+"</div>";
  s.players.forEach(function(p,i){
    var border = (i===0)?"#E70013":"#333";
    html += "<div onclick='tnPick("+tnStep+","+i+")' id='tn-card-"+i+"' style='display:flex;align-items:center;gap:16px;background:#1a1a1a;border:2px solid "+border+";border-radius:12px;padding:12px;cursor:pointer;transition:all 0.2s;'>";
    html += "<img src='"+p.img+"' style='width:80px;height:100px;object-fit:cover;border-radius:8px;'>";
    html += "<div><div style='font-family:Barlow Condensed,sans-serif;color:#fff;font-size:20px;font-weight:900;'>"+p.name+"</div>";
    html += "<div style='color:#E70013;font-size:13px;font-weight:600;'>"+p.club+"</div>";
    html += "<div style='color:#888;font-size:12px;'>Tunisie · "+p.age+"</div></div></div>";
  });
  html += "<button onclick='showPage(\"home\")' style='margin-top:auto;padding:14px;background:transparent;border:1px solid #444;color:#aaa;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:700;cursor:pointer;letter-spacing:2px;'>← RETOUR</button>";
  document.getElementById("tn-panel").innerHTML = html;
}
function tnPick(stepIdx, playerIdx) {
  var s = tnSteps[stepIdx];
  var p = s.players[playerIdx];
  tnPicks[s.pos] = p;
  var slot = document.getElementById(s.slot);
  if(slot) {
    slot.style.border = "2px solid #E70013";
    slot.innerHTML = "<img src='"+p.img+"' style='width:66px;height:88px;object-fit:cover;border-radius:8px;'>";
  }
  if(tnStep < tnSteps.length - 1) {
    tnStep++;
    setTimeout(tnRender, 300);
  }
}
</script>'''
content = content.replace(old_script, new_script)
open('index.html','w',encoding='utf-8').write(content)
print("OK - systeme dynamique installe")
