content = open('index.html','r',encoding='utf-8').read()
tm = content.find('<div id="tn-main"')
right = content.find('<div id="right"')
print("tn-main at:", tm)
print("right at:", right)
print("right is BEFORE tn-main?", right < tm)
# Contexte autour de #right
print("\nContexte avant #right:")
print(repr(content[right-200:right+50]))
