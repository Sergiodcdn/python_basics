import random
import os

erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Digite seu numero, para achar o número secreto entre 0 e 100: ")) #int pra chamar numero

while(sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("Erro, o numero sorteado eh maior")
    elif(sorteado<jogador):
        print("Erro, o numero eh menor")
    erros+=1
    jogador=int(input("Digite outro numero: "))
print("Numero " + str(jogador) + ", voce acertou em " + str(erros+1) + " tentativas!" )