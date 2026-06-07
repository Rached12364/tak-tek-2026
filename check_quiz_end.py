content = open('index.html','r',encoding='utf-8').read()
idx = content.find("showPage('quiz')")
print(content[idx+400:idx+700])
