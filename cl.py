content = open('index_backup_v2.html','r',encoding='utf-8').read()
idx = content.find('id="left"')
print(repr(content[idx-400:idx+50]))
