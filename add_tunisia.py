content = open('index.html', 'r', encoding='utf-8').read()
# Add Tunisia page before </body>
tunisia_page = '''<div id="page-tunisia" style="display:none;width:100%;min-height:100vh;background:#0a0a0a;flex-direction:column;overflow-y:auto;">
  <div style="padding:30px;border-bottom:2px solid #E70013;display:flex;align-items:center;gap:16px;background:#0a0a0a;">
    <img src="https://city-png.b-cdn.net/thumbnail/thumbnail_public/uploads/preview/hd-logo-of-tunisia-national-football-team-transparent-png-701751712400875ip5tcz8e38.png" style="width:60px;mix-blend-mode:screen;">
    <div>
      <div id="tn-step-label" style="color:#E70013;font-size:13px;font-weight:700;letter-spacing:2px;"></div>
      <div id="tn-step-title" style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:36px;font-weight:900;letter-spacing:3px;"></div>
    </div>
    <button onclick="showPage('home')" style="margin-left:auto;background:transparent;color:#E70013;border:1px solid #E70013;border-radius:6px;padding:7px 14px;font-family:Barlow Condensed,sans-serif;font-size:13px;font-weight:700;cursor:pointer;">HOME</button>
  </div>
  <div id="tn-selection" style="padding:30px;display:flex;flex-direction:column;gap:12px;">
    <div id="tn-player-list" style="display:flex;flex-direction:column;gap:12px;"></div>
  </div>
  <div id="tn-result" style="display:none;padding:30px;flex-direction:column;gap:12px;">
    <h2 style="font-family:Barlow Condensed,sans-serif;color:#E70013;font-size:28px;font-weight:900;letter-spacing:3px;">TON BEST XI TUNISIE</h2>
    <div id="tn-res-list" style="display:flex;flex-direction:column;gap:10px;"></div>
    <button onclick="startTunisiaXI()" style="margin-top:10px;width:100%;padding:12px;background:#E70013;color:#fff;border:none;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:15px;font-weight:900;cursor:pointer;">RECOMMENCER</button>
    <button onclick="showPage('home')" style="width:100%;padding:12px;background:transparent;color:#E70013;border:1px solid #E70013;border-radius:8px;font-family:Barlow Condensed,sans-serif;font-size:15px;font-weight:900;cursor:pointer;">HOME</button>
  </div>
</div>
<script>
var TN_STEPS = [
  {key:'gk',  en:'GARDIEN DE BUT',    pos:'GK'},
  {key:'rb',  en:'LATERAL DROIT',     pos:'RB'},
  {key:'cb1', en:'DEFENSEUR CENTRAL', pos:'CB'},
  {key:'cb2', en:'DEFENSEUR CENTRAL', pos:'CB'},
  {key:'lb',  en:'LATERAL GAUCHE',    pos:'LB'},
  {key:'cdm', en:'MILIEU DEFENSIF',   pos:'CDM'},
  {key:'cm',  en:'MILIEU CENTRAL',    pos:'CM'},
  {key:'rw',  en:'AILIER DROIT',      pos:'RW'},
  {key:'lw',  en:'AILIER GAUCHE',     pos:'LW'},
  {key:'st',  en:'ATTAQUANT',         pos:'ST'},
  {key:'coach',en:'ENTRAINEUR',       pos:'COACH'}
];
var TN_PLAYERS = {
  gk:   [{name:'Abdelmouhib Chamakh',club:'Club Africain',img:'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Flag_of_Iran.svg/1200px-Flag_of_Iran.svg.png'},{name:'Moez Ben Cherifia',club:'Esperance Tunis',img:''},{name:'Farouk Ben Mustapha',club:'CS Sfaxien',img:''}],
  rb:   [{name:'Hamdi Nagguez',club:'Club Africain',img:''},{name:'Dylan Bronn',club:'Esperance Tunis',img:''},{name:'Wajdi Kechrida',club:'Stade Tunisien',img:''}],
  cb1:  [{name:'Montassar Talbi',club:'Esperance Tunis',img:''},{name:'Bilel Ifa',club:'Club Africain',img:''},{name:'Nader Ghandri',club:'CS Sfaxien',img:''}],
  cb2:  [{name:'Yassine Meriah',club:'Club Africain',img:''},{name:'Ali Abdi',club:'Esperance Tunis',img:''},{name:'Rodrigo Rodrigues',club:'CS Sfaxien',img:''}],
  lb:   [{name:'Ali Maaloul',club:'CS Sfaxien',img:''},{name:'Houcine Tka',club:'Esperance Tunis',img:''},{name:'Omar Rekik',club:'Club Africain',img:''}],
  cdm:  [{name:'Ghaylane Chaalali',club:'Esperance Tunis',img:''},{name:'Anis Badri',club:'Club Africain',img:''},{name:'Amadou NDiaye',club:'Stade Tunisien',img:''}],
  cm:   [{name:'Saifeddine Khaoui',club:'US Monastir',img:''},{name:'Zied Boughattas',club:'Club Africain',img:''},{name:'Firas Ben Larbi',club:'CS Sfaxien',img:''}],
  rw:   [{name:'Phillippe Kinzumbi',club:'Club Africain',img:''},{name:'Ghaith Zaalouni',club:'Esperance Tunis',img:''},{name:'Omar Ben Ali',club:'CS Sfaxien',img:''}],
  lw:   [{name:'Haythem Jouini',club:'Esperance Tunis',img:''},{name:'Youssef Blaili',club:'Club Africain',img:''},{name:'Anice Badri',club:'Esperance Tunis',img:''}],
  st:   [{name:'Firas Chaouat',club:'Club Africain',img:''},{name:'Omar Ben Ali',club:'CS Sfaxien',img:''},{name:'Issam Jebali',club:'Esperance Tunis',img:''}],
  coach:[{name:'Maher Kanzari',club:'Club Africain',img:''},{name:'Nabil Maaloul',club:'Esperance Tunis',img:''},{name:'Lassad Dridi',club:'CS Sfaxien',img:''}]
};
var tnStep=0, tnPicks={};
function startTunisiaXI() {
  tnStep=0; tnPicks={};
  document.getElementById('tn-result').style.display='none';
  document.getElementById('tn-selection').style.display='flex';
  renderTNStep();
}
function renderTNStep() {
  var s = TN_STEPS[tnStep];
  document.getElementById('tn-step-label').textContent=(tnStep+1)+' / '+TN_STEPS.length+' — '+s.pos;
  document.getElementById('tn-step-title').textContent=s.en;
  var list=document.getElementById('tn-player-list');
  list.innerHTML='';
  TN_PLAYERS[s.key].forEach(function(pl){
    var c=document.createElement('div');
    c.style.cssText='background:#111;border:2px solid #333;border-radius:12px;padding:16px;display:flex;align-items:center;gap:16px;cursor:pointer;transition:all 0.2s;';
    c.onmouseover=function(){this.style.borderColor='#E70013';this.style.background='#1a0000';};
    c.onmouseout=function(){this.style.borderColor='#333';this.style.background='#111';};
    c.innerHTML='<div style="width:60px;height:60px;border-radius:50%;background:#E70013;display:flex;align-items:center;justify-content:center;font-family:Barlow Condensed,sans-serif;font-size:20px;font-weight:900;color:#fff;flex-shrink:0;">'+pl.name.charAt(0)+'</div><div><div style="font-family:Barlow Condensed,sans-serif;font-size:20px;font-weight:900;color:#fff;">'+pl.name+'</div><div style="color:#E70013;font-size:13px;font-weight:700;">'+pl.club+'</div></div>';
    c.onclick=function(){tnPicks[s.key]=pl;tnStep++;if(tnStep>=TN_STEPS.length){renderTNResult();}else{renderTNStep();}};
    list.appendChild(c);
  });
}
function renderTNResult(){
  document.getElementById('tn-selection').style.display='none';
  document.getElementById('tn-result').style.display='flex';
  var list=document.getElementById('tn-res-list');
  list.innerHTML='';
  TN_STEPS.forEach(function(s){
    var pl=tnPicks[s.key];if(!pl)return;
    var d=document.createElement('div');
    d.style.cssText='display:flex;align-items:center;gap:16px;background:#111;border:1px solid #E70013;border-radius:10px;padding:12px;';
    d.innerHTML='<div style="width:50px;height:50px;border-radius:50%;background:#E70013;display:flex;align-items:center;justify-content:center;font-family:Barlow Condensed,sans-serif;font-size:18px;font-weight:900;color:#fff;">'+pl.name.charAt(0)+'</div><div><div style="color:#E70013;font-size:11px;font-weight:700;letter-spacing:2px;">'+s.en+'</div><div style="color:#fff;font-family:Barlow Condensed,sans-serif;font-size:18px;font-weight:900;">'+pl.name+'</div><div style="color:#666;font-size:12px;">'+pl.club+'</div></div>';
    list.appendChild(d);
  });
}
</script>'''
content = content.replace('</body>', tunisia_page + '</body>', 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
