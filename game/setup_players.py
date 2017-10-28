# -*- coding: utf-8 -*-
from player.player_config import PlayerConfig


class SetupPlayers:
    numberOfPlayers = -1
    ai = False
    aiOnly = False

    def __init__(self):
        self.choosePlayers()
        self.players = self.createPlayers()

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

    def chooseNumberOfAIOpponents(self, maxOpponents):
        numberOfOpponents = 0
        while numberOfOpponents not in [i for i in range(maxOpponents - 2, maxOpponents + 1)]:
            numberOfOpponents = input("Enter number of opponents ({0}-{1})? ".format(maxOpponents - 2, maxOpponents))
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
        return [PlayerConfig(i + 1) for i in range(self.numberOfPlayers)]
