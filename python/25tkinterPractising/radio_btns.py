import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)

# r = tk.IntVar()
# r.set(2)

MODES = [
	('Pepperoni', 'Pepperoni'),
	('Cheese', 'Cheese'),
	('Mushroom', 'Mushroom'),
	('Onion', 'Onion'),
]

pizza = tk.StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:
	tk.Radiobutton(root, text = text, variable = pizza, value = mode).pack(anchor = tk.W)

def clicked(value):
	myLabel = tk.Label(root, text = value)
	myLabel.pack()

# tk.Radiobutton(root, text = 'Option 1', variable = r, value = 1, command = lambda: clicked(r.get())).pack()
# tk.Radiobutton(root, text = 'Option 2', variable = r, value = 2, command = lambda: clicked(r.get())).pack()

# myLabel = tk.Label(root, text = pizza.get())
# myLabel.pack()

myButton = tk.Button(root, text = 'Click Me!', command = lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()