#       Tkinter - Listbox
#adicionar elementos manual, ou com looping

from tkinter import *

#função de imprimir esporte da box no terminal
def imprimirEsporte():
    print("Esporte: " + str(lb_esportes.get(ACTIVE)))
#adiciona o esporte da nova box, na lista, possibilita a impressão pro terminal
def addEsporte():
    lb_esportes.insert(END, vnovoesporte.get())

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

listaEsportes=["Futebol", "Vôlei", "Basket"]

lb_esportes=Listbox(app)
for esportes in listaEsportes:
    lb_esportes.insert(END, esportes)
lb_esportes.pack()

btn_esporte=Button(app, text="Imprimir esporte", command=imprimirEsporte)
btn_esporte.pack()

vnovoesporte=Entry(app)
vnovoesporte.pack()

btn_inseriresporte=Button(app, text="Adicionar esporte", command=addEsporte)
btn_inseriresporte.pack()

app.mainloop()