content = open('index.html','r',encoding='utf-8').read()
old = '''function showPage(page) {
  history.pushState({page: page}, '', '#' + page);
  document.querySelectorAll('[id^=page-]').forEach(function(el){
    el.style.display='none';
  });
  var pg = document.getElementById('page-'+page);
  if(pg) {
    if(page==='quiz') pg.style.display='flex';
    else pg.style.display='flex';
  }
  return;'''
new = '''function showPage(page) {
  history.pushState({page: page}, '', '#' + page);
  document.querySelectorAll('[id^=page-]').forEach(function(el){
    el.style.display='none';
  });
  var pg = document.getElementById('page-'+page);
  if(pg) { pg.style.display='flex'; }'''
content = content.replace(old, new)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
