content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'id="page-quiz" style="display:none;width:100%;min-height:100vh;background:#0a0a0a;flex-direction:column;align-items:center;padding:40px 20px;"',
    'id="page-quiz" style="display:none;width:100%;min-height:100vh;background:#0a0a0a;flex-direction:column;align-items:center;padding:40px 20px;box-sizing:border-box;"'
)
# Fix showPage pour mettre flex sur quiz
old_show = "function showPage(page) {\n  history.pushState({page: page}, '', '#' + page);"
new_show = """function showPage(page) {
  history.pushState({page: page}, '', '#' + page);
  document.querySelectorAll('[id^=page-]').forEach(function(el){
    el.style.display='none';
  });
  var pg = document.getElementById('page-'+page);
  if(pg) {
    if(page==='quiz') pg.style.display='flex';
    else pg.style.display='flex';
  }
  return;"""
content = content.replace(old_show, new_show)
# Supprimer l ancien code showPage apres
old_end = "  var pages = ['home','bestxi','tierlist','tunisia','quiz'];"
content = content.replace(old_end, "  // pages handled above")
open('index.html','w',encoding='utf-8').write(content)
print('OK')
