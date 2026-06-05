content = open('index.html','r',encoding='utf-8').read()
lines = content.split('\n')
for i in [728,729,730,731,732,733,734,735,736,737]:
    print(i+1, repr(lines[i]))
