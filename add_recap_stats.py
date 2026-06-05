content = open('index.html','r',encoding='utf-8').read()
# Supprimer le compteur qu'on vient d'ajouter
old = """  var total = tnSteps.length;
  var done = Object.keys(tnPicks).length;
  var pct = Math.round((done/total)*100);
  var html = "<div style='color:#E70013;font-size:11px;font-weight:700;letter-spacing:4px;'>"+s.label+"</div>";
  html += "<div style='color:#FFD700;font-family:Barlow Condensed,sans-serif;font-size:13px;font-weight:600;margin-bottom:4px;'>"+done+" / "+total+" selections</div>";
  html += "<div style='width:100%;height:6px;background:#333;border-radius:4px;margin-bottom:12px;'>";
  html += "<div style='width:"+pct+"%;height:6px;background:linear-gradient(90deg,#E70013,#FF4444);border-radius:4px;transition:width 0.4s ease;'></div></div>";"""
new = "  var html = \"<div style='color:#E70013;font-size:11px;font-weight:700;letter-spacing:4px;'>\"+s.label+\"</div>\";"
content = content.replace(old, new)
# Ajouter stats dans le recap final
old_recap_title = "html += \"<div style='font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:36px;font-weight:900;line-height:1;margin-bottom:8px;'>RECAPITULATIF</div>\";"
new_recap_title = """html += "<div style='font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:36px;font-weight:900;line-height:1;margin-bottom:4px;'>RECAPITULATIF</div>";
  var total = tnSteps.length;
  var done = Object.keys(tnPicks).length;
  html += "<div style='color:#aaa;font-size:13px;margin-bottom:8px;'>"+done+" / "+total+" joueurs selectiones</div>";
  html += "<div style='width:100%;height:6px;background:#333;border-radius:4px;margin-bottom:14px;'><div style='width:100%;height:6px;background:linear-gradient(90deg,#E70013,#FFD700);border-radius:4px;'></div></div>";"""
content = content.replace(old_recap_title, new_recap_title)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
