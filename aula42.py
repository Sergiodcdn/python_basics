#       Expressões Regulares - RegEx Split

import re #RegEx

texto="Teteco é bonzinho dormindo, acordado o Teteco é férinha"

res=re.split("d",texto) #\s = space, d = tira o d

print(res)
print(res[0])
for t in res:
    print(t)