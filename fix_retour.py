content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    "'>??? RETOUR</button>",
    "'>&#8592; RETOUR</button>"
)
open('index.html','w',encoding='utf-8').write(content)
print("OK")
