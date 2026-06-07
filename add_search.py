content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '<div style="color:#888;font-size:14px;margin-top:8px;">Choisis un joueur pour commencer le quiz</div>',
    '''<div style="color:#888;font-size:14px;margin-top:8px;">Choisis un joueur pour commencer le quiz</div>
    <div style="margin-top:20px;">
      <input id="quiz-search" type="text" placeholder="🔍 Rechercher un joueur..." 
        oninput="filterQuizPlayers(this.value)"
        style="width:100%;max-width:400px;padding:12px 20px;border-radius:25px;border:2px solid #00C853;background:#111;color:#fff;font-size:16px;outline:none;box-sizing:border-box;">
    </div>'''
)
# Ajouter la fonction de filtre
content = content.replace(
    'function startQuiz(player) {',
    '''function filterQuizPlayers(val) {
  var cards = document.querySelectorAll(".quiz-player-card");
  cards.forEach(function(card) {
    var name = card.querySelector("div").textContent.toLowerCase();
    card.parentElement.style.display = name.includes(val.toLowerCase()) ? "block" : "none";
  });
}
function startQuiz(player) {'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
