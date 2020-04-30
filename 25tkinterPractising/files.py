import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)

def open():
	global my_image
	root.filename = filedialog.askopenfilename(initialdir = 'files', title = 'select a file')
	my_label = tk.Label(root, text = root.filename).pack()
	my_image = ImageTk.PhotoImage(Image.open(root.filename))
	my_image_label = tk.Label(image = my_image).pack()

my_btn = tk.Button(root, text = 'Open file', command = open).pack()

root.mainloop()