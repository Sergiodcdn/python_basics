#       Iterators , corre lista até o final dela

carros=["HRV", "Polo", "Jetta", "Cruze", "Fusion", "Fusca"]

#for c in carros:   #aqui corre a impressao da lista
#    print(c)

#com metodo iterator
"""
itCarros=iter(carros)

print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros)) #buga nesse, pois não tem mais lista
"""
itCarros=iter(carros)

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        #print("Fim da lista")
        break