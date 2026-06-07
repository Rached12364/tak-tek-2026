content = open('index.html','r',encoding='utf-8').read()
# Chercher le keyframe spin original
idx = content.find('@keyframes spin')
print(content[idx:idx+150])
