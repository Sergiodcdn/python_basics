#uso de if, com teste de comparação, retornando um booliano(T or F)
#se teste lógico True, executa o comando

#a=10
#b=5
#if a<b:
#    print("CFB Teteco")
#print("Fim do programa");

a=10
b=5
res=0
op="/"

if op=="+": # == é comparação
    res=a+b

if op=="-":
    res=a-b

if op=="*":
    res=a*b

if op=="/":
    res=a/b

#print("Operação " + op + " : " + str(res)); #foi "concatenado"
print(str(a) + op +str(b) + " = " + str(res))