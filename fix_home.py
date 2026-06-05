content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'background:rgba(255,255,255,0.05);border:1px solid #333;color:#fff;border-radius:8px;padding:8px 16px;font-family:Barlow Condensed,sans-serif;font-size:14px;font-weight:700;cursor:pointer;">← HOME</button>',
    'background:transparent;border:1px solid #444;color:#aaa;border-radius:8px;padding:8px 16px;font-family:Barlow Condensed,sans-serif;font-size:14px;font-weight:700;cursor:pointer;">← HOME</button>'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
