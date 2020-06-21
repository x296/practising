from random import randrange

print("\nWelcome to Dice Rolling Simulator!\n")

kDice = int(input("How many sides has dice you want to roll? Enter a value: "))
numberOfDice = int(input("How many dice you want to roll? Enter a number: "))

while True:

	print("")

	for dice in range(numberOfDice):
		print("		Dice nr " + str(dice + 1) + ": " + str(randrange(1, kDice + 1)))

	print("\nWhat you want to do?")
	print("1 - roll again with the same conditions,")
	print("2 - roll again with different conditions,")
	print("any other alfanumeric key - exit\n")

	try:
		userAnswer = int(input("Enter your answer (1, 2, 3): "))
	except ValueError:
		print("Thanks for using, simulator has ended!")
		break

	if userAnswer == 1:
		continue

	elif userAnswer == 2:
		print("")
		kDice = int(input("How many sides has dice you want to roll? Enter a value: "))
		numberOfDice = int(input("How many dice you want to roll? Enter a number: "))
		continue

	else:
		print("\nThanks for using, simulator has ended!")
		break