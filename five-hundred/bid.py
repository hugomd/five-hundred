class BidSuit:
	suits = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES', 'NO_TRUMPS', 'MISERE', 'OPEN_MISERE', 'PASS']

	def __init__(self, suit):
		suit = suit.upper()

		if not suit in BidSuit.suits:
			raise ValueError(f'"{suit}" is not a valid bid suit')
		else:
			self.suit = suit

	def to_string(self):
		return self.suit.replace('_', ' ').title()

	def to_minimal_string(self):
		return self.suit[0].upper()

	def __str__(self):
		return self.to_string()

	def __eq__(self, other):
		# Suit to Suit comparison - e.g. suit == other_suit
		if type(other) is BidSuit or type(other) is CardSuit:
			return self.suit == other.suit

		# Suit to string comparison - e.g. suit == "HEARTS"
		if type(other) is str:
			return self.suit == other.upper()

		return False

class BidValue:
	values = [6, 7, 8, 9, 10]

	def __init__(self, value):
		if not value in BidValue.values:
			raise ValueError(f'"{value}" is not a valid bid value')
		else:
			self.value = value

	def to_string(self):
		return str(self.value)

	def to_minimal_string(self):
		return self.to_string()

	def __str__(self):
		return self.to_string()

	def __eq__(self, other):
		# Bid to Bid comparison - e.g. value == other_value
		if type(other) is BidValue:
			return self.value == other.value

		# Bid to int comparison - e.g. value == 8
		if type(other) is int:
			return self.value == other

		return False

class Bid:
	def __init__(self, player, value, suit):
		self.player = player
		self.value = value
		self.suit = suit