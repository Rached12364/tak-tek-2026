content = open('index.html','r',encoding='utf-8').read()
idx = content.find("startQuiz")
# Chercher le dernier <script> avant startQuiz
script_idx = content.rfind('<script', 0, idx)
print('Dernier script avant startQuiz:', script_idx)
print(content[script_idx:script_idx+300])
print('---FIN---')
print(content[idx-100:idx+100])
