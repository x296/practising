import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
from PIL import ImageTk, Image
import urllib.parse
import io
import os

class Application(tk.Frame):
	# Main initialization whole app
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title('YouTube Downloader')
		self.master.geometry('500x400')
		self.pack(fill=tk.BOTH)
		self.create_instruction_label()
		self.create_ytLink_textbox()
		self.create_load_button()
		self.create_quit_button()

		self.master.protocol("WM_DELETE_WINDOW", self.quit_app)

	# Creating specific widgets
	def create_instruction_label(self):
		self.instruction_lbl = tk.Label(self, 
										text='''Hey,\npaste YouTube video URL below, smash LOAD button,\nclick DOWNLOAD button near resolution you are interested in\nand select directory to save file.''',
										justify=tk.LEFT)
		self.instruction_lbl.grid(row=0, column=0, columnspan=3)

	def create_ytLink_textbox(self):
		self.ytLink_txtbx = tk.Entry(self, fg='grey')
		self.ytLink_txtbx.insert(0, 'paste YouTube video URL here...')
		self.ytLink_txtbx.bind('<FocusIn>', self.insert_URL)
		self.ytLink_txtbx.bind('<Return>', self.load_URL)
		self.ytLink_txtbx.grid(row=1, column=0, columnspan=2)

	def create_load_button(self):
		self.load_btn = tk.Button(self, text='LOAD', width=10, command=self.load_URL)
		self.load_btn.bind('<Return>', self.load_URL)
		self.load_btn.grid(row=1, column=2)

	def create_ytVideo_title_label(self):
		self.ytVideo_title_lbl = tk.Label(self, text=self.ytFile.title)
		self.ytVideo_title_lbl.grid(row=2, column=0, columnspan=3)

	def create_download_label(self, i, value):
		self.download_lbl = tk.Label(self, text=value)
		self.download_lbl.grid(row=i, column=1)

	def create_video_download_button(self, i):
		self.download_btn = tk.Button(self, text='DOWNLOAD', fg='DodgerBlue2', width=10, command=lambda: self.download_video(i-3))
		self.download_btn.grid(row=i, column=2)

	def create_audio_download_button(self, i):
		self.download_btn = tk.Button(self, text='DOWNLOAD', fg='DodgerBlue2', width=10, command=lambda: self.download_audio(i-3))
		self.download_btn.grid(row=i, column=2)

	def create_ytVideo_thumbnail_label(self, rowspan):
		image = self.generate_image(240, 135, self.ytFile.thumbnail_url)
		self.ytVideo_thumbnail_lbl = tk.Label(self, image=image)
		self.ytVideo_thumbnail_lbl.image = image
		self.ytVideo_thumbnail_lbl.grid(row=3, column=0, rowspan=rowspan)

	def create_quit_button(self):
		self.quit_btn = tk.Button(self, width=10, text='QUIT', fg='red', command=self.quit_app)
		self.quit_btn.bind('<Return>', self.quit_app)
		self.quit_btn.grid(row=10, column=2)

	# Creating funcs for widgets
	def insert_URL(self, event):
		self.ytLink_txtbx.delete(0, tk.END)
		self.ytLink_txtbx['fg'] = 'black'

	def load_URL(self, *event):
		self.URL = self.ytLink_txtbx.get()
		self.ytFile = YouTube(self.URL)
		self.create_ytVideo_title_label()
		i = 0
		for i, stream in zip(range(len(self.ytFile.streams.filter(adaptive=True, mime_type='video/mp4'))), reversed(self.ytFile.streams.filter(adaptive=True, mime_type='video/mp4').order_by('resolution'))):
			self.create_download_label(i+3, stream.resolution)
			self.create_video_download_button(i+3)
		self.create_download_label(i+4, 'MP3')
		self.create_audio_download_button(i+4)
		self.create_ytVideo_thumbnail_label(i+2)

	def download_video(self, i):
		path_filename = self.save_file('.mp4')
		path = path_filename[:path_filename.rfind('/')]
		filename = path_filename[path_filename.rfind('/')+1:]
		self.ytFile.streams.filter(adaptive=True, mime_type='video/mp4').order_by('resolution')[-1-i].download(output_path=path, filename='video')
		self.ytFile.streams.filter(adaptive=True, mime_type='audio/mp4').order_by('abr')[-1].download(output_path=path, filename='audio')
		os.system('ffmpeg -i {} -i {} -c copy {}'.format(path+'/video.mp4', path+'/audio.mp4', path+'/'+self.creating_output_filename(filename)))
		os.system('rm {} {}'.format(path+'/video.mp4', path+'/audio.mp4'))

	def download_audio(self, i):
		path_filename = self.save_file('.mp3')
		path = path_filename[:path_filename.rfind('/')]
		filename = path_filename[path_filename.rfind('/')+1:]
		self.ytFile.streams.filter(adaptive=True, mime_type='audio/mp4').order_by('abr')[-1].download(output_path=path, filename='audio')
		os.system('ffmpeg -i {} {}'.format(path+'/audio.mp4', path+'/'+self.creating_output_filename(filename)))
		os.system('rm {}'.format(path+'/audio.mp4'))

	# Creating other funcs for app
	def creating_output_filename(self, src_string):

		special_characters = ['|', '&', ':', ';', '(', ')', '<', '>', '~', '*', '@', '?', '!', '$', '#', '[', ']', '{', '}', '\\', '/', '\'', '\"', '`', ' ']
		filename = ''
		for letter in src_string:
			if letter in special_characters:
				filename += '\\'
			filename += letter
		
		return filename

	def save_file(self, ext):
		path = filedialog.asksaveasfilename(initialfile=self.ytFile.title, defaultextension=ext)
		if path is None:
			return
		else:
			return path


	def generate_image(self, x, y, url):
		raw_data = urllib.request.urlopen(url).read()
		image = Image.open(io.BytesIO(raw_data))
		image = image.resize((x, y), Image.ANTIALIAS)
		image = ImageTk.PhotoImage(image)
		return image

	def quit_app(self, *event):
		if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
			self.master.destroy()


def main():
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()
