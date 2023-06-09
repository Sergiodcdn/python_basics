#       MATRIZES, coleção de arrays, linha e coluna

#carros=["HRV", "Golf", "Focus", "Argo"] #aaray/list

carros=[["Modelo", "HRV"],["Fabricante", "Honda"],["Ano", 2016]]

carros.append(["Cor", "Prata"]) #adicionou na matrix

carros[2][1]=2019 #altera valor apenas desta posição

print(carros[1][1] + "\n") #printa elemento indicado

for l,c in carros:
    print("Linha : " + l + " | Coluna: " + str(c)) # str convertendo int pra str