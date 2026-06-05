js = '''
var TN_STEPS=[
  {key:"gk",  label:"GARDIEN DE BUT",    pos:"GK",   x:42, y:8},
  {key:"rb",  label:"LATERAL DROIT",     pos:"RB",   x:72, y:28},
  {key:"cb1", label:"DEFENSEUR CENTRAL", pos:"CB1",  x:55, y:28},
  {key:"cb2", label:"DEFENSEUR CENTRAL", pos:"CB2",  x:30, y:28},
  {key:"lb",  label:"LATERAL GAUCHE",    pos:"LB",   x:13, y:28},
  {key:"cdm", label:"MILIEU DEFENSIF",   pos:"CDM",  x:42, y:47},
  {key:"cm1", label:"MILIEU CENTRAL",    pos:"CM1",  x:22, y:58},
  {key:"cm2", label:"MILIEU CENTRAL",    pos:"CM2",  x:62, y:58},
  {key:"rw",  label:"AILIER DROIT",      pos:"RW",   x:72, y:74},
  {key:"lw",  label:"AILIER GAUCHE",     pos:"LW",   x:13, y:74},
  {key:"st",  label:"ATTAQUANT",         pos:"ST",   x:42, y:80},
  {key:"coach",label:"ENTRAINEUR",       pos:"COACH",x:42, y:95}
];
var CLUB_COLORS={
  "Club Africain":{bg:"#E70013",text:"#fff"},
  "Esperance Tunis":{bg:"#FFD700",text:"#000"},
  "CS Sfaxien":{bg:"#222",text:"#fff"},
  "Stade Tunisien":{bg:"#0057A8",text:"#fff"},
  "US Monastir":{bg:"#00873E",text:"#fff"}
};
var TN_PLAYERS={
  gk:[
    {name:"Abdelmouhib Chamakh",club:"Club Africain",nat:"Tunisie",pos:"GK",rating:82,img:"https://img.a.transfermarkt.technology/portrait/big/584250-1695041284.jpg"},
    {name:"Moez Ben Cherifia",  club:"Esperance Tunis",nat:"Tunisie",pos:"GK",rating:80,img:""},
    {name:"Farouk Ben Mustapha",club:"CS Sfaxien",nat:"Tunisie",pos:"GK",rating:79,img:""}
  ],
  rb:[
    {name:"Hamdi Nagguez",  club:"Club Africain",  nat:"Tunisie",pos:"RB",rating:79,img:""},
    {name:"Dylan Bronn",    club:"Esperance Tunis",nat:"Tunisie",pos:"RB",rating:78,img:""},
    {name:"Wajdi Kechrida", club:"Stade Tunisien", nat:"Tunisie",pos:"RB",rating:77,img:""}
  ],
  cb1:[
    {name:"Montassar Talbi",club:"Esperance Tunis",nat:"Tunisie",pos:"CB",rating:80,img:""},
    {name:"Bilel Ifa",      club:"Club Africain",  nat:"Tunisie",pos:"CB",rating:79,img:""},
    {name:"Nader Ghandri",  club:"CS Sfaxien",     nat:"Tunisie",pos:"CB",rating:78,img:""}
  ],
  cb2:[
    {name:"Yassine Meriah",    club:"Club Africain",  nat:"Tunisie",pos:"CB",rating:79,img:""},
    {name:"Ali Abdi",          club:"Esperance Tunis",nat:"Tunisie",pos:"CB",rating:78,img:""},
    {name:"Rodrigo Rodrigues", club:"CS Sfaxien",     nat:"Tunisie",pos:"CB",rating:77,img:""}
  ],
  lb:[
    {name:"Ali Maaloul", club:"CS Sfaxien",     nat:"Tunisie",pos:"LB",rating:81,img:""},
    {name:"Houcine Tka", club:"Esperance Tunis",nat:"Tunisie",pos:"LB",rating:78,img:""},
    {name:"Omar Rekik",  club:"Club Africain",  nat:"Tunisie",pos:"LB",rating:77,img:""}
  ],
  cdm:[
    {name:"Ghaylane Chaalali",club:"Esperance Tunis",nat:"Tunisie",pos:"CDM",rating:80,img:""},
    {name:"Anis Badri",       club:"Club Africain",  nat:"Tunisie",pos:"CDM",rating:79,img:""},
    {name:"Amadou NDiaye",    club:"Stade Tunisien", nat:"Tunisie",pos:"CDM",rating:77,img:""}
  ],
  cm1:[
    {name:"Saifeddine Khaoui",club:"US Monastir",  nat:"Tunisie",pos:"CM",rating:79,img:""},
    {name:"Zied Boughattas",  club:"Club Africain", nat:"Tunisie",pos:"CM",rating:78,img:""},
    {name:"Firas Ben Larbi",  club:"CS Sfaxien",    nat:"Tunisie",pos:"CM",rating:77,img:""}
  ],
  cm2:[
    {name:"Ghaith Zaalouni",  club:"Esperance Tunis",nat:"Tunisie",pos:"CM",rating:79,img:""},
    {name:"Phillippe Kinzumbi",club:"Club Africain", nat:"Tunisie",pos:"CM",rating:78,img:""},
    {name:"Omar Ben Ali",     club:"CS Sfaxien",     nat:"Tunisie",pos:"CM",rating:77,img:""}
  ],
  rw:[
    {name:"Haythem Jouini",club:"Esperance Tunis",nat:"Tunisie",pos:"RW",rating:81,img:""},
    {name:"Anice Badri",   club:"Esperance Tunis",nat:"Tunisie",pos:"RW",rating:79,img:""},
    {name:"Omar Ben Ali",  club:"CS Sfaxien",     nat:"Tunisie",pos:"RW",rating:78,img:""}
  ],
  lw:[
    {name:"Youssef Blaili",club:"Club Africain",  nat:"Tunisie",pos:"LW",rating:80,img:""},
    {name:"Anice Badri",   club:"Esperance Tunis",nat:"Tunisie",pos:"LW",rating:79,img:""},
    {name:"Firas Ben Larbi",club:"CS Sfaxien",    nat:"Tunisie",pos:"LW",rating:77,img:""}
  ],
  st:[
    {name:"Firas Chaouat",club:"Club Africain",  nat:"Tunisie",pos:"ST",rating:83,img:""},
    {name:"Issam Jebali", club:"Esperance Tunis",nat:"Tunisie",pos:"ST",rating:80,img:""},
    {name:"Omar Ben Ali", club:"CS Sfaxien",     nat:"Tunisie",pos:"ST",rating:81,img:""}
  ],
  coach:[
    {name:"Maher Kanzari",club:"Club Africain",  nat:"Tunisie",pos:"COACH",rating:85,img:""},
    {name:"Nabil Maaloul",club:"Esperance Tunis",nat:"Tunisie",pos:"COACH",rating:84,img:""},
    {name:"Lassad Dridi", club:"CS Sfaxien",     nat:"Tunisie",pos:"COACH",rating:82,img:""}
  ]
};
var tnStep=0, tnPicks={};
function startTunisiaXI(){
  tnStep=0; tnPicks={};
  document.getElementById("tn-result").style.display="none";
  document.getElementById("tn-main").style.display="flex";
  renderTNStep();
}
function renderTNStep(){
  var s=TN_STEPS[tnStep];
  // Update header
  document.getElementById("tn-step-num").textContent=(tnStep+1)+" / "+TN_STEPS.length+" — "+s.pos;
  document.getElementById("tn-step-title").textContent=s.label;
  // Update pitch highlights
  TN_STEPS.forEach(function(st,i){
    var el=document.getElementById("tn-dot-"+st.key);
    if(!el) return;
    var done=tnPicks[st.key];
    var active=i===tnStep;
    el.style.border=active?"2px dashed #FFD700":(done?"2px solid #E70013":"2px dashed rgba(255,255,255,0.2)");
    el.style.background=active?"rgba(255,215,0,0.15)":(done?"rgba(231,0,19,0.3)":"rgba(0,0,0,0.4)");
    el.style.color=active?"#FFD700":(done?"#fff":"rgba(255,255,255,0.4)");
    el.querySelector(".dot-label").textContent=done?tnPicks[st.key].name.split(" ").pop():st.pos;
  });
  // Render player cards
  var list=document.getElementById("tn-player-list");
  list.innerHTML="";
  TN_PLAYERS[s.key].forEach(function(pl){
    var club=CLUB_COLORS[pl.club]||{bg:"#333",text:"#fff"};
    var initials=pl.name.split(" ").map(function(w){return w[0];}).join("").substring(0,2);
    var card=document.createElement("div");
    card.style.cssText="display:flex;align-items:center;gap:16px;padding:16px 20px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:12px;cursor:pointer;transition:all 0.2s;margin-bottom:10px;";
    card.onmouseover=function(){this.style.background="rgba(231,0,19,0.1)";this.style.borderColor="rgba(231,0,19,0.4)";this.style.transform="translateX(6px)";};
    card.onmouseout=function(){this.style.background="rgba(255,255,255,0.03)";this.style.borderColor="rgba(255,255,255,0.07)";this.style.transform="none";};
    var imgBlock=pl.img
      ? '<img src="'+pl.img+'" style="width:72px;height:72px;border-radius:10px;object-fit:cover;object-position:top;border:2px solid '+club.bg+';" onerror="this.outerHTML=\'<div style=width:72px;height:72px;border-radius:10px;background:'+club.bg+';display:flex;align-items:center;justify-content:center;font-family:Barlow Condensed,sans-serif;font-size:24px;font-weight:900;color:'+club.text+';>'+initials+'<\\/div>\'">'
      : '<div style="width:72px;height:72px;border-radius:10px;background:'+club.bg+';display:flex;align-items:center;justify-content:center;font-family:Barlow Condensed,sans-serif;font-size:24px;font-weight:900;color:'+club.text+';">'+initials+'</div>';
    card.innerHTML=imgBlock+
      '<div style="flex:1;">'+
        '<div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:20px;font-weight:900;letter-spacing:1px;">'+pl.name+'</div>'+
        '<div style="color:'+club.bg+';font-size:12px;font-weight:700;margin-top:2px;">'+pl.club+'</div>'+
        '<div style="color:#555;font-size:11px;margin-top:2px;">'+pl.nat+'</div>'+
      '</div>'+
      '<div style="text-align:center;">'+
        '<div style="font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:32px;font-weight:900;line-height:1;">'+pl.rating+'</div>'+
        '<div style="color:#555;font-size:10px;font-weight:700;letter-spacing:1px;">'+pl.pos+'</div>'+
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
  document.getElementById("tn-main").style.display="none";
  var res=document.getElementById("tn-result");
  res.style.display="flex";
  var list=document.getElementById("tn-res-list");
  list.innerHTML="";
  TN_STEPS.forEach(function(s){
    var pl=tnPicks[s.key]; if(!pl) return;
    var club=CLUB_COLORS[pl.club]||{bg:"#333",text:"#fff"};
    var initials=pl.name.split(" ").map(function(w){return w[0];}).join("").substring(0,2);
    var d=document.createElement("div");
    d.style.cssText="display:flex;align-items:center;gap:12px;padding:12px 16px;background:rgba(255,255,255,0.03);border:1px solid rgba(231,0,19,0.2);border-radius:10px;margin-bottom:8px;";
    d.innerHTML='<div style="width:44px;height:44px;border-radius:8px;background:'+club.bg+';display:flex;align-items:center;justify-content:center;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:900;color:'+club.text+';">'+initials+'</div>'+
      '<div style="flex:1;"><div style="color:#E70013;font-size:9px;font-weight:700;letter-spacing:2px;">'+s.pos+'</div>'+
      '<div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:15px;font-weight:900;">'+pl.name+'</div>'+
      '<div style="color:#555;font-size:11px;">'+pl.club+'</div></div>'+
      '<div style="font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:24px;font-weight:900;">'+pl.rating+'</div>';
    list.appendChild(d);
  });
}
'''
open("tunisia.js","w",encoding="utf-8").write(js)
print("done")
