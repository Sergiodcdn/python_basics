"""
a=10
b=5
res=0
op="+"

if op=="+": 
    res=a+b
elif op=="-": #else if = elif
    res=a-b
elif op=="*":
    res=a*b
elif op=="/":
    res=a/b
else: #se for F em todos cai no else, VEJA não há igualdade a bater validação
    print("Operador inválido")

print(str(a) + op + str(b) + " = " + str(res)) 
"""

clima="sol"
dinheiro=600
lugar=""

if clima=="sol" or (dinheiro>=300 and dinheiro<=500): #and coloca como 2 pré requisito, or se 1 pré requisito der já é True
    lugar="clube"
else:
    lugar="cinema"

print("Vou ao " + lugar)

