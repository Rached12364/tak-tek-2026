content = open('index.html','r',encoding='utf-8').read()
import re
# CSS dans <style>
styles = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
for s in styles:
    if 'tn-main' in s or 'tunisia' in s:
        print("CSS FOUND:", repr(s[:800]))
# JS showPage
idx = content.find('function showPage')
print("\nSHOWPAGE JS:", repr(content[idx:idx+600]))
# CSS files
import os
print("\nFiles:", os.listdir('.'))
