content = open('index.html', 'r', encoding='utf-8').read()
extra_anim = '''<style>
@keyframes rotate3d {
  0%   { transform: rotateY(0deg); }
  100% { transform: rotateY(360deg); }
}
.btn-icon {
  animation: rotate3d 4s linear infinite !important;
  transform-style: preserve-3d;
}
.home-btn:hover .btn-icon {
  animation: rotate3d 0.6s linear infinite !important;
}
</style>'''
content = content.replace('</head>', extra_anim + '</head>', 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
