 # import the random package so we can generate a random AI choice from random import randint
from random import randint
from gameFunctions import winlose, gameVars, compare


while gameVars.player is False:
	print ("========================================")
	print ("Computer Lives:", gameVars.computer_lives, "/5")
	print ("Player Lives:", gameVars.player_lives, "/5")
	print ("========================================")
	print("Choose your weapon!" "")
	player=input ("choose rock, paper or scissors: \n")
	compare.compareChoices(player)
#start doing some logic and condition checking


	if gameVars.player_lives is 0:
		winlose.winorlose("lost")
			


	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")
			
	else:
		player = False
		gameVars.computer=gameVars.choices [randint(0,2)]










