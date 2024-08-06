import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import os


def back_function():
    root.destroy()
    import page1


def CreateWidgets():
    link_Label = Label(root, text="Select The File To Copy : ",
                       bg="#E8D579")
    link_Label.grid(row=1, column=0,
                    pady=5, padx=5)

    root.sourceText = Entry(root, width=50,
                            textvariable=sourceLocation)
    root.sourceText.grid(row=1, column=1,
                         pady=5, padx=5,
                         columnspan=2)

    source_browseButton = Button(root, text="Browse",
                                 command=SourceBrowse, width=15)
    source_browseButton.grid(row=1, column=3,
                             pady=5, padx=5)

    destinationLabel = Label(root, text="Select The Destination : ",
                             bg="#E8D579")
    destinationLabel.grid(row=2, column=0,
                          pady=5, padx=5)

    root.destinationText = Entry(root, width=50,
                                 textvariable=destinationLocation)
    root.destinationText.grid(row=2, column=1,
                              pady=5, padx=5,
                              columnspan=2)

    dest_browseButton = Button(root, text="Browse",
                               command=DestinationBrowse, width=15)
    dest_browseButton.grid(row=2, column=3,
                           pady=5, padx=5)

    name_Label = Label(root, text="Enter Your Name :          ",
                       bg="#E8D579")
    name_Label.grid(pady=5, padx=5)
    name_Label.place(x=6, y=80)
    root.nameText = Entry(root, width=50, textvariable=nameText)
    root.nameText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)
    root.nameText.place(x=150, y=80)

    root.sourceText = Entry(root, width=50,
                            textvariable=sourceLocation)
    root.sourceText.grid(row=1, column=1,
                         pady=5, padx=5,
                         columnspan=2)

    copyButton = Button(root, text="Copy File", command=CopyFile, width=15)
    copyButton.grid(pady=5, padx=5)
    copyButton.place(x=110, y=130)

    moveButton = Button(root, text="Move File", command=MoveFile, width=15)
    moveButton.grid(pady=5, padx=5)
    moveButton.place(x=300, y=130)

    back = Button(root, text="Back", command=back_function, width=15)
    back.grid(row=3, column=2, pady=15, padx=15)
    back.place(x=465, y=130)


def SourceBrowse():
    root.files_list = list(filedialog.askopenfilenames(initialdir="C:/Users/AKASH"))
    root.sourceText.insert('1', root.files_list)


def DestinationBrowse():
    destinationdirectory = filedialog.askdirectory(initialdir="C:/Users/AKASH")
    root.destinationText.insert('1', destinationdirectory)


def CopyFile():
    files_list = root.files_list
    nm = nameText.get()
    if nm == '':
        messagebox.showinfo('information', 'Please Enter Your Name')
    else:
        destination_location = destinationLocation.get()
        x = ''
        for f in files_list:
            x = f
            shutil.copy(f, destination_location)
        os.rename(destination_location + "/" + getname(f), destination_location + "/" + nm + '.jpg')
        messagebox.showinfo('information', 'Successfully Copied.')


def getpath(f):
    x = ''
    f = str(f)
    files = f.split('/')
    for i in range(0, len(files) - 1):
        x = x + "/" + files[i]
    return x


def getname(f):
    x = ''
    f = str(f)
    files = f.split('/')
    return files[len(files) - 1]


def MoveFile():
    files_list = root.files_list
    nm = nameText.get()
    if nm == '':
        messagebox.showinfo('information', 'Please Enter Your Picture')
    else:
        destination_location = destinationLocation.get()
        x = ''
        for f in files_list:
            x = f
            shutil.move(f, destination_location)
        os.rename(destination_location + "/" + getname(f), destination_location + "/" + nm + '.jpg')
        messagebox.showinfo('information', 'Successfully Move.')


root = tk.Tk()
root.geometry("650x200")
root.title("Copy-Move GUI")
root.config(background="White")

sourceLocation = StringVar()
destinationLocation = StringVar()
nameText = StringVar()
CreateWidgets()

root.mainloop()
