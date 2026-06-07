content = open('index.html','r',encoding='utf-8').read()
# 1. Changer le fond de page-quiz
content = content.replace(
    'id="page-quiz" style="display:none;width:100%;min-height:100vh;background:#0a0a0a;flex-direction:column;align-items:center;padding:40px 20px;box-sizing:border-box;"',
    'id="page-quiz" style="display:none;width:100%;min-height:100vh;background:linear-gradient(135deg,#0a0a1a 0%,#0d1b2a 40%,#0a0a1a 100%);flex-direction:column;align-items:center;padding:40px 20px;box-sizing:border-box;"'
)
# 2. Remplacer la vue question par un layout gauche/droite + countdown
content = content.replace(
    '''  <!-- Vue question -->
  <div id="quiz-question-view" style="display:none;width:100%;max-width:600px;text-align:center;padding:20px;">
    <div id="quiz-progress" style="color:#888;font-size:13px;margin-bottom:8px;">Question 1 / 7</div>
    <div id="quiz-score-display" style="color:#00C853;font-size:15px;font-weight:700;margin-bottom:20px;">Score: 0</div>
    <div id="quiz-question-container"></div>
  </div>''',
    '''  <!-- Vue question -->
  <div id="quiz-question-view" style="display:none;width:100%;max-width:1100px;padding:20px;box-sizing:border-box;">
    <!-- Header progress -->
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:30px;">
      <div id="quiz-progress" style="color:#888;font-size:15px;font-weight:700;letter-spacing:2px;">Question 1 / 7</div>
      <div id="quiz-countdown" style="width:52px;height:52px;border-radius:50%;border:3px solid #00C853;display:flex;align-items:center;justify-content:center;color:#00C853;font-size:22px;font-weight:900;background:rgba(0,200,83,0.1);">7</div>
      <div id="quiz-score-display" style="color:#00C853;font-size:15px;font-weight:700;letter-spacing:2px;">Score: 0</div>
    </div>
    <!-- Layout gauche/droite -->
    <div style="display:flex;gap:40px;align-items:center;justify-content:center;">
      <!-- Carte joueur gauche -->
      <div id="quiz-player-card-display" style="flex-shrink:0;width:280px;text-align:center;animation:slideInLeft 0.5s ease;">
      </div>
      <!-- Question droite -->
      <div id="quiz-question-container" style="flex:1;max-width:550px;">
      </div>
    </div>
  </div>'''
)
# 3. Ajouter animations CSS
content = content.replace(
    '@keyframes fadeInUp {',
    '''@keyframes slideInLeft {
  from { opacity:0; transform:translateX(-40px); }
  to   { opacity:1; transform:translateX(0); }
}
@keyframes slideInRight {
  from { opacity:0; transform:translateX(40px); }
  to   { opacity:1; transform:translateX(0); }
}
@keyframes countdown-pulse {
  0%   { transform:scale(1); }
  50%  { transform:scale(1.2); color:#FFD700; border-color:#FFD700; }
  100% { transform:scale(1); }
}
@keyframes flash-correct {
  0%   { background:#0a0a1a; }
  50%  { background:rgba(0,200,83,0.3); }
  100% { background:#0a0a1a; }
}
@keyframes flash-wrong {
  0%   { background:#0a0a1a; }
  50%  { background:rgba(231,0,19,0.3); }
  100% { background:#0a0a1a; }
}
@keyframes fadeInUp {'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
