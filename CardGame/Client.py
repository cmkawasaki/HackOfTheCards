def GetNumberInput(text, minvalue, maxvalue):
	isSuccess = False
	while not isSuccess:
		try:
			print text
			playerCt = int(raw_input())
			if playerCt >= minvalue and playerCt <= maxvalue:
				isSuccess = True
			else:
				print "Invalid Number Detected."
		except ValueError, argument:
			print "Exception hit: ", argument
	return playerCt

#This was written for Python 2.7
import Cards
import Player

#Begin Game with Title Announcement.
print "Tanto Cuore - Hack of the Cards Edition!"

#Request Number of Players (2-4 are supported)
playerCt = GetNumberInput("What is the Number of players (2-4)?", 2, 4)

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

#Begin game.
currentTurn = -1
while not gameBoard.IsGameOver():
	love = 0
	servings = 1
	employments = 1
	#Cycle Through Each Players' Turns
	currentTurn = (currentTurn+1)%len(players)
	activePlayer = players[currentTurn]
	print "It is now Player %s's turn:" % activePlayer.PlayerName
	print "Starting Hand: %s" % activePlayer.HandToString()

	#Servings/ChamberMaid Phase
	while servings > 0:
		print "Servings/ChamberMaid Phase:"
		activeCards = []
		for i in activePlayer.Hand:
			if i.IsServable or i.IsChamberable:
				activeCards.append(i)

		print "Pick an Option by Number Below (Servings = %s):" % servings
		for i in range(0, len(activeCards)):
			print "%s: Serve or Chamber %s" % (i, activeCards[i].Title)
		print "%s: End Phase" % len(activeCards)

		choice = GetNumberInput("Choice?", 0, len(activeCards))

		if choice == len(activeCards):
			break
		else:
			if activeCards[choice].IsServable and activeCards[choice].IsChamberable:
				print "Not Implemented Yet."
			elif activeCards[choice].IsServable:
				print "Serving %s" % activeCards[choice].Title
				servings -= 1
				love += activeCards[choice].LoveBonus
				servings += activeCards[choice].ServingsBonus
				employments += activeCards[choice].EmploymentBonus

				for i in range(0, activeCards[choice].DrawBonus):
					activePlayer.DrawCard()

				activePlayer.Hand.remove(activeCards[choice])
				activePlayer.PlayArea.append(activeCards[choice])

			elif activeCards[choice].IsChamberable:
				print "Chambering %s" % activeCards[choice].Title

				if activeCards[choice].ChamberCost > servings:
					print "Cannot Chamber this Card - it requires %s Servings." % activeCards[choice].ChamberCost
					continue

				servings -= activeCards[choice].ChamberCost

				activePlayer.Hand.remove(activeCards[choice])
				activePlayer.MaidChamber.append(activeCards[choice])

	#Add up Love
	for i in range(len(activePlayer.Hand)-1, -1, -1):
		if activePlayer.Hand[i].IsLove:
			love += activePlayer.Hand[i].LoveBonus
			activePlayer.PlayArea.append(activePlayer.Hand[i])
			activePlayer.Hand.pop(i)

	print "Current Hand: %s" % activePlayer.HandToString()
	print "Current Play Area: %s" % activePlayer.PlayAreaToString()

	#Employment Phase
	while employments > 0:
		print "Employment Phase (%s Employments, %s Love): " % (employments, love)
		validValues = []
		validValues.extend(gameBoard.LoveStacks)
		validValues.extend(gameBoard.GreenMaidStacks)
		validValues.extend(gameBoard.BlueMaidStacks)

		for i in range(0, len(validValues)):
			print "%s: %s (Cost %s, Number Remaining: %s)" % (i, validValues[i].CardTitle, validValues[i].Cost, validValues[i].Number)

		print "%s: Quit and End Turn." % len(validValues)
		choice = GetNumberInput("Choice?", 0, len(validValues))

		if choice == len(validValues):
			break
		
		itemToBuy = validValues[choice]
		if itemToBuy.Number is 0:
			print "There are no more items in stack!"
			continue
		if itemToBuy.Cost > love:
			print "Item too Expensive to buy!"
			continue

		employments -= 1
		love -= itemToBuy.Cost
		activePlayer.PlayArea.append(itemToBuy.PopCard())

	#End Turn, Draw Phase
	activePlayer.DiscardAll()
	activePlayer.DrawHand()

#After Game Ends, total Points
print "To Be Implemented!  Everyone Wins. :P"
