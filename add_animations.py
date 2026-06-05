content = open('index.html','r',encoding='utf-8').read()
animations = '''
@keyframes tn-fadein {
  from { opacity:0; transform:translateX(40px); }
  to   { opacity:1; transform:translateX(0); }
}
@keyframes tn-pulse-red {
  0%,100% { box-shadow: 0 0 0px #E70013; }
  50%      { box-shadow: 0 0 18px #E70013, 0 0 40px rgba(231,0,19,0.3); }
}
@keyframes tn-slot-glow {
  0%,100% { box-shadow: none; }
  50%      { box-shadow: 0 0 12px #E70013; }
}
.tn-card {
  animation: tn-fadein 0.4s ease both;
}
.tn-card:nth-child(3) { animation-delay: 0.05s; }
.tn-card:nth-child(4) { animation-delay: 0.12s; }
.tn-card:nth-child(5) { animation-delay: 0.20s; }
.tn-card-selected {
  animation: tn-pulse-red 1.8s ease infinite !important;
  border-color: #E70013 !important;
}
.tn-slot-active {
  animation: tn-slot-glow 1.5s ease infinite;
}
'''
if '@keyframes tn-fadein' not in content:
    content = content.replace('</style>', animations + '</style>')
# Mettre a jour tnRender pour ajouter class tn-card
old = "html += \"<div onclick='tnPick(\"+tnStep+\",\"+i+\")' id='tn-card-\"+i+\"' style='display:flex;align-items:center;gap:16px;background:#1a1a1a;border:2px solid \"+border+\";border-radius:12px;padding:12px;cursor:pointer;transition:all 0.2s;'>\";"
new = "var delay=(i*0.08).toFixed(2); html += \"<div onclick='tnPick(\"+tnStep+\",\"+i+\")' id='tn-card-\"+i+\"' class='tn-card' style='display:flex;align-items:center;gap:16px;background:#1a1a1a;border:2px solid \"+border+\";border-radius:12px;padding:12px;cursor:pointer;transition:all 0.2s;animation-delay:\"+delay+\"s;'>\";"
content = content.replace(old, new)
# Ajouter glow sur slot actif dans tnRender
old2 = "function tnRender() {\n  var s = tnSteps[tnStep];"
new2 = """function tnRender() {
  // Enlever glow precedent
  document.querySelectorAll('.tn-slot-active').forEach(function(el){el.classList.remove('tn-slot-active');});
  var s = tnSteps[tnStep];
  var slotEl = document.getElementById(s.slot);
  if(slotEl && !tnPicks[s.pos]) slotEl.classList.add('tn-slot-active');"""
content = content.replace(old2, new2)
# Ajouter classe selected sur carte choisie
old3 = "function tnPick(stepIdx, playerIdx) {"
new3 = """function tnPick(stepIdx, playerIdx) {
  // Highlight carte selectionnee
  for(var x=0;x<3;x++){var c=document.getElementById('tn-card-'+x);if(c)c.classList.remove('tn-card-selected');}
  var chosen=document.getElementById('tn-card-'+playerIdx);
  if(chosen){chosen.classList.add('tn-card-selected');}"""
content = content.replace(old3, new3)
open('index.html','w',encoding='utf-8').write(content)
print("OK - animations ajoutees")
