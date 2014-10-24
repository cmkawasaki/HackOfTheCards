#This was written for Python 2.7
import random

class Player(object):
	def __init__(self, name):
		self.PlayerName = name
		self.DrawDeck = []
		self.DiscardPile = []
		self.Hand = []
		self.PlayArea = []
		self.MaidChamber = []

	def HandToString(self):
		toggleFirst = False
		totalString = ""
		for i in self.Hand:
			if toggleFirst is False:
				toggleFirst = True
			else:
				totalString += ", "
			totalString += i.Title
		return totalString

	def PlayAreaToString(self):
		toggleFirst = False
		totalString = ""
		for i in self.PlayArea:
			if toggleFirst is False:
				toggleFirst = True
			else:
				totalString += ", "
			totalString += i.Title
		return totalString

	def DrawHand(self):
		#At some point, when we get Private Maids that can change
		#this number, we'll want to update this.
		numberOfCards = 5
		for i in range(1,numberOfCards+1):
			self.DrawCard()
	def DrawCard(self):
		if len(self.DrawDeck) > 0:
			self.Hand.append(self.DrawDeck.pop())
		else:
			#Shuffle Discard Deck into Draw Deck
			random.shuffle(self.DiscardPile)
			self.DrawDeck = self.DiscardPile
			self.DiscardPile = []
			#If there is no discard pile, you cannot draw and it is wasted.
			if len(self.DrawDeck) > 0:
				self.Hand.append(self.DrawDeck.pop())
	def DiscardAll(self):
		self.DiscardPile.extend(self.Hand)
		self.Hand = []
		self.DiscardPile.extend(self.PlayArea)
		self.PlayArea = []



