#       SQLite, Deletando registros na tabela, DELETE

import sqlite3
from sqlite3 import Error

#       CRIAR CONEXÃO
def ConexaoBanco():
    caminho="C:\\programação\\bancodedados\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon=ConexaoBanco()

#INSERIR NA TABELA
def inserir(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido")
    except Error as ex:
        print(ex)
        
'''
nome=input("Digite o nome: ")
telefone=input("Digite o telefone: ")
email=input("Digite o email: ")
vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+nome+"', '"+telefone+"', '"+email+"')"
#inserir(vcon, vsql) 
'''

#DELETAR NA TABELA
def deletar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:    
        print("Registro removido")
vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO=1" #SE NAO USAR WHERE DELETA TUDO
deletar (vcon, vsql)        
