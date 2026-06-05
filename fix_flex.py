content = open('index.html','r',encoding='utf-8').read()
# Fix tn-main to be side by side
old = '<div id="tn-main" style="display:flex;flex-direction:row;height:calc(100vh - 73px);overflow:hidden;width:100%;">'
new = '<div id="tn-main" style="display:flex;flex-direction:row;height:calc(100vh - 73px);overflow:hidden;width:100%;flex:1;">'
if old in content:
    content = content.replace(old, new)
    print("found v1")
else:
    # Try other variants
    import re
    content = re.sub(
        r'<div id="tn-main"[^>]*>',
        '<div id="tn-main" style="display:flex;flex-direction:row;height:calc(100vh - 73px);overflow:hidden;width:100%;">',
        content
    )
    print("replaced via regex")
# Fix pitch div - must have height:100%
content = re.sub(
    r'(id="tn-main"[^>]*>)\s*<div style="[^"]*linear-gradient[^"]*0b3d1f[^"]*"',
    lambda m: m.group(0).replace('<div style="', '<div style="height:100%;'),
    content
)
open('index.html','w',encoding='utf-8').write(content)
print('done')
