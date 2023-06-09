# JSON em PYTHON p4, importando json de arquivos externos

import json

with open('C:/programação/python/aulas/aula39jogador.json') as f:
    jogador = json.load(f)

for c in jogador:
    print(c)

print(35 * "*")
#familiares / tipos - habilidades
for a in jogador["familiares"]:
    print(a["tipo"] + " - " + str(a["habilidade"]))
print(35 * "*")
# itens da mochila
for im in jogador["mochila"]:
    print(im)
print(35 * "*")
