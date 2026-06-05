lines = open('index.html','r',encoding='utf-8').read().split('\n')
# Chercher le </script> fermant le bloc tierlist
for i,l in enumerate(lines):
    if '</script>' in l:
        print(f"L{i+1}: {l[:200]}")
