content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''  cards.forEach(function(card) {
    var player = card.getAttribute("onclick").match(/startQuiz\('(\w+)'\)/)[1];
    card.parentElement.style.display = matches(player, val) ? "block" : "none";
  });''',
    '''  cards.forEach(function(card) {
    var oc = card.getAttribute("onclick");
    var m = oc ? oc.match(/startQuiz\('(\w+)'\)/) : null;
    if (!m) return;
    var player = m[1];
    card.style.display = matches(player, val) ? "" : "none";
  });'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
