lines = open('index.html','r',encoding='utf-8').read().split('\n')
for i in range(1555, 1565):
    print(f"L{i+1}: {lines[i][:300]}")
