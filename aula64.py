#       Tkinter - OptionMenu

from tkinter import *

def imprimirEsporte():
    ve=vesporte.get()
    if ve=="Futebol":
        print("Esporte Futebola")
    elif ve=="Vôlei":
        print("Esporte Voleibola")
    elif ve=="Basket":
        print("Esporte basquetebola")
    else:
        print("Selecione um desporto")

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

listaEsports=["Futebol", "Vôlei", "Basket"]

vesporte=StringVar()
vesporte.set(listaEsports[0]) #aqui define o valor padrão

bl_esportes=Label(app, text="Esportes")
bl_esportes.pack()

op_esportes=OptionMenu(app, vesporte, *listaEsports)
op_esportes.pack()

btn_esporte=Button(app, text="Esporte selecionado", command=imprimirEsporte)
btn_esporte.pack()



app.mainloop()