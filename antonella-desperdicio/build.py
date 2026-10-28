import json
s=json.load(open("slides.json"))
t=open("template.html").read()
open("index.html","w").write(t.replace("/*SLIDES*/[]", json.dumps(s, ensure_ascii=False)))
# página completa para hospedar fora do Claude (Vercel)
head='<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>\n'
open("../desperdicio-de-alimentos.html","w").write(head.replace("<head>","<head><base href=\"antonella-desperdicio/\">")+open("index.html").read()+"\n</body></html>\n")
