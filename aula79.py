#       Tkinter - TreeView
#componente do tipo grade de listagem
#tipo um grid que carrega lista ou banco de dados nele
from tkinter import *
from tkinter import ttk

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

listaNomes=[['0', 'Minie', '1234'], ['1', 'Kai', '2345'], ['2', 'To', '3456']]

tv=ttk.Treeview(app, columns=('id', 'nome', 'fone'), show='headings')
#definindo as colunas e seus tamanhos
tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)
#definindo o cabeçalho
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')
#mostrando a treeview
tv.pack()
#inserindo dados na treeview de forma unica
tv.insert("", "end", values=('4', 'Te', '4567'))
#usando for para inserir na lista
for (i, n, f) in listaNomes:
    tv.insert("", "end", values=(i, n, f))


app.mainloop()