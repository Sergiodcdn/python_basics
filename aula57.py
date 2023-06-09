#       Interface Gráfica no Python com Tkinter
from tkinter import*

app=Tk()
app.title("Teteco filhotico")
app.geometry("500x300")
app.configure(background="#008")

txt1=Label(app, text="Curso de pinchers", background="#008", foreground="#fff")
#place define manualmente a dimensão e localização, melhor usado sem o elem conteiner
txt1.place(x=10, y=10, width=100, height=20)

vtxt="Modulo Tkinter"
vgb="#ff0"
vfg="#000"
txt2=Label(app, text=vtxt, bg=vgb, fg=vfg)
#pack é mais adequado qnd tiver conteiners, se ajustando dentro
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=X, expand=True) #faz diferente do place, fill+expand expande alturaY larguraX


app.mainloop()