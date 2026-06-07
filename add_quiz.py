content = open('index.html','r',encoding='utf-8').read()
# 1. Ajouter bouton QUIZ sur la page home
old_btn = '''<button onclick="showPage('tunisia');startTunisiaXI();"'''
new_btn = '''<button onclick="showPage('quiz')" class="home-btn" style="width:250px;height:380px;background:linear-gradient(135deg,rgba(26,26,26,0.9),rgba(34,34,34,0.9));border:2px solid #00C853;border-radius:16px;color:#00C853;font-family:'Barlow Condensed',sans-serif;font-size:24px;font-weight:900;letter-spacing:3px;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;transition:transform 0.2s;backdrop-filter:blur(4px);" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
      <div style="font-size:11px;letter-spacing:4px;color:#00C853;background:rgba(0,200,83,0.15);padding:6px 16px;border-radius:20px;border:1px solid #00C853;">LIGUE 1</div>
      <div style="font-size:60px;">🧠</div>
      <div style="font-size:28px;font-weight:900;">QUIZ</div>
      <div style="font-size:13px;font-weight:400;color:#aaa;text-align:center;padding:0 16px;line-height:1.4;">Chaque poste : 3 joueurs au choix. Selectionne 1 par poste pour former ton equipe 2025/2026, puis choisis ton coach !</div>
    </button>
    <button onclick="showPage('tunisia');startTunisiaXI();"'''
