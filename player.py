from card import Card


class Player(object):
    def __init__(self, first_role, second_role):
        self.first_card = Card(first_role)
        self.second_card = Card(second_role)
