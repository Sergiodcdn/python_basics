#       Tkinter - Grid
#no lugar de pack e place

from tkinter import *
from tkinter import ttk


app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

lb_canal=Label(app, text="Lobinhos forces")
lb_nome=Label(app, text="Digite seu nome")
lb_idade=Label(app, text="Informe sua idade")

et_nome=Entry(app)
et_idade=Entry(app)

btn=Button(app, text="Auuuuu")
#columnspan mescla 2 colunas, pady poem espaço vertical
lb_canal.grid(column=0, row=0, columnspan=2, pady=15)
#sticky(colocação dentro do grid) valores -> n, s, e, w
lb_nome.grid(column=0, row=1, sticky='w')
#padx poem espacinho horizontal
et_nome.grid(column=0, row=2, padx=5)

lb_idade.grid(column=1, row=1)

et_idade.grid(column=1, row=2, padx=5)



app.mainloop()