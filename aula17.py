#chave/key - Valor/Value  DICTIONARY
"""
carro={"Fabricante" : "Honda", "Modelo": "HRV", "Ano":"2016", "Cor": "Prata"} 

#print(carro["Fabricante"]) #retorna Honda

fab=carro.get("Fabricante") # = fab=carro["Fabricante"]
#print(fab) #retorna Honda

carro["Cor"]="Preto" #mudou value
carro["Cambio"]="Automatico" #adicionou item
carro.pop("Cambio") #removeu = del carro["Cambio"]
#carro.clear() removeria tudo

'''
for x in carro: 
    print(x)  #imprime as chaves
    print(carro[x]) #imprime valor
'''

print("Tamanho do dictionary: " + str(len(carro)))

if "Modelo" in carro:
    print("\nSim, modelo é uma chave\n")

for c,v in carro.items():  #impreme chave: valor
    print(c + ": " + v)
"""
"""
carros={
    "Carro1":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "Carro2":{
        "Fabricante":"Volkswagem",
        "Modelo":"Golf"
    },
    "Carro3":{
        "Fabricante":"Ford",
        "Modelo":"Focus"
    }
}

print(carros["Carro1"]["Fabricante"])
"""


Carro1={
        "Fabricante":"Honda",
        "Modelo":"HRV"
    }
Carro2={
        "Fabricante":"Volkswagem",
        "Modelo":"Golf"
    }
Carro3={
        "Fabricante":"Ford",
        "Modelo":"Focus"
    }

Carros={
    "C1":Carro1,
    "C2":Carro2,
    "C3":Carro3
}

print(Carros["C1"])
print(Carros["C1"]["Modelo"])