content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'src="logo-tunisia.png" style="width:160px;height:160px;object-fit:contain;animation:spin 6s linear infinite;"',
    'src="logo-tunisia.png" class="btn-icon" style="width:160px;height:160px;object-fit:contain;"'
)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
