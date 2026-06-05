content = open('index.html', 'r', encoding='utf-8').read()
# Count how many times startTunisiaXI is defined
import re
matches = [m.start() for m in re.finditer('function startTunisiaXI', content)]
print('Found:', len(matches), 'at positions:', matches)
# Also check tn-player-list count
matches2 = [m.start() for m in re.finditer('tn-player-list', content)]
print('tn-player-list found:', len(matches2))
