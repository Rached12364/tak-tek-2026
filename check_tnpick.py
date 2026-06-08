content = open('index.html','r',encoding='utf-8').read()
# Trouver la fonction qui place le joueur dans le slot
idx = content.find('function tnPick')
print('tnPick position:', idx)
idx2 = content.find('tnShowRecap')
print('tnShowRecap position:', idx2)
idx3 = content.find('tn-slot-')
print('tn-slot usage:', idx3)
# Chercher comment on assigne l image au slot
idx4 = content.find('slot.innerHTML')
print('slot.innerHTML:', idx4)
idx5 = content.find('tnSlot')
print('tnSlot:', idx5)
