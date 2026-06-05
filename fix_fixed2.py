content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'var fixedBtns = document.querySelectorAll(\'div[style*="position:fixed"]\');\n  fixedBtns.forEach(function(b){b.style.display=page==="tunisia"||page==="home"?"none":"block";});',
    'var fixedBtns = document.querySelectorAll(\'div[style*="position:fixed"]\');\n  fixedBtns.forEach(function(b){b.style.display=page==="tunisia"?"none":"";});'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
