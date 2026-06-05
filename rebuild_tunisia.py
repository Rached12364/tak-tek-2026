content = open('index.html', 'r', encoding='utf-8').read()
# Remove old Tunisia script and page
import re
content = re.sub(r'<div id="page-tunisia".*?</div>\s*<script>\s*var TN_STEPS.*?</script>', '', content, flags=re.DOTALL)
# New Tunisia page with FIFA card style
new_tunisia = '''<div id="page-tunisia" style="display:none;width:100%;min-height:100vh;background:#0a0a0a;flex-direction:row;overflow:hidden;">
  <!-- LEFT: Football pitch -->
  <div style="width:380px;flex-shrink:0;background:linear-gradient(180deg,#0d3b1e,#0a2e16,#0d3b1e);position:relative;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding:20px 0;overflow:hidden;">
    <!-- Pitch lines -->
    <div style="position:absolute;inset:0;opacity:0.15;">
      <svg width="100%" height="100%" viewBox="0 0 380 700" xmlns="http://www.w3.org/2000/svg">
        <rect x="30" y="20" width="320" height="660" fill="none" stroke="white" stroke-width="2"/>
        <line x1="30" y1="350" x2="350" y2="350" stroke="white" stroke-width="2"/>
        <circle cx="190" cy="350" r="60" fill="none" stroke="white" stroke-width="2"/>
        <circle cx="190" cy="350" r="4" fill="white"/>
        <rect x="110" y="20" width="160" height="80" fill="none" stroke="white" stroke-width="2"/>
        <rect x="110" y="600" width="160" height="80" fill="none" stroke="white" stroke-width="2"/>
        <rect x="70" y="20" width="240" height="130" fill="none" stroke="white" stroke-width="2"/>
        <rect x="70" y="550" width="240" height="130" fill="none" stroke="white" stroke-width="2"/>
      </svg>
    </div>
    <!-- Header -->
    <div style="position:relative;z-index:2;text-align:center;margin-bottom:16px;">
      <img src="https://city-png.b-cdn.net/thumbnail/thumbnail_public/uploads/preview/hd-logo-of-tunisia-national-football-team-transparent-png-701751712400875ip5tcz8e38.png" style="width:70px;mix-blend-mode:screen;">
      <div style="font-family:Barlow Condensed,sans-serif;color:#E70013;font-size:22px;font-weight:900;letter-spacing:3px;">BEST XI TUNISIE</div>
      <div style="color:#555;font-size:11px;letter-spacing:2px;">LIGUE 1 — 2025/2026</div>
    </div>
    <!-- Step indicator -->
    <div style="position:relative;z-index:2;width:90%;">
      <div id="tn-pitch-pos" style="font-family:Barlow Condensed,sans-serif;color:#E70013;font-size:32px;font-weight:900;letter-spacing:4px;text-align:center;margin-bottom:4px;"></div>
      <div style="background:rgba(231,0,19,0.1);border:1px solid rgba(231,0,19,0.3);border-radius:8px;padding:10px;text-align:center;">
        <div id="tn-pitch-step" style="color:#fff;font-size:13px;letter-spacing:2px;"></div>
        <div style="margin-top:8px;display:flex;gap:4px;justify-content:center;flex-wrap:wrap;" id="tn-progress-dots"></div>
      </div>
    </div>
    <button onclick="showPage(''home'')" style="position:absolute;bottom:20px;left:50%;transform:translateX(-50%);background:transparent;color:#E70013;border:1px solid #E70013;border-radius:6px;padding:8px 20px;font-family:Barlow Condensed,sans-serif;font-size:13px;font-weight:700;cursor:pointer;z-index:2;">HOME</button>
  </div>
  <!-- RIGHT: Player selection -->
  <div style="flex:1;display:flex;flex-direction:column;overflow-y:auto;background:#0a0a0a;">
    <!-- Top bar -->
    <div style="padding:20px 30px;border-bottom:1px solid #1a1a1a;display:flex;align-items:center;gap:12px;position:sticky;top:0;background:#0a0a0a;z-index:10;">
      <div>
        <div id="tn-step-label" style="color:#E70013;font-size:11px;font-weight:700;letter-spacing:3px;"></div>
        <div id="tn-step-title" style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:36px;font-weight:900;letter-spacing:3px;line-height:1;"></div>
      </div>
    </div>
    <!-- Player cards (FIFA style) -->
    <div id="tn-selection" style="padding:30px;display:flex;flex-direction:row;gap:20px;flex-wrap:wrap;align-items:flex-start;">
      <div id="tn-player-list" style="display:flex;gap:20px;flex-wrap:wrap;"></div>
    </div>
    <!-- Result -->
    <div id="tn-result" style="display:none;padding:30px;flex-direction:column;gap:16px;">
      <h2 style="font-family:Barlow Condensed,sans-serif;color:#E70013;font-size:32px;font-weight:900;letter-spacing:3px;">TON BEST XI TUNISIE 🇹🇳</h2>
      <div id="tn-res-list" style="display:flex;gap:16px;flex-wrap:wrap;"></div>
      <div style="display:flex;gap:12px;margin-top:10px;">
        <button onclick="startTunisiaXI()" style="flex:1;padding:14px;background:#E70013;color:#fff;border:none;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:900;cursor:pointer;letter-spacing:2px;">RECOMMENCER</button>
        <button onclick="showPage(''home'')" style="flex:1;padding:14px;background:transparent;color:#E70013;border:2px solid #E70013;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:900;cursor:pointer;letter-spacing:2px;">HOME</button>
      </div>
    </div>
  </div>
</div>
<script>
var TN_STEPS=[
  {key:"gk",  en:"GARDIEN DE BUT",    pos:"GK",  rating:82},
  {key:"rb",  en:"LATERAL DROIT",     pos:"RB",  rating:79},
  {key:"cb1", en:"DEFENSEUR CENTRAL", pos:"CB",  rating:80},
  {key:"cb2", en:"DEFENSEUR CENTRAL", pos:"CB",  rating:79},
  {key:"lb",  en:"LATERAL GAUCHE",    pos:"LB",  rating:81},
  {key:"cdm", en:"MILIEU DEFENSIF",   pos:"CDM", rating:80},
  {key:"cm",  en:"MILIEU CENTRAL",    pos:"CM",  rating:79},
  {key:"rw",  en:"AILIER DROIT",      pos:"RW",  rating:80},
  {key:"lw",  en:"AILIER GAUCHE",     pos:"LW",  rating:81},
  {key:"st",  en:"ATTAQUANT",         pos:"ST",  rating:83},
  {key:"coach",en:"ENTRAINEUR",       pos:"COACH",rating:85}
];
var CLUB_COLORS = {
  "Club Africain":   {bg:"#E70013", text:"#fff", logo:"https://upload.wikimedia.org/wikipedia/fr/thumb/3/38/Logo_Club_Africain.svg/200px-Logo_Club_Africain.svg.png"},
  "Esperance Tunis": {bg:"#FFD700", text:"#000", logo:"https://upload.wikimedia.org/wikipedia/fr/thumb/b/b2/Espérance_sportive_de_Tunis_%28logo%29.svg/200px-Espérance_sportive_de_Tunis_%28logo%29.svg.png"},
  "CS Sfaxien":      {bg:"#000", text:"#fff", logo:"https://upload.wikimedia.org/wikipedia/fr/thumb/4/4b/CS_Sfaxien.svg/200px-CS_Sfaxien.svg.png"},
  "Stade Tunisien":  {bg:"#0057A8", text:"#fff", logo:""},
  "US Monastir":     {bg:"#00873E", text:"#fff", logo:""}
};
var TN_PLAYERS={
  gk:[
    {name:"Abdelmouhib Chamakh", club:"Club Africain",   pos:"GK",  rating:82, img:"https://img.a.transfermarkt.technology/portrait/big/584250-1695041284.jpg"},
    {name:"Moez Ben Cherifia",   club:"Esperance Tunis", pos:"GK",  rating:80, img:"https://img.a.transfermarkt.technology/portrait/big/177802-1680863104.jpg"},
    {name:"Farouk Ben Mustapha", club:"CS Sfaxien",      pos:"GK",  rating:79, img:"https://img.a.transfermarkt.technology/portrait/big/107145-1680863104.jpg"}
  ],
  rb:[
    {name:"Hamdi Nagguez",   club:"Club Africain",   pos:"RB", rating:79, img:"https://img.a.transfermarkt.technology/portrait/big/200971-1680863104.jpg"},
    {name:"Dylan Bronn",     club:"Esperance Tunis", pos:"RB", rating:78, img:"https://img.a.transfermarkt.technology/portrait/big/314964-1680863104.jpg"},
    {name:"Wajdi Kechrida",  club:"Stade Tunisien",  pos:"RB", rating:77, img:"https://img.a.transfermarkt.technology/portrait/big/354083-1680863104.jpg"}
  ],
  cb1:[
    {name:"Montassar Talbi", club:"Esperance Tunis", pos:"CB", rating:80, img:"https://img.a.transfermarkt.technology/portrait/big/451978-1680863104.jpg"},
    {name:"Bilel Ifa",       club:"Club Africain",   pos:"CB", rating:79, img:"https://img.a.transfermarkt.technology/portrait/big/200974-1680863104.jpg"},
    {name:"Nader Ghandri",   club:"CS Sfaxien",      pos:"CB", rating:78, img:"https://img.a.transfermarkt.technology/portrait/big/200969-1680863104.jpg"}
  ],
  cb2:[
    {name:"Yassine Meriah",     club:"Club Africain",   pos:"CB", rating:79, img:"https://img.a.transfermarkt.technology/portrait/big/354085-1680863104.jpg"},
    {name:"Ali Abdi",           club:"Esperance Tunis", pos:"CB", rating:78, img:"https://img.a.transfermarkt.technology/portrait/big/200975-1680863104.jpg"},
    {name:"Rodrigo Rodrigues",  club:"CS Sfaxien",      pos:"CB", rating:77, img:""}
  ],
  lb:[
    {name:"Ali Maaloul",    club:"CS Sfaxien",      pos:"LB", rating:81, img:"https://img.a.transfermarkt.technology/portrait/big/188445-1680863104.jpg"},
    {name:"Houcine Tka",    club:"Esperance Tunis", pos:"LB", rating:78, img:""},
    {name:"Omar Rekik",     club:"Club Africain",   pos:"LB", rating:77, img:"https://img.a.transfermarkt.technology/portrait/big/502601-1680863104.jpg"}
  ],
  cdm:[
    {name:"Ghaylane Chaalali", club:"Esperance Tunis", pos:"CDM", rating:80, img:"https://img.a.transfermarkt.technology/portrait/big/354086-1680863104.jpg"},
    {name:"Anis Badri",        club:"Club Africain",   pos:"CDM", rating:79, img:"https://img.a.transfermarkt.technology/portrait/big/354087-1680863104.jpg"},
    {name:"Amadou NDiaye",     club:"Stade Tunisien",  pos:"CDM", rating:77, img:""}
  ],
  cm:[
    {name:"Saifeddine Khaoui", club:"US Monastir",    pos:"CM", rating:79, img:"https://img.a.transfermarkt.technology/portrait/big/354089-1680863104.jpg"},
    {name:"Zied Boughattas",   club:"Club Africain",  pos:"CM", rating:78, img:""},
    {name:"Firas Ben Larbi",   club:"CS Sfaxien",     pos:"CM", rating:77, img:""}
  ],
  rw:[
    {name:"Phillippe Kinzumbi", club:"Club Africain",   pos:"RW", rating:80, img:""},
    {name:"Ghaith Zaalouni",    club:"Esperance Tunis", pos:"RW", rating:79, img:""},
    {name:"Omar Ben Ali",       club:"CS Sfaxien",      pos:"RW", rating:78, img:""}
  ],
  lw:[
    {name:"Haythem Jouini", club:"Esperance Tunis", pos:"LW", rating:81, img:"https://img.a.transfermarkt.technology/portrait/big/354095-1680863104.jpg"},
    {name:"Youssef Blaili", club:"Club Africain",   pos:"LW", rating:80, img:"https://img.a.transfermarkt.technology/portrait/big/354096-1680863104.jpg"},
    {name:"Anice Badri",    club:"Esperance Tunis", pos:"LW", rating:79, img:"https://img.a.transfermarkt.technology/portrait/big/354097-1680863104.jpg"}
  ],
  st:[
    {name:"Firas Chaouat", club:"Club Africain",   pos:"ST", rating:83, img:""},
    {name:"Omar Ben Ali",  club:"CS Sfaxien",      pos:"ST", rating:81, img:""},
    {name:"Issam Jebali",  club:"Esperance Tunis", pos:"ST", rating:80, img:"https://img.a.transfermarkt.technology/portrait/big/354099-1680863104.jpg"}
  ],
  coach:[
    {name:"Maher Kanzari",  club:"Club Africain",   pos:"COACH", rating:85, img:""},
    {name:"Nabil Maaloul",  club:"Esperance Tunis", pos:"COACH", rating:84, img:""},
    {name:"Lassad Dridi",   club:"CS Sfaxien",      pos:"COACH", rating:82, img:""}
  ]
};
var tnStep=0, tnPicks={};
function startTunisiaXI(){
  tnStep=0; tnPicks={};
  document.getElementById("tn-result").style.display="none";
  document.getElementById("tn-selection").style.display="flex";
  renderTNStep();
}
function renderTNStep(){
  var s=TN_STEPS[tnStep];
  document.getElementById("tn-step-label").textContent=(tnStep+1)+" / "+TN_STEPS.length+" — "+s.pos;
  document.getElementById("tn-step-title").textContent=s.en;
  document.getElementById("tn-pitch-pos").textContent=s.pos;
  document.getElementById("tn-pitch-step").textContent="CHOISIS TON "+s.pos;
  // Progress dots
  var dots=document.getElementById("tn-progress-dots");
  dots.innerHTML="";
  TN_STEPS.forEach(function(st,i){
    var d=document.createElement("div");
    d.style.cssText="width:10px;height:10px;border-radius:50%;background:"+(i<tnStep?"#E70013":i===tnStep?"#fff":"#333")+";transition:background 0.3s;";
    dots.appendChild(d);
  });
  var list=document.getElementById("tn-player-list");
  list.innerHTML="";
  TN_PLAYERS[s.key].forEach(function(pl){
    var club=CLUB_COLORS[pl.club]||{bg:"#333",text:"#fff",logo:""};
    var initials=pl.name.split(" ").map(function(w){return w[0];}).join("").substring(0,2);
    var card=document.createElement("div");
    card.style.cssText="width:160px;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;position:relative;";
    card.onmouseover=function(){this.style.transform="translateY(-8px) scale(1.05)";this.style.boxShadow="0 20px 40px rgba(231,0,19,0.4)";};
    card.onmouseout=function(){this.style.transform="none";this.style.boxShadow="none";};
    card.innerHTML=
      '<div style="background:linear-gradient(160deg,'+club.bg+',rgba(0,0,0,0.9));border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,0.1);">'+
        '<div style="position:relative;height:180px;overflow:hidden;background:linear-gradient(180deg,rgba(0,0,0,0.2),rgba(0,0,0,0.6));">'+
          (pl.img ? '<img src="'+pl.img+'" style="width:100%;height:100%;object-fit:cover;object-position:top;" onerror="this.parentNode.querySelector(\'.initials-fb\').style.display=\'flex\';this.style.display=\'none\';">' : '')+
          '<div class="initials-fb" style="'+(pl.img?"display:none;":"display:flex;")+'position:absolute;inset:0;align-items:center;justify-content:center;font-family:Barlow Condensed,sans-serif;font-size:56px;font-weight:900;color:rgba(255,255,255,0.3);">'+initials+'</div>'+
          '<div style="position:absolute;top:8px;left:8px;background:rgba(0,0,0,0.7);border-radius:6px;padding:4px 8px;text-align:center;">'+
            '<div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:22px;font-weight:900;line-height:1;">'+pl.rating+'</div>'+
            '<div style="font-family:Barlow Condensed,sans-serif;color:'+club.text+';font-size:11px;font-weight:700;">'+pl.pos+'</div>'+
          '</div>'+
        '</div>'+
        '<div style="padding:10px;background:rgba(0,0,0,0.8);">'+
          '<div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:16px;font-weight:900;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">'+pl.name+'</div>'+
          '<div style="font-family:Barlow Condensed,sans-serif;color:'+club.text+';font-size:11px;font-weight:700;margin-top:2px;">'+pl.club+'</div>'+
        '</div>'+
      '</div>';
    card.onclick=(function(player){return function(){
      tnPicks[TN_STEPS[tnStep].key]=player;
      tnStep++;
      if(tnStep>=TN_STEPS.length){renderTNResult();}else{renderTNStep();}
    };})(pl);
    list.appendChild(card);
  });
}
function renderTNResult(){
  document.getElementById("tn-selection").style.display="none";
  document.getElementById("tn-result").style.display="flex";
  var list=document.getElementById("tn-res-list");
  list.innerHTML="";
  TN_STEPS.forEach(function(s){
    var pl=tnPicks[s.key];if(!pl)return;
    var club=CLUB_COLORS[pl.club]||{bg:"#333",text:"#fff"};
    var initials=pl.name.split(" ").map(function(w){return w[0];}).join("").substring(0,2);
    var d=document.createElement("div");
    d.style.cssText="width:130px;";
    d.innerHTML=
      '<div style="background:linear-gradient(160deg,'+club.bg+',rgba(0,0,0,0.9));border-radius:10px;overflow:hidden;border:1px solid rgba(231,0,19,0.4);">'+
        '<div style="position:relative;height:140px;overflow:hidden;">'+
          (pl.img ? '<img src="'+pl.img+'" style="width:100%;height:100%;object-fit:cover;object-position:top;" onerror="this.parentNode.querySelector(\'.ifb2\').style.display=\'flex\';this.style.display=\'none\';">' : '')+
          '<div class="ifb2" style="'+(pl.img?"display:none;":"display:flex;")+'position:absolute;inset:0;align-items:center;justify-content:center;font-family:Barlow Condensed,sans-serif;font-size:40px;font-weight:900;color:rgba(255,255,255,0.3);">'+initials+'</div>'+
          '<div style="position:absolute;top:6px;left:6px;background:rgba(0,0,0,0.7);border-radius:4px;padding:2px 6px;">'+
            '<div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:16px;font-weight:900;">'+pl.rating+'</div>'+
            '<div style="color:#E70013;font-size:9px;font-weight:700;">'+s.pos+'</div>'+
          '</div>'+
        '</div>'+
        '<div style="padding:8px;background:rgba(0,0,0,0.85);">'+
          '<div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:12px;font-weight:900;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">'+pl.name+'</div>'+
          '<div style="font-family:Barlow Condensed,sans-serif;color:'+club.text+';font-size:10px;">'+pl.club+'</div>'+
        '</div>'+
      '</div>';
    list.appendChild(d);
  });
}
</script>'''
content = content.replace('</body>', new_tunisia + '</body>', 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
