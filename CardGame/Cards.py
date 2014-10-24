#This was written for Python 2.7

class Card(object):
	def __init__(self):
		self.Title = ""
		self.Description = ""
		self.Cost = 0
		self.VictoryPoints = 0
		self.IsServable = False
		self.IsChamberable = False
		self.IsLove = False
		self.ChamberCost = 0
		self.DrawBonus = 0
		self.LoveBonus = 0
		self.ServingsBonus = 0
		self.EmploymentBonus = 0

class OneLove(Card):
	def __init__(self):
		super(Card, self)
		self.Title = "1 Love"
		self.Cost = 1
		self.IsLove = True
		self.LoveBonus = 1

class TwoLove(Card):
	def __init__(self):
		super(Card, self)
		self.Title = "2 Love"
		self.Cost = 4
		self.IsLove = True
		self.LoveBonus = 2

class ThreeLove(Card):
	def __init__(self):
		super(Card, self)
		self.Title = "3 Love"
		self.Cost = 7
		self.IsLove = True
		self.LoveBonus = 3

class ColetteFramboise(Card):
	def __init__(self):
		super(Card, self)
		self.Title = "Colette Framboise"
		self.Description = "At the end of the game, if you have more Colette's employed than any other player, you gain 5 VP."
		self.Cost = 3
		self.VictoryPoints = 1
		self.IsChamberable = True
		self.ChamberCost = 2

class MarianneSoleil(Card):
	def __init__(self):
		super(Card, self)
		self.Title = "Marianne Soleil"
		self.Description = ""
		self.Cost = 9
		self.VictoryPoints = 6

#Cards in Deck:
#36x 1 Love, 12x 2 Love, 8x 3 Love
#24x Colette Framboise, 8x Marianne Soleil
#Blue maids are 10x, except Ophelia Grail and Anise Greenaway, which have 8
#1 of Each Private Maid
#10x Illness
#16x Bad Habit
class DeckFactory(object):
	def __init__(self):
		self.OneLove = 36
		self.Colette = 24
	def CreatePlayerDeck(self):
		newDeck = []
		for i in range(1,8):
			newDeck.append(OneLove())
			self.OneLove -= 1
		for i in range(1,4):
			newDeck.append(ColetteFramboise())
			self.Colette -= 1
		return newDeck
	def CreateGameBoard(self):
		board = GameBoard()
		board.LoveStacks.append(CardStack(type(OneLove()), self.OneLove))
		board.LoveStacks.append(CardStack(type(TwoLove()), 12))
		board.LoveStacks.append(CardStack(type(ThreeLove()), 8))
		board.GreenMaidStacks.append(CardStack(type(ColetteFramboise()), self.Colette))
		board.GreenMaidStacks.append(CardStack(type(MarianneSoleil()), 8))

		#TODO: Implement Blue Stacks

		#TODO: Implement Private Maids

		#TODO: Implement Events

		return board


class CardStack(object):
	def __init__(self, cardType, number):
		self.Type = cardType
		item = cardType()
		self.CardTitle = item.Title
		self.Number = number
	def AddCard(self):
		self.Number += 1
	def PopCard(self):
		self.Number -= 1
		return cardType()

class GameBoard(object):
	def __init__(self):
		self.LoveStacks = []
		self.GreenMaidStacks = []
		self.BlueMaidStacks = []
		self.PrivateMaidStacks = []
	def PrintStatus(self):
		for i in self.LoveStacks:
			print "'%s' - %s remaining." % (i.CardTitle, i.Number)
		for i in self.GreenMaidStacks:
			print "'%s' - %s remaining." % (i.CardTitle, i.Number)
		for i in self.BlueMaidStacks:
			print "'%s' - %s remaining." % (i.CardTitle, i.Number)
		for i in self.PrivateMaidStacks:
			print "'%s' - %s remaining." % (i.CardTitle, i.Number)
