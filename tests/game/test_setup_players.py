# coding=utf-8

from rummy.game.setup_players import SetupPlayers
from rummy.ui.user_input import UserInput


class TestSetupPlayers:

    def test_choose_players(self, mocker):
        mocker.patch.object(UserInput, 'create_input', side_effect=['2', '1', '2'])
        SetupPlayers.choose_players()
        assert SetupPlayers.number_of_players == 2
        assert SetupPlayers.number_of_opponents == -1
        # Refresh SetupPlayers
        SetupPlayers.number_of_players = -1
        SetupPlayers.number_of_opponents = -1
        SetupPlayers.choose_players()
        assert SetupPlayers.number_of_players == 1
        assert SetupPlayers.number_of_opponents == 2

    def test_create_players(self, mocker):
        mocker.patch.object(SetupPlayers, 'choose_players')
        SetupPlayers.number_of_players = 2
        SetupPlayers.number_of_opponents = 2
        assert len(SetupPlayers.create_players()) == 4
