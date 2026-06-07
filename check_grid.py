content = open('index.html','r',encoding='utf-8').read()
# Trouver et corriger la structure de la grille
old_grid = '''      <!-- Carte Youssef Msakni -->
      <div onclick="startQuiz('msakni')" class="quiz-player-card">'''
# Verifier ou sont placees les nouvelles cartes
idx = content.find("startQuiz('msakni')")
print('Position msakni:', idx)
print(content[idx-300:idx+50])
