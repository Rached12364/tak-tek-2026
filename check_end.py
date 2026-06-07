content = open('index.html','r',encoding='utf-8').read()
print('Taille fichier:', len(content))
print('--- FIN DU FICHIER ---')
print(content[-500:])
