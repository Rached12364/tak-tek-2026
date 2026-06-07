content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '.home-btn {\n  animation: fadeInUp 0.6s ease both;\n  transition: transform 0.2s ease !important;\n}\n.home-btn:hover {\n  transform: scale(1.05) !important;\n}',
    '''.home-btn {
  animation: fadeInUp 0.6s ease both;
  transition: transform 0.2s ease !important;
}
.home-btn:hover {
  transform: scale(1.05) !important;
}
.home-btn:nth-child(1) { animation-delay: 0.1s; }
.home-btn:nth-child(2) { animation-delay: 0.3s; }
.home-btn:nth-child(3) { animation-delay: 0.5s; }
.home-btn:nth-child(4) { animation-delay: 0.7s; }'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
