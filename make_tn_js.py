# Create clean tunisia.js file
js = """
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
var CLUB_COLORS={
  "Club Africain":{bg:"#E70013",text:"#fff"},
  "Esperance Tunis":{bg:"#FFD700",text:"#000"},
  "CS Sfaxien":{bg:"#111",text:"#fff"},
  "Stade Tunisien":{bg:"#0057A8",text:"#fff"},
  "US Monastir":{bg:"#00873E",text:"#fff"}
};
var TN_PLAYERS={
  gk:[{name:"Abdelmouhib Chamakh",club:"Club Africain",pos:"GK",rating:82,img:"https://img.a.transfermarkt.technology/portrait/big/584250-1695041284.jpg"},{name:"Moez Ben Cherifia",club:"Esperance Tunis",pos:"GK",rating:80,img:""},{name:"Farouk Ben Mustapha",club:"CS Sfaxien",pos:"GK",rating:79,img:""}],
  rb:[{name:"Hamdi Nagguez",club:"Club Africain",pos:"RB",rating:79,img:""},{name:"Dylan Bronn",club:"Esperance Tunis",pos:"RB",rating:78,img:""},{name:"Wajdi Kechrida",club:"Stade Tunisien",pos:"RB",rating:77,img:""}],
  cb1:[{name:"Montassar Talbi",club:"Esperance Tunis",pos:"CB",rating:80,img:""},{name:"Bilel Ifa",club:"Club Africain",pos:"CB",rating:79,img:""},{name:"Nader Ghandri",club:"CS Sfaxien",pos:"CB",rating:78,img:""}],
  cb2:[{name:"Yassine Meriah",club:"Club Africain",pos:"CB",rating:79,img:""},{name:"Ali Abdi",club:"Esperance Tunis",pos:"CB",rating:78,img:""},{name:"Rodrigo Rodrigues",club:"CS Sfaxien",pos:"CB",rating:77,img:""}],
  lb:[{name:"Ali Maaloul",club:"CS Sfaxien",pos:"LB",rating:81,img:""},{name:"Houcine Tka",club:"Esperance Tunis",pos:"LB",rating:78,img:""},{name:"Omar Rekik",club:"Club Africain",pos:"LB",rating:77,img:""}],
  cdm:[{name:"Ghaylane Chaalali",club:"Esperance Tunis",pos:"CDM",rating:80,img:""},{name:"Anis Badri",club:"Club Africain",pos:"CDM",rating:79,img:""},{name:"Amadou NDiaye",club:"Stade Tunisien",pos:"CDM",rating:77,img:""}],
  cm:[{name:"Saifeddine Khaoui",club:"US Monastir",pos:"CM",rating:79,img:""},{name:"Zied Boughattas",club:"Club Africain",pos:"CM",rating:78,img:""},{name:"Firas Ben Larbi",club:"CS Sfaxien",pos:"CM",rating:77,img:""}],
  rw:[{name:"Phillippe Kinzumbi",club:"Club Africain",pos:"RW",rating:80,img:""},{name:"Ghaith Zaalouni",club:"Esperance Tunis",pos:"RW",rating:79,img:""},{name:"Omar Ben Ali",club:"CS Sfaxien",pos:"RW",rating:78,img:""}],
  lw:[{name:"Haythem Jouini",club:"Esperance Tunis",pos:"LW",rating:81,img:""},{name:"Youssef Blaili",club:"Club Africain",pos:"LW",rating:80,img:""},{name:"Anice Badri",club:"Esperance Tunis",pos:"LW",rating:79,img:""}],
  st:[{name:"Firas Chaouat",club:"Club Africain",pos:"ST",rating:83,img:""},{name:"Omar Ben Ali",club:"CS Sfaxien",pos:"ST",rating:81,img:""},{name:"Issam Jebali",club:"Esperance Tunis",pos:"ST",rating:80,img:""}],
  coach:[{name:"Maher Kanzari",club:"Club Africain",pos:"COACH",rating:85,img:""},{name:"Nabil Maaloul",club:"Esperance Tunis",pos:"COACH",rating:84,img:""},{name:"Lassad Dridi",club:"CS Sfaxien",pos:"COACH",rating:82,img:""}]
};
var tnStep=0,tnPicks={};
function startTunisiaXI(){tnStep=0;tnPicks={};document.getElementById("tn-result").style.display="none";document.getElementById("tn-selection").style.display="flex";renderTNStep();}
function renderTNStep(){
  var s=TN_STEPS[tnStep];
  document.getElementById("tn-step-label").textContent=(tnStep+1)+" / "+TN_STEPS.length+" - "+s.pos;
  document.getElementById("tn-step-title").textContent=s.en;
  document.getElementById("tn-pitch-pos").textContent=s.pos;
  document.getElementById("tn-pitch-step").textContent="CHOISIS TON "+s.pos;
  var dots=document.getElementById("tn-progress-dots");
  if(dots){dots.innerHTML="";TN_STEPS.forEach(function(st,i){var d=document.createElement("div");d.style.cssText="width:10px;height:10px;border-radius:50%;background:"+(i<tnStep?"#E70013":i===tnStep?"#fff":"#333")+";";dots.appendChild(d);});}
  var list=document.getElementById("tn-player-list");
  list.innerHTML="";
  TN_PLAYERS[s.key].forEach(function(pl){
    var club=CLUB_COLORS[pl.club]||{bg:"#333",text:"#fff"};
    var initials=pl.name.split(" ").map(function(w){return w[0];}).join("").substring(0,2);
    var card=document.createElement("div");
    card.style.cssText="width:160px;cursor:pointer;transition:transform 0.2s,box-shadow 0.2s;";
    card.onmouseover=function(){this.style.transform="translateY(-8px) scale(1.05)";this.style.boxShadow="0 20px 40px rgba(231,0,19,0.4)";};
    card.onmouseout=function(){this.style.transform="none";this.style.boxShadow="none";};
    var imgHtml=pl.img?'<img src="'+pl.img+'" style="width:100%;height:100%;object-fit:cover;object-position:top;" onerror="this.style.display=\'none\'">':'';
    card.innerHTML='<div style="background:linear-gradient(160deg,'+club.bg+',rgba(0,0,0,0.9));border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,0.1);">'+
      '<div style="position:relative;height:180px;overflow:hidden;">'+imgHtml+
      '<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:Barlow Condensed,sans-serif;font-size:56px;font-weight:900;color:rgba(255,255,255,0.2);">'+initials+'</div>'+
      '<div style="position:absolute;top:8px;left:8px;background:rgba(0,0,0,0.7);border-radius:6px;padding:4px 8px;text-align:center;">'+
      '<div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:22px;font-weight:900;line-height:1;">'+pl.rating+'</div>'+
      '<div style="font-family:Barlow Condensed,sans-serif;color:'+club.text+';font-size:11px;font-weight:700;">'+pl.pos+'</div></div></div>'+
      '<div style="padding:10px;background:rgba(0,0,0,0.8);">'+
      '<div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:16px;font-weight:900;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">'+pl.name+'</div>'+
      '<div style="font-family:Barlow Condensed,sans-serif;color:'+club.text+';font-size:11px;font-weight:700;margin-top:2px;">'+pl.club+'</div></div></div>';
    card.onclick=(function(player,step){return function(){tnPicks[TN_STEPS[step].key]=player;tnStep++;if(tnStep>=TN_STEPS.length){renderTNResult();}else{renderTNStep();}}})(pl,tnStep);
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
    var d=document.createElement("div");
    d.style.cssText="width:130px;";
    d.innerHTML='<div style="background:linear-gradient(160deg,'+club.bg+',rgba(0,0,0,0.9));border-radius:10px;overflow:hidden;border:1px solid rgba(231,0,19,0.4);">'+
      '<div style="padding:12px;background:rgba(0,0,0,0.85);">'+
      '<div style="color:#E70013;font-size:10px;font-weight:700;letter-spacing:2px;">'+s.en+'</div>'+
      '<div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:15px;font-weight:900;margin-top:4px;">'+pl.name+'</div>'+
      '<div style="font-family:Barlow Condensed,sans-serif;color:'+club.text+';font-size:11px;">'+pl.club+'</div></div></div>';
    list.appendChild(d);
  });
}
"""
open('tunisia.js', 'w', encoding='utf-8').write(js)
print('done')
