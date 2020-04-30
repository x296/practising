import tkinter as tk
from PIL import Image, ImageTk
import requests
import json

root = tk.Tk()
root.title('Another app')
root.geometry('400x30')

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=AF4824BB-2EB8-40B0-BC30-8F8494719CF9

try:
	api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=AF4824BB-2EB8-40B0-BC30-8F8494719CF9')
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
	my_lbl.pack()
except Exception as e:
	api = 'Error...'

root.mainloop()