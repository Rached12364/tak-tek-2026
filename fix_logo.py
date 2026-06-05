content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'style="width:110px;height:110px;object-fit:contain;mix-blend-mode:multiply;filter:contrast(1.1);"',
    'style="width:110px;height:110px;object-fit:contain;mix-blend-mode:screen;filter:brightness(1.8) contrast(1.2);"'
)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
