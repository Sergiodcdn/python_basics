#       Tkinter - Messagebox
from tkinter import *
from tkinter import messagebox

#tipos de botão, apenas msg de aviso
def monstrarMsg(tiposmg, msg):
    if(tiposmg== "1"):
        messagebox.showinfo(title="Pinchers Cursos", message=msg)
    elif(tiposmg== "2"):
        messagebox.showwarning(title="Pinchers Cursos", message=msg)
    elif(tiposmg== "3"):
        messagebox.showerror(title="Pinchers Cursos", message=msg)

def resetarTB():
    res=messagebox.askyesno("Resetar", "Confirma reset do textbox?")
    #askyesno / askquestion - sim e não (true e false)
    #askokcancel - ok e cancelar (true e false)
    #askretrycancel - repetir e cancelar (true e false)
    #askyesnocancel - sim, não e cancelar (true, false e none)
    if(res== True):
        tb_num.delete(0, END)
        tb_num.insert(0, "1")
    
vmsg="Cursos de lobinhos/tkinter"

app=Tk()
app.title("Pinchers Cursos")
app.geometry("500x300")

vnum_cstexto=StringVar()

Label(app, text="Tipo de cx(1,2 ou 3)").pack()
tb_num=Entry(app, textvariable=vnum_cstexto)
vnum_cstexto.set("1")
tb_num.pack()

btn_msg=Button(app, text="Mostrar mensagem", command=lambda:monstrarMsg(vnum_cstexto.get(), vmsg))
btn_msg.pack()

btn_reset=Button(app, text="Resetar Textbox", command=resetarTB)
btn_reset.pack()

app.mainloop()