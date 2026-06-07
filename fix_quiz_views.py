content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '  <!-- Liste joueurs -->',
    '''  <!-- Vue question -->
  <div id="quiz-question-view" style="display:none;width:100%;max-width:600px;text-align:center;padding:20px;">
    <div id="quiz-progress" style="color:#888;font-size:13px;margin-bottom:8px;">Question 1 / 7</div>
    <div id="quiz-score-display" style="color:#00C853;font-size:15px;font-weight:700;margin-bottom:20px;">Score: 0</div>
    <div id="quiz-question-container"></div>
  </div>
  <!-- Liste joueurs -->'''
)
content = content.replace(
    '''function startQuiz(player) {
  quizCurrent = quizData[player];
  quizScore = 0;
  quizIndex = 0;
  showPage("quiz");
  renderQuizQuestion();
}''',
    '''function startQuiz(player) {
  quizCurrent = quizData[player];
  quizScore = 0;
  quizIndex = 0;
  showPage("quiz");
  setTimeout(function(){
    document.getElementById("quiz-list-view").style.display = "none";
    document.getElementById("quiz-question-view").style.display = "block";
    renderQuizQuestion();
  }, 50);
}'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
