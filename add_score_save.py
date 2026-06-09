content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'document.getElementById("quiz-progress").textContent = "Termine !";',
    '''document.getElementById("quiz-progress").textContent = "Termine !";
  saveQuizScore(quizCurrent.name, quizScore, total);'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
