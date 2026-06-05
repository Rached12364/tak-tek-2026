# Write Tunisia script as separate file
script = open('index.html', 'r', encoding='utf-8').read()
# Find and extract lines 725-750 to see what's broken
lines = script.split('\n')
for i, l in enumerate(lines[725:755], start=726):
    print(i, repr(l[:120]))
