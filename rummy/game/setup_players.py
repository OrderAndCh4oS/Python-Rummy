# -*- coding: utf-8 -*-

from rummy.player.ai import AI
from rummy.player.human import Human
from rummy.ui.menu_action_dialog import MenuActionDialog
from rummy.ui.user_input import UserInput


class SetupPlayers:
    players = []
    number_of_players = -1
    number_of_opponents = -1

    def __init__(self):
        self.choose_players()

    def choose_players(self):
        self.number_of_players = UserInput.create_input(MenuActionDialog.human_players())
        if self.number_of_players in ['0', '1']:
            self.number_of_opponents = UserInput.create_input(MenuActionDialog.ai_players(self.number_of_players))

    def create_players(self):
        i = 0
        players = []
        for j in range(int(self.number_of_players)):
            i += 1
            players.append(Human(i))
        for j in range(int(self.number_of_opponents)):
            i += 1
            players.append(AI(i))
        return players
