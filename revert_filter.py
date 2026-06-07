content = open('index.html','r',encoding='utf-8').read()
old = '''  cards.forEach(function(card) {
    var onclick = card.getAttribute("onclick");
    var m = onclick.match(/startQuiz\('([^']+)'\)/);
    if (!m) return;
    var player = m[1];
    card.style.display = matches(player, val) ? "flex" : "none";
  });'''
new = '''  cards.forEach(function(card) {
    var player = card.getAttribute("onclick").match(/startQuiz\('(\w+)'\)/)[1];
    card.parentElement.style.display = matches(player, val) ? "block" : "none";
  });'''
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
