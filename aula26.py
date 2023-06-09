#           Try Except / tratamento de erros
"""
x=10
try:
    print(x)
except:
    print("Erro")
else:
    print("Tudo ok")
finally:
    print("Fim do tratamento")
"""

num="Teteco"

if not type(num) is int:
    raise Exception("Somente numeros permitido")
else:
    print(num)