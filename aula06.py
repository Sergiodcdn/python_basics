curso="Curso de Python" #string é array de caracteres

#print(curso[9:15]) imprime de forma apontada, ex : python
#print(curso.strip()) tira espaço começo da oração
#print(curso.lower().strip()) #converte de maisculo para minusculo + tira espaços"
#print(curso.upper()) barra alta em tudo
#print(curso.replace("Python","Teteco")) #susbstitui palavra
a=curso.split(" ") #divide aonde tiver espaço, retornando array, no caso com 3 posições
print(a[2])

print("Tamanho: " + str(len(curso)))