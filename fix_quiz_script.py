content = open('index.html','r',encoding='utf-8').read()
# Trouver et supprimer l ancien script quiz
start = content.find('<script>\nvar quizData')
end = content.find('</script>', start) + len('</script>')
old_quiz_script = content[start:end]
new_quiz_script = '''<script>
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
      { q: "Quelle est la valeur marchande de Firas Chaouat en millions ? (ex: 1.2)", type:"number", answer: 1.2, diff:3 }
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
      { q: "Combien de passages de Belaili a l Esperance Tunis ?", type:"number", answer: 3, diff:3 }
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
  document.getElementById("quiz-list-view").style.display = "none";
  document.getElementById("quiz-game-view").style.display = "block";
  renderQuiz();
}
function renderQuiz() {
  var q = quizCurrent.questions[quizStep];
  var diff = q.diff === 1 ? "FACILE" : q.diff === 2 ? "MOYEN" : "DIFFICILE";
  var diffColor = q.diff === 1 ? "#00C853" : q.diff === 2 ? "#FFD700" : "#E70013";
  var pct = Math.round((quizStep/7)*100);
  var html = "";
  html += "<div style='display:flex;align-items:center;gap:16px;background:#111;border-radius:16px;padding:16px;margin-bottom:20px;'>";
  html += "<img src='" + quizCurrent.img + "' style='width:70px;height:88px;object-fit:cover;border-radius:10px;'>";
  html += "<div><div style='font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:24px;font-weight:900;'>" + quizCurrent.name + "</div>";
  html += "<div style='color:#E70013;font-size:13px;'>" + quizCurrent.club + "</div></div></div>";
  html += "<div style='display:flex;justify-content:space-between;margin-bottom:8px;'>";
  html += "<div style='color:#888;font-size:12px;font-weight:700;'>QUESTION " + (quizStep+1) + " / 7</div>";
  html += "<div style='color:" + diffColor + ";font-size:12px;font-weight:700;'>" + diff + "</div></div>";
  html += "<div style='width:100%;height:6px;background:#333;border-radius:4px;margin-bottom:20px;'>";
  html += "<div style='width:" + pct + "%;height:6px;background:linear-gradient(90deg,#00C853,#FFD700);border-radius:4px;'></div></div>";
  html += "<div style='background:#111;border:1px solid #333;border-radius:16px;padding:24px;margin-bottom:20px;'>";
  html += "<div style='font-family:Barlow Condensed,sans-serif;color:#fff;font-size:22px;font-weight:700;line-height:1.3;margin-bottom:20px;'>" + q.q + "</div>";
  if(q.type === "tf") {
    html += "<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;'>";
    html += "<button onclick='checkAnswer(true)' style='padding:16px;background:#1a3a1a;border:2px solid #00C853;color:#fff;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:20px;font-weight:700;cursor:pointer;'>VRAI</button>";
    html += "<button onclick='checkAnswer(false)' style='padding:16px;background:#3a1a1a;border:2px solid #E70013;color:#fff;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:20px;font-weight:700;cursor:pointer;'>FAUX</button>";
    html += "</div>";
  } else {
    html += "<input type='number' id='quiz-input' placeholder='Entrez un nombre...' style='width:100%;box-sizing:border-box;padding:14px;background:#0a0a0a;border:2px solid #333;color:#fff;border-radius:12px;font-size:18px;font-family:Barlow Condensed,sans-serif;outline:none;'>";
    html += "<button onclick='checkNumberAnswer()' style='width:100%;margin-top:12px;padding:14px;background:#00C853;border:none;color:#000;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:18px;font-weight:900;cursor:pointer;letter-spacing:2px;'>CONFIRMER</button>";
  }
  html += "</div>";
  html += "<div style='color:#888;font-size:13px;text-align:center;'>Score: " + quizScore + " / " + quizStep + "</div>";
  document.getElementById("quiz-panel").innerHTML = html;
}
function checkAnswer(userAnswer) {
  var q = quizCurrent.questions[quizStep];
  var correct = (userAnswer === q.answer);
  showQuizResult(correct, q.answer);
}
function checkNumberAnswer() {
  var input = document.getElementById("quiz-input");
  var val = parseFloat(input.value);
  var q = quizCurrent.questions[quizStep];
  var correct = (val == q.answer);
  showQuizResult(correct, q.answer);
}
function showQuizResult(correct, answer) {
  if(correct) quizScore++;
  var msg = correct
    ? "<div style='background:rgba(0,200,83,0.15);border:2px solid #00C853;border-radius:12px;padding:20px;text-align:center;margin-bottom:16px;'><div style='font-size:36px;'>BONNE REPONSE !</div><div style='font-family:Barlow Condensed,sans-serif;color:#00C853;font-size:24px;font-weight:900;'>+1 point</div></div>"
    : "<div style='background:rgba(231,0,19,0.15);border:2px solid #E70013;border-radius:12px;padding:20px;text-align:center;margin-bottom:16px;'><div style='font-size:20px;color:#E70013;font-weight:700;'>MAUVAISE REPONSE</div><div style='color:#aaa;font-size:14px;margin-top:4px;'>Reponse correcte: <b style=color:#FFD700;>" + answer + "</b></div></div>";
  quizStep++;
  var panel = document.getElementById("quiz-panel");
  if(quizStep < 7) {
    panel.innerHTML = msg + "<button onclick='renderQuiz()' style='width:100%;padding:14px;background:#FFD700;border:none;color:#000;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:18px;font-weight:900;cursor:pointer;'>QUESTION SUIVANTE</button>";
  } else {
    showFinalScore(msg);
  }
}
function showFinalScore(lastMsg) {
  var pct = Math.round((quizScore/7)*100);
  var medal = pct >= 85 ? "EXPERT" : pct >= 57 ? "BON NIVEAU" : "ENCORE DES EFFORTS";
  var panel = document.getElementById("quiz-panel");
  var html = lastMsg;
  html += "<div style='background:#111;border:2px solid #FFD700;border-radius:16px;padding:24px;text-align:center;margin-bottom:16px;'>";
  html += "<div style='font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:48px;font-weight:900;'>" + quizScore + " / 7</div>";
  html += "<div style='color:#aaa;font-size:16px;margin-top:4px;'>" + medal + "</div>";
  html += "<div style='width:100%;height:10px;background:#333;border-radius:6px;margin:16px 0;'><div style='width:" + pct + "%;height:10px;background:linear-gradient(90deg,#E70013,#FFD700);border-radius:6px;'></div></div>";
  html += "</div>";
  html += "<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;'>";
  var playerKey = (quizCurrent === quizData.chaouat) ? "chaouat" : "belaili";
  html += "<button onclick='startQuiz(\"" + playerKey + "\")' style='padding:14px;background:#00C853;border:none;color:#000;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:900;cursor:pointer;'>REJOUER</button>";
  html += "<button onclick='backToList()' style='padding:14px;background:transparent;border:2px solid #FFD700;color:#FFD700;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:900;cursor:pointer;'>LISTE</button>";
  html += "</div>";
  panel.innerHTML = html;
}
function backToList() {
  document.getElementById("quiz-list-view").style.display = "block";
  document.getElementById("quiz-game-view").style.display = "none";
}
</script>'''
content = content[:start] + new_quiz_script + content[end:]
open('index.html','w',encoding='utf-8').write(content)
print('OK')
