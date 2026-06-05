content = open('index.html','r',encoding='utf-8').read()
tunisia_page = '''
<div id="page-tunisia" style="display:none;width:100%;height:100vh;background:#0a0a0a;flex-direction:row;overflow:hidden;">
  <!-- TERRAIN GAUCHE -->
  <div style="flex:1;position:relative;background:linear-gradient(180deg,#0a2a0a,#0d3d0d,#0a2a0a);display:flex;align-items:center;justify-content:center;overflow:hidden;">
    <!-- Lignes terrain -->
    <div style="position:absolute;width:75%;height:88%;border:2px solid rgba(255,255,255,0.25);border-radius:4px;"></div>
    <div style="position:absolute;width:75%;height:1px;background:rgba(255,255,255,0.2);top:50%;"></div>
    <div style="position:absolute;width:120px;height:120px;border-radius:50%;border:2px solid rgba(255,255,255,0.2);top:50%;left:50%;transform:translate(-50%,-50%);"></div>
    <div style="position:absolute;width:28%;height:18%;border:2px solid rgba(255,255,255,0.2);top:6%;left:50%;transform:translateX(-50%);"></div>
    <div style="position:absolute;width:28%;height:18%;border:2px solid rgba(255,255,255,0.2);bottom:6%;left:50%;transform:translateX(-50%);"></div>
    <!-- Slots joueurs 4-3-3 -->
    <!-- GK -->
    <div id="tn-slot-gk" style="position:absolute;top:8%;left:50%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #E70013;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#E70013;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;letter-spacing:1px;">GK</div>
    <!-- DEF -->
    <div id="tn-slot-rb" style="position:absolute;top:26%;left:72%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #555;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#888;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">RB</div>
    <div id="tn-slot-cb1" style="position:absolute;top:26%;left:57%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #555;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#888;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">CB</div>
    <div id="tn-slot-cb2" style="position:absolute;top:26%;left:42%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #555;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#888;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">CB</div>
    <div id="tn-slot-lb" style="position:absolute;top:26%;left:27%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #555;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#888;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">LB</div>
    <!-- MID -->
    <div id="tn-slot-cm1" style="position:absolute;top:46%;left:64%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #555;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#888;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">CM</div>
    <div id="tn-slot-cdm" style="position:absolute;top:46%;left:50%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #555;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#888;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">CDM</div>
    <div id="tn-slot-cm2" style="position:absolute;top:46%;left:36%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #555;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#888;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">CM</div>
    <!-- ATT -->
    <div id="tn-slot-rw" style="position:absolute;top:66%;left:68%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #555;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#888;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">RW</div>
    <div id="tn-slot-st" style="position:absolute;top:66%;left:50%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #555;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#888;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">ST</div>
    <div id="tn-slot-lw" style="position:absolute;top:66%;left:32%;transform:translateX(-50%);width:70px;height:90px;background:rgba(0,0,0,0.5);border:2px dashed #555;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#888;font-family:'Barlow Condensed',sans-serif;font-size:11px;font-weight:700;">LW</div>
  </div>
  <!-- PANNEAU DROITE -->
  <div style="width:420px;background:#111;display:flex;flex-direction:column;padding:24px;gap:16px;overflow-y:auto;">
    <div style="color:#E70013;font-size:11px;font-weight:700;letter-spacing:4px;">1 / 11 — GOALKEEPER</div>
    <div style="font-family:'Barlow Condensed',sans-serif;color:#FFD700;font-size:48px;font-weight:900;letter-spacing:2px;line-height:1;">GARDIEN DE BUT</div>
    <!-- Carte GK 1 - Dahmen -->
    <div onclick="tnPick('gk','Dahmen','https://static.flashscore.com/res/image/data/QmUS6OCa-lSbL00eG.png','CS Sfaxien','tn-slot-gk')" style="display:flex;align-items:center;gap:16px;background:#1a1a1a;border:2px solid #E70013;border-radius:12px;padding:12px;cursor:pointer;transition:all 0.2s;" onmouseover="this.style.background='#2a1a1a'" onmouseout="this.style.background='#1a1a1a'">
      <img src="https://static.flashscore.com/res/image/data/QmUS6OCa-lSbL00eG.png" style="width:80px;height:100px;object-fit:cover;border-radius:8px;">
      <div>
        <div style="font-family:'Barlow Condensed',sans-serif;color:#fff;font-size:22px;font-weight:900;letter-spacing:1px;">AYMEN DAHMEN</div>
        <div style="color:#E70013;font-size:13px;font-weight:600;">CS Sfaxien</div>
        <div style="color:#888;font-size:12px;">🇹🇳 Tunisie · 29 ans</div>
      </div>
    </div>
    <!-- Carte GK 2 - Chamakh -->
    <div onclick="tnPick('gk','Chamakh','https://static.flashscore.com/res/image/data/K0bbVQDa-WnKvWss7.png','Club Africain','tn-slot-gk')" style="display:flex;align-items:center;gap:16px;background:#1a1a1a;border:2px solid #333;border-radius:12px;padding:12px;cursor:pointer;transition:all 0.2s;" onmouseover="this.style.background='#2a1a1a'" onmouseout="this.style.background='#1a1a1a'">
      <img src="https://static.flashscore.com/res/image/data/K0bbVQDa-WnKvWss7.png" style="width:80px;height:100px;object-fit:cover;border-radius:8px;">
      <div>
        <div style="font-family:'Barlow Condensed',sans-serif;color:#fff;font-size:22px;font-weight:900;letter-spacing:1px;">ABDELMOUHIB CHAMAKH</div>
        <div style="color:#E70013;font-size:13px;font-weight:600;">Club Africain</div>
        <div style="color:#888;font-size:12px;">🇹🇳 Tunisie · 24 ans</div>
      </div>
    </div>
    <!-- Carte GK 3 - Ben Said -->
    <div onclick="tnPick('gk','BenSaid','https://static.flashscore.com/res/image/data/4C42SQFG-Eg24ohRo.png','Esperance Tunis','tn-slot-gk')" style="display:flex;align-items:center;gap:16px;background:#1a1a1a;border:2px solid #333;border-radius:12px;padding:12px;cursor:pointer;transition:all 0.2s;" onmouseover="this.style.background='#2a1a1a'" onmouseout="this.style.background='#1a1a1a'">
      <img src="https://static.flashscore.com/res/image/data/4C42SQFG-Eg24ohRo.png" style="width:80px;height:100px;object-fit:cover;border-radius:8px;">
      <div>
        <div style="font-family:'Barlow Condensed',sans-serif;color:#fff;font-size:22px;font-weight:900;letter-spacing:1px;">BECHIR BEN SAID</div>
        <div style="color:#E70013;font-size:13px;font-weight:600;">Esperance Tunis</div>
        <div style="color:#888;font-size:12px;">🇹🇳 Tunisie · 31 ans</div>
      </div>
    </div>
    <button onclick="showPage('home')" style="margin-top:auto;padding:14px;background:transparent;border:1px solid #444;color:#aaa;border-radius:8px;font-family:'Barlow Condensed',sans-serif;font-size:16px;font-weight:700;cursor:pointer;letter-spacing:2px;">← RETOUR</button>
  </div>
</div>
<script>
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
</script>
'''
# Inserer avant </body>
content = content.replace('</body>', tunisia_page + '</body>')
open('index.html','w',encoding='utf-8').write(content)
print("OK - page Tunisia GK creee")
