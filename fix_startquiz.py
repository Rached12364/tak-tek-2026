content = open('index.html','r',encoding='utf-8').read()
old = '''function startQuiz(player) {
  quizCurrent = quizData[player];
  quizScore = 0;
  quizIndex = 0;
  showPage("quiz");
  renderQuizQuestion();
}'''
new = '''function startQuiz(player) {
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
}'''
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
