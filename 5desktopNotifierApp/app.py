import os
import time

def notifiesSetup(quantity, frequency, title, subtitle, text, sound):

	def notify(title, text, subtitle, sound):
	    os.system("""
	              osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "{}"'
	              """.format(text, title, subtitle, sound))

	for i in range(quantity):
		notify(title, text, subtitle, sound)
		time.sleep(frequency)


print("Welcome to simple notifier/reminder for MacOS!\n")
print("Please input some data:")

notificationTitle = str(input("Type notification Title (leave for default): "))
if notificationTitle == "":
	notificationTitle = "Notification"

notificationSubtitle = str(input("Type notification Subtitle (leave for blank): "))

notificationText = str(input("Type notification Text (leave for default): "))
if notificationText == "":
	notificationText = "This is your notification."

notificationSound = str(input("Type notification Sound (leave for default): "))
if notificationSound == "":
	notificationSound = "default"

try:
	notificationQuantity = int(input("Type notification Quantity (leave for 1): "))
except ValueError:
	notificationQuantity = 1

try:
	notificationFrequency = int(input("Type notification Frequency (in secs)(leave if it happend once): "))
except ValueError:
	notificationFrequency = 0

notifiesSetup(notificationQuantity, notificationFrequency, notificationTitle, notificationSubtitle, notificationText, notificationSound)