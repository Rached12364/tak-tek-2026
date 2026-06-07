content = open('index.html','r',encoding='utf-8').read()
old_spin = '''@keyframes quiz-spin {
  0%   { transform:rotateY(0deg); }
  100% { transform:rotateY(360deg); }
}'''
new_spin = '''@keyframes quiz-spin {
  0%   { transform:rotate(0deg); }
  100% { transform:rotate(360deg); }
}'''
content = content.replace(old_spin, new_spin)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
