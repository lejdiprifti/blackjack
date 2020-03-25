from deck import Deck
from player import Player

class Game():
    '''
    Lejdi Prifti @lejdi.dev
    Implements the whole logic for playing the BlackJack game.
    '''
    player_cards = []
    computer_cards = []

    def __init__(self):
        print('Welcome to BlackJack developed by Lejdi Prifti!')
        self.begin_game()

    def begin_game(self):
        '''
        Asks for input to play game or not and continues with the procedure.
        '''
        choice = input('Do you want to play a game? y/n ')
        if choice not in ('y', 'n'):
            self.begin_game()
        elif choice == 'y':
            player = self.identify_player()
            self.place_bet(player)
        else:
            pass

    def identify_player(self):
        '''
        '''
        name = input('Please, write your name to start the game. ')
        while True:
            try:
                account = int(input('Please, input the amount of money you want to play with. '))
                player = Player(name, account)
                return player
            except ValueError:
                print('Wrong amount of money provided. Please provide a valid amount.')
    
    def place_bet(self, player):
        '''
        '''
        while True:
            try:
                bet = int(input(f"Hello, {player.name}! What's your bet for this hand? "))
                if bet < player.account:
                    player.place_bet(bet)
                    self.start_game(player, bet)
                    pass
                else:
                    print('Bet cannot be larger than your current account.')
            except:
                print('Please, provide a valid bet.')
                self.place_bet(player)

    def handle_first_cards(self, cards, player):
        '''
        INPUT: an array of cards
        OUTPUT: adds two cards to the players' cards array and computer's cards array
        '''
        for i in range(0, 3, 2):
            self.player_cards.append(cards.pop(i))
            self.computer_cards.append(cards.pop(i))
        print(f'{player.name}, you have this cards.\n{str(self.player_cards[0])}\n{str(self.player_cards[1])}')
        print(f'Dealer, you have this cards: \n{str(self.computer_cards[0])}\nHidden')


    def check_sum(self, user_array):
        '''
        '''
        sum_array = 0
        for card in user_array:
            sum_array = sum_array + card.points
        if sum_array < 21:
            return 'CONTINUE'
        elif sum_array == 21:
            return 'WON'
        else:
            return 'BUST'

    def hit(self, cards, user_array):
        user_array.append(cards.pop())

    def check_result(self):
        player_sum = 0
        computer_sum = 0
        for card in self.player_cards:
            player_sum = player_sum + card.points
        for card in self.computer_cards:
            computer_sum = computer_sum + card.points
        return player_sum > computer_sum

    def replay(self, player):
        answer = input(f'{player.name}, do you want to play another hand? y/n ')
        if answer == 'y':
            self.place_bet(player)
        elif answer == 'n':
            print(f'It was a pleasure to play with you. You now have {player.account}$.')
        else:
            self.replay(player)

    def validate_hit_result(self, hit_result, player, bet):
        if hit_result == 'WON':
            print(f'Congrats, {player.name}! You won!')
            player.win_bet(bet)
        elif hit_result == 'BUST':
            if player.name == 'Dealer':
                 print(f'Congrats! You won {bet}$.')
            else:
                print(f'Whoops! {player.name}, you lost this hand.')

    def get_sum_computer_cards(self):
        sum_cards = 0
        for card in self.computer_cards:
            sum_cards += card.points
        return sum_cards
    
    def print_player_cards(self):
        '''
        '''
        for card in self.player_cards:
            print(card)
    
    def print_dealer_cards(self):
        '''
        '''
        for i in range(0, len(self.computer_cards) - 1):
            print(self.computer_cards[i])

    def print_full_dealer_cards(self):
        for card in self.computer_cards:
            print(card)

    def start_game(self, player, bet):
        self.player_cards = []
        self.computer_cards = []

        # create the deck of cards
        deck = Deck()
        cards = deck.create_card_array()
        # distribute the first two cards to the players
        self.handle_first_cards(cards, player)
        # ask for hit or stay
        while True:
            player_choice = input(f'{player.name}, do you want to hit or stay? h/s ')

            if player_choice == 'h':

                self.hit(cards, self.player_cards)
                player_result = self.check_sum(self.player_cards)
                print(f'{player.name}')
                self.print_player_cards()

                # check if the player has won or busted
                if player_result == 'WON' or player_result == 'BUST':
                    self.validate_hit_result(player_result, player, bet)
                    print(f'{player.name}')
                    self.print_player_cards()
                    print('Dealer')
                    self.print_full_dealer_cards()
                    break

            elif player_choice == 's':
                while self.get_sum_computer_cards() < 17:
                    self.hit(cards, self.computer_cards)
                print('Dealer:')
                self.print_full_dealer_cards()
                # check the sum of both players and if True, finish this hand
                if self.check_result():
                    player.win_bet(bet)
                    print(f'Congrats! You won {bet}$.')
                else:
                    print(f'Whoops! You lost the bet.')
                break
        print(f'{player.name}, you currently have {player.account}$.')
        self.replay(player)

game = Game()
