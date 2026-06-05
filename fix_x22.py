content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    "html += \"<button onclick='showPage(\\x22home\\x22)'",
    "html += \"<button onclick='showPage(\\\"home\\\")'\"[:-1]"
)
# Methode plus simple - remplacer directement
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'showPage(\\x22home\\x22)' in line:
        lines[i] = line.replace('showPage(\\x22home\\x22)', 'showPage(home_page)')
        print('Fixe ligne', i+1)
content = '\n'.join(lines)
# Ajouter var home_page = 'home' dans le script
content = content.replace(
    'var tnStep = 0;',
    'var tnStep = 0; var home_page = "home";'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
