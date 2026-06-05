import re
content = open('index.html','r',encoding='utf-8').read()
# Remplacer la fermeture drop sans </script> par avec </script>
content = content.replace(
    '  target.appendChild(makeCard(player, false));\n}\n</script>',
    '  target.appendChild(makeCard(player, false));\n}\n</script>'
)
# Verifier si </script> est present apres drop
if 'makeCard(player, false);\n}\n</script>' not in content:
    content = content.replace(
        '  target.appendChild(makeCard(player, false));\n}',
        '  target.appendChild(makeCard(player, false));\n}\n</script>'
    )
    print("</script> ajoute")
else:
    print("</script> deja present")
open('index.html','w',encoding='utf-8').write(content)
