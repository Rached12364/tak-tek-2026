content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'src="logo-tunisia.png" style="width:110px;height:110px;object-fit:contain;"',
    'src="logo-tunisia.png" style="width:160px;height:160px;object-fit:contain;animation:spin 6s linear infinite;"'
)
# Ajouter l animation spin si pas encore presente
if '@keyframes spin' not in content:
    content = content.replace(
        '</style>',
        '@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }\n</style>'
    )
open('index.html','w',encoding='utf-8').write(content)
print("OK")
