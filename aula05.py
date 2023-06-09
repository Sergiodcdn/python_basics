import random
num_i=10 #inteiro , float(num_i) mostra o i em f
num_f=5.2 #float se usar int(num_f), mostra a parte inteira
num_c=1j #complexo

num_r=[ #elemento lista // "array"
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    ]


#x=(num_r) #ajuda no valor printado abaixo
# para os primeiros print("valor :" + str(x) + " - tipo: " + str(type(x)))

print("valor 1:" + str(num_r[0]))
print("valor 2:" + str(num_r[1]))
print("valor 3:" + str(num_r[2]))
print("valor 4:" + str(num_r[3]))
print("valor 5:" + str(num_r[4]))
print("valor 6:" + str(num_r[5]))