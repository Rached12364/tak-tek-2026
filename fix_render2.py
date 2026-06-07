content = open('index.html','r',encoding='utf-8').read()
old = '''function renderQuizQuestion() {
  var q = quizCurrent.questions[quizIndex];
  document.getElementById("quiz-list-view").style.display = "none";
  document.getElementById("quiz-question-view").style.display = "block";
  var container = document.getElementById("quiz-question-container");
  var html = "<div style=\\"text-align:center;padding:20px;\\">";
  html += "<img src=\\"" + quizCurrent.img + "\\" style=\\"width:100px;height:120px;object-fit:cover;border-radius:10px;margin-bottom:12px;\\">";
  html += "<div style=\\"color:#fff;font-size:22px;font-weight:900;margin-bottom:20px;\\">" + quizCurrent.name + "</div>";
  html += "<div style=\\"color:#ccc;font-size:16px;margin-bottom:24px;padding:0 20px;\\">" + q.q + "</div>";
  if (q.type === "tf") {
    html += "<div style=\\"display:flex;gap:20px;justify-content:center;\\">";
    html += "<button onclick=\\"answerQuiz(true)\\" style=\\"background:#00C853;color:#000;font-size:18px;font-weight:900;padding:14px 32px;border:none;border-radius:12px;cursor:pointer;\\">VRAI</button>";
    html += "<button onclick=\\"answerQuiz(false)\\" style=\\"background:#E70013;color:#fff;font-size:18px;font-weight:900;padding:14px 32px;border:none;border-radius:12px;cursor:pointer;\\">FAUX</button>";
    html += "</div>";
  } else {
    html += "<input id=\\"quiz-number-input\\" type=\\"number\\" style=\\"font-size:22px;padding:10px;border-radius:8px;border:2px solid #00C853;background:#111;color:#fff;text-align:center;width:150px;\\">";
    html += "<br><br><button onclick=\\"submitNumber()\\" style=\\"background:#00C853;color:#000;font-size:16px;font-weight:900;padding:12px 28px;border:none;border-radius:10px;cursor:pointer;\\">CONFIRMER</button>";
  }
  html += "</div>";
  container.innerHTML = html;
  document.getElementById("quiz-progress").textContent = "Question " + (quizIndex+1) + " / " + quizCurrent.questions.length;
  document.getElementById("quiz-score-display").textContent = "Score: " + quizScore;
}'''
new = '''var quizTimer = null;
var quizTimeLeft = 7;
function startCountdown() {
  if (quizTimer) clearInterval(quizTimer);
  quizTimeLeft = 7;
  var el = document.getElementById("quiz-countdown");
  if (el) { el.textContent = quizTimeLeft; el.style.borderColor="#00C853"; el.style.color="#00C853"; }
  quizTimer = setInterval(function(){
    quizTimeLeft--;
    var el = document.getElementById("quiz-countdown");
    if (el) {
      el.textContent = quizTimeLeft;
      el.style.animation = "countdown-pulse 0.5s ease";
      setTimeout(function(){ if(el) el.style.animation=""; }, 500);
      if (quizTimeLeft <= 3) { el.style.borderColor="#E70013"; el.style.color="#E70013"; }
    }
    if (quizTimeLeft <= 0) {
      clearInterval(quizTimer);
      answerQuiz(null);
    }
  }, 1000);
}
function renderQuizQuestion() {
  var q = quizCurrent.questions[quizIndex];
  document.getElementById("quiz-list-view").style.display = "none";
  document.getElementById("quiz-question-view").style.display = "block";
  // Carte joueur gauche
  var cardDiv = document.getElementById("quiz-player-card-display");
  cardDiv.innerHTML = "<img src=\\"" + quizCurrent.img + "\\" style=\\"width:260px;height:320px;object-fit:contain;border-radius:16px;box-shadow:0 0 40px rgba(0,200,83,0.3);\\">" +
    "<div style=\\"color:#fff;font-family:Barlow Condensed,sans-serif;font-size:26px;font-weight:900;margin-top:16px;\\">" + quizCurrent.name + "</div>" +
    "<div style=\\"color:#E70013;font-size:14px;margin-top:4px;\\">" + quizCurrent.club + "</div>";
  cardDiv.style.animation = "slideInLeft 0.5s ease";
  // Question droite
  var container = document.getElementById("quiz-question-container");
  var html = "<div style=\\"animation:slideInRight 0.5s ease;\\">";
  html += "<div style=\\"color:#FFD700;font-size:13px;font-weight:700;letter-spacing:3px;margin-bottom:16px;\\">QUESTION " + (quizIndex+1) + " / " + quizCurrent.questions.length + "</div>";
  html += "<div style=\\"color:#fff;font-size:24px;font-weight:700;line-height:1.4;margin-bottom:36px;padding:24px;background:rgba(255,255,255,0.05);border-radius:16px;border:1px solid rgba(255,255,255,0.1);\\">" + q.q + "</div>";
  if (q.type === "tf") {
    html += "<div style=\\"display:flex;gap:16px;justify-content:center;\\">";
    html += "<button onclick=\\"answerQuiz(true)\\" style=\\"flex:1;background:linear-gradient(135deg,#00C853,#00a843);color:#000;font-size:20px;font-weight:900;padding:18px 0;border:none;border-radius:14px;cursor:pointer;letter-spacing:2px;transition:transform 0.1s;\\" onmouseover=\\"this.style.transform='scale(1.05)'\\" onmouseout=\\"this.style.transform='scale(1)'\\">✓ VRAI</button>";
    html += "<button onclick=\\"answerQuiz(false)\\" style=\\"flex:1;background:linear-gradient(135deg,#E70013,#b50010);color:#fff;font-size:20px;font-weight:900;padding:18px 0;border:none;border-radius:14px;cursor:pointer;letter-spacing:2px;transition:transform 0.1s;\\" onmouseover=\\"this.style.transform='scale(1.05)'\\" onmouseout=\\"this.style.transform='scale(1)'\\">✗ FAUX</button>";
    html += "</div>";
  } else {
    html += "<div style=\\"text-align:center;\\">";
    html += "<input id=\\"quiz-number-input\\" type=\\"number\\" style=\\"font-size:28px;padding:14px;border-radius:12px;border:2px solid #00C853;background:#111;color:#fff;text-align:center;width:180px;\\">";
    html += "<br><br><button onclick=\\"submitNumber()\\" style=\\"background:linear-gradient(135deg,#00C853,#00a843);color:#000;font-size:18px;font-weight:900;padding:14px 40px;border:none;border-radius:12px;cursor:pointer;letter-spacing:2px;\\">CONFIRMER</button>";
    html += "</div>";
  }
  html += "</div>";
  container.innerHTML = html;
  document.getElementById("quiz-progress").textContent = "Question " + (quizIndex+1) + " / " + quizCurrent.questions.length;
  document.getElementById("quiz-score-display").textContent = "Score: " + quizScore;
  startCountdown();
}'''
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
