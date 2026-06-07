content = open('index.html','r',encoding='utf-8').read()
quiz_script = '''
<script>
var quizData = {
  chaouat: {
    name: "FIRAS CHAOUAT",
    img: "https://static.flashscore.com/res/image/data/EL8CsfBr-2X9WEIyE.png",
    club: "Club Africain",
    questions: [
      { q: "Chaouat a joue pour l Esperance de Tunis ?", type:"tf", answer: false, diff:3 },
      { q: "Chaouat joue au poste d avant-centre ?", type:"tf", answer: true, diff:3 },
      { q: "Chaouat est ne en Tunisie ?", type:"tf", answer: true, diff:3 },
      { q: "Chaouat a represente la Tunisie en selection nationale ?", type:"tf", answer: true, diff:3 },
      { q: "Chaouat joue au Club Africain ?", type:"tf", answer: true, diff:3 },
      { q: "Chaouat a marque plus de 10 buts en championnat ?", type:"tf", answer: true, diff:3 },
      { q: "Chaouat a 30 ans ?", type:"tf", answer: true, diff:3 }
    ]
  },
  belaili: {
    name: "YOUCEF BELAILI",
    img: "https://static.flashscore.com/res/image/data/6V5W3QyS-YDy6iaVc.png",
    club: "Esperance Tunis",
    questions: [
      { q: "Belaili est Algerien ?", type:"tf", answer: true, diff:3 },
      { q: "Belaili a joue en Qatar ?", type:"tf", answer: true, diff:3 },
      { q: "Belaili a joue pour le Brest en Ligue 1 ?", type:"tf", answer: true, diff:3 },
      { q: "Belaili a marque contre l Allemagne en Coupe du Monde 2022 ?", type:"tf", answer: false, diff:3 },
      { q: "Belaili joue comme ailier gauche ?", type:"tf", answer: true, diff:3 },
      { q: "Belaili a plus de 50 selections avec l Algerie ?", type:"tf", answer: true, diff:3 },
      { q: "Belaili a 34 ans ?", type:"tf", answer: true, diff:3 }
    ]
  },
  msakni: {
    name: "YOUSSEF MSAKNI",
    img: "https://static.flashscore.com/res/image/data/OCwL77FG-4WhOr90b.png",
    club: "Esperance Tunis",
    questions: [
      { q: "Msakni a joue au Qatar pendant plus de 10 ans ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de buts Msakni a marque avec la Tunisie ?", type:"number", answer: 23, diff:3 },
      { q: "Msakni a joue en Belgique a KAS Eupen ?", type:"tf", answer: true, diff:3 },
      { q: "Msakni a marque un triple contre la Guinee en 2017 ?", type:"tf", answer: true, diff:3 },
      { q: "Msakni a remporte le CHAN avec la Tunisie en 2011 ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de selections officielles Msakni a avec la Tunisie ?", type:"number", answer: 104, diff:3 },
      { q: "Msakni a remporte la CAN avec la Tunisie ?", type:"tf", answer: false, diff:3 }
    ]
  },
  aouani: {
    name: "RAKI AOUANI",
    img: "https://static.flashscore.com/res/image/data/YNOJHqwS-ltYaYaBP.png",
    club: "Etoile du Sahel",
    questions: [
      { q: "Raki Aouani est ne en 2004 ?", type:"tf", answer: true, diff:3 },
      { q: "Aouani a signe pour Riga FC en Lettonie en 2026 ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de buts Aouani a marque avec Etoile du Sahel ?", type:"number", answer: 12, diff:3 },
      { q: "Aouani joue au poste de gardien de but ?", type:"tf", answer: false, diff:3 },
      { q: "Combien de matchs Aouani a joue avec Etoile du Sahel ?", type:"number", answer: 103, diff:3 },
      { q: "Aouani a represente la Tunisie U20 ?", type:"tf", answer: true, diff:3 },
      { q: "Aouani mesure 1.79m ?", type:"tf", answer: true, diff:3 }
    ]
  },
  benzarti: {
    name: "FAOUZI BENZARTI",
    img: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Faouzi_Benzarti_au_Raja_%28cropped%29.jpg/960px-Faouzi_Benzarti_au_Raja_%28cropped%29.jpg",
    club: "Club Africain",
    questions: [
      { q: "Benzarti est ne a Monastir ?", type:"tf", answer: true, diff:3 },
      { q: "Benzarti a mene le Raja en finale du Mondial des clubs ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de fois Benzarti a ete selectionneur de la Tunisie ?", type:"number", answer: 3, diff:3 },
      { q: "Benzarti a remporte la Ligue des champions CAF comme entraineur ?", type:"tf", answer: true, diff:3 },
      { q: "En quelle annee Benzarti est ne ?", type:"number", answer: 1950, diff:3 },
      { q: "Benzarti a entraine le Wydad de Casablanca ?", type:"tf", answer: true, diff:3 },
      { q: "Benzarti est classe 9e meilleur entraineur africain de tous les temps ?", type:"tf", answer: true, diff:3 }
    ]
  }
};
var quizCurrent = null;
var quizScore = 0;
var quizIndex = 0;
function startQuiz(player) {
  quizCurrent = quizData[player];
  quizScore = 0;
  quizIndex = 0;
  showPage("quiz");
  renderQuizQuestion();
}
function renderQuizQuestion() {
  var q = quizCurrent.questions[quizIndex];
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
}
function answerQuiz(answer) {
  var q = quizCurrent.questions[quizIndex];
  if (answer === q.answer) quizScore++;
  quizIndex++;
  if (quizIndex < quizCurrent.questions.length) {
    renderQuizQuestion();
  } else {
    showQuizResult();
  }
}
function submitNumber() {
  var val = parseInt(document.getElementById("quiz-number-input").value);
  var q = quizCurrent.questions[quizIndex];
  if (val === q.answer) quizScore++;
  quizIndex++;
  if (quizIndex < quizCurrent.questions.length) {
    renderQuizQuestion();
  } else {
    showQuizResult();
  }
}
function showQuizResult() {
  var container = document.getElementById("quiz-question-container");
  var total = quizCurrent.questions.length;
  var pct = Math.round((quizScore/total)*100);
  var msg = pct >= 80 ? "EXCELLENT !" : pct >= 50 ? "PAS MAL !" : "A RETRAVAILLER !";
  container.innerHTML = "<div style=\\"text-align:center;padding:30px;\\">" +
    "<div style=\\"font-size:60px;margin-bottom:10px;\\">" + (pct>=80?"🏆":pct>=50?"⭐":"💪") + "</div>" +
    "<div style=\\"color:#00C853;font-size:36px;font-weight:900;\\">" + msg + "</div>" +
    "<div style=\\"color:#fff;font-size:24px;margin:16px 0;\\">" + quizScore + " / " + total + "</div>" +
    "<button onclick=\\"showPage('quiz-list')\\" style=\\"background:#00C853;color:#000;font-size:16px;font-weight:900;padding:12px 28px;border:none;border-radius:10px;cursor:pointer;margin-top:10px;\\">RETOUR</button>" +
    "</div>";
  document.getElementById("quiz-progress").textContent = "Termine !";
  document.getElementById("quiz-score-display").textContent = "Score final: " + quizScore + "/" + total;
}
</script>
'''
content = content.replace('</body>', quiz_script + '</body>')
open('index.html','w',encoding='utf-8').write(content)
print('OK')
