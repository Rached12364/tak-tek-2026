content = open('index.html','r',encoding='utf-8').read()
# 1. Fixer le spin - ajouter directement dans le style inline du logo tunisia
content = content.replace(
    'src="logo-tunisia.png" class="logo-spin" style="width:160px;height:160px;object-fit:contain;"',
    'src="logo-tunisia.png" style="width:160px;height:160px;object-fit:contain;animation:spin 6s linear infinite;"'
)
# 2. S assurer que spin est dans le CSS et ne touche pas btn-icon
if '@keyframes spin' not in content:
    content = content.replace('</style>', '@keyframes spin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}\n</style>')
# 3. Empecher spin sur btn-icon
if '.btn-icon{animation:none' not in content and 'btn-icon { animation: none' not in content:
    content = content.replace('</style>', '.btn-icon{animation:none !important;}\n</style>')
open('index.html','w',encoding='utf-8').write(content)
print("OK")
