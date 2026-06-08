content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'https://media.cnn.com/api/v1/images/stellar/prod/01jd374k9mfg1d42nn027sha2a.jpg?c=16x9&q=h_833,w_1480,c_fill',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/2022-07-30_Fu%C3%9Fball%2C_M%C3%A4nner%2C_DFL-Supercup%2C_RB_Leipzig_-_FC_Bayern_M%C3%BCnchen_1DX_3166_by_Stepro.jpg/960px-2022-07-30_Fu%C3%9Fball%2C_M%C3%A4nner%2C_DFL-Supercup%2C_RB_Leipzig_-_FC_Bayern_M%C3%BCnchen_1DX_3166_by_Stepro.jpg'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
