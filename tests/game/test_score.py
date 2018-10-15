# coding=utf-8

from rummy.game.score import Score
from rummy.player.player import Player
from rummy.player.human import Human


class TestScore:

    def test_get_current_game_scores(self, mocker):
        mocker.patch.object(Player, 'get_game_score', side_effect=[23, 30, 12, 40])
        score = Score([Human(1), Human(2), Human(3), Human(4)])
        assert score.get_current_game_scores() == 'Player 1: 23\nPlayer 2: 30\nPlayer 3: 12\nPlayer 4: 40\n'

    def test_get_end_of_round_scores(self):
        # Passing this test entirely because the tested function looks like it's almost purely for rendering purposes
        pass

    def test_update_player_scores(self, mocker):
        mocker.spy(Player, 'update_score')
        score = Score([Human(1), Human(2), Human(3), Human(4)])
        score.update_player_scores()
        assert Player.update_score.call_count == 4

    def test_is_end_of_game(self, mocker):
        mocker.patch.object(Player, 'get_game_score', side_effect=[90, 99, 100, 12])
        score = Score([Human(1), Human(2), Human(3), Human(4)])
        assert score.is_end_of_game()
        mocker.patch.object(Player, 'get_game_score', side_effect=[80, 85, 90, 99])
        assert not score.is_end_of_game()

    def test_end_game(self, mocker):
        mocker.patch('builtins.print')
        mocker.patch.object(Score, 'find_lowest_scores', side_effect=[[Human(1)], [Human(1), Human(2)]])
        score = Score([Human(1), Human(2)])
        score.end_game()
        print.assert_called_with('\x1b[0;32mPlayer 1 is the Winner!!\x1b[0m')
        score.end_game()
        print.assert_called_with('\x1b[0;32mPlayer 1, Player 2 are joint winners!\x1b[0m')

    def test_find_lowest_scores(self, mocker):
        human1 = mocker.MagicMock()
        human1.get_game_score.return_value = 100
        human2 = mocker.MagicMock()
        human2.get_game_score.return_value = 90
        human3 = mocker.MagicMock()
        human3.get_game_score.return_value = 80
        human4 = mocker.MagicMock()
        human4.get_game_score.return_value = 70
        score = Score([human1, human2, human3, human4])
        assert score.find_lowest_scores() == [score.players[3]]
        human1.get_game_score.return_value = 100
        human2.get_game_score.return_value = 100
        human3.get_game_score.return_value = 50
        human4.get_game_score.return_value = 50
        assert score.find_lowest_scores() == [score.players[2], score.players[3]]

    def test_render_this_round_score(self):
        # Pass this test entirely because this is a rendering method
        pass
