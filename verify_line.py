content = open('index.html','r',encoding='utf-8').read()
lines = content.split('\n')
print(lines[2014][:150])
