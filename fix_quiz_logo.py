content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '<div style="font-size:60px;">🧠</div>',
    '<img src="tuns.png" style="width:120px;height:120px;object-fit:contain;animation:quiz-spin 3s linear infinite;">'
)
# Ajouter animation spin
spin_css = '''
@keyframes quiz-spin {
  0%   { transform:rotate(0deg) scale(1); }
  50%  { transform:rotate(180deg) scale(1.1); }
  100% { transform:rotate(360deg) scale(1); }
}
'''
if 'quiz-spin' not in content:
    content = content.replace('</style>', spin_css + '</style>')
open('index.html','w',encoding='utf-8').write(content)
print('OK')
