import json
s=json.load(open("slides.json")); f=json.load(open("fotos.json"))
for x in s:
    if x["id"] in f: x["foto"]=f[x["id"]]
t=open("template-fotos.html").read()
open("fotos.html","w").write(t.replace("/*SLIDES*/[]", json.dumps(s, ensure_ascii=False)))
