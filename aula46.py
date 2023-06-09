#       Deletando arquivos - P3

#r - read - leitura
#a - append - anexar
#w - write - escrita
#x - create - criar
#t - texto
#b - binário

import re
import os

nome = "texte46.txt"
caminho = "C:/programação/python/aulas/"

if os.path.exists(caminho+nome):
    print("Arquivo existente")
else:
    f = open(caminho+nome, "x")
    f.close()
    print("Arquivo criado")

if os.path.exists(caminho+nome):
    os.remove(caminho+nome)
    print("Arquivo removido")
else:
    print("Arquivo inexistente")
