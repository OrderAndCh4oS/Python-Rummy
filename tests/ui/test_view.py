# coding=utf-8

from rummy.deck.card import Card
from rummy.game.score import Score
from rummy.player.ai import AI
from rummy.player.human import Human
from rummy.ui.view import View


class TestView:

    def test_render(self, mocker):
        mocker.patch('builtins.print')
        View.render("Test print", end="\t\n")
        print.assert_called_with("Test print", end="\t\n")

    def test_render_template(self, mocker):
        expected = '\x1b[0;31mA Player has knocked, this is your last turn!!!\x1b[0m\n'
        output_message = View.prepare_template('/knocked.txt')
        assert output_message == expected

    def test_render_turn_start(self, mocker):
        player = Human(1)
        player.round = mocker.MagicMock()
        player.round.turn = 1
        player.round.current_player = 0
        player.round.deck.show_discard.return_value = 'Empty'
        player.hand.hand = [Card(x, y) for x, y in [("8", "S"), ("9", "S"), ("K", "S"), ("4", "H"),
                                                    ("8", "D"), ("J", "C"), ("K", "C")]]
        expected = "\x1b[0;34m#############################\x1b[0m\n" \
                   "Turn 1\n" \
                   "\x1b[0;37m-----------------------------\x1b[0m\n" \
                   "Player 1's turn\n" \
                   "\x1b[0;37m.............................\x1b[0m\n" \
                   "Hand Score: 66\n" \
                   "8♠, 9♠, K♠, 4\x1b[0;31m♥\x1b[0m, 8\x1b[0;31m♦\x1b[0m, J♣, K♣\n" \
                   "Discard Pile: Empty\n" \
                   "\x1b[0;37m.............................\x1b[0m\n"
        output_message = View.template_turn_start(player)
        assert output_message == expected

    def test_render_player_turn_end(self):
        player = Human(1)
        player.hand.hand = [Card(x, y) for x, y in [("8", "S"), ("9", "S"), ("J", "S"), ("K", "S"),
                                                    ("4", "H"), ("8", "D"), ("J", "C"), ("K", "C")]]
        expected = "\x1b[0;37m.............................\x1b[0m\n" \
                   "8♠, 9♠, J♠, K♠, 4\x1b[0;31m♥\x1b[0m, 8\x1b[0;31m♦\x1b[0m, J♣, K♣\n" \
                   "\x1b[0;32m1\x1b[0m,  \x1b[0;32m2\x1b[0m,  \x1b[0;32m3\x1b[0m,  \x1b[0;32m4\x1b[0m,  " \
                   "\x1b[0;32m5\x1b[0m,  \x1b[0;32m6\x1b[0m,  \x1b[0;32m7\x1b[0m,  \x1b[0;32m8\x1b[0m\n" \
                   "\x1b[0;37m.............................\x1b[0m\n"
        output_message = View.template_player_turn_end(player)
        assert output_message == expected

    def test_render_ai_thought(self, mocker):
        ai = AI(2, False)
        expected = "Drawing from deck\nPlayer is thinking...\n"
        output_message = View.template_ai_thought(ai, 'Drawing from deck')
        assert output_message == expected
        ai.ai_only = True
        output_message = View.template_ai_thought(ai, 'Drawing from deck')
        assert output_message == expected

    def test_render_ai_turn_start(self, mocker):
        ai = AI(2, False)
        ai.round = mocker.MagicMock()
        ai.round.turn = 2
        ai.round.current_player = 1
        ai.round.deck.show_discard.return_value = str(Card("8", "S"))
        expected = "\x1b[0;34m#############################\x1b[0m\n" \
                   "Turn 2\n" \
                   "\x1b[0;37m-----------------------------\x1b[0m\n" \
                   "Player 2's turn\n" \
                   "\x1b[0;37m.............................\x1b[0m\n" \
                   "Discard Pile: 8♠\n"
        output_message = View.template_ai_turn_start(ai)
        assert output_message == expected

    def test_render_ai_turn_end(self):
        ai = AI(2, False)
        ai.hand.hand = [Card(x, y) for x, y in [("A", "H"), ("A", "S"), ("A", "C"), ("A", "D")]]
        expected = "\x1b[0;37m.............................\x1b[0m\n" \
                   "A♠, A\x1b[0;31m♥\x1b[0m, A\x1b[0;31m♦\x1b[0m, A♣\n" \
                   "\x1b[0;37m.............................\x1b[0m\n"
        output_message = View.template_ai_turn_end(ai)
        assert output_message == expected

    def test_template_end_of_round_scores(self, mocker):
        player = Human(1)
        player.hand.hand = [Card(x, y) for x, y in [("A", "S"), ("2", "S"), ("3", "S"), ("4", "S"),
                                                    ("A", "C"), ("2", "C"), ("3", "C")]]
        expected = "Player 1\n" \
                   "Hand Score: 0\n" \
                   "A♠, 2♠, 3♠, 4♠, A♣, 2♣, 3♣\n" \
                   "\x1b[0;37m.............................\x1b[0m\n"
        output_message = View.template_end_of_round_scores(player)
        assert output_message == expected

    def test_template_this_round_score(self):
        player = Human(1)
        player.hand.hand = [Card(x, y) for x, y in [("A", "S"), ("2", "S"), ("3", "S"), ("4", "S"),
                                                    ("A", "C"), ("2", "C"), ("3", "C")]]
        score = Score([player])
        expected = "\x1b[0;34m#############################\x1b[0m\n" \
                   "\n" \
                   "Round Scores\n" \
                   "\x1b[0;37m-----------------------------\x1b[0m\n" \
                   "Player 1\n" \
                   "Hand Score: 0\n" \
                   "A♠, 2♠, 3♠, 4♠, A♣, 2♣, 3♣\n" \
                   "\x1b[0;37m.............................\x1b[0m\n" \
                   "\n" \
                   "Game Scores\n" \
                   "\x1b[0;37m-----------------------------\x1b[0m\n" \
                   "Player 1: 0\n" \
                   "\n"
        output_message = View.template_this_round_score(score.get_end_of_round_scores(),
                                                        score.get_current_game_scores())
        assert output_message == expected
