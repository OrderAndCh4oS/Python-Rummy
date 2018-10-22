# -*- coding: utf-8 -*-

from rummy.player.ai import AI
from rummy.player.human import Human
from rummy.ui.menu_action_dialog import MenuActionDialog
from rummy.ui.user_input import UserInput


class SetupPlayers:
    players = []
    number_of_players = -1
    number_of_opponents = -1

    @staticmethod
    def choose_players():
        SetupPlayers.number_of_players = int(UserInput.create_input(MenuActionDialog.human_players()))
        if SetupPlayers.number_of_players in [0, 1]:
            SetupPlayers.number_of_opponents = int(UserInput.create_input(MenuActionDialog.ai_players(SetupPlayers.number_of_players)))

    @staticmethod
    def create_players():
        i = 0
        SetupPlayers.players = []
        for j in range(int(SetupPlayers.number_of_players)):
            i += 1
            SetupPlayers.players.append(Human(i))
        for j in range(int(SetupPlayers.number_of_opponents)):
            i += 1
            SetupPlayers.players.append(AI(i))
        return SetupPlayers.players
