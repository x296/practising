import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)

frame = tk.LabelFrame(root, text = 'This is my frame', padx = 50, pady = 50)
frame.pack(padx = 10, pady = 10)

b1 = tk.Button(frame, text = 'Dont Click Me!')
b2 = tk.Button(frame, text = 'Nitehr Me!')
b1.grid(row = 0, column = 0)
b2.grid(row = 1, column = 1)

root.mainloop()