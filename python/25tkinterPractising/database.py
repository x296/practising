import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

root = tk.Tk()
root.title('Another app')
img = ImageTk.PhotoImage(Image.open('files/logo.png'))
root.iconphoto(True, img)
root.geometry('400x600')

# Create table
# c.execute("""CREATE TABLE adresses (
# 		first_name text,
# 		last_name text,
# 		adress text,
# 		city text,
# 		state text,
# 		zipcode integer
# 		)""")

def update():
	# Create or connect
	connection = sqlite3.connect('files/address_book.db')

	# Create cursor
	c = connection.cursor()

	record_id = delete_box.get()
	c.execute("""UPDATE adresses SET
		first_name = :first,
		last_name = :last,
		adress = :adress,
		city = :city,
		state = :state,
		zipcode = :zipcode

		WHERE oid = :oid""", 
		{
		'first': f_name_editor.get(),
		'last': l_name_editor.get(),
		'adress': adress_editor.get(),
		'city': city_editor.get(),
		'state': state_editor.get(),
		'zipcode': zipcode_editor.get(),
		'oid': record_id
		})

	# Commit changes
	connection.commit()

	# Close connection
	connection.close()

	# Closing the editor window
	editor.destroy()


# Create function to edit record
def edit():
	global editor
	editor = tk.Tk()
	editor.title('Edit Record')
	editor.geometry('400x225')

	# Create or connect
	connection = sqlite3.connect('files/address_book.db')

	# Create cursor
	c = connection.cursor()

	record_id = delete_box.get()
	
	# Query the database
	c.execute('SELECT * FROM adresses WHERE oid = ' + str(record_id))
	records = c.fetchall()

	# Create global variables for tex box names
	global f_name_editor
	global l_name_editor
	global adress_editor
	global city_editor
	global state_editor
	global zipcode_editor

	# Create textboxes
	f_name_editor = tk.Entry(editor, width = 30)
	f_name_editor.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
	l_name_editor = tk.Entry(editor, width = 30)
	l_name_editor.grid(row = 1, column = 1)
	adress_editor = tk.Entry(editor, width = 30)
	adress_editor.grid(row = 2, column = 1)
	city_editor = tk.Entry(editor, width = 30)
	city_editor.grid(row = 3, column = 1)
	state_editor = tk.Entry(editor, width = 30)
	state_editor.grid(row = 4, column = 1)
	zipcode_editor = tk.Entry(editor, width = 30)
	zipcode_editor.grid(row = 5, column = 1)

	# Create Textbox labels
	f_name_label_editor = tk.Label(editor, text = 'First Name')
	f_name_label_editor.grid(row = 0, column = 0, pady = (10, 0))
	l_name_label_editor = tk.Label(editor, text = 'Last Name')
	l_name_label_editor.grid(row = 1, column = 0)
	adress_label_editor = tk.Label(editor, text = 'Adress')
	adress_label_editor.grid(row = 2, column = 0)
	city_label_editor = tk.Label(editor, text = 'City')
	city_label_editor.grid(row = 3, column = 0)
	state_label_editor = tk.Label(editor, text = 'State')
	state_label_editor.grid(row = 4, column = 0)
	zipcode_label_editor = tk.Label(editor, text = 'Zipcode')
	zipcode_label_editor.grid(row = 5, column = 0)

	# Loop thru result
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		adress_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		zipcode_editor.insert(0, record[5])

	# Create and Save edited button
	save_btn = tk.Button(editor, text = 'Save Record', command = update)
	save_btn.grid(row =6, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 135)

	# Commit changes
	connection.commit()

	# Close connection
	connection.close()


# Create function to delete record
def delete():
	# Create or connect
	connection = sqlite3.connect('files/address_book.db')

	# Create cursor
	c = connection.cursor()

	# Delete a record
	c.execute('DELETE from adresses WHERE oid = ' + str(delete_box.get()))

	# Commit changes
	connection.commit()

	# Close connection
	connection.close()

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
		print_records += str(record[6]) + '. ' + str(record[0]) + ' ' + str(record[1]) + '\n'

	query_lbl = tk.Label(root, text = print_records)
	query_lbl.grid(row = 11, column = 0, columnspan = 2)

	# Commit changes
	connection.commit()

	# Close connection
	connection.close()


# Create textboxes
f_name = tk.Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
l_name = tk.Entry(root, width = 30)
l_name.grid(row = 1, column = 1)
adress = tk.Entry(root, width = 30)
adress.grid(row = 2, column = 1)
city = tk.Entry(root, width = 30)
city.grid(row = 3, column = 1)
state = tk.Entry(root, width = 30)
state.grid(row = 4, column = 1)
zipcode = tk.Entry(root, width = 30)
zipcode.grid(row = 5, column = 1)
delete_box = tk.Entry(root, width = 30)
delete_box.grid(row = 8, column = 1, pady = 5)

# Create Textbox labels
f_name_label = tk.Label(root, text = 'First Name')
f_name_label.grid(row = 0, column = 0, pady = (10, 0))
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
delete_box_label = tk.Label(root, text = 'Select ID')
delete_box_label.grid(row = 8, column = 0, pady = 5)

# Create Submit Button
submit_btn = tk.Button(root, text = 'Add Record To Database', command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 100)

# Create query button
query_btn = tk.Button(root, text = 'Show Records', command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 131)

# Create delete button
delete_btn = tk.Button(root, text = 'Delete Record', command = delete)
delete_btn.grid(row =9, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 131)

# Create and update button
edit_btn = tk.Button(root, text = 'Edit Record', command = edit)
edit_btn.grid(row =10, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 138)


root.mainloop()