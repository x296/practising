import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)
root.geometry('400x400')

var = tk.StringVar()

def show():
	my_lbl = tk.Label(root, text = var.get()).pack()

c = tk.Checkbutton(root, text = 'Check this box!', variable = var, onvalue = 'on', offvalue = 'off')
c.deselect()
c.pack()

my_btn = tk.Button(root, text = 'show selection', command = show).pack()

root.mainloop()