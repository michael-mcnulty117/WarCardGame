import time
import random

#!/usr/bin/python
def displayRules():
	rulesCheckAnswer = 'true'
	rules = """
--------------------------------------------------------------------------------------------

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

--------------------------------------------------------------------------------------------
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
def convertFaceCard(cardToCheck):
	if cardToCheck == 'Jack':
		cardToReturn = 11
	elif cardToCheck == 'Queen':
		cardToReturn = 12
	elif cardToCheck == 'King':
		cardToReturn = 13
	elif cardToCheck == 'Ace':
		cardToReturn = 14
	else:
		cardToReturn = cardToCheck
	return cardToReturn
	
def compareCards(playerCard, compCard):
	# need to add steps here to compare the two cards.
	playerCardToCompare = playerCard[0]
	compCardToCompare = compCard[0]
	convertedPlayerCardToCompare = convertFaceCard(playerCardToCompare)
	convertedCompCardToCompare = convertFaceCard(compCardToCompare)

	if convertedPlayerCardToCompare == convertedCompCardToCompare:
		pass
		# add how to handle a tie here.
	elif convertedPlayerCardToCompare > convertedCompCardToCompare:
		return 'playerWinner'
	else:
		return "compWinner"

def dealCards():
    # Create a deck of cards
	suits = [" of Hearts", " of Diamonds", " of Clubs", " of Spades"]
	ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
	deck = [(rank, suit) for suit in suits for rank in ranks]
	# Shuffle the deck
	random.shuffle(deck)
	# Divide the deck into two arrays
	half_size = len(deck) // 2
	playerCards = deck[:half_size]
	compCards = deck[half_size:]
	return playerCards, compCards
	

def playHand(playerCard, compCard, playerCardCollection, compCardCollection, pCardCount, cCardCount):

	print('\nComputer (Cards',cCardCount,')')
	print('Player 1 (Cards',pCardCount,')')
	time.sleep(1)
	print('\n3')
	time.sleep(1)
	print('2')
	time.sleep(1)
	print('1')
	time.sleep(1)
	tryFlip = 'true'
	while tryFlip == 'true':
		flip = input('\nHit f to flip!\n')
		if flip == 'exit':
			quit()
		elif flip == 'f':
			tryFlip == 'false'
			break

    # this removes the , from the cards and converts it to a string.
	playerCardString = ''.join(str(card) for card in playerCard)
	compCardString = ''.join(str(card) for card in compCard)
	
    # Display each players card.
	print('Computer:', compCardString)
	print('Player 1:', playerCardString)
	
    # Determine the winner of the hand
	battleResult = compareCards(playerCard, compCard)
	
	time.sleep(4)
    # Output hand winner
	if battleResult == 'playerWinner':
		print('\nCongratulations, you won this hand!')
		playerCardCollection.append(compCard)
		playerCardCollection.append(playerCard)
		return playerCardCollection, compCardCollection
	elif battleResult == 'compWinner':
		print('\nSorry, you lost this hand.')
		compCardCollection.append(playerCard)
		compCardCollection.append(compCard)
		return playerCardCollection, compCardCollection
	else:
		# Need to figure out how to handle ties. 
		tieCards = 'true'
	time.sleep(2)
		
	
def playGame():
	# this gets the starting player hands.
	playerCards, compCards = dealCards()
	
    # this continues the game while either player has more than 0 cards.
	while playerCards != 0 or compCards != 0:
		# count how many cards each player has in their hand.
		playerCardCount = len(playerCards)
		compCardCount = len(compCards)

		# This gets each players card for this hand and removes it from the array
		playerCardToPlay = playerCards.pop(0)
		compCardToPlay = compCards.pop(0)
		
		playerCards, compCards = playHand(playerCardToPlay, compCardToPlay, playerCards, compCards, playerCardCount, compCardCount)

def beginGame():
	print("\nDealing Cards")
	time.sleep(1)
	print('.')
	time.sleep(1)
	print('.')
	time.sleep(1)
	print('.')
	time.sleep(1)
	print('Okay, let\'s begin!')
	playGame()
		
def playAgain():
	loopQuestion = 'true'
	while loopQuestion == 'true':
		tryAgain = input('Would you like to play again? Type yes or no to continue.\n')
		if tryAgain == 'Yes' or tryAgain == 'yes':
			loopQuestion == 'false'
			break
		elif tryAgain  == 'No' or tryAgain == 'no':
			loopQuestion = 'false'
			return loopQuestion
	
def gameRunning():
	playGame = 'true'
	while playGame == 'true':
		beginGame()
		keepPlaying = playAgain()
		if keepPlaying == 'false':
			playGame = 'false'
			print('\nThank you for playing WarCardGame!')
			print('\nGoodbye!\n')
			break
		continue

print("\n\nWelcome to the War Card Game!\n")
rulesIntro()
gameRunning()