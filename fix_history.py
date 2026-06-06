content = open('index.html','r',encoding='utf-8').read()
old_showpage = '''function showPage(page) {'''
new_showpage = '''function showPage(page) {
  history.pushState({page: page}, '', '#' + page);'''
content = content.replace(old_showpage, new_showpage)
# Ajouter listener pour le bouton retour navigateur
old_init = '''function init() { showPage("home"); return; }'''
new_init = '''function init() {
  // Gerer le bouton retour navigateur
  window.addEventListener('popstate', function(e) {
    if(e.state && e.state.page) {
      showPage(e.state.page);
    } else {
      showPage('home');
    }
  });
  // Charger la page depuis le hash si present
  var hash = window.location.hash.replace('#','');
  if(hash) { showPage(hash); } else { showPage("home"); }
  return;
}'''
content = content.replace(old_init, new_init)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
