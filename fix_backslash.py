content = open('index.html', 'r', encoding='utf-8').read()
# Fix the broken Tunisia button onclick - backslashes cause syntax error
content = content.replace(
    "onclick=\"showPage(\\'tunisia\\');startTunisiaXI();\"",
    'onclick="showPage(\'tunisia\');startTunisiaXI();"'
)
# Also fix tierlist button
content = content.replace(
    "onclick=\"showPage(\\'tierlist\\')\"",
    "onclick=\"showPage('tierlist')\""
)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
