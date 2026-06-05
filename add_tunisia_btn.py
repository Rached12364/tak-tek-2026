content = open('index.html','r',encoding='utf-8').read()
btn_tunisia = '''
      <button onclick="showPage('tunisia');startTunisiaXI();" style="width:250px;height:380px;background:linear-gradient(135deg,rgba(26,26,26,0.9),rgba(34,34,34,0.9));border:2px solid #E70013;border-radius:16px;color:#E70013;font-family:Barlow Condensed,sans-serif;font-size:24px;font-weight:900;letter-spacing:3px;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;transition:transform 0.2s;backdrop-filter:blur(4px);" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        <div style="background:#E70013;color:#fff;font-size:11px;font-weight:800;letter-spacing:4px;padding:4px 14px;border-radius:4px;margin-bottom:4px;">TUNISIE</div>
        <img src="https://city-png.b-cdn.net/thumbnail/thumbnail_public/uploads/preview/hd-logo-of-tunisia-national-football-team-transparent-png-701751712400875ip5tcz8e38.png" style="width:110px;height:110px;object-fit:contain;mix-blend-mode:screen;">
        <span>BEST XI</span>
        <p style="font-size:13px;font-weight:400;color:#ccc;text-align:center;padding:0 16px;letter-spacing:1px;line-height:1.4;">Chaque fois 3 joueurs par poste, choisis 1 pour former ton equipe tunisienne</p>
      </button>'''
# Inserer apres le bouton tierlist (apres la derniere </button> de la ligne 736)
anchor = "onmouseout=\"this.style.transform='scale(1)'\">\n        <div style=\"background:#00ff88"
insert_after = "</button>"
# Trouver le bouton tierlist et inserer apres
tierlist_btn_start = content.find("onclick=\"showPage('tierlist')\"")
tierlist_btn_end = content.find("</button>", tierlist_btn_start) + len("</button>")
content = content[:tierlist_btn_end] + btn_tunisia + content[tierlist_btn_end:]
open('index.html','w',encoding='utf-8').write(content)
print("OK - bouton Tunisia ajoute")
