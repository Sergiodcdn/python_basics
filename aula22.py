#           Funções Lamda ou Funções Anônimas
""" fazendo de forma passo a passo
soma=lambda a,b:a+b
mult=lambda a,b,c:(a+b)*c
print(soma(2,5))
print(mult(2,5,3))
"""
""" fazendo tdo jnto
print((lambda a,b:a+b)(2,5))
"""
r= lambda x,func:x+func(x)
res=r(2, lambda x:x*x)
print(res)
res=r(2, lambda x:x+3)
print(res)