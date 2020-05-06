from pytube import YouTube
import tkinter as tk

class Application(tk.Frame):
	# Main initialization whole app
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title('YouTube Downloader')
		self.master.geometry('700x300')
		self.pack()
		self.create_instruction_label()
		self.create_ytLink_textbox()
		self.create_load_button()
		self.create_quit_button()

	# Creating specific widgets
	def create_instruction_label(self):
		self.instruction_lbl = tk.Label(self, text='Here is an instruction...')
		self.instruction_lbl.pack()

	def create_ytLink_textbox(self):
		self.ytLink_txtbx = tk.Entry(self, fg='grey')
		self.ytLink_txtbx.insert(0, 'paste YouTube video URL here...')
		self.ytLink_txtbx.bind('<FocusIn>', self.insert_URL)
		self.ytLink_txtbx.bind('<Return>', self.load_URL)
		self.ytLink_txtbx.pack()

	def create_load_button(self):
		self.load_btn = tk.Button(self, text='LOAD', command=self.load_URL)
		self.load_btn.bind('<Return>', self.load_URL)
		self.load_btn.pack()

	def create_download_label(self, value):
		self.download_lbl = tk.Label(self, text=value)
		self.download_lbl.pack()

	def create_download_button(self):
		self.download_btn = tk.Button(self, text='DOWNLOAD')
		self.download_btn.pack()

	def create_quit_button(self):
		self.quit_btn = tk.Button(self, text='QUIT', fg='red', command=self.quit_app)
		self.quit_btn.bind('<Return>', self.quit_app)
		self.quit_btn.pack()

	# Creating funcs for widgets
	def insert_URL(self, event):
		self.ytLink_txtbx.delete(0, tk.END)
		self.ytLink_txtbx['fg'] = 'black'

	def load_URL(self, *event):
		self.URL = self.ytLink_txtbx.get()
		self.ytFile = YouTube(self.URL)
		self.create_download_label(self.ytFile.title)
		for i, stream in zip(range(len(self.ytFile.streams.filter(adaptive=True, mime_type='video/mp4'))), reversed(self.ytFile.streams.filter(adaptive=True, mime_type='video/mp4').order_by('resolution'))):
			print(i + 1, stream.resolution)
			self.create_download_label(stream.resolution)
			self.create_download_button()

	def quit_app(self, *event):
		self.master.destroy()


def main():
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()
