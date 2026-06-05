content = open('index.html', 'r', encoding='utf-8').read()
# Hide HOME button when on home page - add to showPage
content = content.replace(
    'function showPage(page) {',
    '''function showPage(page) {
  var hbtn = document.getElementById("home-nav-btn");
  if(hbtn) hbtn.style.display = page==="home" ? "none" : "block";'''
, 1)
# Add id to the HOME button
import re
content = re.sub(
    r'<div style="position:fixed;top:12px;(left|right):12px;z-index:[0-9]+;">\s*<button onclick="showPage\([\'"]home[\'"]\)"',
    '<div style="position:fixed;top:12px;\\1:12px;z-index:999;" id="home-nav-btn"><button onclick="showPage(\'home\')"',
    content
)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
