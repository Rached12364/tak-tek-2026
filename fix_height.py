content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'tn.style.display=page==="tunisia"?"flex":"none";if(page==="tunisia"){tn.style.flexDirection="column";}',
    'tn.style.display=page==="tunisia"?"flex":"none";if(page==="tunisia"){tn.style.flexDirection="column";tn.style.height="100vh";}'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
