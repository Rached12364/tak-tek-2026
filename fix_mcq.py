content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''  } else {
    html += "<div style=\\"text-align:center;\\">";
    html += "<input id=\\"quiz-number-input\\" type=\\"number\\" style=\\"font-size:28px;padding:14px;border-radius:12px;border:2px solid #00C853;background:#111;color:#fff;text-align:center;width:180px;\\">";
    html += "<br><br><button onclick=\\"submitNumber()\\" style=\\"background:linear-gradient(135deg,#00C853,#00a843);color:#000;font-size:18px;font-weight:900;padding:14px 40px;border:none;border-radius:12px;cursor:pointer;letter-spacing:2px;\\">CONFIRMER</button>";
    html += "</div>";
  }''',
    '''  } else if (q.type === "mcq") {
    html += "<div style=\\"display:flex;flex-direction:column;gap:14px;\\">";
    q.choices.forEach(function(choice) {
      var isCorrect = choice === q.answer;
      html += "<button onclick=\\"answerQuiz(" + isCorrect + ")\\" style=\\"background:rgba(255,255,255,0.08);color:#fff;font-size:20px;font-weight:700;padding:16px 0;border:2px solid rgba(255,255,255,0.15);border-radius:14px;cursor:pointer;transition:all 0.2s;letter-spacing:1px;\\" onmouseover=\\"this.style.background='rgba(0,200,83,0.2)';this.style.borderColor='#00C853';\\" onmouseout=\\"this.style.background='rgba(255,255,255,0.08)';this.style.borderColor='rgba(255,255,255,0.15)';\\">  " + choice + "</button>";
    });
    html += "</div>";
  } else {
    html += "<div style=\\"text-align:center;\\">";
    html += "<input id=\\"quiz-number-input\\" type=\\"number\\" style=\\"font-size:28px;padding:14px;border-radius:12px;border:2px solid #00C853;background:#111;color:#fff;text-align:center;width:180px;\\">";
    html += "<br><br><button onclick=\\"submitNumber()\\" style=\\"background:linear-gradient(135deg,#00C853,#00a843);color:#000;font-size:18px;font-weight:900;padding:14px 40px;border:none;border-radius:12px;cursor:pointer;letter-spacing:2px;\\">CONFIRMER</button>";
    html += "</div>";
  }'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
