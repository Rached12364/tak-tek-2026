content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    "font-size:8px;font-weight:900;text-align:center;padding:2px 0;border-radius:0 0 8px 8px;letter-spacing:0.5px;'>"+'"'+"+p.name.split",
    "font-size:11px;font-weight:900;text-align:center;padding:3px 0;border-radius:0 0 8px 8px;letter-spacing:0.5px;'>"+'"'+"+p.name.split"
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
