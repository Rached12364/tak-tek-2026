content = open('index.html','r',encoding='utf-8').read()
# Chercher le style des slots tunisia
idx = content.find('tn-slot-gk')
print(content[idx-200:idx+200])
