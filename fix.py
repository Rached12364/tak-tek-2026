# -*- coding: utf-8 -*-
content = open('index.html', 'r', encoding='utf-8').read()
old1 = content[content.find('<span style="font-size:11px'):content.find('</span>', content.find('<span style="font-size:11px'))+7]
old2 = content[content.rfind('<span style="font-size:11px'):content.rfind('</span>')+7]
new1 = '<span style="font-size:12px;color:#ccc;font-weight:400;margin-top:8px;display:block;direction:rtl;">كل مرة يجوك 3 لاعبين بالبوست، اختار واحد باش تكون تشكيلة الموسم 2025/2026 و اختار في الاخير المدرب</span>'
new2 = '<span style="font-size:12px;color:#ccc;font-weight:400;margin-top:8px;display:block;direction:rtl;">24 لاعب باش تعمر TIER LIST، فما 3 كلاسات S A B و كان تنجم تبدل اسامي كل كلاس</span>'
content = content.replace(old1, new1)
content = content.replace(old2, new2)
open('index.html', 'w', encoding='utf-8').write(content)
print('done')
