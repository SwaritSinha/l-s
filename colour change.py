#Main
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Screen colour")
#Def or Button function
def btnClick(button):
    if(btnClick == True):
      tkinter.messagebox.showinfo("You lie") or tkinter.messagebox.showinfo("changed")
#Button
button = Button( text="Change", font='Times 30 bold', bg='blue', fg='black', height=40, width=80, command=btnClick)
button.pack()
tk.mainloop()