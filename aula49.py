#       SQLite, Inserindo registros na tabela, INSERT INTO

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

nome=input("Digite o nome: ")
telefone=input("Digite o telefone: ")
email=input("Digite o email: ")

vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+nome+"', '"+telefone+"', '"+email+"')"
def inserir(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit() #usado para executar a mudança no banco
        print("Registro inserido")
    except Error as ex:
        print(ex)
inserir(vcon, vsql)