class Card():

    def __init__(self, name, suit, points):
        self.name = name
        self.suit = suit
        self.points = points

    def __str__(self):
        return f'Card: name = {self.name} and suit = {self.suit}'

    def __len__(self):
        return f'Card has a total of {self.points} points.'
