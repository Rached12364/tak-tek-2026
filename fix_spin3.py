content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '<img src="tuns.png" style="width:180px;height:180px;object-fit:contain;animation:quiz-spin 4s linear infinite;">',
    '<img src="tuns.png" id="quiz-logo-spin" style="width:180px;height:180px;object-fit:contain;">'
)
# Ajouter JS pour animer via setInterval
spin_js = '''
<script>
var quizAngle = 0;
setInterval(function(){
  var el = document.getElementById("quiz-logo-spin");
  if(el) { quizAngle += 2; el.style.transform = "rotate(" + quizAngle + "deg)"; }
}, 20);
</script>
'''
content = content.replace('</body>', spin_js + '</body>')
open('index.html','w',encoding='utf-8').write(content)
print('OK')
