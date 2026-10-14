# Regenerates index.html, 404.html and one folder per route from sweet-sticks.html
import os, sys
src=sys.argv[1] if len(sys.argv)>1 else 'sweet-sticks.html'
body=open(src).read()
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Sweet Sticks: flick open a pack, pull a stick, and it unrolls into a visiting card.">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
'''
doc=head+body+'\n</body>\n</html>\n'
for f in ['index.html','404.html']: open(f,'w').write(doc)
for r in ['all','vishesh','kbhumbri','kashish','athvkd','atharva','sam','sameen','eemon','deepika','arjun','mohak','pari','parinishtha']:
    os.makedirs(r,exist_ok=True); open(f'{r}/index.html','w').write(doc)
