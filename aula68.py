#       Tkinter - PhotoImage 
from tkinter import *
import os

pastaApp=os.path.dirname(__file__)

app = Tk()
app.title("Pinchers Cursos")
app.geometry("800x500")

imgLogo=PhotoImage(file=pastaApp+"\\R.gif")
l_logo=Label(app, image=imgLogo)
l_logo.place(x=10, y=10)


app.mainloop()
