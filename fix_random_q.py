content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''function startQuiz(player) {
  quizCurrent = quizData[player];
  quizScore = 0;
  quizIndex = 0;
  showPage("quiz");
  document.getElementById("quiz-list-view").style.display = "none";
  document.getElementById("quiz-question-view").style.display = "block";
  renderQuizQuestion();
}''',
    '''function shuffleArray(arr) {
  var a = arr.slice();
  for (var i = a.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
  }
  return a;
}
function startQuiz(player) {
  var data = quizData[player];
  quizCurrent = {
    name: data.name,
    img: data.img,
    club: data.club,
    questions: shuffleArray(data.questions).slice(0, 10)
  };
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
