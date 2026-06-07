content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''function startQuiz(player) {
  quizCurrent = quizData[player];
  quizScore = 0;
  quizIndex = 0;
  showPage("quiz");
  setTimeout(function(){
    document.getElementById("quiz-list-view").style.display = "none";
    document.getElementById("quiz-question-view").style.display = "block";
    renderQuizQuestion();
  }, 200);
}''',
    '''function startQuiz(player) {
  quizCurrent = quizData[player];
  quizScore = 0;
  quizIndex = 0;
  showPage("quiz");
  document.getElementById("quiz-list-view").style.display = "none";
  document.getElementById("quiz-question-view").style.display = "block";
  renderQuizQuestion();
}'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
