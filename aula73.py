#       Tkinter - LabelFrame
#igual frame, com Label acoplado, tem de identificar o text
from tkinter import *

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

#vai deixar a palavra esportes escrita na bordinha do quadro
lb_esportes=LabelFrame(app, text="Esportes", borderwidth=1, relief="solid")
lb_esportes.place(x=10, y=10, width=300, height=100)

le1=Label(lb_esportes, text="Futebola")
le1.pack()

le2=Label(lb_esportes, text="Kriket")
le2.pack()

le3=Label(lb_esportes, text="Lutinha")
le3.pack()

app.mainloop()