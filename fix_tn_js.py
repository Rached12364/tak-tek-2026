js = open('tunisia.js', 'r', encoding='utf-8').read()
# Fix the onerror attribute - replace single quotes inside onerror
js = js.replace(
    "onerror=\"this.style.display='none'\"",
    'onerror="this.style.display=\'none\'"'
)
# Actually let's just rewrite the imgHtml line completely safe
import re
js = re.sub(
    r"var imgHtml=pl\.img\?.*?:'';",
    "var imgHtml=pl.img?'<img src=\"'+pl.img+'\" style=\"width:100%;height:100%;object-fit:cover;object-position:top;\">':'';",
    js
)
open('tunisia.js', 'w', encoding='utf-8').write(js)
print('done')
