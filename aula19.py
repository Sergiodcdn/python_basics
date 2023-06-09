#       FUNÇÕES e função dentro de função!

n1 = int(input("Digite o valor no primeiro numero: "))
n2 = 10


def somar():
    r = n1+n2
    print(f"O valor da soma de {n1} com {n2} é: {r}")


def subtrair():
    r = n1-n2
    print(f"O valor da subtração de {n1} com {n2} é: {r}")


def calculos():
    somar()
    subtrair()


calculos()
