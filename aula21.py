#       Funções

valores = [5, 1, 2, 3, 2]


def somar(num):
    r = 0
    for n in num:
        r += n
    return r


def valLista(num):
    for v in num:
        print(v)

# valLista(valores) #imprime a lista


r = somar(valores)  # usando variavel pra imprimir result da conta

print(str(valores) + ": soma = " + str(r))
