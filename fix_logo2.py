content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'src="https://city-png.b-cdn.net/thumbnail/thumbnail_public/uploads/preview/hd-logo-of-tunisia-national-football-team-transparent-png-701751712400875ip5tcz8e38.png" style="width:110px;height:110px;object-fit:contain;mix-blend-mode:screen;filter:brightness(1.8) contrast(1.2);"',
    'src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Football_Federation_of_Tunisia_logo.svg/200px-Football_Federation_of_Tunisia_logo.svg.png" style="width:110px;height:110px;object-fit:contain;mix-blend-mode:screen;filter:brightness(1.5);"'
)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
