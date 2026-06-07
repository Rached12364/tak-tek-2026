content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''@keyframes spin {
  0%   { transform: rotateY(0deg) scale(1); }
  50%  { transform: rotateY(180deg) scale(1.1); }
  100% { transform: rotateY(360deg) scale(1); }
}''',
    '''@keyframes spin {
  0%   { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
