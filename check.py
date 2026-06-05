content = open('index.html','r',encoding='utf-8').read()
lines = content.split('\n')
for i, line in enumerate(lines):
    if 'tn-panel' in line and 'innerHTML' in line:
        print('innerHTML ligne:', i+1)
    if i in range(1773, 1779):
        print(str(i+1)+':', line[:100])
