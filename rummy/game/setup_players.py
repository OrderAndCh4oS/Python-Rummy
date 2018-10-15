# -*- coding: utf-8 -*-

from rummy.player.ai import AI
from rummy.player.human import Human


class SetupPlayers:
    players = []
    number_of_players = -1
    number_of_opponents = -1

    def __init__(self):
        self.choose_players()

    def choose_players(self):
        number_of_players = -1
        while number_of_players not in [i for i in range(0, 5)]:
            number_of_players = input("Enter number of players (0-4)? ")
            number_of_players = self.valid_number_check(number_of_players)
        if number_of_players in [0, 1]:
            self.setup_ai(number_of_players)
        self.number_of_players = number_of_players

    def setup_ai(self, number_of_players):
        if number_of_players == 0:
            self.choose_number_of_ai_opponents(4)
        elif number_of_players == 1:
            self.choose_number_of_ai_opponents(3)

    def choose_number_of_ai_opponents(self, max_opponents):
        number_of_opponents = -1
        while number_of_opponents not in [i for i in range(max_opponents - 2, max_opponents + 1)]:
            number_of_opponents = input(
                "Enter number of opponents ({0}-{1})? ".format(max_opponents - 2, max_opponents))
            number_of_opponents = self.valid_number_check(number_of_opponents)
        self.number_of_opponents = number_of_opponents

    def create_players(self):
        i = 0
        players = []
        for j in range(self.number_of_players):
            i += 1
            players.append(Human(i))
        for j in range(self.number_of_opponents):
            i += 1
            players.append(AI(i))
        return players

    # Todo: move to a new class
    @staticmethod
    def valid_number_check(number):
        try:
            number = int(number)
        except ValueError:
            number = -1
            print("Not a valid number, please try again...")
        return number
