content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'onclick="showPage(\'quiz\')" class="home-btn"',
    'onclick="showPage(\'quiz\')" class="home-btn" onmouseover="this.style.transform=\'scale(1.05)\'" onmouseout="this.style.transform=\'scale(1)\'"'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
