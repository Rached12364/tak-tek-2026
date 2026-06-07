content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''function renderQuizQuestion() {
  var q = quizCurrent.questions[quizIndex];
  var container = document.getElementById("quiz-question-container");''',
    '''function renderQuizQuestion() {
  var q = quizCurrent.questions[quizIndex];
  document.getElementById("quiz-list-view").style.display = "none";
  document.getElementById("quiz-question-view").style.display = "block";
  var container = document.getElementById("quiz-question-container");'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
