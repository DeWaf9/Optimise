#Gui.py
#Includes the Gui backbone for Optimise.py, utilising the tkinter library

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
mainwindow = tk.Frame(root)
mainwindow.master.title("Optimise")
mainwindow.grid()

icon = tk.PhotoImage(file = "logo.png")
root.iconphoto(False, icon)


leftframe = tk.LabelFrame(mainwindow, width = 300)
rightframe = tk.LabelFrame(mainwindow, width = 700)


infobar = tk.Message(leftframe, aspect = 150, text = "infobar", bd = "5mm", font = "Times")
infobar.grid()

log = tk.Message(rightframe, aspect = 150, text = "log", bd = "5mm", font = "Times")
log.grid()

textin = tk.Entry(rightframe)
textin.grid(row = 1)

buttonframe = tk.Frame(mainwindow, width = 700)

leftframe.grid(row = 0, column = 0, columnspan = 2)
rightframe.grid(row = 0, column = 1)
buttonframe.grid(row = 1, column = 1)
mainwindow.mainloop()