content = open('index.html', 'r', encoding='utf-8').read()
import re
# Make all pages scrollable
content = re.sub(r'(id="page-home" style="[^"]*)"', lambda m: m.group(0).replace('overflow-y:auto', '').rstrip('"') + ';overflow-y:auto;"', content)
content = re.sub(r'(id="wrap" style="[^"]*)"', lambda m: m.group(0).replace('overflow-y:auto', '').rstrip('"') + ';overflow-y:auto;"', content)
content = re.sub(r'(id="page-tierlist" style="[^"]*)"', lambda m: m.group(0).replace('overflow-y:auto', '').rstrip('"') + ';overflow-y:auto;"', content)
# Fix body/html
content = content.replace('html, body {', 'html { height:100%; } body { min-height:100%; overflow-y:auto; /*')
content = content.replace('overflow: hidden;', 'overflow-y: auto;')
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