content = content.replace(old_btn, new_btn)
# 2. Ajouter la page QUIZ
quiz_page = '''
<div id="page-quiz" style="display:none;width:100%;min-height:100vh;background:#0a0a0a;flex-direction:column;align-items:center;padding:40px 20px;">
  <button onclick="showPage('home')" style="position:fixed;top:16px;left:16px;background:#111;border:1px solid #FFD700;color:#FFD700;padding:8px 18px;border-radius:8px;font-family:'Barlow Condensed',sans-serif;font-size:15px;font-weight:700;cursor:pointer;letter-spacing:2px;z-index:99;">&#8592; HOME</button>
  <!-- Liste joueurs -->
  <div id="quiz-list-view" style="width:100%;max-width:900px;">
    <div style="text-align:center;margin-bottom:32px;">
      <div style="color:#00C853;font-size:11px;font-weight:700;letter-spacing:4px;margin-bottom:8px;">LIGUE 1 TUNISIENNE</div>
      <div style="font-family:'Barlow Condensed',sans-serif;color:#FFD700;font-size:52px;font-weight:900;line-height:1;">QUIZ JOUEURS</div>
      <div style="color:#888;font-size:14px;margin-top:8px;">Choisis un joueur pour commencer le quiz</div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:20px;">
      <!-- Carte Firas Chaouat -->
      <div onclick="startQuiz('chaouat')" style="background:#111;border:2px solid #333;border-radius:16px;padding:20px;text-align:center;cursor:pointer;transition:all 0.3s;" onmouseover="this.style.border='2px solid #00C853';this.style.transform='translateY(-4px)'" onmouseout="this.style.border='2px solid #333';this.style.transform='translateY(0)'">
        <img src="https://static.flashscore.com/res/image/data/EL8CsfBr-2X9WEIyE.png" style="width:120px;height:150px;object-fit:cover;border-radius:12px;margin-bottom:12px;">
        <div style="font-family:'Barlow Condensed',sans-serif;color:#fff;font-size:20px;font-weight:900;">FIRAS CHAOUAT</div>
        <div style="color:#E70013;font-size:13px;">Club Africain</div>
        <div style="color:#888;font-size:12px;margin-top:4px;">Avant-centre · 30 ans</div>
        <div style="margin-top:10px;background:#00C853;color:#000;font-size:12px;font-weight:700;padding:6px 12px;border-radius:20px;display:inline-block;">7 QUESTIONS</div>
      </div>
      <!-- Carte Youcef Belaili -->
      <div onclick="startQuiz('belaili')" style="background:#111;border:2px solid #333;border-radius:16px;padding:20px;text-align:center;cursor:pointer;transition:all 0.3s;" onmouseover="this.style.border='2px solid #00C853';this.style.transform='translateY(-4px)'" onmouseout="this.style.border='2px solid #333';this.style.transform='translateY(0)'">
        <img src="https://static.flashscore.com/res/image/data/6V5W3QyS-YDy6iaVc.png" style="width:120px;height:150px;object-fit:cover;border-radius:12px;margin-bottom:12px;">
        <div style="font-family:'Barlow Condensed',sans-serif;color:#fff;font-size:20px;font-weight:900;">YOUCEF BELAILI</div>
        <div style="color:#E70013;font-size:13px;">Esperance Tunis</div>
        <div style="color:#888;font-size:12px;margin-top:4px;">Ailier gauche · 34 ans</div>
        <div style="margin-top:10px;background:#00C853;color:#000;font-size:12px;font-weight:700;padding:6px 12px;border-radius:20px;display:inline-block;">7 QUESTIONS</div>
      </div>
    </div>
  </div>
  <!-- Vue quiz -->
  <div id="quiz-game-view" style="display:none;width:100%;max-width:700px;">
    <div id="quiz-panel"></div>
  </div>
</div>
'''
content = content.replace('</body>', quiz_page + '</body>')
# 3. Script quiz
quiz_script = '''
<script>
var quizData = {
  chaouat: {
    name: "FIRAS CHAOUAT",
    img: "https://static.flashscore.com/res/image/data/EL8CsfBr-2X9WEIyE.png",
    club: "Club Africain",
    questions: [
      { q: "Firas Chaouat joue au Club Africain ?", type:"tf", answer: true, diff:1 },
      { q: "Firas Chaouat est ne a Sfax ?", type:"tf", answer: true, diff:1 },
      { q: "Firas Chaouat est un gardien de but ?", type:"tf", answer: false, diff:1 },
      { q: "Combien de buts a marque Firas Chaouat en Ligue 1 2025/2026 ?", type:"number", answer: 14, diff:2 },
      { q: "Firas Chaouat a joue en Arabie Saoudite ?", type:"tf", answer: true, diff:2 },
      { q: "Combien de selections internationales a Firas Chaouat ?", type:"number", answer: 26, diff:3 },
      { q: "Quelle est la valeur marchande de Firas Chaouat en millions d euros ? (ex: 1.2)", type:"number", answer: 1.2, diff:3 }
    ]
  },
  belaili: {
    name: "YOUCEF BELAILI",
    img: "https://static.flashscore.com/res/image/data/6V5W3QyS-YDy6iaVc.png",
    club: "Esperance Tunis",
    questions: [
      { q: "Youcef Belaili est algerien ?", type:"tf", answer: true, diff:1 },
      { q: "Belaili a joue en Ligue 1 francaise ?", type:"tf", answer: true, diff:1 },
      { q: "Belaili joue au poste de gardien ?", type:"tf", answer: false, diff:1 },
      { q: "En quelle annee Belaili est ne ?", type:"number", answer: 1992, diff:2 },
      { q: "Belaili a remporte la CAN avec l Algerie ?", type:"tf", answer: true, diff:2 },
      { q: "Combien de buts en carriere internationale avec l Algerie ?", type:"number", answer: 10, diff:3 },
      { q: "Combien de fois Belaili a joue a l Esperance Tunis ? (nombre de passages)", type:"number", answer: 3, diff:3 }
    ]
  }
};
var quizCurrent = null;
var quizStep = 0;
var quizScore = 0;
function startQuiz(player) {
  quizCurrent = quizData[player];
  quizStep = 0;
  quizScore = 0;
  document.getElementById('quiz-list-view').style.display = 'none';
  document.getElementById('quiz-game-view').style.display = 'block';
  renderQuiz();
}
function renderQuiz() {
  var q = quizCurrent.questions[quizStep];
  var diff = q.diff === 1 ? '🟢 FACILE' : q.diff === 2 ? '🟡 MOYEN' : '🔴 DIFFICILE';
  var panel = document.getElementById('quiz-panel');
  var html = "<div style='display:flex;align-items:center;gap:16px;background:#111;border-radius:16px;padding:16px;margin-bottom:20px;'>";
  html += "<img src='"+quizCurrent.img+"' style='width:70px;height:88px;object-fit:cover;border-radius:10px;'>";
  html += "<div><div style='font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:24px;font-weight:900;'>"+quizCurrent.name+"</div>";
  html += "<div style='color:#E70013;font-size:13px;'>"+quizCurrent.club+"</div></div></div>";
  html += "<div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;'>";
  html += "<div style='color:#888;font-size:12px;font-weight:700;'>QUESTION "+(quizStep+1)+" / 7</div>";
  html += "<div style='font-size:12px;font-weight:700;'>"+diff+"</div></div>";
  // Barre progression
  var pct = Math.round((quizStep/7)*100);
  html += "<div style='width:100%;height:6px;background:#333;border-radius:4px;margin-bottom:20px;'>";
  html += "<div style='width:"+pct+"%;height:6px;background:linear-gradient(90deg,#00C853,#FFD700);border-radius:4px;transition:width 0.4s;'></div></div>";
  html += "<div style='background:#111;border:1px solid #333;border-radius:16px;padding:24px;margin-bottom:20px;'>";
  html += "<div style='font-family:Barlow Condensed,sans-serif;color:#fff;font-size:22px;font-weight:700;line-height:1.3;margin-bottom:20px;'>"+q.q+"</div>";
  if(q.type === 'tf') {
    html += "<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;'>";
    html += "<button onclick='checkAnswer(true)' style='padding:16px;background:#1a1a1a;border:2px solid #333;color:#fff;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:20px;font-weight:700;cursor:pointer;transition:all 0.2s;' onmouseover=\"this.style.borderColor='#00C853'\" onmouseout=\"this.style.borderColor='#333'\">✅ VRAI</button>";
    html += "<button onclick='checkAnswer(false)' style='padding:16px;background:#1a1a1a;border:2px solid #333;color:#fff;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:20px;font-weight:700;cursor:pointer;transition:all 0.2s;' onmouseover=\"this.style.borderColor='#E70013'\" onmouseout=\"this.style.borderColor='#333'\">❌ FAUX</button>";
    html += "</div>";
  } else {
    html += "<input type='number' id='quiz-input' placeholder='Entrez un nombre...' style='width:100%;box-sizing:border-box;padding:14px;background:#0a0a0a;border:2px solid #333;color:#fff;border-radius:12px;font-size:18px;font-family:Barlow Condensed,sans-serif;outline:none;'>";
    html += "<button onclick='checkNumberAnswer()' style='width:100%;margin-top:12px;padding:14px;background:#00C853;border:none;color:#000;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:18px;font-weight:900;cursor:pointer;letter-spacing:2px;'>CONFIRMER</button>";
  }
  html += "</div>";
  html += "<div style='color:#888;font-size:13px;text-align:center;'>Score: "+quizScore+" / "+quizStep+"</div>";
  panel.innerHTML = html;
}
function checkAnswer(userAnswer) {
  var q = quizCurrent.questions[quizStep];
  var correct = userAnswer === q.answer;
  showResult(correct, q.answer);
}
function checkNumberAnswer() {
  var input = document.getElementById('quiz-input');
  var val = parseFloat(input.value);
  var q = quizCurrent.questions[quizStep];
  var correct = val == q.answer;
  showResult(correct, q.answer);
}
function showResult(correct, answer) {
  if(correct) quizScore++;
  var panel = document.getElementById('quiz-panel');
  var msg = correct
    ? "<div style='background:rgba(0,200,83,0.15);border:2px solid #00C853;border-radius:12px;padding:20px;text-align:center;margin-bottom:16px;'><div style='font-size:36px;'>✅</div><div style='font-family:Barlow Condensed,sans-serif;color:#00C853;font-size:24px;font-weight:900;'>BONNE REPONSE !</div></div>"
    : "<div style='background:rgba(231,0,19,0.15);border:2px solid #E70013;border-radius:12px;padding:20px;text-align:center;margin-bottom:16px;'><div style='font-size:36px;'>❌</div><div style='font-family:Barlow Condensed,sans-serif;color:#E70013;font-size:24px;font-weight:900;'>MAUVAISE REPONSE</div><div style='color:#aaa;font-size:14px;margin-top:4px;'>Reponse correcte: <b style='color:#FFD700;'>"+answer+"</b></div></div>";
  quizStep++;
  if(quizStep < 7) {
    panel.innerHTML = msg + "<button onclick='renderQuiz()' style='width:100%;padding:14px;background:#FFD700;border:none;color:#000;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:18px;font-weight:900;cursor:pointer;'>QUESTION SUIVANTE &#8594;</button>";
  } else {
    showFinalScore(msg);
  }
}
function showFinalScore(lastMsg) {
  var pct = Math.round((quizScore/7)*100);
  var medal = pct >= 85 ? "🥇" : pct >= 57 ? "🥈" : "🥉";
  var comment = pct >= 85 ? "Expert !" : pct >= 57 ? "Bon niveau !" : "Encore des efforts !";
  var panel = document.getElementById('quiz-panel');
  var html = lastMsg;
  html += "<div style='background:#111;border:2px solid #FFD700;border-radius:16px;padding:24px;text-align:center;margin-bottom:16px;'>";
  html += "<div style='font-size:48px;margin-bottom:8px;'>"+medal+"</div>";
  html += "<div style='font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:36px;font-weight:900;'>"+quizScore+" / 7</div>";
  html += "<div style='color:#aaa;font-size:16px;margin-top:4px;'>"+comment+"</div>";
  html += "<div style='width:100%;height:10px;background:#333;border-radius:6px;margin:16px 0;'><div style='width:"+pct+"%;height:10px;background:linear-gradient(90deg,#E70013,#FFD700);border-radius:6px;'></div></div>";
  html += "</div>";
  html += "<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;'>";
  html += "<button onclick='startQuiz(quizCurrent===quizData.chaouat?\"chaouat\":\"belaili\")' style='padding:14px;background:#00C853;border:none;color:#000;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:900;cursor:pointer;'>&#8635; REJOUER</button>";
  html += "<button onclick='backToList()' style='padding:14px;background:transparent;border:2px solid #FFD700;color:#FFD700;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:900;cursor:pointer;'>&#8592; LISTE</button>";
  html += "</div>";
  panel.innerHTML = html;
}
function backToList() {
  document.getElementById('quiz-list-view').style.display = 'block';
  document.getElementById('quiz-game-view').style.display = 'none';
}
</script>
'''
content = content.replace('</body>', quiz_script + '</body>')
# 4. Ajouter page-quiz dans showPage
old_show = "var pages = ['home','bestxi','tierlist','tunisia'];"
new_show = "var pages = ['home','bestxi','tierlist','tunisia','quiz'];"
content = content.replace(old_show, new_show)
open('index.html','w',encoding='utf-8').write(content)
print('OK - Quiz ajoute !')
