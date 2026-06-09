content = open('index.html','r',encoding='utf-8').read()
content = content.replace(
    'window.saveProfile = async function(name, club, flag) {',
    'window.saveProfile = async function(name, club, flag) {'
)
# Changer type="module" en script normal avec import via CDN
content = content.replace(
    '<script type="module">\nimport { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";\nimport { getFirestore, collection, addDoc, getDocs, orderBy, query, limit, doc, setDoc, getDoc } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";',
    '''<script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore-compat.js"></script>
<script>'''
)
# Remplacer les fonctions Firebase modernes par compat
content = content.replace(
    'const app = initializeApp(firebaseConfig);',
    'const app = firebase.initializeApp(firebaseConfig);'
)
content = content.replace(
    'const db = getFirestore(app);',
    'const db = firebase.firestore();'
)
content = content.replace(
    'window.db = db;\nwindow.fbCollection = collection;\nwindow.fbAddDoc = addDoc;\nwindow.fbGetDocs = getDocs;\nwindow.fbOrderBy = orderBy;\nwindow.fbQuery = query;\nwindow.fbLimit = limit;\nwindow.fbDoc = doc;\nwindow.fbSetDoc = setDoc;\nwindow.fbGetDoc = getDoc;',
    ''
)
content = content.replace(
    'await fbSetDoc(fbDoc(db, \'users\', name), profile);',
    'await db.collection(\'users\').doc(name).set(profile);'
)
content = content.replace(
    'await fbAddDoc(fbCollection(db, \'scores\'), {',
    'await db.collection(\'scores\').add({'
)
content = content.replace(
    'var q = fbQuery(fbCollection(db, \'scores\'), fbOrderBy(\'pct\', \'desc\'), fbLimit(10));',
    'var q = db.collection(\'scores\').orderBy(\'pct\', \'desc\').limit(10);'
)
content = content.replace(
    'var snap = await fbGetDocs(q);',
    'var snap = await q.get();'
)
open('index.html','w',encoding='utf-8').write(content)
print('OK')
