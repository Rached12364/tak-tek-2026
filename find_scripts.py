content = open('index.html','r',encoding='utf-8').read()
# Chercher tous les tags script
import re
scripts = [(m.start(), content[m.start():m.start()+80]) for m in re.finditer(r'<script', content)]
for pos, text in scripts:
    print(f'Position {pos}: {text[:80]}')
    print('---')
