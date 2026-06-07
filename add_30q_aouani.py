content = open('index.html','r',encoding='utf-8').read()
old = '''  aouani: {
    name: "RAKI AOUANI",
    img: "raki_aouani2.png",
    club: "Etoile du Sahel",
    questions: [
      { q: "Raki Aouani est ne en 2004 ?", type:"tf", answer: true, diff:3 },
      { q: "Aouani a signe pour Riga FC en Lettonie en 2026 ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de buts Aouani a marque avec Etoile du Sahel ?", type:"number", answer: 12, diff:3 },
      { q: "Aouani joue au poste de gardien de but ?", type:"tf", answer: false, diff:3 },
      { q: "Combien de matchs Aouani a joue avec Etoile du Sahel ?", type:"number", answer: 103, diff:3 },
      { q: "Aouani a represente la Tunisie U20 ?", type:"tf", answer: true, diff:3 },
      { q: "Aouani mesure 1.79m ?", type:"tf", answer: true, diff:3 }
    ]
  },'''
new = '''  aouani: {
    name: "RAKI AOUANI",
    img: "raki_aouani2.png",
    club: "Etoile du Sahel",
    questions: [
      { q: "Raki Aouani est ne le 11 septembre 2004 ?", type:"tf", answer: true },
      { q: "Aouani est Tunisien ?", type:"tf", answer: true },
      { q: "Aouani mesure 1.79m ?", type:"tf", answer: true },
      { q: "Aouani joue au poste d attaquant ?", type:"tf", answer: true },
      { q: "Aouani a joue pour l Esperance de Tunis ?", type:"tf", answer: false },
      { q: "Aouani a signe pour Riga FC en Lettonie en janvier 2026 ?", type:"tf", answer: true },
      { q: "Aouani a fait ses debuts avec l Etoile du Sahel en 2022 ?", type:"tf", answer: true },
      { q: "Aouani a represente la Tunisie U20 ?", type:"tf", answer: true },
      { q: "Combien de buts Aouani a marque avec l Etoile du Sahel ?", type:"mcq", answer: 12, choices:[7, 12, 18] },
      { q: "Combien de matchs Aouani a joue avec l Etoile du Sahel ?", type:"mcq", answer: 103, choices:[78, 103, 125] },
      { q: "Aouani a participe a la Coupe du monde U20 en Argentine 2023 ?", type:"tf", answer: true },
      { q: "Aouani a joue en Lettonie dans la Virsliga ?", type:"tf", answer: true },
      { q: "Aouani a joue 5 matchs avec la Tunisie U20 ?", type:"tf", answer: true },
      { q: "Aouani avait moins de 22 ans quand il a signe a Riga FC ?", type:"tf", answer: true },
      { q: "Aouani a marque 2 buts lors de sa premiere saison avec l Etoile du Sahel ?", type:"tf", answer: true },
      { q: "Riga FC est un club letton ?", type:"tf", answer: true },
      { q: "Aouani a joue plus de 100 matchs avec l Etoile du Sahel ?", type:"tf", answer: true },
      { q: "Aouani est considere comme l un des jeunes talents les plus prometteurs de Tunisie ?", type:"tf", answer: true },
      { q: "Aouani a quitte l Etoile du Sahel en janvier 2026 ?", type:"tf", answer: true },
      { q: "Aouani joue au poste de gardien de but ?", type:"tf", answer: false },
      { q: "Aouani est ne en 2004 ce qui fait de lui un joueur de moins de 22 ans ?", type:"tf", answer: true },
      { q: "Aouani a joue sa premiere saison pro en CLP-1 en 2021-2022 ?", type:"tf", answer: true },
      { q: "Combien de selections Aouani a avec la Tunisie U20 ?", type:"mcq", answer: 5, choices:[2, 5, 9] },
      { q: "Aouani a joue en Coupe arabe U20 contre l Algerie ?", type:"tf", answer: true },
      { q: "Aouani a signe a Riga FC sur un transfert permanent ?", type:"tf", answer: true },
      { q: "Aouani a marque lors de ses debuts en CLP-1 en 2021-2022 ?", type:"tf", answer: true },
      { q: "Aouani joue son football en Europe depuis 2026 ?", type:"tf", answer: true },
      { q: "Aouani portait son nom complet Raki Aouani en arabe ?", type:"tf", answer: true },
      { q: "L Etoile du Sahel est le seul club tunisien d Aouani avant de partir ?", type:"tf", answer: true },
      { q: "Aouani a debute sa carriere pro a l age de 17 ans ?", type:"tf", answer: true }
    ]
  },'''
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
