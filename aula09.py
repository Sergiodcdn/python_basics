carros=["HRV", "Golf", "Argo", "Focus"] #lista é o array, lista de str
#carros[3]="Fusion" #adiciona o Fusion no lugar do Focus
carros.append("Fit") #adiciona item
carros.append("Fusion")
carros.append("Polo")

#carros2=list(carros) #cria nova lista o print(carros2) demonstra ela
carros2=["Fusca", "147", "Brasilia", "Celta"]

carros3=carros+carros2

#carros.remove("Fusion") #remove item
#carros.pop() #remove o ultimo elemento da lista
#del carros[2] #remove indice 2
#carros.clear() #limpa lista

print(str(len(carros)) + " carros na lista") #verifica tamanho
print(str(len(carros3)) + " carros na lista")

#print(carros[0]) #numero de indice, imprime o item correspondete, se por negativo, conta do final, tira o 0
print(carros)
print(carros2)
print(carros3)