content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'background:url(backround.jpg) center/cover no-repeat fixed',
    'background:url(backround.jpg) center/cover no-repeat fixed;position:relative;'
)
# Ajouter overlay sombre apres l ouverture de page-quiz
content = content.replace(
    'id="page-quiz"',
    'id="page-quiz" data-has-overlay="true"'
)
# Ajouter pseudo-overlay via un div au debut de page-quiz
content = content.replace(
    'data-has-overlay="true" style="',
    'style="'
)
content = content.replace(
    '''  <!-- Vue question -->''',
    '''  <div style="position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.75);z-index:0;pointer-events:none;"></div>
  <div style="position:relative;z-index:1;width:100%;display:flex;flex-direction:column;align-items:center;">
  <!-- Vue question -->'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
