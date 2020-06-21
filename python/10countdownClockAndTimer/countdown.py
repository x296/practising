import tkinter as tk
from tkinter import messagebox
import os
import time

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title('Countdown')
		self.master.resizable(height=0, width=0)
		self.pack(fill=tk.BOTH)

		self.create_entry_minutes()
		self.create_label_minutes()
		self.create_entry_seconds()
		self.create_label_seconds()
		self.create_button()

	def create_label_seconds(self):
		self.lbl = tk.Label(self, text='secs')
		self.lbl.grid(row=1, column=1)

	def create_label_minutes(self):
		self.lbl = tk.Label(self, text='mins')
		self.lbl.grid(row=0, column=1)

	def create_button(self):
		self.btn = tk.Button(self, text='Run', width=10, command=self.counting)
		self.btn.bind('<Return>', self.counting)
		self.btn.grid(row=2, column=0, columnspan=2)

	def create_entry_seconds(self):
		self.ety_secs = tk.Entry(self, width=5, justify=tk.RIGHT)
		self.ety_secs.insert(0, 0)
		self.ety_secs.bind('<Return>', self.counting)
		self.ety_secs.grid(row=1, column=0)

	def create_entry_minutes(self):
		self.ety_mins = tk.Entry(self, width=5, justify=tk.RIGHT)
		self.ety_mins.insert(0, 0)
		self.ety_mins.bind('<Return>', self.counting)
		self.ety_mins.grid(row=0, column=0)

	def insert_secs(self, event):
		self.ety_secs.delete(0, tk.END)
		self.ety_secs['fg'] = 'black'

	def insert_mins(self, event):
		self.ety_mins.delete(0, tk.END)
		self.ety_mins['fg'] = 'black'

	def counting(self, *event):
		if self.ety_mins.get().isnumeric() and self.ety_secs.get().isnumeric():
			seconds_to_count = int(self.ety_mins.get())*60+int(self.ety_secs.get())
			time.sleep(seconds_to_count)
			self.notify('Countdown', 'Time is over!')
		else:
			messagebox.showerror('Error', 'You put wrong input, only integers are allowed.')

	def notify(self, title, text):
	    os.system("""
	              osascript -e 'display notification "{}" with title "{}" sound name "Ping"'
	              """.format(text, title))


def main():
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()
