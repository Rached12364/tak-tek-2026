content = open('index.html','r',encoding='utf-8').read()
old = "var quizCurrent = null;"
new = """  msakni: {
    name: "YOUSSEF MSAKNI",
    img: "https://static.flashscore.com/res/image/data/OCwL77FG-4WhOr90b.png",
    club: "Esperance Tunis",
    questions: [
      { q: "Msakni a joue au Qatar pendant plus de 10 ans ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de buts Msakni a marque avec la Tunisie ?", type:"number", answer: 23, diff:3 },
      { q: "Msakni a joue en Belgique a KAS Eupen ?", type:"tf", answer: true, diff:3 },
      { q: "Msakni a ete meilleur buteur du championnat de Tunisie avec 17 buts ?", type:"tf", answer: true, diff:3 },
      { q: "Msakni a marque un triple contre la Guinee en 2017 ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de selections officielles Msakni a avec la Tunisie ?", type:"number", answer: 104, diff:3 },
      { q: "Msakni a remporte le CHAN avec la Tunisie en 2011 ?", type:"tf", answer: true, diff:3 }
    ]
  },
  aouani: {
    name: "RAKI AOUANI",
    img: "https://static.flashscore.com/res/image/data/YNOJHqwS-ltYaYaBP.png",
    club: "Etoile du Sahel",
    questions: [
      { q: "Raki Aouani est ne en 2004 ?", type:"tf", answer: true, diff:3 },
      { q: "Aouani a signe pour un club letton (Riga FC) en 2026 ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de buts Aouani a marque avec Etoile du Sahel ?", type:"number", answer: 12, diff:3 },
      { q: "Aouani joue au poste de gardien de but ?", type:"tf", answer: false, diff:3 },
      { q: "Combien de matchs Aouani a joue avec Etoile du Sahel ?", type:"number", answer: 103, diff:3 },
      { q: "Aouani a represente la Tunisie U20 ?", type:"tf", answer: true, diff:3 },
      { q: "Aouani mesure 1.79m ?", type:"tf", answer: true, diff:3 }
    ]
  },
  benzarti: {
    name: "FAOUZI BENZARTI",
    img: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Faouzi_Benzarti_au_Raja_%28cropped%29.jpg/960px-Faouzi_Benzarti_au_Raja_%28cropped%29.jpg",
    club: "Club Africain",
    questions: [
      { q: "Benzarti est ne a Monastir ?", type:"tf", answer: true, diff:3 },
      { q: "Benzarti a mene le Raja en finale du Mondial des clubs ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de fois Benzarti a ete selectionneur de la Tunisie ?", type:"number", answer: 3, diff:3 },
      { q: "Benzarti a remporte la Ligue des champions CAF comme entraineur ?", type:"tf", answer: true, diff:3 },
      { q: "En quelle annee Benzarti est ne ?", type:"number", answer: 1950, diff:3 },
      { q: "Benzarti a entraine le Wydad de Casablanca ?", type:"tf", answer: true, diff:3 },
      { q: "Benzarti est classe 9e meilleur entraineur africain de tous les temps ?", type:"tf", answer: true, diff:3 }
    ]
  }
};
var quizCurrent = null;"""
content = content.replace("var quizCurrent = null;", new)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
