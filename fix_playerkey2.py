content = open('index.html','r',encoding='utf-8').read()
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'startQuiz' in line and 'playerKey' in line:
        lines[i] = '  html += "<button onclick=\\"startQuiz(\'" + playerKey + "\')\\" style=\'padding:14px;background:#00C853;border:none;color:#000;border-radius:12px;font-family:Barlow Condensed,sans-serif;font-size:16px;font-weight:900;cursor:pointer;\'>REJOUER</button>";'
        print("Fixe ligne", i+1)
content = '\n'.join(lines)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
