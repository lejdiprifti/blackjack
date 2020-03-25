from card import Card
import random
class Deck():

    suits = ['clubs','diamonds','hearts','spades']
    names = ['ace', '2', '3', '4', '5', '6','7','8','9','10','Jack','Queen','King']
    cardArray = []
    def __init__(self):
        pass

    def create_card_array(self):
        for name in self.names:
            for suit in self.suits:
                card = Card(name, suit, self.get_points(name))
                self.cardArray.append(card)
        return random.shuffle(self.cardArray)
    
    def get_points(self,name):
        switcher = {
            'ace': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 10,
            'Queen': 10,
            'King': 10
        }
        return switcher.get(name, "Invalid name!")