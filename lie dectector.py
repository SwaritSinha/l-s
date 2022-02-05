#Main
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Lie detector")
tk.configure(background="red")
#HI Messege
tkinter.messagebox.showinfo("HI")
#Scan part
tkinter.messagebox.showinfo("SCANED")
tkinter.messagebox.showinfo("YOU")
tkinter.messagebox.showinfo("RESULE=")
tkinter.messagebox.showinfo("Lie")
#Def or Button function
def btnClick(button):
    if(btnClick == True):
      tkinter.messagebox.showinfo("changed") or tkinter.messagebox.showinfo("changed")
tkinter.messagebox.showinfo("red=") or tkinter.messagebox.showinfo("red=")
tkinter.messagebox.showinfo("lie") or tkinter.messagebox.showinfo("lie")
tkinter.messagebox.showinfo("blue=") or tkinter.messagebox.showinfo("blue=")
tkinter.messagebox.showinfo("truth") or tkinter.messagebox.showinfo("truth")
tkinter.messagebox.showinfo("blue=") or tkinter.messagebox.showinfo("white=")
tkinter.messagebox.showinfo("truth") or tkinter.messagebox.showinfo("both")  
#Button
button = Button( text="Scan", font='Times 30 bold', bg='red', fg='black', height=40, width=80, command=btnClick)
button.pack() 
tk.mainloop()

