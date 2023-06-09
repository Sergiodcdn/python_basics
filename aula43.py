#       Expressões Regulares - RegEx Sub
# ajuda a substituir as coisas, pode rolar mais de uma vez
import re  # RegEx

texto = "Teteco é bonzinho dormindo, acordado o Teteco é férinha"

res = re.sub("\s", ".", texto)
res = re.sub("\,", "!", res)
print(res)
