from sql import *
from tkinter import *


#variables
myfont = ("comicsans", 19, "bold")


mytink = Tk()
mytink.geometry("640x640") #App width
mytink = Label(text="***********BOLLYWOOD GAME**********",
               bg="red",
               padx="40",
               pady="20",
               font = myfont)


mytink = Label(text="welcome")
mytink.pack()

mytink.mainloop()
