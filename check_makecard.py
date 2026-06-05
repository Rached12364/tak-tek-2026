lines = open('index.html','r',encoding='utf-8').read().split('\n')
for i in range(1530, 1552):
    print(f"L{i+1}: {lines[i][:200]}")
