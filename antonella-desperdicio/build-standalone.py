import json,base64,os,re
s=json.load(open("slides.json")); t=open("template.html").read()
t=t.replace("/*SLIDES*/[]", json.dumps(s, ensure_ascii=False))
A={}
for f in sorted(os.listdir("img")): A["img/"+f]="data:image/png;base64,"+base64.b64encode(open("img/"+f,"rb").read()).decode()
for f in sorted(os.listdir("audio")): A["audio/"+f]="data:audio/mpeg;base64,"+base64.b64encode(open("audio/"+f,"rb").read()).decode()
t=t.replace('src="img/tomato.png"','src="'+A["img/tomato.png"]+'"')
t=t.replace('<img src="img/${n}.png"','<img src="${asset(`img/${n}.png`)}"')
t=t.replace('`img/${n}.png`;','asset(`img/${n}.png`);')
t=t.replace('fetch(`audio/${s.id}.mp3`)','fetch(asset(`audio/${s.id}.mp3`))')
t=t.replace("<script>\nconst SLIDES","<script>\nconst A="+json.dumps(A)+";\nconst asset=p=>A[p]||p;\nconst SLIDES",1)
head='<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
out=head+t.replace("<style>","</head><body>\n<style>",1) if False else head+"</head><body>\n"+t+"\n</body></html>"
open("Desperdicio-de-Alimentos-Antonella-Helena-Giuseppe-Murilo-Julia.html","w").write(out)
print(len(out)//1024,"KB", t.count("asset("))
