content = open('index.html','r',encoding='utf-8').read()
start = content.find('function showPage(page) {')
print(content[start:start+400])
