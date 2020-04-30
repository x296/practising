import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)
root.geometry('400x400')

# Create or connect
connection = sqlite3.connect('files/address_book.db')

# Create cursor
c = connection.cursor()

# Create table
c.execute("""CREATE TABLE adresses (
		first_name text,
		last_name text,
		adress text,
		city text,
		state text,
		zipcode integer
		)""")

# Commit changes
connection.commit()

# Close connection
connection.close()

root.mainloop()