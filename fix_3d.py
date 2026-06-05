content = open('index.html','r',encoding='utf-8').read()
# Add 3D perspective to the pitch container
content = content.replace(
    'background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;',
    'background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;perspective:800px;'
)
# Add 3D rotation to the inner pitch div (the one with position:relative containing dots)
content = content.replace(
    '<div style="position:relative;width:100%;height:100%;z-index:2;">',
    '<div style="position:relative;width:100%;height:100%;z-index:2;transform:rotateX(18deg) scale(0.95);transform-origin:top center;transform-style:preserve-3d;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
