#       Operações em arquivos P1
#r - read - leitura
#a - append - anexar
#w - write - escrita
#x - create - criar
#t - texto
#b - binário
nome="texte44.txt"
f=open("C:/programação/python/aulas/"+nome,"wt")

txt=input("Digite um texto")
f.write(txt + "\nTeteco ta bagunçando. \nPois é muito bagunceiro")

f.close()