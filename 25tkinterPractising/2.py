from tkinter import *

root = Tk()

# Creating label widget
myLabel1 = Label(root, text = "Hello world!")
myLabel2 = Label(root, text = "My name is Elton John")

# Packing it onto the screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 1)

root.mainloop()