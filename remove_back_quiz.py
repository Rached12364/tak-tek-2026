content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''<button onclick="showPage('home')" style="position:fixed;top:16px;left:16px;background:#111;border:1px solid #FFD700;color:#FFD700;padding:8px 18px;border-radius:8px;font-family:'Barlow Condensed',sans-serif;font-size:15px;font-weight:700;cursor:pointer;letter-spacing:2px;z-index:99;">&#8592; HOME</button>''',
    ''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
