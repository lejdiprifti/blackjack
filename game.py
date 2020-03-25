from deck import Deck
from player import Player
from card import Card

class Game():

    def __init__(self):
        print('Welcome to BlackJack developed by Lejdi Prifti!')
        self.begin_game()

    def begin_game(self):
        choice = input('Do you want to play a game? y/n ')
        if choice != 'y' and choice != 'n':
            self.begin_game()
        elif choice == 'y':
            self.identify_player()
        else:
            pass
        
    def identify_player(self):
            name = input('Please, write your name to start the game. ')
            while True:
                try:
                    account = int(input('Please, input the amount of money you want to play with. '))
                    player = Player(name, account)
                    return player
                except ValueError:
                    print('Wrong amount of money provided. Please provide a valid amount.')
    
    def start_game(self):
        player = self.identify_player()
        deck = Deck()
        cards = deck.create_card_array()
        