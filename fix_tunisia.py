content = open('index.html', 'r', encoding='utf-8').read()
tunisia_steps = '''
var TUNISIA_STEPS = [
  {key:'gk', en:'GARDIEN DE BUT', pos:'GK'},
  {key:'rb', en:'LATERAL DROIT', pos:'RB'},
  {key:'cb1', en:'DEFENSEUR CENTRAL', pos:'CB'},
  {key:'cb2', en:'DEFENSEUR CENTRAL', pos:'CB'},
  {key:'lb', en:'LATERAL GAUCHE', pos:'LB'},
  {key:'cdm', en:'MILIEU DEFENSIF', pos:'CDM'},
  {key:'cm', en:'MILIEU CENTRAL', pos:'CM'},
  {key:'rw', en:'AILIER DROIT', pos:'RW'},
  {key:'lw', en:'AILIER GAUCHE', pos:'LW'},
  {key:'st', en:'ATTAQUANT', pos:'ST'},
  {key:'coach', en:'ENTRAINEUR', pos:'COACH'}
];
var TUNISIA_PLAYERS = {
  gk: [
    {name:'Abdelmouhib Chamakh', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/693140-1694797200.jpg'},
    {name:'Moez Ben Cherifia', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/177802-1660735551.jpg'},
    {name:'Farouk Ben Mustapha', club:'CS Sfaxien', img:'https://img.a.transfermarkt.technology/portrait/big/107145-1660736836.jpg'}
  ],
  rb: [
    {name:'Hamdi Nagguez', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/200971-1660737600.jpg'},
    {name:'Dylan Bronn', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/314964-1660737600.jpg'},
    {name:'Wajdi Kechrida', club:'Stade Tunisien', img:'https://img.a.transfermarkt.technology/portrait/big/354083-1660737600.jpg'}
  ],
  cb1: [
    {name:'Montassar Talbi', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/451978-1660737600.jpg'},
    {name:'Bilel Ifa', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/200974-1660737600.jpg'},
    {name:'Nader Ghandri', club:'CS Sfaxien', img:'https://img.a.transfermarkt.technology/portrait/big/200969-1660737600.jpg'}
  ],
  cb2: [
    {name:'Montassar Talbi', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/451978-1660737600.jpg'},
    {name:'Bilel Ifa', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/200974-1660737600.jpg'},
    {name:'Nader Ghandri', club:'CS Sfaxien', img:'https://img.a.transfermarkt.technology/portrait/big/200969-1660737600.jpg'}
  ],
  lb: [
    {name:'Ali Maaloul', club:'CS Sfaxien', img:'https://img.a.transfermarkt.technology/portrait/big/188445-1660737600.jpg'},
    {name:'Houcine Tka', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/354084-1660737600.jpg'},
    {name:'Yassine Meriah', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/354085-1660737600.jpg'}
  ],
  cdm: [
    {name:'Ghaylane Chaalali', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/354086-1660737600.jpg'},
    {name:'Anis Badri', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/354087-1660737600.jpg'},
    {name:'Firas Ben Larbi', club:'CS Sfaxien', img:'https://img.a.transfermarkt.technology/portrait/big/354088-1660737600.jpg'}
  ],
  cm: [
    {name:'Saifeddine Khaoui', club:'US Monastir', img:'https://img.a.transfermarkt.technology/portrait/big/354089-1660737600.jpg'},
    {name:'Zied Boughattas', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/354090-1660737600.jpg'},
    {name:'Khalil Chammam', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/354091-1660737600.jpg'}
  ],
  rw: [
    {name:'Omar Ben Ali', club:'CS Sfaxien', img:'https://img.a.transfermarkt.technology/portrait/big/354092-1660737600.jpg'},
    {name:'Phillippe Kinzumbi', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/354093-1660737600.jpg'},
    {name:'Ghaith Zaalouni', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/354094-1660737600.jpg'}
  ],
  lw: [
    {name:'Haythem Jouini', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/354095-1660737600.jpg'},
    {name:'Youssef Blaili', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/354096-1660737600.jpg'},
    {name:'Anice Badri', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/354097-1660737600.jpg'}
  ],
  st: [
    {name:'Firas Chaouat', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/354098-1660737600.jpg'},
    {name:'Omar Ben Ali', club:'CS Sfaxien', img:'https://img.a.transfermarkt.technology/portrait/big/354092-1660737600.jpg'},
    {name:'Issam Jebali', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/354099-1660737600.jpg'}
  ],
  coach: [
    {name:'Maher Kanzari', club:'Club Africain', img:'https://img.a.transfermarkt.technology/portrait/big/354100-1660737600.jpg'},
    {name:'Nabil Maaloul', club:'Esperance Tunis', img:'https://img.a.transfermarkt.technology/portrait/big/354101-1660737600.jpg'},
    {name:'Lassad Dridi', club:'CS Sfaxien', img:'https://img.a.transfermarkt.technology/portrait/big/354102-1660737600.jpg'}
  ]
};
var tStep = 0, tPicks = {};
function startTunisiaXI() {
  showPage("tunisia");
  tStep = 0; tPicks = {};
  renderTunisiaStep();
}
function renderTunisiaStep() {
  var s = TUNISIA_STEPS[tStep];
  document.getElementById("t-step-label").textContent = (tStep+1) + " / " + TUNISIA_STEPS.length + " — " + s.pos;
  document.getElementById("t-step-title").textContent = s.en;
  var list = document.getElementById("t-player-list");
  list.innerHTML = "";
  TUNISIA_PLAYERS[s.key].forEach(function(pl) {
    var card = document.createElement("div");
    card.style.cssText = "background:#111;border:2px solid #333;border-radius:12px;padding:16px;display:flex;align-items:center;gap:16px;cursor:pointer;transition:border-color 0.2s,background 0.2s;";
    card.onmouseover = function(){this.style.borderColor="#E70013";this.style.background="#1a0000";};
    card.onmouseout = function(){this.style.borderColor="#333";this.style.background="#111";};
    card.innerHTML = "<img src=\\""+pl.img+"\\" style=\\"width:70px;height:98px;object-fit:contain;border-radius:8px;\\" onerror=\\"this.src='https://via.placeholder.com/70x98/222/fff?text='+encodeURIComponent(pl.name.split(' ')[0])\\"><div><div style=\\"font-family:Barlow Condensed,sans-serif;font-size:20px;font-weight:900;color:#fff;\\">"+pl.name+"</div><div style=\\"color:#E70013;font-size:14px;font-weight:700;\\">"+pl.club+"</div></div>";
    card.onclick = function() { tPicks[s.key] = pl; tStep++; if(tStep >= TUNISIA_STEPS.length) { renderTunisiaResult(); } else { renderTunisiaStep(); } };
    list.appendChild(card);
  });
}
function renderTunisiaResult() {
  document.getElementById("t-selection").style.display = "none";
  document.getElementById("t-result").style.display = "flex";
  var list = document.getElementById("t-res-list");
  list.innerHTML = "";
  TUNISIA_STEPS.forEach(function(s) {
    var pl = tPicks[s.key]; if(!pl) return;
    var d = document.createElement("div");
    d.style.cssText = "display:flex;align-items:center;gap:16px;background:#111;border:1px solid #E70013;border-radius:10px;padding:12px;";
    d.innerHTML = "<img src=\\""+pl.img+"\\" style=\\"width:60px;height:84px;object-fit:contain;border-radius:6px;\\"><div><div style=\\"color:#E70013;font-size:12px;font-weight:700;letter-spacing:2px;\\">"+s.en+"</div><div style=\\"color:#fff;font-family:Barlow Condensed,sans-serif;font-size:18px;font-weight:900;\\">"+pl.name+"</div><div style=\\"color:#666;font-size:12px;\\">"+pl.club+"</div></div>";
    list.appendChild(d);
  });
}
'''
page_tunisia = '''<div id="page-tunisia" style="display:none;width:100%;min-height:100vh;background:#0a0a0a;flex-direction:row;">
  <div id="t-left" style="flex:1;display:flex;align-items:center;justify-content:center;padding:20px;background:url(https://img.freepik.com/photos-premium/ballon-football-terrain_250422-501.jpg) center/cover;position:relative;">
    <div style="position:absolute;inset:0;background:rgba(0,0,0,0.6);"></div>
    <div style="position:relative;z-index:1;text-align:center;">
      <img src="https://city-png.b-cdn.net/thumbnail/thumbnail_public/uploads/preview/hd-logo-of-tunisia-national-football-team-transparent-png-701751712400875ip5tcz8e38.png" style="width:150px;mix-blend-mode:screen;">
      <h2 style="font-family:Barlow Condensed,sans-serif;color:#E70013;font-size:32px;font-weight:900;letter-spacing:4px;margin-top:16px;">BEST XI TUNISIE</h2>
      <p style="color:#777;font-size:14px;letter-spacing:2px;">LIGUE 1 — 2025/2026</p>
    </div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;overflow-y:auto;padding:30px;gap:16px;">
    <div id="t-selection">
      <div id="t-step-label" style="color:#E70013;font-size:13px;font-weight:700;letter-spacing:2px;margin-bottom:8px;"></div>
      <div id="t-step-title" style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:36px;font-weight:900;letter-spacing:3px;margin-bottom:20px;"></div>
      <div id="t-player-list" style="display:flex;flex-direction:column;gap:12px;"></div>
      <button onclick="showPage(''home'')" style="margin-top:20px;width:100%;padding:10px;background:transparent;color:#E70013;border:1px solid #E70013;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:15px;font-weight:900;cursor:pointer;">RETOUR</button>
    </div>
    <div id="t-result" style="display:none;flex-direction:column;gap:12px;">
      <h2 style="font-family:Barlow Condensed,sans-serif;color:#E70013;font-size:28px;font-weight:900;">TON BEST XI TUNISIE</h2>
      <div id="t-res-list" style="display:flex;flex-direction:column;gap:10px;"></div>
      <button onclick="tStep=0;tPicks={};document.getElementById(''t-result'').style.display=''none'';document.getElementById(''t-selection'').style.display=''block'';renderTunisiaStep();" style="margin-top:10px;width:100%;padding:10px;background:#E70013;color:#fff;border:none;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:15px;font-weight:900;cursor:pointer;">RECOMMENCER</button>
      <button onclick="showPage(''home'')" style="width:100%;padding:10px;background:transparent;color:#E70013;border:1px solid #E70013;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:15px;font-weight:900;cursor:pointer;">HOME</button>
    </div>
  </div>
</div>'''
content = content.replace('document.getElementById("page-home")', tunisia_steps + '\ndocument.getElementById("page-home")', 1)
content = content.replace('function showPage(page) {', 'function showPage(page) {\n  var tp = document.getElementById("page-tunisia"); if(tp) tp.style.display = page==="tunisia" ? "flex" : "none";', 1)
content = content.replace('</body>', page_tunisia + '</body>', 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
