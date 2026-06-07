content = open('index.html','r',encoding='utf-8').read()
# Trouver le debut et la fin de la grille
start = content.find('<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:20px;width:100%;">')
end = content.find('</div>\n  </div>\n\n  <!-- Vue quiz -->')
old_grid = content[start:end]
new_grid = '''<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:20px;width:100%;">
      <div onclick="startQuiz('chaouat')" class="quiz-player-card">
        <img src="https://static.flashscore.com/res/image/data/EL8CsfBr-2X9WEIyE.png" style="width:120px;height:150px;object-fit:cover;border-radius:12px;margin-bottom:12px;">
        <div style="font-family:'Barlow Condensed',sans-serif;color:#fff;font-size:20px;font-weight:900;">FIRAS CHAOUAT</div>
        <div style="color:#E70013;font-size:13px;">Club Africain</div>
        <div style="color:#888;font-size:12px;margin-top:4px;">Avant-centre · 30 ans</div>
        <div style="margin-top:10px;background:#00C853;color:#000;font-size:12px;font-weight:700;padding:6px 12px;border-radius:20px;display:inline-block;">7 QUESTIONS</div>
      </div>
      <div onclick="startQuiz('belaili')" class="quiz-player-card">
        <img src="https://static.flashscore.com/res/image/data/6V5W3QyS-YDy6iaVc.png" style="width:120px;height:150px;object-fit:cover;border-radius:12px;margin-bottom:12px;">
        <div style="font-family:'Barlow Condensed',sans-serif;color:#fff;font-size:20px;font-weight:900;">YOUCEF BELAILI</div>
        <div style="color:#E70013;font-size:13px;">Esperance Tunis</div>
        <div style="color:#888;font-size:12px;margin-top:4px;">Ailier gauche · 34 ans</div>
        <div style="margin-top:10px;background:#00C853;color:#000;font-size:12px;font-weight:700;padding:6px 12px;border-radius:20px;display:inline-block;">7 QUESTIONS</div>
      </div>
      <div onclick="startQuiz('msakni')" class="quiz-player-card">
        <img src="https://static.flashscore.com/res/image/data/OCwL77FG-4WhOr90b.png" style="width:120px;height:150px;object-fit:cover;border-radius:12px;margin-bottom:12px;">
        <div style="font-family:'Barlow Condensed',sans-serif;color:#fff;font-size:20px;font-weight:900;">YOUSSEF MSAKNI</div>
        <div style="color:#E70013;font-size:13px;">Esperance Tunis</div>
        <div style="color:#888;font-size:12px;margin-top:4px;">Ailier gauche · 35 ans</div>
        <div style="margin-top:10px;background:#00C853;color:#000;font-size:12px;font-weight:700;padding:6px 12px;border-radius:20px;display:inline-block;">7 QUESTIONS</div>
      </div>
      <div onclick="startQuiz('aouani')" class="quiz-player-card">
        <img src="https://static.flashscore.com/res/image/data/YNOJHqwS-ltYaYaBP.png" style="width:120px;height:150px;object-fit:cover;border-radius:12px;margin-bottom:12px;">
        <div style="font-family:'Barlow Condensed',sans-serif;color:#fff;font-size:20px;font-weight:900;">RAKI AOUANI</div>
        <div style="color:#E70013;font-size:13px;">Etoile du Sahel</div>
        <div style="color:#888;font-size:12px;margin-top:4px;">Attaquant · 21 ans</div>
        <div style="margin-top:10px;background:#00C853;color:#000;font-size:12px;font-weight:700;padding:6px 12px;border-radius:20px;display:inline-block;">7 QUESTIONS</div>
      </div>
      <div onclick="startQuiz('benzarti')" class="quiz-player-card">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Faouzi_Benzarti_au_Raja_%28cropped%29.jpg/960px-Faouzi_Benzarti_au_Raja_%28cropped%29.jpg" style="width:120px;height:150px;object-fit:cover;border-radius:12px;margin-bottom:12px;">
        <div style="font-family:'Barlow Condensed',sans-serif;color:#fff;font-size:20px;font-weight:900;">FAOUZI BENZARTI</div>
        <div style="color:#E70013;font-size:13px;">Club Africain</div>
        <div style="color:#888;font-size:12px;margin-top:4px;">Entraineur · 76 ans</div>
        <div style="margin-top:10px;background:#00C853;color:#000;font-size:12px;font-weight:700;padding:6px 12px;border-radius:20px;display:inline-block;">7 QUESTIONS</div>
      </div>'''
content = content[:start] + new_grid + content[end:]
open('index.html','w',encoding='utf-8').write(content)
print('OK')
