import random
from player import Player


class Coup(object):
    def __init__(self):
        self.game_on = False

    def start_game(self, no_of_players):
        self.game_on = True

        deck = 4*['ambassador', 'assassin', 'captain', 'contessa', 'duke']
        random.shuffle(deck)

        self.deck = deck

    def new_player(self):
        first_card = self.deck.pop()
        second_card = self.deck.pop()

        return Player(first_card, second_card)
