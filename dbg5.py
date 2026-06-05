import re
content = open('index.html', 'r', encoding='utf-8').read()
# Check renderTNStep for tn-player-list
idx = content.find('function renderTNStep')
print(repr(content[idx:idx+400]))
