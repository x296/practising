import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)
root.geometry('400x400')

vertical = tk.Scale(root, from_ = 0, to = 400)
vertical.pack()

horizontal = tk.Scale(root, from_ = 0, to = 400, orient = tk.HORIZONTAL)
horizontal.pack()

def slide():
	my_lbl = tk.Label(root, text = horizontal.get()).pack()
	root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))

my_btn = tk.Button(root, text = 'Click Me!', command = slide).pack()

root.mainloop()