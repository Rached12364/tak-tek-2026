content = open('index.html','r',encoding='utf-8').read()
old_chaouat_q = '''questions: [
      { q: "Firas Chaouat joue au Club Africain ?", type:"tf", answer: true, diff:1 },
      { q: "Firas Chaouat est ne a Sfax ?", type:"tf", answer: true, diff:1 },
      { q: "Firas Chaouat est un gardien de but ?", type:"tf", answer: false, diff:1 },
      { q: "Combien de buts a marque Firas Chaouat en Ligue 1 2025/2026 ?", type:"number", answer: 14, diff:2 },
      { q: "Firas Chaouat a joue en Arabie Saoudite ?", type:"tf", answer: true, diff:2 },
      { q: "Combien de selections internationales a Firas Chaouat ?", type:"number", answer: 26, diff:3 },
      { q: "Quelle est la valeur marchande de Firas Chaouat en millions ? (ex: 1.2)", type:"number", answer: 1.2, diff:3 }
    ]'''
new_chaouat_q = '''questions: [
      { q: "Combien de buts Chaouat a marque en Ligue 1 2025/2026 ?", type:"number", answer: 14, diff:3 },
      { q: "Dans quel club Chaouat jouait avant Club Africain ?", type:"tf", answer: false, diff:3, hint:"ES Sahel - VRAI ou Club Sfaxien - FAUX" },
      { q: "Combien de matchs Chaouat a joue en Ligue 1 2025/2026 ?", type:"number", answer: 25, diff:3 },
      { q: "Chaouat a joue au Barhain (Al-Muharraq) ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de buts Chaouat a marque avec la Tunisie ?", type:"number", answer: 6, diff:3 },
      { q: "Chaouat a gagne la Coupe de Tunisie avec CS Sfaxien ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de cartons jaunes Chaouat a recu en Ligue 1 2025/2026 ?", type:"number", answer: 6, diff:3 }
    ]'''
old_belaili_q = '''questions: [
      { q: "Youcef Belaili est algerien ?", type:"tf", answer: true, diff:1 },
      { q: "Belaili a joue en Ligue 1 francaise ?", type:"tf", answer: true, diff:1 },
      { q: "Belaili joue au poste de gardien ?", type:"tf", answer: false, diff:1 },
      { q: "En quelle annee Belaili est ne ?", type:"number", answer: 1992, diff:2 },
      { q: "Belaili a remporte la CAN avec l Algerie ?", type:"tf", answer: true, diff:2 },
      { q: "Combien de buts en carriere internationale avec l Algerie ?", type:"number", answer: 10, diff:3 },
      { q: "Combien de passages de Belaili a l Esperance Tunis ?", type:"number", answer: 3, diff:3 }
    ]'''
new_belaili_q = '''questions: [
      { q: "Belaili a joue au Qatar SC ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de buts Belaili a marque avec MC Alger en championnat ?", type:"number", answer: 14, diff:3 },
      { q: "Belaili a ete suspendu pour dopage ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de Ligues des Champions CAF Belaili a gagne avec EST ?", type:"number", answer: 2, diff:3 },
      { q: "Belaili a joue a Brest en Ligue 1 francaise ?", type:"tf", answer: true, diff:3 },
      { q: "Combien de buts Belaili a marque avec EST en 2024/2025 ?", type:"number", answer: 9, diff:3 },
      { q: "Belaili a remporte la Coupe Arabe 2021 avec l Algerie ?", type:"tf", answer: true, diff:3 }
    ]'''
content = content.replace(old_chaouat_q, new_chaouat_q)
content = content.replace(old_belaili_q, new_belaili_q)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
