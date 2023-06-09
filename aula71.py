#       Tkinter - ComboBox
#   caixinha de escolha dos itens da lista
from tkinter import *
from tkinter import ttk

def imprimirEsporte():
    ve=cb_esportes.get()
    print("Esporte "+ve)

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

listEsportes=["Futebol", "Vôlei", "Basket"]

lb_esportes=Label(app, text="Esportes")
lb_esportes.pack()

cb_esportes=ttk.Combobox(app, values=listEsportes)
cb_esportes.set("Futebol") #pode tirar essa linha
cb_esportes.pack()

btn_esporte=Button(app, text="Esporte Selecionado", command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()