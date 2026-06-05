import re
content = open("index.html","r",encoding="utf-8").read()
# Remove the white HOME button (the duplicate one)
content = re.sub(
    r'<button[^>]*onclick="showPage\(\\\'home\\\'\)"[^>]*style="[^"]*background:rgba\(255,255,255[^"]*"[^>]*>.*?</button>',
    '',
    content,
    flags=re.DOTALL
)
# Fix double labels in dots - replace "POS\nPOS" pattern with single label
# The dot-label div should only show one thing
content = re.sub(
    r'(<div id="tn-dot-[^"]+")[^>]*(>)\s*<div[^>]*font-size:9px[^>]*>[^<]*</div>\s*(<div class="dot-label")',
    r'\1\2\3',
    content
)
open("index.html","w",encoding="utf-8").write(content)
print("done")
