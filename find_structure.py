import re
content = open('index.html','r',encoding='utf-8').read()
# Trouver et extraire le bloc #right complet
right_match = re.search(r'<div id="right"[^>]*>.*?</div>\s*<!-- END RIGHT', content, re.DOTALL)
if not right_match:
    # Essayer sans commentaire de fin
    # Compter les divs pour trouver la fermeture
    start = content.find('<div id="right"')
    depth = 0
    i = start
    while i < len(content):
        if content[i:i+4] == '<div':
            depth += 1
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                end = i + 6
                break
        i += 1
    right_block = content[start:end]
    print("RIGHT block found, length:", len(right_block))
    print("First 100:", repr(right_block[:100]))
    print("Last 50:", repr(right_block[-50:]))
    # Trouver la fermeture de tn-main
    tn_close = content.find('</div>', content.find('id="tn-main"'))
    print("tn-main closes at:", tn_close)
    print("Context:", repr(content[tn_close-50:tn_close+50]))
