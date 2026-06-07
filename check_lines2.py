content = open('index.html','r',encoding='utf-8').read()
lines = content.split('\n')
for i in range(1980, 2010):
    print(str(i+1)+':', lines[i][:120])
