content = open('index.html','r',encoding='utf-8').read()
firebase_script = '''
<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getFirestore, collection, addDoc, getDocs, orderBy, query, limit, doc, setDoc, getDoc } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";
const firebaseConfig = {
  apiKey: "AIzaSyAA27562qKVSDsUrUp48ROCk7K3UmgUoBE",
  authDomain: "tak-tek-2026.firebaseapp.com",
  projectId: "tak-tek-2026",
  storageBucket: "tak-tek-2026.firebasestorage.app",
  messagingSenderId: "825987706018",
  appId: "1:825987706018:web:912937a3d5a133d979bbfb"
};
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
window.db = db;
window.fbCollection = collection;
window.fbAddDoc = addDoc;
window.fbGetDocs = getDocs;
window.fbOrderBy = orderBy;
window.fbQuery = query;
window.fbLimit = limit;
window.fbDoc = doc;
window.fbSetDoc = setDoc;
window.fbGetDoc = getDoc;
// Charger profil
var savedProfile = localStorage.getItem('tak-tek-profile');
if (savedProfile) {
  window.userProfile = JSON.parse(savedProfile);
} else {
  window.userProfile = null;
}
window.saveProfile = async function(name, club, flag) {
  var profile = { name: name, club: club, flag: flag, createdAt: new Date().toISOString() };
  localStorage.setItem('tak-tek-profile', JSON.stringify(profile));
  window.userProfile = profile;
  await fbSetDoc(fbDoc(db, 'users', name), profile);
  document.getElementById('profile-display').innerHTML = flag + ' <b>' + name + '</b> · ' + club;
  document.getElementById('profile-modal').style.display = 'none';
}
window.saveQuizScore = async function(playerName, score, total) {
  if (!window.userProfile) {
    document.getElementById('profile-modal').style.display = 'flex';
    return;
  }
  var pct = Math.round((score/total)*100);
  await fbAddDoc(fbCollection(db, 'scores'), {
    user: window.userProfile.name,
    flag: window.userProfile.flag,
    club: window.userProfile.club,
    player: playerName,
    score: score,
    total: total,
    pct: pct,
    date: new Date().toISOString()
  });
}
window.loadLeaderboard = async function() {
  var q = fbQuery(fbCollection(db, 'scores'), fbOrderBy('pct', 'desc'), fbLimit(10));
  var snap = await fbGetDocs(q);
  var html = '';
  var rank = 1;
  snap.forEach(function(d) {
    var data = d.data();
    var medal = rank === 1 ? '🥇' : rank === 2 ? '🥈' : rank === 3 ? '🥉' : rank + '.';
    html += '<div style="display:flex;align-items:center;gap:12px;padding:12px;background:rgba(255,255,255,0.05);border-radius:10px;margin-bottom:8px;">' +
      '<div style="font-size:20px;width:32px;">' + medal + '</div>' +
      '<div style="flex:1;">' +
        '<div style="color:#fff;font-weight:900;font-family:Barlow Condensed,sans-serif;font-size:18px;">' + data.flag + ' ' + data.user + '</div>' +
        '<div style="color:#888;font-size:12px;">' + data.player + ' · ' + data.club + '</div>' +
      '</div>' +
      '<div style="color:#00C853;font-size:22px;font-weight:900;">' + data.pct + '%</div>' +
    '</div>';
    rank++;
  });
  document.getElementById('leaderboard-list').innerHTML = html || '<div style="color:#888;text-align:center;padding:20px;">Aucun score encore</div>';
}
</script>
'''
# Ajouter modal profil + leaderboard page
profile_html = '''
<!-- Modal Profil -->
<div id="profile-modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.85);z-index:9999;align-items:center;justify-content:center;flex-direction:column;">
  <div style="background:#1a1a1a;border:2px solid #00C853;border-radius:20px;padding:40px;max-width:400px;width:90%;text-align:center;">
    <div style="font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:32px;font-weight:900;margin-bottom:24px;">CREER MON PROFIL</div>
    <input id="profile-name" type="text" placeholder="Ton nom/pseudo" style="width:100%;padding:12px;border-radius:10px;border:2px solid #00C853;background:#111;color:#fff;font-size:16px;margin-bottom:12px;box-sizing:border-box;">
    <select id="profile-club" style="width:100%;padding:12px;border-radius:10px;border:2px solid #00C853;background:#111;color:#fff;font-size:16px;margin-bottom:12px;box-sizing:border-box;">
      <option value="Esperance Tunis">Esperance Tunis</option>
      <option value="Club Africain">Club Africain</option>
      <option value="CS Sfaxien">CS Sfaxien</option>
      <option value="Etoile du Sahel">Etoile du Sahel</option>
      <option value="US Monastirienne">US Monastirienne</option>
      <option value="Autre">Autre</option>
    </select>
    <select id="profile-flag" style="width:100%;padding:12px;border-radius:10px;border:2px solid #00C853;background:#111;color:#fff;font-size:16px;margin-bottom:20px;box-sizing:border-box;">
      <option value="🇹🇳">🇹🇳 Tunisie</option>
      <option value="🇩🇿">🇩🇿 Algerie</option>
      <option value="🇲🇦">🇲🇦 Maroc</option>
      <option value="🇫🇷">🇫🇷 France</option>
      <option value="🌍">🌍 Autre</option>
    </select>
    <button onclick="saveProfile(document.getElementById('profile-name').value, document.getElementById('profile-club').value, document.getElementById('profile-flag').value)" style="background:#00C853;color:#000;font-size:18px;font-weight:900;padding:14px 40px;border:none;border-radius:12px;cursor:pointer;width:100%;">SAUVEGARDER</button>
    <button onclick="document.getElementById('profile-modal').style.display='none'" style="background:transparent;color:#888;font-size:14px;padding:10px;border:none;cursor:pointer;margin-top:8px;">Annuler</button>
  </div>
</div>
<!-- Page Leaderboard -->
<div id="page-leaderboard" style="display:none;width:100%;min-height:100vh;background:linear-gradient(135deg,#0a0a1a,#0d1b2a);flex-direction:column;align-items:center;padding:40px 20px;box-sizing:border-box;">
  <div style="width:100%;max-width:600px;">
    <div style="text-align:center;margin-bottom:32px;">
      <div style="color:#00C853;font-size:11px;font-weight:700;letter-spacing:4px;margin-bottom:8px;">TAK TEK 2026</div>
      <div style="font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:52px;font-weight:900;">LEADERBOARD</div>
      <div style="color:#888;font-size:14px;margin-top:8px;">Les meilleurs scores du Quiz</div>
    </div>
    <div id="leaderboard-list" style="width:100%;"></div>
    <button onclick="showPage('home')" style="margin-top:24px;background:transparent;border:2px solid #00C853;color:#00C853;font-size:16px;font-weight:900;padding:12px 32px;border-radius:12px;cursor:pointer;width:100%;">RETOUR</button>
  </div>
</div>
'''
content = content.replace('</body>', firebase_script + profile_html + '</body>')
open('index.html','w',encoding='utf-8').write(content)
print('OK')
