import re
content = open('index.html', 'r', encoding='utf-8').read()
# Remove old Tunisia script block
content = re.sub(r'<script>\s*var TN_STEPS=\[.*?</script>', '<script src="tunisia.js"></script>', content, flags=re.DOTALL)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
