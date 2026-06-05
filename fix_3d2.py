content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'transform:rotateX(18deg) scale(0.95);transform-origin:top center;transform-style:preserve-3d;',
    'transform:rotateX(30deg) scale(1.05);transform-origin:top center;transform-style:preserve-3d;'
)
content = content.replace(
    'perspective:800px;',
    'perspective:600px;'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
