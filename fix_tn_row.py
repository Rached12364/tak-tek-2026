content = open('index.html','r',encoding='utf-8').read()
# 1. Forcer tn-main en flex ROW (pitch à gauche, liste à droite)
content = content.replace(
    '<div id="tn-main" style="display:flex;flex:1;overflow:hidden;">',
    '<div id="tn-main" style="display:flex;flex-direction:row;flex:1;overflow:hidden;width:100%;">'
)
# 2. Pitch Tunisia : largeur 55%
content = content.replace(
    '<!-- LEFT: Pitch -->\n    <div style="width:420px;flex-shrink:0;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;">',
    '<!-- LEFT: Pitch -->\n    <div style="width:55%;flex-shrink:0;height:100%;background:linear-gradient(180deg,#0b3d1f,#0a3018,#0b3d1f);position:relative;overflow:hidden;padding:20px;">'
)
# 3. Panneau droit Tunisia : largeur 45%
content = content.replace(
    '<!-- RIGHT: Player selection -->\n    <div style="width:33%;flex-shrink:0;overflow-y:auto;padding:24px 20px;background:#111;">',
    '<!-- RIGHT: Player selection -->\n    <div style="width:45%;flex-shrink:0;height:100%;overflow-y:auto;padding:24px 20px;background:#111;">'
)
# 4. S'assurer que page-tunisia a flex-direction: column
content = content.replace(
    '<div id="page-tunisia" style="display:none;width:100%;height:100vh;background:#111;overflow:hidden;">',
    '<div id="page-tunisia" style="display:none;flex-direction:column;width:100%;height:100vh;background:#111;overflow:hidden;">'
)
open('index.html','w',encoding='utf-8').write(content)
print("✅ Tunisia corrigé : pitch (55%) + liste (45%) côte à côte")
