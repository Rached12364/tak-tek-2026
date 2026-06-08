content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''  if(slot) {
    slot.style.border = "2px solid #E70013";
    slot.innerHTML = "<img src='"+p.img+"' style='width:66px;height:88px;object-fit:cover;border-radius:8px;'>";''',
    '''  if(slot) {
    slot.style.border = "2px solid #00C853";
    slot.style.animation = "tn-slot-selected 0.6s ease forwards";
    slot.innerHTML = "<img src='"+p.img+"' style='width:66px;height:88px;object-fit:cover;border-radius:8px;animation:tn-fly-in 0.5s ease forwards;'>";
    setTimeout(function(){ slot.style.animation = ""; }, 600);'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
