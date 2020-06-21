from tkinter import *

root = Tk()
root.title('Another app')
img = Image('photo', file='files/logo.png')
root.iconphoto(True, img)

my_img = Image('photo', file = 'files/logo.png')

my_label = Label(image = my_img)

my_label.pack()

button_quit = Button(root, text = 'Exit Program', command = root.quit)
button_quit.pack()

root.mainloop()