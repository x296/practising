from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text = "Look! I clicked a button!")
	myLabel.pack()

myButton = Button(root, text = "Click Me!", command = myClick, fg = "#5555ff")
myButton.pack()

root.mainloop()