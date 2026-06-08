content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''    slot.innerHTML = "<img src='"+p.img+"' style='width:66px;height:88px;object-fit:cover;border-radius:8px;animation:tn-fly-in 0.5s ease forwards;'>";''',
    '''    slot.innerHTML = "<div style='display:flex;flex-direction:column;align-items:center;'><img src='"+p.img+"' style='width:66px;height:80px;object-fit:cover;border-radius:8px;animation:tn-fly-in 0.5s ease forwards;'><div style='color:#fff;font-family:Barlow Condensed,sans-serif;font-size:9px;font-weight:900;text-align:center;margin-top:2px;text-shadow:0 0 4px #000;background:rgba(0,0,0,0.6);padding:1px 3px;border-radius:3px;max-width:70px;overflow:hidden;white-space:nowrap;'>"+p.name+"</div></div>";'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
