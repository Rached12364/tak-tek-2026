content = open('index.html', 'r', encoding='utf-8').read()
content = content.replace(
    '<span style="font-size:50px;">&#127942;</span>\n        TIER LIST',
    '''<div style="background:linear-gradient(135deg,#001a0d,#002a15);border-radius:8px;padding:6px 20px;border-bottom:2px solid #00ff88;margin-bottom:4px;"><span style="font-family:Barlow Condensed,sans-serif;color:#00ff88;font-size:13px;font-weight:900;letter-spacing:3px;">MONDE</span></div>
<img src="https://tse4.mm.bing.net/th/id/OIP.MlP5lDLcWPG0vdny3RILSQHaGA?pid=Api&P=0&h=180" style="width:160px;height:140px;object-fit:contain;border-radius:12px;transition:transform 0.4s ease;filter:drop-shadow(0 10px 30px rgba(0,255,136,0.6));" class="btn-icon">
        TIER LIST''',
    1
)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
