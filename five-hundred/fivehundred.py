from account import *
from bid import Bid
from deck import Deck

from collections import OrderedDict
from enum import Enum

class Player:
	def __init__(self, account):
		self.account = account

	def __str__(self):
		return self.account.username

	def __repr__(self):
		return f'Player({self.account.uuid})'

class Team:
	def __init__(self, players):
		self.players = players
		self.score = 0

	def __str__(self):
		return 'Players: ' + ', '.join([str(player.account) for player in self.players]) + '\n'
			+ 'Score: ' + str(self.score)

	def __repr__(self):
		return 'Team(players=[' + ', '.join([player.account.uuid for player in self.players]) + f'], score={self.score})'

class Kitty:
	def __init__(self, cards=None):
		self.cards = cards or []
		self.collected = False

	def append(self, value):
		self.cards.append(value)

	def collect_cards(self):
		if len(self.cards) < 3:
			raise ValueError(f'Kitty has fewer than 3 cards')

		cards, self.cards = self.cards, []
		self.collected = True
		return cards

	def __str__(self):
		return ', '.join([str(card) for card in self.cards]) + ' (' + ('' if self.collected else 'un') + 'collected)'

	def __repr__(self):
		return 'Kitty(cards=[' + ', '.join([card.to_minimal_string() for card in self.cards]) + f'], collected={self.collected})

class Trick:
	def __init__(self, leader):
		self.leader = leader
		self.cards = []

	def __str__(self):
		return f'Leader: {self.leader}\n'
			+ 'Cards: ' + ', '.join([str(card) for card in self.cards])

	def __repr__(self):
		return f'Trick(leader={self.leader}, cards=[' + ', '.join([card.to_minimal_str() for card in self.cards]) + '])'

class Hand:
	def __init__(self, dealer_id, player_ids):
		self.dealer_id = dealer_id
		self.deck = Deck()
		self.hands = OrderedDict({ player_id: [] for player_id in player_ids + dealer_id})
		self.kitty = None
		self.bids = []
		self.tricks = []

		self.deal()

	def deal(self):
		self.deck.shuffle()

		# Yeah, I know, there's no point following the dealing order. It just feels better this way.

		for player_id, hand in self.hands:
			for _ in range(3):
				hand.append(self.deck.draw_card())

		self.kitty = Kitty()
		self.kitty.append(self.deck.draw_card())

		for player_id, hand in self.hands:
			for _ in range(4):
				hand.append(self.deck.draw_card())

		self.kitty.append(self.deck.draw_card())

		for player_id, hand in self.hands:
			for _ in range(3):
				hand.append(self.deck.draw_card())

		self.kitty.append(self.deck.draw_card())

	def __str__(self):
		return 'Bids:' + '\n  '.join([str(bid) for bid in self.bids]) + '\nTricks:' + '\n  '.join([str(trick) for trick in self.tricks])

class FiveHundredGame:
	def __init__(self, teams):
		self.teams = teams
		self.hands = []

	def get_player(self, player_id):
		for team in self.teams:
			for player in team.players:
				if player.id == player_id:
					return player
		return None
