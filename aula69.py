#       Tkinter - Checkbutton

from tkinter import *

def futebolClicado():
    esp=str(vfutebol.get())
    print("Futebol:"+esp)
    
def voleiClicado():
    esp=str(vvolei.get())
    print("Vôlei:"+esp)
    
def basketClicado():
    esp=str(vbasket.get())
    print("Basket:"+esp)

app = Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

vfutebol=IntVar()
vvolei=IntVar()
vbasket=IntVar()

fr_quadro1=Frame(app, borderwidth=1, relief="solid")
fr_quadro1.place(x=10, y=10, width=300, height=100)

cb_futebol=Checkbutton(fr_quadro1, text="Futebol", variable=vfutebol, onvalue=1, offvalue=0, command=futebolClicado)
cb_futebol.pack(side=LEFT)

cb_volei=Checkbutton(fr_quadro1, text="Vôlei", variable=vvolei, onvalue=1, offvalue=0, command=voleiClicado)
cb_volei.pack(side=LEFT)

cb_basket=Checkbutton(fr_quadro1, text="Basket", variable=vbasket, onvalue=1, offvalue=0, command=basketClicado)
cb_basket.pack(side=LEFT)



app.mainloop()
