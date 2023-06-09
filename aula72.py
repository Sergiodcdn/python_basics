#       Tkinter - Scale
#   componente deslizante 

from tkinter import *

def valorEscala():
    print("Valor da escala: " + str(sc_escala.get()))

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

lb_valor=Label(app, text="Valor")
lb_valor.pack()

sc_escala=Scale(app, from_=0, to=100, orient=HORIZONTAL)
sc_escala.set(50)
sc_escala.pack()

btn_valor=Button(app, text="Valor Escala", command=valorEscala)
btn_valor.pack()

app.mainloop()