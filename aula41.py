#       Expressões Regulares - RegEx findall

import re #RegEx

texto="Teteco é bonzinho dormindo, acordado o Teteco é férinha"

res=re.search("bonzinio",texto)

if(res != None):
    pi=res.start()
    pf=res.end()
    tam=pf-pi
    print(res.start())
    print(res.end())
    print(tam)
else:
    print(res) #"não encontrado"