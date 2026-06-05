import re
content = open('index.html', 'r', encoding='utf-8').read()
# Find both occurrences
matches = [m.start() for m in re.finditer('tn-player-list', content)]
for pos in matches:
    print(pos, repr(content[pos-50:pos+100]))
    print('---')
