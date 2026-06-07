content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '<div style="font-size:13px;font-weight:400;color:#aaa;text-align:center;padding:0 16px;line-height:1.4;">Chaque poste : 3 joueurs au choix. Selectionne 1 par poste pour former ton equipe 2025/2026, puis choisis ton coach !</div>',
    '<div style="font-size:13px;font-weight:400;color:#aaa;text-align:center;padding:0 16px;line-height:1.4;">Teste tes connaissances sur les joueurs de la Ligue 1 Tunisienne ! 7 questions de facile a difficile !</div>'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
