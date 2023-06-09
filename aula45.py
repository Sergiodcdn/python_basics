#       Operações em arquivos - P2
#r - read - leitura
#a - append - anexar
#w - write - escrita
#x - create - criar
#t - texto
#b - binário

import re #para alterar as coisas
nome="texte45.txt"
f=open("C:/programação/python/aulas/"+nome,"rt")

#se deixar() sem nada le tudo, se por numero apenas os X caracteres
#print(f.read())

#le a linha 0, e a cada comando le as subsequentes
#print(f.readline())
#print(f.readline())

#le as linhas até terminar o for
#for l in f:
#    print(l)

#apenas no terminal troca os spaces por -
res=re.sub("\s", "-",f.readline())
f.close()

#chama o arquivo com o "w" e edita ele com o comando acima, todavia fica apenas a linha chamada no terminal como o txt todo
f=open("C:/programação/python/aulas/"+nome,"wt")
f.write(res)
f.close()
print(res)