from random import randint
from gameFunctions import gameVars

def winorlose(status):
	#print (canlled win or lose function", status, "\n")
	print("you", status, "! would you like to play again?")
	choice = input ("Y / N?")

	if choice == "Y" or choice == "y":
		#reset the game and start all over again
		gameVars.player_lives = 1
		gameVars.computer_lives = 1
		player = False
		gameVars.computer = gameVars.choices [randint(0, 2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice. Yes or No!")
		winorlose(status)