import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)
root.geometry('400x400')

# Create table
# c.execute("""CREATE TABLE adresses (
# 		first_name text,
# 		last_name text,
# 		adress text,
# 		city text,
# 		state text,
# 		zipcode integer
# 		)""")

# Create submit function to database
def submit():
	# Create or connect
	connection = sqlite3.connect('files/address_book.db')

	# Create cursor
	c = connection.cursor()

	# Insert into table
	c.execute('INSERT INTO adresses VALUES (:f_name, :l_name, :adress, :city, :state, :zipcode)',
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'adress': adress.get(),
				'city': city.get(),
				'state': state.get(),
				'zipcode': zipcode.get()
			})

	# Commit changes
	connection.commit()

	# Close connection
	connection.close()

	# Clear textboxes
	f_name.delete(0, tk.END)
	l_name.delete(0, tk.END)
	adress.delete(0, tk.END)
	city.delete(0, tk.END)
	state.delete(0, tk.END)
	zipcode.delete(0, tk.END)

# Create query function
def query():
	# Create or connect
	connection = sqlite3.connect('files/address_book.db')

	# Create cursor
	c = connection.cursor()

	# Query the database
	c.execute('SELECT *, oid FROM adresses')
	records = c.fetchall()
	# print(records)

	# Loop thru result
	print_records = ''
	for record in records:
		print_records += str(record[0]) + ' ' + str(record[1]) + '\n'

	query_lbl = tk.Label(root, text = print_records)
	query_lbl.grid(row = 8, column = 0, columnspan = 2)

	# Commit changes
	connection.commit()

	# Close connection
	connection.close()


# Create textboxes
f_name = tk.Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)


l_name = tk.Entry(root, width = 30)
l_name.grid(row = 1, column = 1)


adress = tk.Entry(root, width = 30)
adress.grid(row = 2, column = 1)


city = tk.Entry(root, width = 30)
city.grid(row = 3, column = 1)


state = tk.Entry(root, width = 30)
state.grid(row = 4, column = 1)

# Create Textbox labels
zipcode = tk.Entry(root, width = 30)
zipcode.grid(row = 5, column = 1)

f_name_label = tk.Label(root, text = 'First Name')
f_name_label.grid(row = 0, column = 0)

l_name_label = tk.Label(root, text = 'Last Name')
l_name_label.grid(row = 1, column = 0)

adress_label = tk.Label(root, text = 'Adress')
adress_label.grid(row = 2, column = 0)

city_label = tk.Label(root, text = 'City')
city_label.grid(row = 3, column = 0)

state_label = tk.Label(root, text = 'State')
state_label.grid(row = 4, column = 0)

zipcode_label = tk.Label(root, text = 'Zipcode')
zipcode_label.grid(row = 5, column = 0)

# Create Submit Button
submit_btn = tk.Button(root, text = 'Add Record To Database', command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 100)

# Create query button
query_btn = tk.Button(root, text = 'Show Records', command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 131)


root.mainloop()