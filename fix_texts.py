content = open('index.html','r',encoding='utf-8').read()
# Texte Best XI Monde
content = content.replace(
    'Chaque fois 3 joueurs par poste, choisis 1 pour former ton equipe 2025/2026 et choisis le coach a la fin',
    'كل مرة يجيك 3 جواير، اعمل سيشن بهيا سنة في كل بوست، باش في الآخر تعمل تشكيلتك 2025/2026 + اختار المدرب'
)
# Texte Tier List
content = content.replace(
    '24 joueurs a classer, 3 categories S A B, tu peux renommer chaque categorie',
    'فما 24 صفاقة جوايرز صاروا 2025/2026 في العالم، انت بش ترتبهم كانوا ناجحين ولا فاشلين في 3 كلاس S A B وتنجم تبدل أسمائهم'
)
# Texte Best XI Tunisia
content = content.replace(
    'Chaque fois 3 joueurs par poste, choisis 1 pour former ton equipe tunisienne',
    'تشكيلة الموسم في البطولة التونسية + اختار المدرب'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
