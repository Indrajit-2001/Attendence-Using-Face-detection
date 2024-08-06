import tkinter
from tkinter import *

root = Tk()
root.title("Mark Infinity")
root.geometry('350x200')

def back_function():
    root.destroy()
    import  page1

def conti():
    root.destroy()
    import attendence

lbl = Label(root, text="Please Wait!!", font=("Arial", 13))
lbl.pack(padx=10, pady=2,)

lbl = Label(root, text="While The camera is turned on......", font=("Arial", 13))
lbl.pack(padx=10, pady=2,)

back = Button(root, text="Back", fg="black", command=back_function)
back.place(x=50, y=100)

attendence = Button(root, text="Continue", fg="black", command=conti)
attendence.place(x=200, y=100)
root.mainloop()