content = open('index.html', 'r', encoding='utf-8').read()
# Fix: don't call startTunisiaXI from showPage, use setTimeout instead
content = content.replace(
    'if(page==="tunisia" && typeof startTunisiaXI==="function") { startTunisiaXI(); }',
    'if(page==="tunisia" && typeof startTunisiaXI==="function") { setTimeout(startTunisiaXI, 50); }'
)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
