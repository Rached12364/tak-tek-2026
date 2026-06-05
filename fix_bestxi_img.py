content = open('index.html', 'r', encoding='utf-8').read()
# Replace the soccer ball emoji/img with the FIFA best XI image + MONDE badge
old_ball = '<img src="https://preview.redd.it/a16ix7qsskl31.jpg?auto=webp&s=782617e640648eeba26253e321cd7507c4c357aa" style="width:120px;height:120px;object-fit:contain;border-radius:12px;transition:transform 0.4s ease;filter:drop-shadow(0 10px 20px rgba(255,215,0,0.5));" class="btn-icon">'
new_ball = '''<div style="background:linear-gradient(135deg,#1a1200,#2a1f00);border-radius:8px;padding:6px 20px;border-bottom:2px solid #FFD700;margin-bottom:8px;"><span style="font-family:Barlow Condensed,sans-serif;color:#FFD700;font-size:13px;font-weight:900;letter-spacing:3px;">MONDE</span></div>
<img src="https://tse2.mm.bing.net/th/id/OIP.IVLQgNj1yYrd-UO710ihOgHaGQ?pid=Api&P=0&h=180" style="width:160px;height:140px;object-fit:contain;border-radius:12px;transition:transform 0.4s ease;filter:drop-shadow(0 10px 20px rgba(255,215,0,0.6));" class="btn-icon">'''
content = content.replace(old_ball, new_ball, 1)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
