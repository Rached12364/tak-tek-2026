content = open('index.html','r',encoding='utf-8').read()
# Enlever le blocage animation sur btn-icon
content = content.replace('.btn-icon{animation:none !important;}', '.btn-icon{animation:spin 8s linear infinite;}')
open('index.html','w',encoding='utf-8').write(content)
print("OK")
