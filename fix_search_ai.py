content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'function filterQuizPlayers(val) {\n  var cards = document.querySelectorAll(".quiz-player-card");\n  cards.forEach(function(card) {\n    var name = card.querySelector("div").textContent.toLowerCase();\n    card.parentElement.style.display = name.includes(val.toLowerCase()) ? "block" : "none";\n  });\n}',
    '''function filterQuizPlayers(val) {
  val = val.toLowerCase().trim();
  var cards = document.querySelectorAll(".quiz-player-card");
  // Aliases et variantes phonetiques
  var aliases = {
    "chaouat": ["chaouat","chaout","chawat","firas","fc","chaouet"],
    "belaili": ["belaili","blaili","belaïli","youcef","youssef belaili","blaïli","beli"],
    "msakni": ["msakni","msakni","meskni","youssef","msekni","msakny"],
    "aouani": ["aouani","aoueni","awani","raki","rakki","aouany"],
    "benzarti": ["benzarti","benzartie","benzarty","faouzi","fauzi","fouzi","benzarti"]
  };
  function matches(player, query) {
    if (!query) return true;
    var targets = aliases[player] || [];
    // Match direct
    for (var i=0; i<targets.length; i++) {
      if (targets[i].includes(query) || query.includes(targets[i])) return true;
    }
    // Match fuzzy: compter lettres communes
    var common = 0;
    for (var c=0; c<query.length; c++) {
      if (targets.join("").includes(query[c])) common++;
    }
    return query.length > 2 && common / query.length > 0.7;
  }
  cards.forEach(function(card) {
    var player = card.getAttribute("onclick").match(/startQuiz\(\'(\w+)\'\)/)[1];
    card.parentElement.style.display = matches(player, val) ? "block" : "none";
  });
}'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
