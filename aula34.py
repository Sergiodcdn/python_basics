#       Modulos externos / Funções em arquivos externos
"""
import aula34canal as cn #(cn vira apelido do nome da pasta)

ac.canal_nome()
print(aula34canal.jogador["nome"])
"""
"""
from aula34canal import jogador #importar apenas um pedacinho da biblioteca

print(jogador["nome"])
"""
#mostra oque tem no import
import aula34canal

res=dir(aula34canal)

print(res)