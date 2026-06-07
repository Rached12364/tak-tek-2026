content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'https://static.flashscore.com/res/image/data/EL8CsfBr-2X9WEIyE.png',
    'firas_chaouat.jpg'
)
content = content.replace(
    'https://static.flashscore.com/res/image/data/6V5W3QyS-YDy6iaVc.png',
    'youcef_belaili.jpg'
)
content = content.replace(
    'https://static.flashscore.com/res/image/data/OCwL77FG-4WhOr90b.png',
    'youssef_msakni.jpg'
)
content = content.replace(
    'https://static.flashscore.com/res/image/data/YNOJHqwS-ltYaYaBP.png',
    'raki_aouani.jpg'
)
content = content.replace(
    'https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Faouzi_Benzarti_au_Raja_%28cropped%29.jpg/960px-Faouzi_Benzarti_au_Raja_%28cropped%29.jpg',
    'faouzi_benzarti.jpg'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
