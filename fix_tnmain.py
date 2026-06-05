content = open('index.html','r',encoding='utf-8').read()
# Nuclear option: force tn-main to have explicit height
content = content.replace(
    '<div id="tn-main" style="display:flex;flex-direction:row;flex:1;min-height:0;overflow:hidden;">',
    '<div id="tn-main" style="display:flex;flex-direction:row;width:100%;height:calc(100vh - 73px);overflow:hidden;">'
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
