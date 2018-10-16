# coding=utf-8

from rummy.game.view import View
from rummy.deck.card import Card
from rummy.player.hand import Hand


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
        pass

    def test_render_player_turn_end(self, mocker):
        mocker.patch('builtins.print')
        pass

    def test_render_ai_thought(self, mocker):
        mocker.patch('builtins.print')
        pass

    def test_render_ai_turn_start(self, mocker):
        mocker.patch('builtins.print')
        pass

    def test_render_ai_turn_end(self, mocker):
        mocker.patch('builtins.print')
        pass
