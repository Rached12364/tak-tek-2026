content = open('index.html','r',encoding='utf-8').read()
# Texte Best XI Monde
content = content.replace(
    'كل مرة يجيك 3 جواير، اعمل سيشن بهيا سنة في كل بوست، باش في الآخر تعمل تشكيلتك 2025/2026 + اختار المدرب',
    'Chaque poste : 3 joueurs au choix. Selectionne 1 par poste pour former ton equipe 2025/2026, puis choisis ton coach !'
)
# Texte Tier List
content = content.replace(
    'فما 24 صفاقة جوايرز صاروا 2025/2026 في العالم، انت بش ترتبهم كانوا ناجحين ولا فاشلين في 3 كلاس S A B وتنجم تبدل أسمائهم',
    '24 joueurs stars de 2025/2026. Classe-les en 3 categories S, A, B selon leurs performances. Tu peux renommer les categories !'
)
# Texte Best XI Tunisia
content = content.replace(
    'تشكيلة الموسم في البطولة التونسية + اختار المدرب',
    'Forme la meilleure equipe de la saison en Ligue 1 Tunisienne, poste par poste, puis choisis ton coach !'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
