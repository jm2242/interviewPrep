import random

# describing classes for a card deck, based on Chapter 8 from openbookproject.net




''' card should have rank and suit attributes
Use integers to encode ranks and suits for easy comparison
Spades -> 3
Hearts -> 2
Diamonds -> 1
Clubs -> 0


Jack -> 11
Queen -> 12
King -> 13

'''


class Card:
	SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    RANKS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King')

	def __init__(self, suit=0, rank=0):
		self.suit = suit
		self.rank = rank


	# define a to string method for easy printing
	def __str__(self):
		return '{0} of {1}'.format(Card.RANKS[self.rank], Card.SUITS[self.suit])


	# define a comparison function
	def __cmp__(self, other):
		# check suits first, this decision is arbitrary
		if self.suit > other.suit:
			return 1
		elif self.suit < other.suit:
			return -1

		# check ranks next
		if self.rank > other.rank:
			return 1
		elif self.rank < other.rank:
			return -1

		# ranks are the same
		return 0


class Deck:
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				self.cards.append(Card(suit, rank))

	# shuffles the deck of cards in place using the Fisher-Yates shuffle implemented
	# in place
	def shuffle(self):
		random.shuffle(self.cards)

	# remove a card if it exists and return True, otherwise return False
	def remove(self, card):
		if card in self.cards:
			self.cards.remove(card)
			return True
		else:
			return False

	# pop an item from the bottom of the deck
	def pop(self):
		return self.cards.pop()

	def is_empty(self):
		return len(self.cards) == 0

	# not obvious where this method should go, but since it oerates on a deck
	# and on potentially many hands, makes sense to put it here
	def deal(self, hands, num_cards=999):
		num_hands = len(hands)
		for i in range(num_cards):

			# break if we are out of hands
			if self.is_empty():
				break

			card = self.pop()

			# round robbin style dealing
			hand = hands[i%num_hands]
			hand.add(card)



	def __str__(self):
		for card in self.cards:
			print card

# A Hand has similar operations to a deck, such as adding and removing cards
# makes sense to to make Hand a subclass of Deck
class Hand(Deck):
	def __init__(self, name=""):
		self.cards = []
		self.name = name


	def add(self, card):
		self.cards.append(card)


# basic chores of a card game
# can inherit from this class to add features
class CardGame:
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()


























