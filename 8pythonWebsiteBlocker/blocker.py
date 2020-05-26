# Run this script as root
import tkinter as tk
import time 
from datetime import datetime as dt 

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title('Website Blocker')
		self.master.resizable(height=0, width=0)
		self.pack(fill=tk.BOTH)

		self.create_label('This is button which is used to switching modes...')
		self.create_button()
		self.create_label('Now all websites are allowed')

	def create_label(self, txt):
		self.lbl = tk.Label(self, text=txt)
		self.lbl.pack()

	def create_button(self):
		self.btn = tk.Button(self, text='Working time', command=self.if_blocking)
		self.btn.pack()

	def if_blocking(self):
		print(self.btn['text'])
		if self.btn['text'] == 'Working time':
			self.btn['text'] = 'Fun time'
			self.lbl['text'] = 'Now some websites are forbidden'

			with open(hosts_path, 'r+') as file:
				content = file.read()
				for website in website_list:
					if website in content:
						pass
					else:
						# mapping hostnames to your localhost IP address
						file.write(redirect + " " + website + "\n")
		else:
			self.btn['text'] = 'Working time'
			self.lbl['text'] = 'Now all websites are allowed'

			with open(hosts_path, 'r+') as file:
				content=file.readlines()
				file.seek(0)
				for line in content:
					if not any(website in line for website in website_list):
						file.write(line)
				# removing hostnmes from host file
				file.truncate()

# change hosts path according to your OS
hosts_path = "/etc/hosts"
# bad IP
redirect = "0.0.0.0"

# websites That you want to block
website_list = ["www.instagram.com", "instagram.com", "www.youtube.com", "youtube.com"]

def main():
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()

