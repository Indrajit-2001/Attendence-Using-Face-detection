import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Mark Infinity")
root.geometry('350x200')

def add_function():
    root.destroy()
    import  page2

def attendence_function():
    root.destroy()
    import Annimation

image1 = Image.open("Right.png")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=130, y=50)

lbl = Label(root, text="WelCome To Mark Infinity Group of Industry", fg="Blue", font=("Arial", 13))
lbl.pack(padx=10, pady=2,)

add = Button(root, text="Add New Entry", fg="black", command=add_function)
add.place(x=50, y=150)

attendence = Button(root, text="Attendence", fg="black", command=attendence_function)
attendence.place(x=200, y=150)
root.mainloop()