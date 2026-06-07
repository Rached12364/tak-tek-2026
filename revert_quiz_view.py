content = open('index.html','r',encoding='utf-8').read()
# Supprimer la vue question ajoutee
content = content.replace(
    '''  <!-- Vue question -->
  <div id="quiz-question-view" style="display:none;width:100%;max-width:600px;text-align:center;">
    <div id="quiz-progress" style="color:#888;font-size:13px;margin-bottom:8px;">Question 1 / 7</div>
    <div id="quiz-score-display" style="color:#00C853;font-size:15px;font-weight:700;margin-bottom:20px;">Score: 0</div>
    <div id="quiz-question-container"></div>
    <button onclick="showPage('quiz-list')" style="margin-top:20px;background:transparent;border:1px solid #444;color:#888;padding:8px 20px;border-radius:8px;cursor:pointer;font-size:13px;">ABANDONNER</button>
  </div>
  <!-- Liste joueurs -->
  <div id="quiz-list-view"''',
    '''  <!-- Liste joueurs -->
  <div id="quiz-list-view"'''
)
# Supprimer le showPage quiz-list ajoute
content = content.replace(
    '''function startQuiz(player) {
  quizCurrent = quizData[player];
  quizScore = 0;
  quizIndex = 0;
  document.getElementById("quiz-list-view").style.display = "none";
  document.getElementById("quiz-question-view").style.display = "block";
  renderQuizQuestion();
}
function showPage(page) {
  if(page === "quiz-list") {
    document.getElementById("quiz-list-view").style.display = "block";
    document.getElementById("quiz-question-view").style.display = "none";
    return;
  }
}''',
    '''function startQuiz(player) {
  quizCurrent = quizData[player];
  quizScore = 0;
  quizIndex = 0;
  showPage("quiz");
  renderQuizQuestion();
}'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
