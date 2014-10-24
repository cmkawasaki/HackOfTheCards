#This was written for Python 2.7
import Cards
import Player

#Begin Game with Title Announcement.
print "Tanto Cuore - Hack of the Cards Edition!"

isSuccess = False
#Request Number of Players (2-4 are supported)
while not isSuccess:
	try:
		print "What is the Number of players (2-4)?"
		playerCt = int(raw_input())
		if playerCt >= 2 and playerCt <= 4:
			isSuccess = True
		else:
			print "Invalid Number Detected."
	except ValueError, argument:
		print "Exception hit: ", argument

print "Number of Players: ", playerCt
players = []
factory = Cards.DeckFactory()

#Set up Players' Decks, which include 7 '1 Love' cards and 3 'Chambermaid' cards
for i in range(1,playerCt+1):
	print "Please insert Player #%s's name: " % i
	name = raw_input()
	item = Player.Player(name)
	item.DiscardPile = factory.CreatePlayerDeck()
	item.DrawHand()
	players.append(item)

#Set up Central Purchasing area - Love Cards, Chambermaids, Maids, and so on.
gameBoard = factory.CreateGameBoard()

gameBoard.PrintStatus()
