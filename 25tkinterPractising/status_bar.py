import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)

my_img1 = ImageTk.PhotoImage(Image.open('files/Plik1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('files/Plik2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('files/Plik3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('files/Plik4.jpeg'))
my_img5 = ImageTk.PhotoImage(Image.open('files/Plik5.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

def back(image_number):
	global my_label
	global button_back
	global button_forward
	
	my_label.grid_forget()
	my_label = tk.Label(image = image_list[image_number - 1])

	if image_number == 0:
		button_back = tk.Button(root, text = '<<', state = tk.DISABLED)
	else:
		button_back = tk.Button(root, text = '<<', command = lambda: back(image_number - 1))

	button_forward = tk.Button(root, text = '>>', command = lambda: forward(image_number + 1))
	status = tk.Label(root, text = 'Image ' + str(image_number + 1) + ' of ' + str(len(image_list)), bd = 1, relief = tk.SUNKEN, anchor = tk.E)

	my_label.grid(row = 0, column = 0, columnspan = 3)
	button_back.grid(row = 1, column = 0)
	button_forward.grid(row = 1, column = 2)
	status.grid(row = 2, column = 0, columnspan = 3, sticky = tk.W+tk.E)

def forward(image_number):
	global my_label
	global button_back
	global button_forward
	
	my_label.grid_forget()
	my_label = tk.Label(image = image_list[image_number])
	
	if image_number == 4:
		button_forward = tk.Button(root, text = '>>', state = tk.DISABLED)
	else:
		button_forward = tk.Button(root, text = '>>', command = lambda: forward(image_number + 1))

	button_back = tk.Button(root, text = '<<', command = lambda: back(image_number - 1))
	status = tk.Label(root, text = 'Image ' + str(image_number + 1) + ' of ' + str(len(image_list)), bd = 1, relief = tk.SUNKEN, anchor = tk.E)
	
	my_label.grid(row = 0, column = 0, columnspan = 3)
	button_back.grid(row = 1, column = 0)
	button_forward.grid(row = 1, column = 2)
	status.grid(row = 2, column = 0, columnspan = 3, sticky = tk.W+tk.E)


my_label = tk.Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

button_back = tk.Button(root, text = '<<', command = back, state = tk.DISABLED)
button_quit = tk.Button(root, text = 'Exit Program', command = root.quit)
button_forward = tk.Button(root, text = '>>', command = lambda: forward(1))

status = tk.Label(root, text = 'Image 1 of ' + str(len(image_list)), bd = 1, relief = tk.SUNKEN, anchor = tk.E)

button_back.grid(row = 1, column = 0)
button_quit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)
status.grid(row = 2, column = 0, columnspan = 3, sticky = tk.W+tk.E)

root.mainloop()