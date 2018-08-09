# -*- coding: utf-8 -*-
from rummy.player.ai import AI
from rummy.player.human import Human


class SetupPlayers:
    players = []
    numberOfPlayers = -1
    numberOfOpponents = -1

    def __init__(self):
        self.choosePlayers()

    def choosePlayers(self):
        numberOfPlayers = -1
        while numberOfPlayers not in [i for i in range(0, 5)]:
            numberOfPlayers = input("Enter number of players (0-4)? ")
            numberOfPlayers = self.validNumberCheck(numberOfPlayers)
        if numberOfPlayers in [0, 1]:
            self.setupAI(numberOfPlayers)
        self.numberOfPlayers = numberOfPlayers

    def setupAI(self, numberOfPlayers):
        self.ai = True
        if numberOfPlayers == 0:
            self.chooseNumberOfAIOpponents(4)
        elif numberOfPlayers == 1:
            self.chooseNumberOfAIOpponents(3)

    def chooseNumberOfAIOpponents(self, maxOpponents):
        numberOfOpponents = -1
        while numberOfOpponents not in [i for i in range(maxOpponents - 2, maxOpponents + 1)]:
            numberOfOpponents = input("Enter number of opponents ({0}-{1})? ".format(maxOpponents - 2, maxOpponents))
            numberOfOpponents = self.validNumberCheck(numberOfOpponents)
        self.numberOfOpponents = numberOfOpponents

    @staticmethod
    def validNumberCheck(number):
        try:
            number = int(number)
        except ValueError:
            number = -1
            print("Not a valid number, please try again...")
        return number

    def createPlayers(self):
        i = 0
        players = []
        for j in range(self.numberOfPlayers):
            i += 1
            players.append(Human(i))
        for j in range(self.numberOfOpponents):
            i += 1
            players.append(AI(i))
        return players
