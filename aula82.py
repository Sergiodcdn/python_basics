#       Tkinter - TreeView com Banco de Dados

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Banco
#função para resetar na hora da busca dentro do TreeV
def popular():
    tv.delete(*tv.get_children()) #deleta os filhos
    vquery="SELECT * FROM tb_nomes order by ID" #agora mostra todos, classificados por ID
    linhas=Banco.dql(vquery)
    for i in linhas: #for usado para preencher todos elementos
        tv.insert("", "end", values=i)

def inserir():
    if vnome.get()=="" or vfone.get()=="": #verifica se nome e fone estão digitados, senão da msg de erro
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    try:
        vquery="INSERT INTO tb_nomes (nome, fone) VALUES ( '"+vnome.get()+"', '"+vfone.get()+"')"
        Banco.dml(vquery)
    except:
        messagebox.showinfo(title="ERRO", message="Erro ao inserir")
        return
    popular() #apos entrar com novo contato, deleta as linhas, e..
    vnome.delete(0, END)
    vnome.delete(0, END)
    vnome.focus() #...e coloca o cursor no vid
      
def deletar():
    vid=-1
    itemSelecionado=tv.selection()[0]
    valores=tv.item(itemSelecionado, "values")
    vid=valores[0]
    try:
        vquery="DELETE FROM tb_nomes WHERE id="+vid
        Banco.dml(vquery)
    except:
        messagebox.showinfo(title="ERRO", message="Erro ao deletar")
        return
    tv.delete(itemSelecionado)
    
def pesquisar():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM tb_nomes WHERE nome LIKE '%"+vnomepesquisar.get()+"%' order by ID"
    linhas=Banco.dql(vquery)
    for i in linhas:
        tv.insert("", "end", values=i)
    
app=Tk()
app.title("Pinchers Cursos")
app.geometry("600x450")
#############
quadroGrid=LabelFrame(app, text="Contatos")
quadroGrid.pack(fill="both", expand="yes", padx=10, pady=10)

tv=ttk.Treeview(quadroGrid, columns=('id', 'nome', 'fone'), show='headings')
tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')
tv.pack()
popular() #essa função faz o prenchimento no banco de dados no treview
###############
quadroInserir=LabelFrame(app, text="Inserir novos contatos")
quadroInserir.pack(fill="both", expand="yes", padx=10, pady=10)

lbnome=Label(quadroInserir, text="Nome")
lbnome.pack(side="left")
vnome=Entry(quadroInserir)
vnome.pack(side="left", padx=10)
lbfone=Label(quadroInserir, text="Fone")
lbfone.pack(side="left")
vfone=Entry(quadroInserir)
vfone.pack(side="left", padx=10)
btn_inserir=Button(quadroInserir, text="Inserir", command=inserir)
btn_inserir.pack(side="left", padx=10)
##############
quadroPesquisar=LabelFrame(app, text="Pesquisar contatos")
quadroPesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

lbid=Label(quadroPesquisar, text="Nome")
lbid.pack(side="left")
vnomepesquisar=Entry(quadroPesquisar)
vnomepesquisar.pack(side="left", padx=10)
btn_pesquisar=Button(quadroPesquisar, text="Pesquisar", command=pesquisar)
btn_pesquisar.pack(side="left", padx=10)
btn_todos=Button(quadroPesquisar, text="Mostrar todos", command=popular)
btn_todos.pack(side="left", padx=10)

app.mainloop()