from player.player import Player

class Setup:
    numberOfPlayers = -1
    ai = False
    aiOnly = False

    def __init__(self):
        self.choosePlayers()
        self.createPlayers()

    def choosePlayers(self):
        while self.numberOfPlayers not in [i for i in range(0, 5)]:
            self.numberOfPlayers = input("Enter number of players (0-4)? ")
            self.numberOfPlayers = self.validNumberCheck(self.numberOfPlayers)
        if self.numberOfPlayers in range(0, 2):
            self.ai = True
        if self.numberOfPlayers == 1:
            self.chooseNumberOfAIOpponents(3)
        if self.numberOfPlayers == 0:
            self.aiOnly = True
            self.chooseNumberOfAIOpponents(4)

    def chooseNumberOfAIOpponents(self, max):
        numberOfOpponents = 0
        while numberOfOpponents not in [i for i in range(max - 2, max + 1)]:
            numberOfOpponents = input("Enter number of opponents ({0}-{1})? ".format(max-2, max))
            numberOfOpponents = self.validNumberCheck(numberOfOpponents)
        self.numberOfPlayers += numberOfOpponents

    @staticmethod
    def validNumberCheck(number):
        try:
            number = int(number)
        except ValueError:
            number = 0
            print("Not a valid number, please try again...")
        return number

    def createPlayers(self):
        self.players = [Player(i + 1) for i in range(self.numberOfPlayers)]