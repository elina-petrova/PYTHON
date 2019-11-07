# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose
from gameFunctions import comparison
from gameFunctions import config



# choices is an array => an array is a container that can hold multiple values
# arrays are 0-based -> first entry is 0, 2nd is 1, 3rd is 2 etc


# set the computer variable to one of these choices (0, 1 or 2)
config.computer = config.choices[randint(0, 2)]

# set up the game loop so that we don't have to restart all the time
config.player = False

while config.player is False:
	# set player to True
	print("**********************************")
	print("Computer lives: ", config.computer_lives, "/5\n")
	print("Player lives: ",config. player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("**********************************")

	config.player = input("choose rock, paper or scissors: ")
	config.player = config.player.lower()

	print("computer chose ", config.computer, "\n")
	print("player chose ", config.player, "\n")

	comparison.compare(config.player, config.computer)




	# handle all lives lost for player or AI
	if config.player_lives == 0:
		winlose.winorlose("lost")

	elif config.computer_lives == 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		config.player = False
		config.computer = config.choices[randint(0, 2)]	