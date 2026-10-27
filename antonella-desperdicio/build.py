import json
s=json.load(open("slides.json"))
t=open("template.html").read()
open("index.html","w").write(t.replace("/*SLIDES*/[]", json.dumps(s, ensure_ascii=False)))
