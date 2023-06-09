#       Tkinter - Frame
from tkinter import *
from tkinter import messagebox

#tipos de botão, apenas msg de aviso
def monstrarMsg():
    messagebox.showerror(title="Pinchers Cursos", message="Pnxrs Cursos, curso de lobinho")

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

vnum_cstexto=StringVar()

fr_quadro1=Frame(app, borderwidth=1, relief="solid")
#valores possiveis para relief(flat, raised, sunken, solid)
fr_quadro1.place(x=10, y=10, width=300, height=100)

#o pai dos botões abaixo foi trocado de app pra fr_quadro1
#e seram posicionados dentro dele, usando place no lugar de pack

lb_tipo=Label(fr_quadro1, text="Tipo de cx(1,2 ou 3)")
lb_tipo.place(x=10, y=10)
tb_num=Entry(fr_quadro1, textvariable=vnum_cstexto)
vnum_cstexto.set("1")
tb_num.place(x=10, y=30)



fr_quadro2=Frame(app, borderwidth=1, relief="solid", background="#008")
fr_quadro2.place(x=10, y=120, width=300, height=100)

btn_msg=Button(fr_quadro2, text="Mostrar mensagem", command=monstrarMsg)
btn_msg.place(x=10, y=10)

app.mainloop()