import re
content = open("index.html","r",encoding="utf-8").read()
# Rebuild all dots with proper absolute positioning
dots = [
  ("gk",  "GK",    42, 8),
  ("rb",  "RB",    78, 26),
  ("cb1", "CB",    58, 26),
  ("cb2", "CB",    27, 26),
  ("lb",  "LB",    8,  26),
  ("cdm", "CDM",   42, 46),
  ("cm1", "CM",    20, 58),
  ("cm2", "CM",    64, 58),
  ("rw",  "RW",    78, 74),
  ("lw",  "LW",    8,  74),
  ("st",  "ST",    42, 80),
  ("coach","COACH",42, 93),
]
new_dots = ""
for key, pos, x, y in dots:
    new_dots += f'<div id="tn-dot-{key}" style="position:absolute;left:{x}%;top:{y}%;transform:translate(-50%,-50%);width:56px;height:42px;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;border:2px dashed rgba(255,255,255,0.2);background:rgba(0,0,0,0.4);transition:all 0.3s;"><div style="font-family:Barlow Condensed,sans-serif;font-size:9px;font-weight:700;letter-spacing:1px;color:rgba(255,255,255,0.5);">{pos}</div><div class="dot-label" style="font-family:Barlow Condensed,sans-serif;font-size:8px;color:rgba(255,255,255,0.35);margin-top:1px;text-align:center;max-width:52px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;"></div></div>'
# Replace all dots block
content = re.sub(
    r'<div id="tn-dot-gk">.*?</div>\s*</div>\s*</div>\s*<!-- RIGHT',
    new_dots + '\n      </div>\n    </div>\n\n    <!-- RIGHT',
    content,
    flags=re.DOTALL
)
# Remove the white HOME button duplicate
content = re.sub(
    r'<button[^>]*>← HOME</button>\s*<button[^>]*>← HOME</button>',
    '<button onclick="showPage(\'home\')" style="background:transparent;border:1px solid #444;color:#fff;border-radius:8px;padding:8px 16px;font-family:Barlow Condensed,sans-serif;font-size:14px;font-weight:700;cursor:pointer;flex-shrink:0;">← HOME</button>',
    content
)
open("index.html","w",encoding="utf-8").write(content)
print("done")
