class Player():

    def __init__(self, name, account):
        self.name = name
        self.account = account

    def place_bet(self, bet):
        self.account -= bet
    
    def win_bet(self, bet):
        self.account += 2 * bet
    
    def __str__(self):
        return f'Player: name = {self.name} and account = {self.account}'