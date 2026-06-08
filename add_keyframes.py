content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '@keyframes slideInLeft {',
    '''@keyframes tn-slot-fadein {
  from { opacity:0; transform:scale(0.8); }
  to   { opacity:1; transform:scale(1); }
}
@keyframes tn-glow-lines {
  0%   { border-color: rgba(255,255,255,0.25); }
  50%  { border-color: rgba(255,255,255,0.7); box-shadow: 0 0 15px rgba(255,255,255,0.3); }
  100% { border-color: rgba(255,255,255,0.25); }
}
@keyframes tn-fly-in {
  0%   { opacity:0; transform:translateX(200px) scale(0.5); }
  60%  { transform:translateX(-5px) scale(1.05); }
  100% { opacity:1; transform:translateX(0) scale(1); }
}
@keyframes tn-slot-selected {
  0%   { box-shadow:0 0 0px #00C853; }
  50%  { box-shadow:0 0 25px #00C853; }
  100% { box-shadow:0 0 8px #00C853; }
}
@keyframes slideInLeft {'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
