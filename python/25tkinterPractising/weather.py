import tkinter as tk
from PIL import Image, ImageTk
import requests
import json

root = tk.Tk()
root.title('Another app')
root.geometry('500x70')

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=AF4824BB-2EB8-40B0-BC30-8F8494719CF9

# Create zip lookup function
def ziplookup():
	# zip.get()
	# zip_lbl = tk.Label(root, text = zip.get())
	# zip_lbl.grid(row = 2, column = 0, columnspan = 2)

	try:
		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zip_box.get() + '&distance=5&API_KEY=AF4824BB-2EB8-40B0-BC30-8F8494719CF9')
		api = json.loads(api_request.content)
		city = api[0]['ReportingArea']
		quality = api[0]['AQI']
		category = api[0]['Category']['Name']

		if category == 'Good':
			weather_color = '#00E400'
		elif category == 'Moderate':
			weather_color = '#ffff00'
		elif category == 'Unhealthy for Sensitife Groups (USG)':
			weather_color = '#ff7e00'
		elif category == 'Unhealthy':
			weather_color = '#ff0000'
		elif category == 'Very Unhealthy':
			weather_color = '#8F3F97'
		elif category == 'Hazardous':
			weather_color = '#7E0023'

		root.configure(background = weather_color)
		my_lbl = tk.Label(root, text = city + ' air quality ' + str(quality) + ' ' + category, font = ('Helvetica', 20), background = weather_color)
		my_lbl.grid(row = 1, column = 0, columnspan = 2)
	except Exception as e:
		api = 'Error...'

zip_box = tk.Entry(root, width = 13)
zip_box.grid(row = 0, column = 0, sticky = tk.W + tk.E + tk.N + tk.S)

zip_btn = tk.Button(root, text = 'Lookup Zipcode', command = ziplookup)
zip_btn.grid(row = 0, column = 1, sticky = tk.W + tk.E + tk.N + tk.S)


root.mainloop()