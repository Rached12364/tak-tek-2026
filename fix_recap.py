content = open('index.html','r',encoding='utf-8').read()
# Trouver et remplacer toute la fonction tnShowRecap
start = content.find('function tnShowRecap()')
end = content.find('\nfunction tnBack()')
old_recap = content[start:end]
new_recap = '''function tnShowRecap() {
  var html = "<div style='color:#E70013;font-size:11px;font-weight:700;letter-spacing:4px;'>VOTRE EQUIPE TUNISIA XI</div>";
  html += "<div style='font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:36px;font-weight:900;line-height:1;margin-bottom:8px;'>RECAPITULATIF</div>";
  var labels = {gk:'GK',cb1:'CB',cb2:'CB',rb:'RB',lb:'LB',cdm:'CDM',cm1:'CM',cm2:'CM',rw:'RW',st:'ST',lw:'LW',coach:'COACH'};
  for(var pos in tnPicks) {
    var p = tnPicks[pos];
    html += "<div style='display:flex;align-items:center;gap:12px;background:#1a1a1a;border:1px solid #333;border-radius:10px;padding:8px;'>";
    html += "<div style='background:#E70013;color:#fff;font-size:10px;font-weight:800;padding:3px 8px;border-radius:4px;min-width:40px;text-align:center;'>"+(labels[pos]||pos)+"</div>";
    html += "<img src='"+p.img+"' style='width:44px;height:55px;object-fit:cover;border-radius:6px;'>";
    html += "<div style='font-family:Barlow Condensed,sans-serif;color:#fff;font-size:15px;font-weight:700;'>"+p.name+"<br><span style='color:#E70013;font-size:12px;font-weight:400;'>"+p.club+"</span></div>";
    html += "</div>";
  }
  html += "<button onclick='startTunisiaXI()' style='margin-top:8px;padding:14px;background:#E70013;border:none;color:#fff;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:700;cursor:pointer;letter-spacing:2px;'>&#8635; RECOMMENCER</button>";
  html += "<button onclick='showPage(String.fromCharCode(104,111,109,101))' style='padding:14px;background:transparent;border:1px solid #444;color:#aaa;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:700;cursor:pointer;letter-spacing:2px;'>&#8592; ACCUEIL</button>";
  document.getElementById("tn-panel").innerHTML = html;
}
'''
content = content[:start] + new_recap + content[end:]
open('index.html','w',encoding='utf-8').write(content)
print('OK')
