# coding=utf-8
from rummy.game.players import Players
from rummy.ui.user_input import UserInput


class TestSetupPlayers:

    def test_choose_players(self, mocker):
        mocker.patch.object(UserInput, 'create_input', side_effect=['2'])
        players = Players()
        players.choose_players()
        players.choose_opponents()
        assert players.number_of_players == 2
        assert players.number_of_opponents == -1

    def test_choose_players_with_opponents(self, mocker):
        mocker.patch.object(UserInput, 'create_input', side_effect=['1', '2'])
        players = Players()
        players.choose_players()
        players.choose_opponents()
        assert players.number_of_players == 1
        assert players.number_of_opponents == 2
        assert len(players.get_players()) == 3
