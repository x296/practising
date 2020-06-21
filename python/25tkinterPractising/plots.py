import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
root.title('Another app')
root.geometry('400x200')

def graph():
	house_prices = np.random.normal(200000, 25000, 5000)
	plt.polar(house_prices)
	plt.show()

my_btn = tk.Button(root, text = 'Graph it!', command = graph)
my_btn.pack()

root.mainloop()