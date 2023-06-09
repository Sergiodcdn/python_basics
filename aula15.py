#       TUPLAS, listas diferentonas
"""
l_carros=["HRV", "Golf", "Argo"] #usa chaves
t_carros=("HRV", "Golf", "Argo") #usa paranteses

#l_carros[2]"Focus"  #tupla não suporta add ou modificação nesse metodo
#t_carros[2]="Focus"
#print(t_carros[0])

for x in l_carros:
    print(x)

"""
#       TAPCAST, convertendo de tupla pra lista pra modificar
t_carros=("HRV", "Golf", "Argo") 
l_carros=list(t_carros) #virando lista
l_carros[2]="Focus" #mudando item
t_carros=tuple(l_carros) #voltando a ser tupla

for x in t_carros:
    print(x)