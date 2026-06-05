content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'https://tse3.explicit.bing.net/th/id/OIP.0LOfaCtIFH5N4u4x106IAQAAAA?pid=Api&P=0&h=180',
    'https://tse3.mm.bing.net/th/id/OIP.6p8eYVZJWiJ8vOqFAhnJ4wHaIl?pid=Api&P=0&h=180'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
