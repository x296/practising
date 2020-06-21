import tkinter as tk
import tkinter.ttk as ttk
import os
import secrets
import string

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title('Password Generator')
		self.master.resizable(height=0, width=0)
		self.pack(fill=tk.BOTH)

		self.create_instruction_label()
		self.create_checkbuttons()
		self.create_optionMenu()
		self.create_generate_button()
		self.create_password_label()
		self.create_copy_button()

	def create_instruction_label(self):
		self.int_lbl = tk.Label(self, text='Select, which and how many characters \nYou want in your super-safe password.')
		self.int_lbl.grid(row=0, column=0, columnspan=2)

	def create_checkbuttons(self):
		self.password_options = {
			'uppercase': tk.IntVar(),
			'digit': tk.IntVar(),
			'lowercase': tk.IntVar(),
			'punctuation': tk.IntVar()
		}
		for i, option in zip(range(len(self.password_options.items())), self.password_options):
			self.chkbtn = 'checkbutton ' + option
			self.chkbtn = tk.Checkbutton(self, text=option, anchor=tk.W, variable=self.password_options[option])
			self.chkbtn.select()
			if i%4 < 2:
				self.chkbtn.grid(row=(i+1)%2+1, column=i%2, sticky=tk.W)
			else:
				self.chkbtn.grid(row=i%2+1, column=i%2, sticky=tk.W)
	
	def create_optionMenu(self):
		pass_len = []
		for i in range(4, 21):
			pass_len.append(i)

		self.password_length = tk.StringVar(self)
		self.password_length.set('length') # initial value

		option = tk.OptionMenu(self, self.password_length, *pass_len)
		option.grid(row=3, column=0, sticky=tk.W+tk.E)

	def create_password_label(self):
		self.your_password = tk.StringVar()
		self.your_password.set('Your password')
		self.pass_lbl = tk.Label(self, font=('Helvetica', '14', 'bold'), width=30, textvariable=self.your_password)
		self.pass_lbl.grid(row=5, column=0)

	def create_generate_button(self):
		self.gen_btn = tk.Button(self, text='Generate', fg='red', command=self.generate_password)
		self.gen_btn.grid(row=3, column=1, sticky=tk.W+tk.E)

	def create_copy_button(self):
		self.cpy_btn = tk.Button(self, text="Copy", fg='blue', command=self.copy_password)
		self.cpy_btn.grid(row=5, column=1, sticky=tk.W+tk.E)

	def generate_password(self):
		characters_bank = ''
		password = ''
		if self.password_length.get() == 'length':
			self.password_length.set(8)
		
		if self.password_options['lowercase'].get() == 1:
			password += secrets.choice(string.ascii_lowercase)
			characters_bank += string.ascii_lowercase
		if self.password_options['uppercase'].get() == 1:
			password += secrets.choice(string.ascii_uppercase)
			characters_bank += string.ascii_uppercase
		if self.password_options['digit'].get() == 1:
			password += secrets.choice(string.digits)
			characters_bank += string.digits
		if self.password_options['punctuation'].get() == 1:
			password += secrets.choice(string.punctuation)
			characters_bank += string.punctuation

		for i in range(int(self.password_length.get())-len(password)):
			password += secrets.choice(characters_bank)

		char_list = list(password)
		secrets.SystemRandom().shuffle(char_list)

		password = ''.join(char_list)

		self.your_password.set(password)

	def copy_password(self):
		command = 'echo ' + self.your_password.get().strip() + ' | pbcopy'
		os.system(command)


def main():
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()
