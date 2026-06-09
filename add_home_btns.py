content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'id="page-home" style="display:none;width:100%;min-height:100vh;background:#0a0a0a;flex-direction:column;position:relative;z-index:1;;position:relative;;overflow-y:auto;">',
    '''id="page-home" style="display:none;width:100%;min-height:100vh;background:#0a0a0a;flex-direction:column;position:relative;z-index:1;;position:relative;;overflow-y:auto;">
  <div style="position:absolute;top:12px;right:12px;z-index:100;display:flex;gap:8px;">
    <div id="profile-display-home" onclick="document.getElementById('profile-modal').style.display='flex'" style="background:rgba(0,0,0,0.85);border:1px solid #00C853;color:#00C853;padding:7px 14px;border-radius:6px;cursor:pointer;font-family:'Barlow Condensed',sans-serif;font-size:13px;font-weight:700;">👤 PROFIL</div>
    <div onclick="showPage('leaderboard');loadLeaderboard();" style="background:rgba(0,0,0,0.85);border:1px solid #FFD700;color:#FFD700;padding:7px 14px;border-radius:6px;cursor:pointer;font-family:'Barlow Condensed',sans-serif;font-size:13px;font-weight:700;">🏆 TOP 10</div>
  </div>'''
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
