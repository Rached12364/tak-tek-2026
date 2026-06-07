content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''document.getElementById(\\'quiz-question-view\\').style.display=\\'none\\';document.getElementById(\\'quiz-list-view\\').style.display=\\'block\\';''',
    '''document.getElementById('quiz-question-view').style.display='none';document.getElementById('quiz-list-view').style.display='block';'''
)
# Fix aussi le bouton retour dans showQuizResult
content = content.replace(
    "showPage(\\'quiz-list\\')",
    "document.getElementById('quiz-question-view').style.display='none';document.getElementById('quiz-list-view').style.display='block';"
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
