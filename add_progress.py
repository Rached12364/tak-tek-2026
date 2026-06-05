content = open('index.html','r',encoding='utf-8').read()
old_render = "  var html = \"<div style='color:#E70013;font-size:11px;font-weight:700;letter-spacing:4px;'>\"+s.label+\"</div>\";"
new_render = """  var total = tnSteps.length;
  var done = Object.keys(tnPicks).length;
  var pct = Math.round((done/total)*100);
  var html = "<div style='color:#E70013;font-size:11px;font-weight:700;letter-spacing:4px;'>"+s.label+"</div>";
  html += "<div style='color:#FFD700;font-family:Barlow Condensed,sans-serif;font-size:13px;font-weight:600;margin-bottom:4px;'>"+done+" / "+total+" selections</div>";
  html += "<div style='width:100%;height:6px;background:#333;border-radius:4px;margin-bottom:12px;'>";
  html += "<div style='width:"+pct+"%;height:6px;background:linear-gradient(90deg,#E70013,#FF4444);border-radius:4px;transition:width 0.4s ease;'></div></div>";"""
content = content.replace(old_render, new_render)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
