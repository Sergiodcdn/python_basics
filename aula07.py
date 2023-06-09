#curso="Curso de Python"
#res="Python" in curso , verifica se Python está no "curso", not in verifica o contraio
#print(res)

#texto="Curso de Python"
#palavra="python"
#res=palavra.upper() in texto.upper() poem tudo em caixa alta e verifica
#print(res), resposta true

#curso="Curso de Python"
#canal="CFB Cursos"
#res=curso+" do canal "+canal
#print(res)

cidade= "São Paulo"
dia=22
mes="Outubro"
ano=2022
canal="TETECO Cursos"
data="{}, \'{} de \b{} de {}\n \"{}\""
#print(cidade + ", " + str(dia) + " de " + mes + " de " + str(ano)) dá pra fazer assim, ou usando data + edição abaixo
print(data.format(cidade,dia,mes,ano,canal))

#\'-poem pistolinha  \""-coloca aspas  \n-pula linha  \r-remove estranho  \t-da espaço tab  \b-tira espaço



