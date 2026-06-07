content = open('index.html','r',encoding='utf-8').read()
# Remplacer les questions de chaouat
old = '''  chaouat: {
    name: "FIRAS CHAOUAT",
    img: "firas2.png",
    club: "Club Africain",
    questions: [
      { q: "Chaouat a joue pour l Esperance de Tunis ?", type:"tf", answer: false, diff:3 },
      { q: "Chaouat joue au poste d avant-centre ?", type:"tf", answer: true, diff:3 },
      { q: "Chaouat est ne en Tunisie ?", type:"tf", answer: true, diff:3 },
      { q: "Chaouat a represente la Tunisie en selection nationale ?", type:"tf", answer: true, diff:3 },
      { q: "Chaouat joue au Club Africain ?", type:"tf", answer: true, diff:3 },
      { q: "Chaouat a marque plus de 10 buts en championnat ?", type:"tf", answer: true, diff:3 },
      { q: "Chaouat a 30 ans ?", type:"tf", answer: true, diff:3 }
    ]
  },'''
new = '''  chaouat: {
    name: "FIRAS CHAOUAT",
    img: "firas2.png",
    club: "Club Africain",
    questions: [
      { q: "Chaouat est ne a Sfax ?", type:"tf", answer: true },
      { q: "Chaouat a joue en Arabie Saoudite avec Abha Club ?", type:"tf", answer: true },
      { q: "Chaouat a joue en Egypte avec Ismaily SC ?", type:"tf", answer: true },
      { q: "Chaouat a joue au Bahrain avec Al-Muharraq ?", type:"tf", answer: true },
      { q: "Combien de buts Chaouat a marque avec le CS Sfaxien ?", type:"mcq", answer: 50, choices:[35, 50, 63] },
      { q: "Chaouat mesure 1.85m ?", type:"tf", answer: true },
      { q: "Chaouat a remporte 2 Coupes de Tunisie avec Sfaxien (2019 et 2021) ?", type:"tf", answer: true },
      { q: "Le premier but de Chaouat en selection etait contre le Niger ?", type:"tf", answer: true },
      { q: "Combien de buts Chaouat a marque avec l ES Sahel en 2024-2025 ?", type:"mcq", answer: 19, choices:[12, 19, 24] },
      { q: "Chaouat a remporte le championnat de Tunisie 2026 avec le Club Africain ?", type:"tf", answer: true }
    ]
  },'''
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
