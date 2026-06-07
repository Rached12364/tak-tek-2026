content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'onclick="showPage(\'bestxi\')" class="home-btn"',
    'onclick="showPage(\'bestxi\')" class="home-btn" style="animation:fadeInUp 0.6s ease both;animation-delay:0.1s;opacity:0;"'
)
content = content.replace(
    'onclick="showPage(\'tierlist\')" class="home-btn"',
    'onclick="showPage(\'tierlist\')" class="home-btn" style="animation:fadeInUp 0.6s ease both;animation-delay:0.3s;opacity:0;"'
)
content = content.replace(
    'onclick="showPage(\'quiz\')" class="home-btn"',
    'onclick="showPage(\'quiz\')" class="home-btn" style="animation:fadeInUp 0.6s ease both;animation-delay:0.5s;opacity:0;"'
)
content = content.replace(
    'onclick="showPage(\'tunisia\');startTunisiaXI();" class="home-btn"',
    'onclick="showPage(\'tunisia\');startTunisiaXI();" class="home-btn" style="animation:fadeInUp 0.6s ease both;animation-delay:0.7s;opacity:0;"'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
