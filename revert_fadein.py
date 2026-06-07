content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'onclick="showPage(\'bestxi\')" class="home-btn" style="animation:fadeInUp 0.6s ease both;animation-delay:0.1s;opacity:0;"',
    'onclick="showPage(\'bestxi\')" class="home-btn"'
)
content = content.replace(
    'onclick="showPage(\'tierlist\')" class="home-btn" style="animation:fadeInUp 0.6s ease both;animation-delay:0.3s;opacity:0;"',
    'onclick="showPage(\'tierlist\')" class="home-btn"'
)
content = content.replace(
    'onclick="showPage(\'quiz\')" class="home-btn" style="animation:fadeInUp 0.6s ease both;animation-delay:0.5s;opacity:0;"',
    'onclick="showPage(\'quiz\')" class="home-btn"'
)
content = content.replace(
    'onclick="showPage(\'tunisia\');startTunisiaXI();" class="home-btn" style="animation:fadeInUp 0.6s ease both;animation-delay:0.7s;opacity:0;"',
    'onclick="showPage(\'tunisia\');startTunisiaXI();" class="home-btn"'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
