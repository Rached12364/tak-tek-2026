content = open('index.html','r',encoding='utf-8').read()
# Appeler tnRender au chargement de la page tunisia
content = content.replace(
    'function startTunisiaXI() { tnStep=0; tnPicks={}; tnRender(); }',
    'function startTunisiaXI() { tnStep=0; tnPicks={}; setTimeout(tnRender,50); }'
)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
