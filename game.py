from deck import Deck
from player import Player

class Game():

    playerCards = []
    computerCards = []

    def __init__(self):
        print('Welcome to BlackJack developed by Lejdi Prifti!')
        self.begin_game()

    def begin_game(self):
        choice = input('Do you want to play a game? y/n ')
        if choice != 'y' and choice != 'n':
            self.begin_game()
        elif choice == 'y':
            self.start_game()
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
    
    def place_bet(self, player):
        try:
            bet = int(input(f"Hello, {player.name}! What's your bet for this hand? "))
            return bet
        except:
            print('Please, provide a valid bet.')
            self.place_bet(player)

    def handle_first_cards(self,cards):
        '''
        INPUT: an array of cards
        OUTPUT: adds two cards to the players' cards array and computer's cards array
        '''
        for i in range(0,3,2):
            self.playerCards.append(cards.pop(i))
            self.computerCards.append(cards.pop(i))


    def hit_or_stay(self, player):
        choice = input(f'{player.name}, do you want to hit or stay? h/s')
        return choice


    def check_sum(self, userArray):
        sum = 0
        for card in userArray:
            sum = sum + card.points
        if sum < 21:
            return sum
        elif sum == 21:
            return 'WON'
        else:
            return 'BUST'
    
    def hit(self, cards, userArray):
        self.userArray.append(cards.pop())
        self.check_sum(self.userArray)
            
    def check_result(self):
        playerSum = 0 
        computerSum = 0
        for card in self.playerCards:
            playerSum = playerSum + card.points
        for card in self.computerCards:
            computerSum = computerSum + card.points
        return playerSum > computerSum
        

    def start_game(self):
        player = self.identify_player()
        deck = Deck()
        cards = deck.create_card_array()
        bet = self.place_bet(player)
        # distribute the first two cards to the players
        self.handle_first_cards(cards)
        #ask for hit or stay
        while True:
            playerChoice = self.hit_or_stay(self, player)
            if playerChoice == 'h':
                self.hit(cards, self.playerCards)
                self.hit(cards, self.computerCards)
            elif playerChoice == 's':
                if self.check_result():
                    player.win_bet(bet)
                    print(f'Congrats! You won {bet}$.')
                    break
        self.start_game()

game = Game()