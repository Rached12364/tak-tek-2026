import re
content = open('index.html', 'r', encoding='utf-8').read()
matches = [m.start() for m in re.finditer('id="page-tunisia"', content)]
print('page-tunisia found:', len(matches), 'at:', matches)
matches2 = [m.start() for m in re.finditer('id="tn-selection"', content)]
print('tn-selection found:', len(matches2), 'at:', matches2)
