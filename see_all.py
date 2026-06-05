content = open('index.html','r',encoding='utf-8').read()
# Où est tn-player-list ?
idx = content.find('id="tn-player-list"')
print("PLAYER-LIST:", repr(content[idx-200:idx+100]))
# Structure complète de tn-main
tm = content.find('<div id="tn-main"')
print("\nTN-MAIN children (first 1500):", repr(content[tm:tm+1500]))
