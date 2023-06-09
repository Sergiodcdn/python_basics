#       JSON

import json
"""
carros_json='{"marca": "honda", "modelo": "HRV", "cor": "prata"}'

carros=json.loads(carros_json) #carregado no carros como um dict

#print(carros["marca"])

for x in carros.values():
    print(x)

print(35 * "*")
   
for k,v in carros.items(): #imprimindo chave e valor
    print(k, v)
    
print(35 * "*")
   
for k,v in carros.items(): #pode estruturar a impressão
    print(k + " - " + v)
"""
#convertendo dict em json
carros={"marca": "honda", "modelo": "HRV", "cor": "prata"}

carros_json=json.dumps(carros)

print(carros_json)