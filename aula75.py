#       Tkinter - SpinBox
from tkinter import *

def impval():
    print("Valor: " + str(sb_valores.get()))

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

#modo com range de valores
#sb_valores=Spinbox(app, from_=1, to=10)
#modo com valores definidos
sb_valores=Spinbox(app, values=(1, 2, 3, 4, 5)) #se usasse "value", valor fica fixo
sb_valores.pack()

btn_valor=Button(app, text="Imprimir valor", command=impval)
btn_valor.pack()

app.mainloop()