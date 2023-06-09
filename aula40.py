#       Expressões Regulares - RegEx findall

import re #RegEx

texto="Teteco é bonzinho dormindo, acordado o Teteco é férinha"
#res=re.findall("Teteco", texto);
pesq=input("Pesquisar: ")
res=re.findall(pesq, texto);
print(res)

qtde=len(res)
print(f"qtde: {qtde}")

for t in res:
    print(t)