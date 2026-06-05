content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'id="page-tunisia" style="display:none;width:100%;height:100vh;background:#111;flex-direction:column;overflow:hidden;"',
    'id="page-tunisia" style="display:none;width:100%;height:100vh;background:#111;overflow:hidden;"'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
