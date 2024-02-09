import time

#!/usr/bin/python
def displayRules():
	rulesCheckAnswer = 'true'
	rules = """
The War card game is a simple and classic two-player card game that requires no special equipment other than a standard 52-card deck. Here are the basic rules:
        
Objective: The goal of the game is to win all the cards.


Dealing: Each player receives 26 cards, dealt one at a time. Players place their stack of cards face down in front of them.

Gameplay:
Simultaneous Play: Players do not look at their cards. To play, both players count down from 3 and flip the top card of their stack face up.
Winning a Round: The player with the higher card wins the round and collects both cards, placing them at the bottom of their personal deck.
Ties (War): If both players flip the same card, a war begins:
Each player places three more cards face-down on the table.
Then, both players flip over a fourth card face up.
The player with the highest fourth card wins the war and collects all the cards (totaling 10 cards).
If the fourth cards are also the same, repeat the process until there is a winner.
Running Out of Cards: If a player doesn’t have enough cards for a war, they must place their last card face up.
		"""
	while rulesCheckAnswer == 'true':
		print(rules)
		rulesReRead = input("Would you like to read these rules again? Please enter yes or no to continue.\n")
		if rulesReRead == 'No' or rulesReRead == 'no':
			rulesCheckAnswer = 'false'
			break
		continue

def rulesIntro(): 
	rulesLock = 'true'
	while rulesLock == 'true':
		rulesQuestion = input("Would you like to read the rules for War? Please enter yes or no to continue.\n")
		
		if rulesQuestion == 'Yes' or rulesQuestion == 'yes':
			displayRules()
			rulesLock = 'false'
		elif rulesQuestion == 'No' or rulesQuestion == 'no':
			rulesLock = 'false'
def compareCards(playerCard, compCard):
	# need to add steps here to compare the two cards.
    pass

def dealCards():
	playerCards = 0
	compCards = 0
	return playerCards, compCards
	

def playHand(playerCard, compCard):
	print('Computer: X')
	print('\n\n\n')
	print('Player 1: X')
	time.sleep(1)
	print('3')
	time.sleep(1)
	print('2')
	time.sleep(1)
	print('1')
	time.sleep(1)
	flip = input('Hit f to flip!\n')
	# add a check here later to confirm f input
	print('Computer: ', playerCard)
	print('\n\n\n')
	print('Player 1: X', compCard)
	winner = compareCards(playerCard, compCard)
	if winner == 'player':
		print('Congratulations, you won this hand!')
	elif winner == 'computer':
		print('Sorry, you lost this hand.')
	else:
		# Need to figure out how to handle ties. 
        tieCards = 'true'
		
	
def playGame():
	playerCards, compCards = dealCards()
	while playerCards != 0 or compCards != 0:
		playHand()

def beginGame():
	print("Beginning game in")
	time.sleep(1)
	print('3')
	time.sleep(1)
	print('2')
	time.sleep(1)
	print('1')
	time.sleep(1)
	print('begin!')
	playGame()
		
def playAgain():
	loopQuestion = 'true'
	while loopQuestion == 'true':
		tryAgain = input('Would you like to play again? Type yes or no to continue.\n')
		if tryAgain == 'Yes' or tryAgain == 'yes':
			loopQuestion == 'false'
			break
		continue
	beginGame()
	
def gameRunning():
	beginGame()
	playAgain()

print("\n\nWelcome to the War Card Game!\n")
rulesIntro()
gameRunning()