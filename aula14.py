"""      WHILE

inicialização de variável de controle
while (teste lógico) , se o teste der T, executa, señ sai do while
    comando1  , tem q forçar um F, para parar o teste
    comando2
    comandox
    inc ou dec ou controle

"""
import os
#os.system ('cls') #limpar a tela

"""""
i = 0
while i < 10 :
    print(i)
    i+=1
    if (i>=5):
        break
print("Fim do loop")
"""
'''
carros=["HRV", "golf", "argo", "onix", "focus"]
i = 0
tam=len(carros)
while i < tam :
    print(carros[i])
    i+=1
print("\nFim do loop")
'''
carros=[]
carro=input("digite o nome do carro novo: ")
while carro != "-1" :
    carros.append(carro)
    carro=input("digite o nome do carro novo: ")
    
os.system ('cls')
for x in carros:
    print(x)
    
print("\nFim do loop")
