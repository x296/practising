import sys

print("\nHello, this is Email Slicer, which can cut username and domain from you email adress.\n")

forbiddenCharacters = [" ", "!", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "[", "{", "]", "}", ":", ";", "\'", "\"", "\\", "|", ",", "<", ">", "/", "?", "`", "~", "£", "§"]

# Getting and stripping email adress
userEmail = input("Enter your email adress: ").strip()

# Searching for unwanted characters
for letter in userEmail:
	if letter in forbiddenCharacters:
		print("You probably mistyped email adress...")
		sys.exit()

try:
	# Cutting email adress to username and domain by searching "@" char
	userName = userEmail[:userEmail.index("@")]
	userDomain = userEmail[userEmail.index("@") + 1:]

	print("Your username is:", userName, "\nYour domain is:", userDomain)

# Catching errors, probably user didn't type "@" cahr
except ValueError:
	print("You probably mistyped email adress...")

except:
	print("Something went wrong")
