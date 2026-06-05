content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'src="https://city-png.b-cdn.net/thumbnail/thumbnail_public/uploads/preview/hd-logo-of-tunisia-national-football-team-transparent-png-701751712400875ip5tcz8e38.png" style="width:110px;height:110px;object-fit:contain;mix-blend-mode:screen;"',
    'src="logo-tunisia.png" style="width:110px;height:110px;object-fit:contain;"'
)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
