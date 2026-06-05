content = open('index.html','r',encoding='utf-8').read()
old = "  var total = tnSteps.length;\n  var done = Object.keys(tnPicks).length;\n  html += \"<div style='color:#aaa;font-size:13px;margin-bottom:8px;'>\"+done+\" / \"+total+\" joueurs selectiones</div>\";\n  html += \"<div style='width:100%;height:6px;background:#333;border-radius:4px;margin-bottom:14px;'><div style='width:100%;height:6px;background:linear-gradient(90deg,#E70013,#FFD700);border-radius:4px;'></div></div>\";"
new = """  var total = tnSteps.length;
  var done = Object.keys(tnPicks).length;
  html += "<div style='color:#aaa;font-size:13px;margin-bottom:6px;'>"+done+" / "+total+" joueurs selectiones</div>";
  html += "<div style='width:100%;height:6px;background:#333;border-radius:4px;margin-bottom:14px;'><div style='width:100%;height:6px;background:linear-gradient(90deg,#E70013,#FFD700);border-radius:4px;'></div></div>";
  // Calculer stats
  var totalMV = 0; var countMV = 0;
  var totalAge = 0; var countAge = 0;
  var clubs = {};
  for(var p in tnPicks) {
    var pl = tnPicks[p];
    if(pl.mv && pl.mv !== 'N/A' && pl.mv !== '-' && pl.mv !== 'n/a') {
      var mv = pl.mv.toString().replace('k','000').replace('m','000000').replace('.','');
      if(!isNaN(mv)) { totalMV += parseInt(mv); countMV++; }
    }
    if(pl.age) {
      var a = parseInt(pl.age);
      if(!isNaN(a)) { totalAge += a; countAge++; }
    }
    if(pl.club) { clubs[pl.club] = (clubs[pl.club]||0)+1; }
  }
  var mvStr = totalMV >= 1000000 ? (totalMV/1000000).toFixed(1)+'M' : (totalMV/1000).toFixed(0)+'K';
  var avgAge = countAge > 0 ? (totalAge/countAge).toFixed(1) : '-';
  html += "<div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px;'>";
  html += "<div style='background:#1a1a1a;border:1px solid #333;border-radius:10px;padding:10px;text-align:center;'>";
  html += "<div style='color:#E70013;font-size:10px;font-weight:700;letter-spacing:2px;'>VALEUR TOTALE</div>";
  html += "<div style='color:#FFD700;font-family:Barlow Condensed,sans-serif;font-size:22px;font-weight:900;'>€"+mvStr+"</div></div>";
  html += "<div style='background:#1a1a1a;border:1px solid #333;border-radius:10px;padding:10px;text-align:center;'>";
  html += "<div style='color:#E70013;font-size:10px;font-weight:700;letter-spacing:2px;'>AGE MOYEN</div>";
  html += "<div style='color:#FFD700;font-family:Barlow Condensed,sans-serif;font-size:22px;font-weight:900;'>"+avgAge+" ans</div></div>";
  html += "</div>";
  html += "<div style='background:#1a1a1a;border:1px solid #333;border-radius:10px;padding:10px;margin-bottom:12px;'>";
  html += "<div style='color:#E70013;font-size:10px;font-weight:700;letter-spacing:2px;margin-bottom:8px;'>JOUEURS PAR CLUB</div>";
  for(var club in clubs) {
    var pct2 = Math.round((clubs[club]/done)*100);
    html += "<div style='margin-bottom:6px;'>";
    html += "<div style='display:flex;justify-content:space-between;color:#fff;font-size:12px;margin-bottom:3px;'><span>"+club+"</span><span style='color:#FFD700;font-weight:700;'>"+clubs[club]+" joueurs</span></div>";
    html += "<div style='width:100%;height:4px;background:#333;border-radius:4px;'><div style='width:"+pct2+"%;height:4px;background:#E70013;border-radius:4px;'></div></div>";
    html += "</div>";
  }
  html += "</div>";"""
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
