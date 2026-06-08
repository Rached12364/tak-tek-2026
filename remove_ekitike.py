content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '  {name:"Ekitike", img:"https://game-assets.fut.gg/cdn-cgi/image/quality=85,width=300,format=auto/2026/player-item/26-117697801.c539b4a8ce047b89c2889db38d43011deebf6abd5357911afeaf2ff9588633a8.webp"},\n  {name:',
    '  {name:'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
