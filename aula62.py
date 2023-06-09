#       Abrindo novos formulários passando parâmetros

#       arquivo filho de aula60.py, e COPIA DE agenda2.PY, aula61.py

from tkinter import *
import os

pastaApp=os.path.dirname(__file__)

def semComando():
    print("")

def novoContato():
    exec(open(pastaApp+"\\aula60.py").read(),{'x':10})


app = Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")
app.configure(background="#dde")

barraDeMenus = Menu(app)
menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label="Novo", command=novoContato)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Deletar", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)
barraDeMenus.add_cascade(label="Contatos", menu=menuContatos)

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label="Banco de Dados", command=semComando)
barraDeMenus.add_cascade(label="Manutenção", menu=menuManutencao)


menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label="Pinchers Curso", command=semComando)
barraDeMenus.add_cascade(label="Sobre", menu=menuSobre)


app.config(menu=barraDeMenus)


app.mainloop()
