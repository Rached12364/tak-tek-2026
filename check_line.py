content = open('index.html','r',encoding='utf-8').read()
lines = content.split('\n')
for i in range(1963, 1972):
    print(str(i+1)+':', lines[i][:120])
