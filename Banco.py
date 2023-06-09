#       ROTINAS DE ACESSO A AULA60+
import sqlite3
from sqlite3 import Error
import os
#arquivo original era agenda.db
pastaApp=os.path.dirname(__file__)
nomeBanco=pastaApp+"\\contatos.db"

def ConexaoBanco():
    con=None
    try:
        con=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con

def dql(query): #usando comando select
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query): #insert, update, delete
    try:
        vcon=ConexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)    

