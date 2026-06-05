content = open('index.html', 'r', encoding='utf-8').read()
content = content.replace(
    '<span style="font-size:50px;">&#9917;</span>\n        BEST XI',
    '''<div style="background:linear-gradient(135deg,#1a1200,#2a1f00);border-radius:8px;padding:6px 20px;border-bottom:2px solid #FFD700;margin-bottom:4px;"><span style="font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:13px;font-weight:900;letter-spacing:3px;">MONDE</span></div>
<img src="https://tse2.mm.bing.net/th/id/OIP.IVLQgNj1yYrd-UO710ihOgHaGQ?pid=Api&P=0&h=180" style="width:160px;height:140px;object-fit:contain;border-radius:12px;transition:transform 0.4s ease;filter:drop-shadow(0 10px 30px rgba(255,215,0,0.6));" class="btn-icon">
        BEST XI''',
    1
)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
