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
            player = self.identify_player()
            self.start_game(player)
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
        while True:
            try:
                bet = int(input(f"Hello, {player.name}! What's your bet for this hand? "))
                if bet < player.account:
                    player.place_bet(bet)
                    return bet
                else:
                    print('Bet cannot be larger than your current account.')
            except:
                print('Please, provide a valid bet.')
                self.place_bet(player)

    def handle_first_cards(self,cards,player):
        '''
        INPUT: an array of cards
        OUTPUT: adds two cards to the players' cards array and computer's cards array
        '''
        for i in range(0,3,2):
            self.playerCards.append(cards.pop(i))
            self.computerCards.append(cards.pop(i))
        print(f'{player.name}, you have this cards.\n{self.playerCards[0].name} {self.playerCards[1].suit}\n{self.playerCards[1].name} {self.playerCards[1].suit}')
        print(f'Dealer, you have this cards: \n{self.computerCards[0].name} {self.computerCards[0].suit} \n Hidden')


    def check_sum(self, userArray):
        sum = 0
        for card in userArray:
            sum = sum + card.points
        if sum < 21:
            return 'CONTINUE'
        elif sum == 21:
            return 'WON'
        else:
            return 'BUST'
    
    def hit(self, cards, userArray):
        userArray.append(cards.pop())
        return self.check_sum(userArray)
            
    def check_result(self):
        playerSum = 0 
        computerSum = 0
        for card in self.playerCards:
            playerSum = playerSum + card.points
        for card in self.computerCards:
            computerSum = computerSum + card.points
        return playerSum > computerSum
        
    def validate_hit(self, hitResult, player, bet):
        if hitResult == 'WON':
            print(f'Congrats, {player.name}! You won!')
            player.win_bet(bet)
            print(f'{player.name}, you currently have {player.account}$.')
        elif hitResult == 'BUST':
            if player.name == 'Dealer':
                 print(f'Congrats! You won {bet}$.')
            else:
                print(f'Whoops! {player.name}, you lost this hand.')
                print(f'{player.name}, you currently have {player.account}$.')
    
    def print_card_arrays(self, array):
        for card in array:
            print(f'Card: {card.name} {card.suit}')

    def start_game(self, player):
        self.playerCards = []
        self.computerCards = []
        dealer = Player('Dealer',0)
        # create the deck of cards
        deck = Deck()
        cards = deck.create_card_array()
        # place the bet
        bet = self.place_bet(player)
        # distribute the first two cards to the players
        self.handle_first_cards(cards,player)
        # ask for hit or stay
        while True:
            playerChoice = input(f'{player.name}, do you want to hit or stay? h/s ')
            if playerChoice == 'h':
                playerResult = self.hit(cards, self.playerCards)
                self.validate_hit(playerResult,player,bet)
                print(f'{player.name}')
                self.print_card_arrays(self.playerCards)
                if playerResult == 'WON' or playerResult == 'BUST':
                    break
                computerResult = self.hit(cards, self.computerCards)
                self.validate_hit(computerResult,dealer,bet)
                print('Dealer')
                self.print_card_arrays(self.computerCards)
                if computerResult == 'WON' or computerResult == 'BUST':
                    break
            elif playerChoice == 's':
                # print the cards each player currently has
                print(f'{player.name}')
                self.print_card_arrays(self.playerCards)
                print('Dealer')
                self.print_card_arrays(self.computerCards)
                # check the sum of both players and if True, finish this hand
                if self.check_result():
                    player.win_bet(bet)
                    print(f'Congrats! You won {bet}$.')
                else:
                    print(f'Whoops! You lost the bet.')
                print(f'{player.name}, you currently have {player.account}$.')
                break
        self.start_game(player)

game = Game()