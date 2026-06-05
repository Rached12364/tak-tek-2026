f = open('write_tn.py', 'w', encoding='utf-8')
f.write('''
import pathlib
js = open("tunisia.js","w",encoding="utf-8")
js.write("""var TN_STEPS=[
  {key:"gk",label:"GARDIEN DE BUT",pos:"GK"},
  {key:"rb",label:"LATERAL DROIT",pos:"RB"},
  {key:"cb1",label:"DEFENSEUR CENTRAL",pos:"CB"},
  {key:"cb2",label:"DEFENSEUR CENTRAL",pos:"CB"},
  {key:"lb",label:"LATERAL GAUCHE",pos:"LB"},
  {key:"cdm",label:"MILIEU DEFENSIF",pos:"CDM"},
  {key:"cm1",label:"MILIEU CENTRAL",pos:"CM"},
  {key:"cm2",label:"MILIEU CENTRAL",pos:"CM"},
  {key:"rw",label:"AILIER DROIT",pos:"RW"},
  {key:"lw",label:"AILIER GAUCHE",pos:"LW"},
  {key:"st",label:"ATTAQUANT",pos:"ST"},
  {key:"coach",label:"ENTRAINEUR",pos:"COACH"}
];
var CLUB={
  "Club Africain":{bg:"#E70013",t:"#fff"},
  "Esperance Tunis":{bg:"#FFD700",t:"#000"},
  "CS Sfaxien":{bg:"#222",t:"#fff"},
  "Stade Tunisien":{bg:"#0057A8",t:"#fff"},
  "US Monastir":{bg:"#00873E",t:"#fff"}
};
var PL={
  gk:[{n:"Abdelmouhib Chamakh",c:"Club Africain",pos:"GK",r:82},{n:"Moez Ben Cherifia",c:"Esperance Tunis",pos:"GK",r:80},{n:"Farouk Ben Mustapha",c:"CS Sfaxien",pos:"GK",r:79}],
  rb:[{n:"Hamdi Nagguez",c:"Club Africain",pos:"RB",r:79},{n:"Dylan Bronn",c:"Esperance Tunis",pos:"RB",r:78},{n:"Wajdi Kechrida",c:"Stade Tunisien",pos:"RB",r:77}],
  cb1:[{n:"Montassar Talbi",c:"Esperance Tunis",pos:"CB",r:80},{n:"Bilel Ifa",c:"Club Africain",pos:"CB",r:79},{n:"Nader Ghandri",c:"CS Sfaxien",pos:"CB",r:78}],
  cb2:[{n:"Yassine Meriah",c:"Club Africain",pos:"CB",r:79},{n:"Ali Abdi",c:"Esperance Tunis",pos:"CB",r:78},{n:"Rodrigo Rodrigues",c:"CS Sfaxien",pos:"CB",r:77}],
  lb:[{n:"Ali Maaloul",c:"CS Sfaxien",pos:"LB",r:81},{n:"Houcine Tka",c:"Esperance Tunis",pos:"LB",r:78},{n:"Omar Rekik",c:"Club Africain",pos:"LB",r:77}],
  cdm:[{n:"Ghaylane Chaalali",c:"Esperance Tunis",pos:"CDM",r:80},{n:"Anis Badri",c:"Club Africain",pos:"CDM",r:79},{n:"Amadou NDiaye",c:"Stade Tunisien",pos:"CDM",r:77}],
  cm1:[{n:"Saifeddine Khaoui",c:"US Monastir",pos:"CM",r:79},{n:"Zied Boughattas",c:"Club Africain",pos:"CM",r:78},{n:"Firas Ben Larbi",c:"CS Sfaxien",pos:"CM",r:77}],
  cm2:[{n:"Ghaith Zaalouni",c:"Esperance Tunis",pos:"CM",r:79},{n:"Phillippe Kinzumbi",c:"Club Africain",pos:"CM",r:78},{n:"Omar Ben Ali",c:"CS Sfaxien",pos:"CM",r:77}],
  rw:[{n:"Haythem Jouini",c:"Esperance Tunis",pos:"RW",r:81},{n:"Anice Badri",c:"Esperance Tunis",pos:"RW",r:79},{n:"Omar Ben Ali",c:"CS Sfaxien",pos:"RW",r:78}],
  lw:[{n:"Youssef Blaili",c:"Club Africain",pos:"LW",r:80},{n:"Anice Badri",c:"Esperance Tunis",pos:"LW",r:79},{n:"Firas Ben Larbi",c:"CS Sfaxien",pos:"LW",r:77}],
  st:[{n:"Firas Chaouat",c:"Club Africain",pos:"ST",r:83},{n:"Issam Jebali",c:"Esperance Tunis",pos:"ST",r:80},{n:"Omar Ben Ali",c:"CS Sfaxien",pos:"ST",r:81}],
  coach:[{n:"Maher Kanzari",c:"Club Africain",pos:"COACH",r:85},{n:"Nabil Maaloul",c:"Esperance Tunis",pos:"COACH",r:84},{n:"Lassad Dridi",c:"CS Sfaxien",pos:"COACH",r:82}]
};
var tnStep=0,tnPicks={};
function startTunisiaXI(){
  tnStep=0;tnPicks={};
  document.getElementById("tn-result").style.display="none";
  document.getElementById("tn-main").style.display="flex";
  renderTNStep();
}
function renderTNStep(){
  var s=TN_STEPS[tnStep];
  document.getElementById("tn-step-num").textContent=(tnStep+1)+" / "+TN_STEPS.length+" - "+s.pos;
  document.getElementById("tn-step-title").textContent=s.label;
  TN_STEPS.forEach(function(st,i){
    var el=document.getElementById("tn-dot-"+st.key);
    if(!el)return;
    var done=tnPicks[st.key];
    var active=i===tnStep;
    el.style.border=active?"2px dashed #FFD700":(done?"2px solid #E70013":"2px dashed rgba(255,255,255,0.2)");
    el.style.background=active?"rgba(255,215,0,0.15)":(done?"rgba(231,0,19,0.3)":"rgba(0,0,0,0.4)");
    var lbl=el.querySelector(".dot-label");
    if(lbl)lbl.textContent=done?tnPicks[st.key].n.split(" ").pop():st.pos;
  });
  var list=document.getElementById("tn-player-list");
  list.innerHTML="";
  PL[s.key].forEach(function(pl){
    var club=CLUB[pl.c]||{bg:"#333",t:"#fff"};
    var ini=pl.n.split(" ").map(function(w){return w[0];}).join("").substring(0,2);
    var card=document.createElement("div");
    card.style.cssText="display:flex;align-items:center;gap:16px;padding:16px 20px;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:12px;cursor:pointer;transition:all 0.2s;margin-bottom:10px;";
    card.onmouseover=function(){this.style.background="rgba(231,0,19,0.1)";this.style.borderColor="rgba(231,0,19,0.5)";this.style.transform="translateX(6px)";};
    card.onmouseout=function(){this.style.background="rgba(255,255,255,0.03)";this.style.borderColor="rgba(255,255,255,0.07)";this.style.transform="none";};
    var avatar='<div style="width:64px;height:64px;border-radius:10px;background:'+club.bg+';display:flex;align-items:center;justify-content:center;font-family:Barlow Condensed,sans-serif;font-size:22px;font-weight:900;color:'+club.t+';flex-shrink:0;">'+ini+'</div>';
    card.innerHTML=avatar+'<div style="flex:1;"><div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:20px;font-weight:900;">'+pl.n+'</div><div style="color:'+club.bg+';font-size:12px;font-weight:700;margin-top:3px;">'+pl.c+'</div></div><div style="text-align:center;"><div style="font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:32px;font-weight:900;line-height:1;">'+pl.r+'</div><div style="color:#555;font-size:10px;letter-spacing:1px;">'+pl.pos+'</div></div>';
    card.onclick=(function(p){return function(){
      tnPicks[TN_STEPS[tnStep].key]=p;
      tnStep++;
      if(tnStep>=TN_STEPS.length){renderTNResult();}else{renderTNStep();}
    };})(pl);
    list.appendChild(card);
  });
}
function renderTNResult(){
  document.getElementById("tn-main").style.display="none";
  document.getElementById("tn-result").style.display="flex";
  var list=document.getElementById("tn-res-list");
  list.innerHTML="";
  TN_STEPS.forEach(function(s){
    var pl=tnPicks[s.key];if(!pl)return;
    var club=CLUB[pl.c]||{bg:"#333",t:"#fff"};
    var ini=pl.n.split(" ").map(function(w){return w[0];}).join("").substring(0,2);
    var d=document.createElement("div");
    d.style.cssText="display:flex;align-items:center;gap:12px;padding:12px 16px;background:rgba(255,255,255,0.03);border:1px solid rgba(231,0,19,0.2);border-radius:10px;margin-bottom:8px;";
    d.innerHTML='<div style="width:44px;height:44px;border-radius:8px;background:'+club.bg+';display:flex;align-items:center;justify-content:center;font-family:Barlow Condensed,sans-serif;font-size:15px;font-weight:900;color:'+club.t+';">'+ini+'</div><div style="flex:1;"><div style="color:#E70013;font-size:9px;font-weight:700;letter-spacing:2px;">'+s.pos+'</div><div style="font-family:Barlow Condensed,sans-serif;color:#fff;font-size:15px;font-weight:900;">'+pl.n+'</div><div style="color:#555;font-size:11px;">'+pl.c+'</div></div><div style="font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:24px;font-weight:900;">'+pl.r+'</div>';
    list.appendChild(d);
  });
}
""")
js.close()
print("done")
''')
f.close()
