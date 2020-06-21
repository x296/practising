import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)

def popup():
	response = messagebox.askyesnocancel('This is my Popup!', 'Hello World!')
	if response == 1:
		tk.Label(root, text = 'You clicked yes!').pack()
	elif response == 0:
		tk.Label(root, text = 'You clicked no!').pack()
	else:
		tk.Label(root, text = 'You\'ve canceled task!').pack()

tk.Button(root, text = 'popup', command = popup).pack()

root.mainloop()