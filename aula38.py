#       JSON em PYTHON - Parte 3
import json

jogador_j='{"nome": "Teteco", "time": "pinchers", "vivo": "True", "energia": 100, "mochila" :["sashe", "petisco", "tataminho", "cobertinha"], "familiares" :[{"tipo" : "Minie", "habilidade" :80}, {"tipo": "Kai", "habilidade" : 100}, {"tipo": "To", "habilidade": 50}]}'

jogador=json.loads(jogador_j)

#chaves
for c in jogador:
    print(c)
print(35 * "*")
#itens
for i in jogador.items():
    print(i)
print(35 * "*")
#valores
for v in jogador.values():
    print(v)
print(35 * "*")
#nome do jogador
print(jogador["nome"])
print(35 * "*")
#itens da mochila
for im in jogador["mochila"]:
    print(im)
print(35 * "*")
#familiares
for a in jogador["familiares"]:
    print(a)
print(35 * "*")
#familiares / tipos
for a in jogador["familiares"]:
    print(a["tipo"])
print(35 * "*")
#familiares / habilidades
for a in jogador["familiares"]:
    print(a["habilidade"])
print(35 * "*")
#familiares / tipos - habilidades
for a in jogador["familiares"]:
    print(a["tipo"] + " - " + str(a["habilidade"]))
print(35 * "*")