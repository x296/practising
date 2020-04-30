import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)

my_img = ImageTk.PhotoImage(Image.open('files/Plik1.jpg'))

def open():
	top = tk.Toplevel()
	top.title('top window')

	lbl = tk.Label(top, text = 'Hello World!').pack()
	my_label = tk.Label(top, image = my_img).pack()

	btn = tk.Button(top, text = 'close window', command = top.destroy).pack()

btn = tk.Button(root, text = 'Open second window', command = open).pack()



root.mainloop()