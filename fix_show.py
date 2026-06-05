import re
content = open('index.html', 'r', encoding='utf-8').read()
# Fix showPage function - remove the broken insertion
content = re.sub(r'var tp = document\.getElementById\("page-tunisia"\).*?var home =\s*\nvar TUNISIA_STEPS', 
    'var tp = document.getElementById("page-tunisia"); if(tp) tp.style.display = page==="tunisia" ? "flex" : "none";\n  var home =\nvar TUNISIA_STEPS',
    content, flags=re.DOTALL)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
