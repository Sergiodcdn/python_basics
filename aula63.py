#       Tkinter Radio Button

from tkinter import *

def imprimirEsporte():
    ve=vesporte.get()
    if ve=="f":
        print("Esporte Futebola")
    elif ve=="v":
        print("Esporte Voleibola")
    elif ve=="b":
        print("Esporte basquetebola")
    else:
        print("Selecione um desporto")

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

#guarda o elemento selecionado nos radiob. abaixo
vesporte=StringVar()
vcor=StringVar()

bl_esportes=Label(app, text="Esportes")
bl_esportes.pack()

rb_futebol=Radiobutton(app, text="Futebol", value="f", variable=vesporte)
rb_futebol.pack()


rb_volei=Radiobutton(app, text="Vôlei", value="v", variable=vesporte)
rb_volei.pack()


rb_basket=Radiobutton(app, text="Basket", value="b", variable=vesporte)
rb_basket.pack()


rb_verde=Radiobutton(app, text="Verde", value="#0f0", variable=vcor)
rb_verde.pack()


rb_vermelho=Radiobutton(app, text="Vermelho", value="#f00", variable=vcor)
rb_vermelho.pack()

btn_esporte=Button(app, text="Esporte selecionado", command=imprimirEsporte)
btn_esporte.pack()

app.mainloop()