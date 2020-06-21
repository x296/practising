from tkinter import *

root = Tk()
root.title('Simple calc')

math = ''
f_num = None
is_operation = False

def float_or_int(number):
	if str(number).find('.') == -1:
		return int(number)
	elif str(number)[str(number).find('.'):] == '.0':
		return int(number)
	else:
		return float(number)

def solving_equations(second_number):
	global math
	global f_num
	if math == 'addition':
		return float_or_int(f_num + float(second_number))

	if math == 'substraction':
		return float_or_int(f_num - float(second_number))

	if math == 'multiplication':
		return float_or_int(f_num * float(second_number))

	if math == 'division':
		return float_or_int(f_num / float(second_number))

def button_click(number):
	global is_operation
	button_AC['text'] = 'C'
	if not(is_operation):
		inputField.insert(END, number)
	else:
		inputField.delete(0, END)
		inputField.insert(END, number)
		is_operation = False

def button_insert(sign):
	input_number = inputField.get()
	if sign == '.':
		if input_number.find('.') == -1:
			inputField.insert(END, sign)

	if sign == '-':
		if input_number[0] == '-':
			inputField.delete(0, END)
			inputField.insert(0, input_number[1:])
		else:
			inputField.insert(0, sign)

def button_clear():
	global math
	global f_num
	global is_operation
	if button_AC['text'] == 'AC':
		math = ''
		f_num = None
		is_operation = False
		inputField.delete(0, END)

	elif button_AC['text'] == 'C':
		button_AC['text'] = 'AC'
		inputField.delete(0, END)

def button_add():
	first_number = inputField.get()
	global f_num
	global math
	global is_operation
	is_operation = True
	math = 'addition'
	f_num = float(first_number)

def button_substract():
	first_number = inputField.get()
	global f_num
	global math
	global is_operation
	is_operation = True
	math = 'substraction'
	f_num = float(first_number)

def button_multiply():
	first_number = inputField.get()
	global f_num
	global math
	global is_operation
	is_operation = True
	math = 'multiplication'
	f_num = float(first_number)

def button_divide():
	first_number = inputField.get()
	global f_num
	global math
	global is_operation
	is_operation = True
	math = 'division'
	f_num = float(first_number)

def button_percentage():
	input_number = float(inputField.get())
	if f_num == None:
		inputField.delete(0, END)
		inputField.insert(0, float_or_int(input_number / 100))
	else:
		inputField.delete(0, END)
		inputField.insert(0, float_or_int(f_num * (input_number / 100)))

def button_equal():
	if math == '':
		return

	second_number = inputField.get()
	inputField.delete(0, END)

	inputField.insert(0, solving_equations(second_number))


inputField = Entry(root, width = 28, borderwidth = 5)

button_0 = Button(root, text = '0', width = 14, padx = 3, height = 3, command = lambda: button_click(0))
button_1 = Button(root, text = '1', width = 7, height = 3, command = lambda: button_click(1))
button_2 = Button(root, text = '2', width = 7, height = 3, command = lambda: button_click(2))
button_3 = Button(root, text = '3', width = 7, height = 3, command = lambda: button_click(3))
button_4 = Button(root, text = '4', width = 7, height = 3, command = lambda: button_click(4))
button_5 = Button(root, text = '5', width = 7, height = 3, command = lambda: button_click(5))
button_6 = Button(root, text = '6', width = 7, height = 3, command = lambda: button_click(6))
button_7 = Button(root, text = '7', width = 7, height = 3, command = lambda: button_click(7))
button_8 = Button(root, text = '8', width = 7, height = 3, command = lambda: button_click(8))
button_9 = Button(root, text = '9', width = 7, height = 3, command = lambda: button_click(9))

button_coma = Button(root, text = ',', width = 7, height = 3, command = lambda: button_insert('.'))
button_plusMinus = Button(root, text = '+/-', width = 7, height = 3, command = lambda: button_insert('-'))
button_AC = Button(root, text = 'AC', width = 7, height = 3, command = button_clear)
button_add = Button(root, text = '+', width = 7, height = 3, command = button_add)
button_substract = Button(root, text = '-', width = 7, height = 3, command = button_substract)
button_multiply = Button(root, text = '*', width = 7, height = 3, command = button_multiply)
button_divide = Button(root, text = '/', width = 7, height = 3, command = button_divide)
button_percentage = Button(root, text = '%', width = 7, height = 3, command = button_percentage)
button_equal = Button(root, text = '=', width = 7, height = 3, command = button_equal)

# Put the buttons on the screen
inputField.grid(row = 0, column = 0, columnspan = 4)

button_AC.grid(row = 1, column = 0)
button_plusMinus.grid(row = 1, column = 1)
button_percentage.grid(row = 1, column = 2)
button_divide.grid(row = 1, column = 3)

button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)
button_multiply.grid(row = 2, column = 3)

button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)
button_substract.grid(row = 3, column = 3)

button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)
button_add.grid(row = 4, column = 3)

button_0.grid(row = 5, column = 0, columnspan = 2)
button_coma.grid(row = 5, column = 2)
button_equal.grid(row = 5, column = 3)


root.mainloop()