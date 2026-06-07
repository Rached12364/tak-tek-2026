content = open('index.html','r',encoding='utf-8').read()
# Remplacer la classe btn-icon par style direct avec perspective
content = content.replace(
    '<img src="tuns.png" class="btn-icon" style="width:160px;height:160px;object-fit:contain;">',
    '<div style="perspective:400px;"><img src="tuns.png" style="width:160px;height:160px;object-fit:contain;animation:quiz-spin 4s linear infinite;"></div>'
)
# Changer l animation pour rotateY avec perspective
content = content.replace(
    '''@keyframes quiz-spin {
  0%   { transform:rotate(0deg); }
  100% { transform:rotate(360deg); }
}''',
    '''@keyframes quiz-spin {
  0%   { transform:rotateY(0deg); }
  100% { transform:rotateY(360deg); }
}'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
