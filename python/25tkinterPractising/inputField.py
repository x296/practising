from tkinter import *

root = Tk()

e = Entry(root, width = 50, borderwidth = 1)
e.pack()
e.insert(0, "Enter your name...")

def myClick():
	hello = "Hello, " + e.get()
	myLabel = Label(root, text = hello)
	myLabel.pack()

myButton = Button(root, text = "Enter your name", command = myClick)
myButton.pack()

root.mainloop()