content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''    slot.style.overflow = "visible";
    slot.style.height = "auto";
    slot.innerHTML = "<div style='display:flex;flex-direction:column;align-items:center;'><img src='"+p.img+"' style='width:66px;height:80px;object-fit:cover;border-radius:8px;animation:tn-fly-in 0.5s ease forwards;'><div style='color:#fff;font-family:Barlow Condensed,sans-serif;font-size:8px;font-weight:900;text-align:center;margin-top:3px;text-shadow:1px 1px 2px #000;white-space:nowrap;letter-spacing:0.5px;'>"+p.name.split(" ")[p.name.split(" ").length-1]+"</div></div>";''',
    '''    slot.style.overflow = "visible";
    slot.innerHTML = "<div style='position:relative;width:66px;'><img src='"+p.img+"' style='width:66px;height:88px;object-fit:cover;border-radius:8px;animation:tn-fly-in 0.5s ease forwards;display:block;'><div style='position:absolute;bottom:0;left:0;right:0;background:rgba(0,0,0,0.75);color:#fff;font-family:Barlow Condensed,sans-serif;font-size:8px;font-weight:900;text-align:center;padding:2px 0;border-radius:0 0 8px 8px;letter-spacing:0.5px;'>"+p.name.split(" ").slice(-1)[0]+"</div></div>";'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
