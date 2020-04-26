from random import seed
from random import randint

secretNumber = randint(0, 30~)

print("\nHello World! It is guessing game! (shh..! this is the answer: " + str(secretNumber) + ")\n")

playerNumber = input("Guess the number: ")

for i in range(4):
	if int(playerNumber) == secretNumber:
		print("\nCongratulations! You've guessed the secret number!")
		break
	elif int(playerNumber) > secretNumber:
		print("Wrong! Your number is higher ;)\n" + "Chances: " + str(i + 1) + "/5\n")
		playerNumber = input("Try again: ")
		continue
	else:
		print("Wrong! Your number is lower ;)\n" + "Chances: " + str(i + 1) + "/5\n")
		playerNumber = input("Try again: ")
		continue
else:
	print("You've lost!")