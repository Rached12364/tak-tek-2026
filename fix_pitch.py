content = open('index.html','r',encoding='utf-8').read()
# Make pitch column taller and wider
content = content.replace(
    'width:420px;flex-shrink:0;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;perspective:900px;',
    'width:420px;flex-shrink:0;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:0;perspective:900px;min-height:calc(100vh - 73px);'
)
# Better 3D angles - trapezoid like the reference image
content = content.replace(
    'transform:perspective(900px) rotateX(25deg) scaleX(0.82);transform-origin:bottom center;" viewBox',
    'transform:perspective(700px) rotateX(20deg);transform-origin:bottom center;" viewBox'
)
content = content.replace(
    'transform:perspective(900px) rotateX(25deg) scaleX(0.82);transform-origin:bottom center;">',
    'transform:perspective(700px) rotateX(20deg);transform-origin:bottom center;>'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
