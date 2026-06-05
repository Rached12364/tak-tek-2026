content = open('index.html', 'r', encoding='utf-8').read()
# Fix: add class home-btn to Tunisia button too and fix pulse animation selector
# The issue is the Tunisia button selector doesn't match. Let's add explicit animation via class.
old_style = '''button[style*="FFD700"][style*="border:2px solid"] {
  animation: pulse-border-gold 2.5s ease-in-out infinite;
}
/* Green card pulse */
button[style*="00ff88"][style*="border:2px solid"] {
  animation: pulse-border-green 2.5s ease-in-out infinite;
}
/* Red card pulse */
button[style*="E70013"][style*="border:2px solid"] {
  animation: pulse-border-red 2.5s ease-in-out infinite;
}'''
new_style = '''.home-btn-gold { animation: pulse-border-gold 2.5s ease-in-out infinite !important; }
.home-btn-green { animation: pulse-border-green 2.5s ease-in-out infinite !important; }
.home-btn-red { animation: pulse-border-red 2.5s ease-in-out infinite !important; }'''
content = content.replace(old_style, new_style, 1)
# Add classes to buttons
import re
# Gold button (startBestXI)
content = re.sub(
    r'onclick="startBestXI\(\)" class="home-btn"',
    'onclick="startBestXI()" class="home-btn home-btn-gold"',
    content
)
# Green button (tierlist)
content = re.sub(
    r'onclick="showPage\(\'tierlist\'\)" class="home-btn home-btn-green"',
    'onclick="showPage(\'tierlist\')" class="home-btn home-btn-green"',
    content
)
# Red button (Tunisia) - find and add class
content = re.sub(
    r'onclick="showPage\(\'tunisia\'\);startTunisiaXI\(\);" class="home-btn"',
    'onclick="showPage(\'tunisia\');startTunisiaXI();" class="home-btn home-btn-red"',
    content
)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
