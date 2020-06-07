import tkinter as tk
from tkinter import messagebox
import wikipedia
from selenium import webdriver

class Application(tk.Frame):
	# Main initialization whole app
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title('wikipedia article reader')
		self.master.resizable(height=0, width=0)
		self.pack(fill=tk.BOTH)

		wikipedia.set_lang('en')
		self.is_generated = False

		# self.create_search_entry()
		# self.create_search_button()
		self.create_generate_button()

		self.master.protocol("WM_DELETE_WINDOW", self.quit_app)

	# def create_search_entry(self):
	# 	self.sch_ety = tk.Entry(self)
	# 	self.sch_ety.grid(row=0, column=0)

	# def create_search_button(self):
	# 	self.sch_btn = tk.Button(self, text='Search', command=self.search_article)
	# 	self.sch_btn.grid(row=0, column=1)

	def create_generate_button(self):
		self.gnt_btn = tk.Button(self, text='Generate', fg='red', width=20, command=self.generate_article)
		self.gnt_btn.pack()

	def create_article_title_label(self, article):
		self.art_ttl_lbl = tk.Label(self, text=article.title, font=('Helvetica', '15', 'bold'), wraplength=200)
		self.art_ttl_lbl.pack()

	def create_article_summary_label(self, article):
		self.art_cnt_lbl = tk.Label(self, text=article.summary, wraplength=400)
		self.art_cnt_lbl.pack()

	def create_redirect_button(self, article):
		self.rdt_btn = tk.Button(self, text='See all in Wikipedia', fg='blue', width=20, command=lambda:self.redirect_to_website(article.url))
		self.rdt_btn.pack()

	# def search_article(self):
	# 	return

	def generate_article(self):
		if self.is_generated:
			self.art_ttl_lbl.destroy()
			self.art_cnt_lbl.destroy()
			self.rdt_btn.destroy()
		else:
			self.is_generated = True
		try:
			random_article = wikipedia.page(wikipedia.random())
		except wikipedia.DisambiguationError as e:
			random_article = wikipedia.page(e.options[0])
		self.create_article_title_label(random_article)
		self.create_article_summary_label(random_article)
		self.create_redirect_button(random_article)

	def redirect_to_website(self, url):
		driver = webdriver.Safari() # Defining driver for Safari
		driver.get(url)

	def quit_app(self, *event):
		if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
			self.master.destroy()


def main():
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()
