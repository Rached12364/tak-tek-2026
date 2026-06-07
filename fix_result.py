content = open('index.html','r',encoding='utf-8').read()
old = '''function showQuizResult() {
  var container = document.getElementById("quiz-question-container");
  var total = quizCurrent.questions.length;
  var pct = Math.round((quizScore/total)*100);
  var msg = pct >= 80 ? "EXCELLENT !" : pct >= 50 ? "PAS MAL !" : "A RETRAVAILLER !";
  container.innerHTML = "<div style=\\"text-align:center;padding:30px;\\">" +
    "<div style=\\"font-size:60px;margin-bottom:10px;\\">" + (pct>=80?"🏆":pct>=50?"⭐":"💪") + "</div>" +
    "<div style=\\"color:#00C853;font-size:36px;font-weight:900;\\">" + msg + "</div>" +
    "<div style=\\"color:#fff;font-size:24px;margin:16px 0;\\">" + quizScore + " / " + total + "</div>" +
    "<button onclick=\\"document.getElementById('quiz-question-view').style.display='none';document.getElementById('quiz-list-view').style.display='block';\\" style=\\"background:#00C853;color:#000;font-size:16px;font-weight:900;padding:12px 28px;border:none;border-radius:10px;cursor:pointer;margin-top:10px;\\">RETOUR</button>" +
    "</div>";
  document.getElementById("quiz-progress").textContent = "Termine !";
  document.getElementById("quiz-score-display").textContent = "Score final: " + quizScore + "/" + total;
}'''
new = '''function showQuizResult() {
  var container = document.getElementById("quiz-question-container");
  var cardDiv = document.getElementById("quiz-player-card-display");
  if (cardDiv) cardDiv.innerHTML = "";
  var total = quizCurrent.questions.length;
  var pct = Math.round((quizScore/total)*100);
  var msg = pct >= 80 ? "EXCELLENT !" : pct >= 50 ? "PAS MAL !" : "A RETRAVAILLER !";
  var color = pct >= 80 ? "#00C853" : pct >= 50 ? "#FFD700" : "#E70013";
  var emoji = pct>=80 ? "🏆" : pct>=50 ? "⭐" : "💪";
  var circumference = 2 * Math.PI * 70;
  var offset = circumference - (pct / 100) * circumference;
  container.innerHTML = "<div style=\\"text-align:center;padding:20px;\\">" +
    "<div style=\\"font-size:50px;margin-bottom:16px;\\">" + emoji + "</div>" +
    "<svg width=\\"180\\" height=\\"180\\" style=\\"margin:0 auto 20px;display:block;\\">" +
      "<circle cx=\\"90\\" cy=\\"90\\" r=\\"70\\" fill=\\"none\\" stroke=\\"rgba(255,255,255,0.1)\\" stroke-width=\\"12\\"/>" +
      "<circle cx=\\"90\\" cy=\\"90\\" r=\\"70\\" fill=\\"none\\" stroke=\\"" + color + "\\" stroke-width=\\"12\\" stroke-linecap=\\"round\\"" +
        " stroke-dasharray=\\"" + circumference + "\\" stroke-dashoffset=\\"" + offset + "\\" transform=\\"rotate(-90 90 90)\\"" +
        " style=\\"transition:stroke-dashoffset 1s ease;\\"/>" +
      "<text x=\\"90\\" y=\\"85\\" text-anchor=\\"middle\\" fill=\\"" + color + "\\" font-size=\\"32\\" font-weight=\\"900\\" font-family=\\"Barlow Condensed,sans-serif\\">" + pct + "%</text>" +
      "<text x=\\"90\\" y=\\"112\\" text-anchor=\\"middle\\" fill=\\"#fff\\" font-size=\\"14\\" font-family=\\"Barlow Condensed,sans-serif\\">" + quizScore + " / " + total + "</text>" +
    "</svg>" +
    "<div style=\\"color:" + color + ";font-size:32px;font-weight:900;letter-spacing:2px;margin-bottom:24px;\\">" + msg + "</div>" +
    "<button onclick=\\"document.getElementById('quiz-question-view').style.display='none';document.getElementById('quiz-list-view').style.display='block';\\" style=\\"background:" + color + ";color:#000;font-size:16px;font-weight:900;padding:14px 40px;border:none;border-radius:30px;cursor:pointer;letter-spacing:2px;\\">RETOUR</button>" +
    "</div>";
  document.getElementById("quiz-progress").textContent = "Termine !";
  document.getElementById("quiz-score-display").textContent = "Score final: " + quizScore + "/" + total;
}'''
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
