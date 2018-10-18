# coding=utf-8

from rummy.game.view import View
from rummy.player.human import Human
from rummy.player.ai import AI
from rummy.deck.card import Card


class TestView:

    def test_render(self, mocker):
        mocker.patch('builtins.print')
        View.render("Test print", end="\t\n")
        print.assert_called_with("Test print", end="\t\n")

    def test_render_template(self, mocker):
        mocker.patch('builtins.print')
        expected = '\x1b[0;31mA Player has knocked, this is your last turn!!!\x1b[0m\n'
        output_message = View.render_template('/knocked.txt')
        assert output_message == expected

    def test_render_turn_start(self, mocker):
        mocker.patch('builtins.print')
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
        output_message = View.render_turn_start(player)
        assert output_message == expected

    def test_render_player_turn_end(self, mocker):
        mocker.patch('builtins.print')
        player = Human(1)
        player.hand.hand = [Card(x, y) for x, y in [("8", "S"), ("9", "S"), ("J", "S"), ("K", "S"),
                                                    ("4", "H"), ("8", "D"), ("J", "C"), ("K", "C")]]
        expected = "\x1b[0;37m.............................\x1b[0m\n" \
                   "8♠, 9♠, J♠, K♠, 4\x1b[0;31m♥\x1b[0m, 8\x1b[0;31m♦\x1b[0m, J♣, K♣\n" \
                   "\x1b[0;32m1\x1b[0m,  \x1b[0;32m2\x1b[0m,  \x1b[0;32m3\x1b[0m,  \x1b[0;32m4\x1b[0m,  " \
                   "\x1b[0;32m5\x1b[0m,  \x1b[0;32m6\x1b[0m,  \x1b[0;32m7\x1b[0m,  \x1b[0;32m8\x1b[0m\n" \
                   "\x1b[0;37m.............................\x1b[0m\n"
        output_message = View.render_player_turn_end(player)
        assert output_message == expected

    def test_render_ai_thought(self, mocker):
        mocker.patch('builtins.print')
        sleep = mocker.patch('rummy.game.view.sleep')
        ai = AI(2)
        expected = "Drawing from deck\nPlayer is thinking...\n"
        output_message = View.render_ai_thought(ai, 'Drawing from deck')
        assert output_message == expected
        assert sleep.call_count == 1
        ai.ai_only = True
        output_message = View.render_ai_thought(ai, 'Drawing from deck')
        assert sleep.call_count == 1
        assert output_message == expected

    def test_render_ai_turn_start(self, mocker):
        mocker.patch('builtins.print')
        ai = AI(2)
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
        output_message = View.render_ai_turn_start(ai)
        assert output_message == expected

    def test_render_ai_turn_end(self, mocker):
        mocker.patch('builtins.print')
        ai = AI(2)
        ai.hand.hand = [Card(x, y) for x, y in [("A", "H"), ("A", "S"), ("A", "C"), ("A", "D")]]
        expected = "\x1b[0;37m.............................\x1b[0m\n" \
                   "A♠, A\x1b[0;31m♥\x1b[0m, A\x1b[0;31m♦\x1b[0m, A♣\n" \
                   "\x1b[0;37m.............................\x1b[0m\n"
        output_message = View.render_ai_turn_end(ai)
        assert output_message == expected
