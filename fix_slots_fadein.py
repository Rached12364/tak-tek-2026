content = open('index.html','r',encoding='utf-8').read()
# Ajouter fadeIn sur tous les slots tn-slot
import re
def add_fadein(match):
    style = match.group(0)
    if 'tn-slot-fadein' not in style:
        style = style.replace('border-radius:10px;display:flex', 
                             'border-radius:10px;animation:tn-slot-fadein 0.8s ease both;display:flex')
    return style
content = re.sub(r'id="tn-slot-[^"]+"\s+style="[^"]*border-radius:10px;display:flex', 
                 lambda m: m.group(0).replace('border-radius:10px;display:flex', 
                 'border-radius:10px;animation:tn-slot-fadein 0.8s ease both;display:flex'), content)
open('index.html','w',encoding='utf-8').write(content)
print('OK slots fadein')
