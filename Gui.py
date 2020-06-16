#Gui.py
#Includes the Gui backbone for Optimise.py, utilising the tkinter library

import tkinter as tk
from tkinter import ttk

def print2log(textout):
    log.insert(tk.INSERT, textout)


root = tk.Tk()
mainwindow = tk.Frame(root)
mainwindow.master.title("Optimise")
mainwindow.grid()

icon = tk.PhotoImage(file = "logo.png")
root.iconphoto(False, icon)


leftframe = tk.LabelFrame(mainwindow, width = 150)
rightframe = tk.LabelFrame(mainwindow, width = 350)
buttonframe = tk.Frame(mainwindow, width = 350)

infobar = tk.Text(leftframe, bd = "1mm", font = "Times", width = 30)
infobar.grid()

log = tk.Text(rightframe, bd = "1mm", font = "Times", width = 60)
log.grid()

textin = tk.Entry(buttonframe, width = 102)
textin.grid()

testbutt = tk.Button(buttonframe, text = "test", command = print2log("testing log!"))
testbutt.grid(row = 1)

leftframe.grid(row = 0, column = 0)
rightframe.grid(row = 0, column = 1)
buttonframe.grid(row = 1, column = 1)
mainwindow.mainloop()

