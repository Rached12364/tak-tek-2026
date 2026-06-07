content = open('index.html','r',encoding='utf-8').read()
quiz_css = '''
@keyframes quiz-fadein {
  from { opacity:0; transform:translateY(20px); }
  to   { opacity:1; transform:translateY(0); }
}
@keyframes quiz-pop {
  0%   { transform:scale(0.8); opacity:0; }
  70%  { transform:scale(1.05); }
  100% { transform:scale(1); opacity:1; }
}
@keyframes quiz-shake {
  0%,100% { transform:translateX(0); }
  20%     { transform:translateX(-8px); }
  40%     { transform:translateX(8px); }
  60%     { transform:translateX(-6px); }
  80%     { transform:translateX(6px); }
}
@keyframes quiz-correct {
  0%   { box-shadow:0 0 0px #00C853; }
  50%  { box-shadow:0 0 30px #00C853, 0 0 60px rgba(0,200,83,0.4); }
  100% { box-shadow:0 0 0px #00C853; }
}
@keyframes quiz-card-hover {
  from { transform:translateY(0); box-shadow:none; }
  to   { transform:translateY(-6px); box-shadow:0 8px 30px rgba(0,200,83,0.3); }
}
#quiz-list-view { animation: quiz-fadein 0.5s ease both; }
#quiz-panel { animation: quiz-fadein 0.4s ease both; }
.quiz-player-card {
  background:#111;
  border:2px solid #333;
  border-radius:16px;
  padding:20px;
  text-align:center;
  cursor:pointer;
  transition:all 0.3s ease;
  position:relative;
  z-index:1;
}
.quiz-player-card:hover {
  border-color:#00C853;
  transform:translateY(-6px);
  box-shadow:0 8px 30px rgba(0,200,83,0.3);
}
.quiz-btn-vrai {
  padding:16px;
  background:#1a3a1a;
  border:2px solid #00C853;
  color:#fff;
  border-radius:12px;
  font-family:Barlow Condensed,sans-serif;
  font-size:20px;
  font-weight:700;
  cursor:pointer;
  transition:all 0.2s;
  width:100%;
}
.quiz-btn-vrai:hover { background:#00C853; color:#000; transform:scale(1.03); }
.quiz-btn-faux {
  padding:16px;
  background:#3a1a1a;
  border:2px solid #E70013;
  color:#fff;
  border-radius:12px;
  font-family:Barlow Condensed,sans-serif;
  font-size:20px;
  font-weight:700;
  cursor:pointer;
  transition:all 0.2s;
  width:100%;
}
.quiz-btn-faux:hover { background:#E70013; color:#fff; transform:scale(1.03); }
.quiz-correct-anim { animation: quiz-correct 0.6s ease; }
.quiz-wrong-anim { animation: quiz-shake 0.5s ease; }
'''
if 'quiz-fadein' not in content:
    content = content.replace('</style>', quiz_css + '</style>')
# Remplacer les boutons VRAI/FAUX par des classes CSS
content = content.replace(
    "html += \"<button onclick='checkAnswer(true)' style='padding:16px;background:#1a3a1a;border:2px solid #00C853;color:#fff;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:20px;font-weight:700;cursor:pointer;'>VRAI</button>\";",
    "html += \"<button onclick='checkAnswer(true)' class='quiz-btn-vrai'>VRAI</button>\";"
)
content = content.replace(
    "html += \"<button onclick='checkAnswer(false)' style='padding:16px;background:#3a1a1a;border:2px solid #E70013;color:#fff;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:20px;font-weight:700;cursor:pointer;'>FAUX</button>\";",
    "html += \"<button onclick='checkAnswer(false)' class='quiz-btn-faux'>FAUX</button>\";"
)
# Remplacer les cartes joueurs par classe CSS
content = content.replace(
    '<div onclick="startQuiz(\'chaouat\')" style="background:#111;border:2px solid #333;border-radius:16px;padding:20px;text-align:center;cursor:pointer;transition:all 0.3s;position:relative;z-index:1;">',
    '<div onclick="startQuiz(\'chaouat\')" class="quiz-player-card">'
)
content = content.replace(
    '<div onclick="startQuiz(\'belaili\')" style="background:#111;border:2px solid #333;border-radius:16px;padding:20px;text-align:center;cursor:pointer;transition:all 0.3s;position:relative;z-index:1;">',
    '<div onclick="startQuiz(\'belaili\')" class="quiz-player-card">'
)
# Ajouter animation shake/correct sur le panel apres reponse
old_show_result = '''function showQuizResult(correct, answer) {
  if(correct) quizScore++;'''
new_show_result = '''function showQuizResult(correct, answer) {
  if(correct) quizScore++;
  var panel = document.getElementById("quiz-panel");
  if(panel) {
    panel.style.animation = "none";
    setTimeout(function(){
      panel.style.animation = correct ? "quiz-correct 0.6s ease" : "quiz-shake 0.5s ease";
    }, 10);
  }'''
content = content.replace(old_show_result, new_show_result)
open('index.html','w',encoding='utf-8').write(content)
print('OK - animations quiz ajoutees')
