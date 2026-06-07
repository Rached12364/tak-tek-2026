content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    '''        <div style="margin-top:10px;background:#00C853;color:#000;font-size:12px;font-weight:700;padding:6px 12px;border-radius:20px;display:inline-block;">7 QUESTIONS</div>
      <!-- Carte Youssef Msakni -->''',
    '''        <div style="margin-top:10px;background:#00C853;color:#000;font-size:12px;font-weight:700;padding:6px 12px;border-radius:20px;display:inline-block;">7 QUESTIONS</div>
      </div>
      <!-- Carte Youssef Msakni -->'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
