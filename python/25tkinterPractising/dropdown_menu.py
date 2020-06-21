import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)
root.geometry('400x400')

options = [
	'Monday',
	'Tuesday',
	'Wednesday',
	'Thursday',
	'Friday',
	'Saturday',
	'Sunday'
]

clicked = tk.StringVar()
clicked.set(options[0])

def show():
	my_lbl = tk.Label(root, text = clicked.get()).pack()

drop = tk.OptionMenu(root, clicked, *options)
drop.pack()

my_btn = tk.Button(root, text = 'Show selection', command = show).pack()

root.mainloop()