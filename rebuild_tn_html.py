import re
content = open("index.html","r",encoding="utf-8").read()
new_page = '''<div id="page-tunisia" style="display:none;width:100%;min-height:100vh;background:#111;flex-direction:column;">
  <!-- TOP BAR -->
  <div style="display:flex;align-items:center;gap:16px;padding:16px 24px;border-bottom:1px solid #1a1a1a;background:#0d0d0d;">
    <button onclick="showPage(\'home\')" style="background:rgba(255,255,255,0.05);border:1px solid #333;color:#fff;border-radius:8px;padding:8px 16px;font-family:Barlow Condensed,sans-serif;font-size:14px;font-weight:700;cursor:pointer;">← HOME</button>
    <img src="https://city-png.b-cdn.net/thumbnail/thumbnail_public/uploads/preview/hd-logo-of-tunisia-national-football-team-transparent-png-701751712400875ip5tcz8e38.png" style="height:40px;mix-blend-mode:screen;">
    <div>
      <div id="tn-step-num" style="color:#E70013;font-size:11px;font-weight:700;letter-spacing:3px;"></div>
      <div id="tn-step-title" style="font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:32px;font-weight:900;letter-spacing:2px;line-height:1;"></div>
    </div>
  </div>
  <!-- MAIN: pitch + list -->
  <div id="tn-main" style="display:flex;flex:1;overflow:hidden;">
    <!-- LEFT: Pitch -->
    <div style="width:420px;flex-shrink:0;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;">
      <!-- Pitch lines SVG -->
      <svg style="position:absolute;inset:0;width:100%;height:100%;opacity:0.18;" viewBox="0 0 420 700" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
        <rect x="30" y="10" width="360" height="680" fill="none" stroke="white" stroke-width="2"/>
        <line x1="30" y1="350" x2="390" y2="350" stroke="white" stroke-width="2"/>
        <circle cx="210" cy="350" r="55" fill="none" stroke="white" stroke-width="2"/>
        <circle cx="210" cy="350" r="4" fill="white"/>
        <rect x="130" y="10" width="160" height="70" fill="none" stroke="white" stroke-width="2"/>
        <rect x="130" y="620" width="160" height="70" fill="none" stroke="white" stroke-width="2"/>
        <rect x="80" y="10" width="260" height="120" fill="none" stroke="white" stroke-width="2"/>
        <rect x="80" y="570" width="260" height="120" fill="none" stroke="white" stroke-width="2"/>
        <circle cx="210" cy="110" r="5" fill="white" opacity="0.5"/>
        <circle cx="210" cy="590" r="5" fill="white" opacity="0.5"/>
      </svg>
      <!-- Position dots -->
      <div style="position:relative;width:100%;height:100%;z-index:2;">''' + "".join([
        '<div id="tn-dot-'+s['key']+'" style="position:absolute;left:'+str(s['x'])+'%;top:'+str(s['y'])+'%;transform:translate(-50%,-50%);width:62px;height:62px;border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:center;border:2px dashed rgba(255,255,255,0.2);background:rgba(0,0,0,0.4);cursor:default;transition:all 0.3s;"><div style=\'font-family:Barlow Condensed,sans-serif;font-size:9px;font-weight:700;letter-spacing:1px;color:rgba(255,255,255,0.4);\'>' + s['pos'] + '</div><div class="dot-label" style="font-family:Barlow Condensed,sans-serif;font-size:9px;color:rgba(255,255,255,0.4);margin-top:2px;text-align:center;max-width:58px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;"></div></div>'
        for s in [
          {"key":"gk",  "pos":"GK",   "x":42,"y":8},
          {"key":"rb",  "pos":"RB",   "x":78,"y":26},
          {"key":"cb1", "pos":"CB",   "x":58,"y":26},
          {"key":"cb2", "pos":"CB",   "x":27,"y":26},
          {"key":"lb",  "pos":"LB",   "x":8, "y":26},
          {"key":"cdm", "pos":"CDM",  "x":42,"y":46},
          {"key":"cm1", "pos":"CM",   "x":20,"y":58},
          {"key":"cm2", "pos":"CM",   "x":64,"y":58},
          {"key":"rw",  "pos":"RW",   "x":78,"y":74},
          {"key":"lw",  "pos":"LW",   "x":8, "y":74},
          {"key":"st",  "pos":"ST",   "x":42,"y":80},
          {"key":"coach","pos":"COACH","x":42,"y":93}
        ]
      ]) + '''
      </div>
    </div>
    <!-- RIGHT: Player selection -->
    <div style="flex:1;overflow-y:auto;padding:24px 32px;background:#111;">
      <div id="tn-player-list"></div>
      <button onclick="if(tnStep>0){tnStep--;renderTNStep();}" style="margin-top:12px;width:100%;padding:14px;background:transparent;color:#555;border:1px solid #222;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:14px;font-weight:700;cursor:pointer;letter-spacing:2px;">RETOUR</button>
    </div>
  </div>
  <!-- RESULT -->
  <div id="tn-result" style="display:none;flex-direction:column;padding:32px;background:#111;min-height:100vh;">
    <div style="display:flex;align-items:center;gap:16px;margin-bottom:24px;">
      <img src="https://city-png.b-cdn.net/thumbnail/thumbnail_public/uploads/preview/hd-logo-of-tunisia-national-football-team-transparent-png-701751712400875ip5tcz8e38.png" style="height:50px;mix-blend-mode:screen;">
      <div style="font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:40px;font-weight:900;letter-spacing:3px;">TON BEST XI TUNISIE</div>
    </div>
    <div id="tn-res-list" style="max-width:600px;"></div>
    <div style="display:flex;gap:12px;margin-top:20px;max-width:600px;">
      <button onclick="startTunisiaXI()" style="flex:1;padding:14px;background:#E70013;color:#fff;border:none;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:900;cursor:pointer;letter-spacing:2px;">RECOMMENCER</button>
      <button onclick="showPage(\'home\')" style="flex:1;padding:14px;background:transparent;color:#E70013;border:2px solid #E70013;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:900;cursor:pointer;letter-spacing:2px;">HOME</button>
    </div>
  </div>
</div>'''
content = re.sub(r'<div id="page-tunisia".*?(?=<div id="page-|<script src="tunisia)', new_page+"\n", content, flags=re.DOTALL)
open("index.html","w",encoding="utf-8").write(content)
print("done")
