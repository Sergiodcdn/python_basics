#       FUNÇÕES/2 - argumentos arbitrarios

def somar(*num):
    r = 0
    for n in num:
        r+=n
    print(f"O valor da soma é: {r}")

valores=[5,1,2,3,2]
def somar2(num):
    r = 0
    for n in num:
        r+=n
    print(f"O valor da soma2 é: {r}")
    
somar(5,7)
somar2(valores)
