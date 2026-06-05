content = open('index.html','r',encoding='utf-8').read()
# Remplacer animation inline par une classe
content = content.replace(
    'src="logo-tunisia.png" style="width:160px;height:160px;object-fit:contain;animation:spin 6s linear infinite;"',
    'src="logo-tunisia.png" class="logo-spin" style="width:160px;height:160px;object-fit:contain;"'
)
# Ajouter la classe spin dans le style
if '.logo-spin' not in content:
    content = content.replace(
        '@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }',
        '@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }\n.logo-spin { animation: spin 6s linear infinite; }'
    )
open('index.html','w',encoding='utf-8').write(content)
print("OK")
