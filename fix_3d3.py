content = open('index.html','r',encoding='utf-8').read()
# Reset to flat then apply trapezoid 3D on the pitch wrapper div
content = content.replace(
    'transform:rotateX(30deg) scale(1.05);transform-origin:top center;transform-style:preserve-3d;',
    ''
)
content = content.replace(
    'perspective:600px;',
    'perspective:900px;'
)
# Apply 3D on the SVG pitch lines only
content = content.replace(
    '<svg style="position:absolute;inset:0;width:100%;height:100%;opacity:0.18;"',
    '<svg style="position:absolute;inset:0;width:100%;height:100%;opacity:0.25;transform:perspective(900px) rotateX(25deg) scaleX(0.82);transform-origin:bottom center;"'
)
# Apply same transform on dots container
content = content.replace(
    '<div style="position:relative;width:100%;height:100%;z-index:2;">',
    '<div style="position:relative;width:100%;height:100%;z-index:2;transform:perspective(900px) rotateX(25deg) scaleX(0.82);transform-origin:bottom center;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
