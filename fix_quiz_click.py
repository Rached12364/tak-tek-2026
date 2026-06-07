content = open('index.html','r',encoding='utf-8').read()
# Remplacer les cartes avec pointer-events fixes
old_chaouat = '''<div onclick="startQuiz('chaouat')" style="background:#111;border:2px solid #333;border-radius:16px;padding:20px;text-align:center;cursor:pointer;transition:all 0.3s;" onmouseover="this.style.border='2px solid #00C853';this.style.transform='translateY(-4px)'" onmouseout="this.style.border='2px solid #333';this.style.transform='translateY(0)'">'''
new_chaouat = '''<div onclick="startQuiz('chaouat')" style="background:#111;border:2px solid #333;border-radius:16px;padding:20px;text-align:center;cursor:pointer;transition:all 0.3s;position:relative;z-index:1;">'''
old_belaili = '''<div onclick="startQuiz('belaili')" style="background:#111;border:2px solid #333;border-radius:16px;padding:20px;text-align:center;cursor:pointer;transition:all 0.3s;" onmouseover="this.style.border='2px solid #00C853';this.style.transform='translateY(-4px)'" onmouseout="this.style.border='2px solid #333';this.style.transform='translateY(0)'">'''
new_belaili = '''<div onclick="startQuiz('belaili')" style="background:#111;border:2px solid #333;border-radius:16px;padding:20px;text-align:center;cursor:pointer;transition:all 0.3s;position:relative;z-index:1;">'''
content = content.replace(old_chaouat, new_chaouat)
content = content.replace(old_belaili, new_belaili)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
