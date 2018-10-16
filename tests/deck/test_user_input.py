# coding=utf-8

from rummy.game.user_input import UserInput


class TestUserInput:

    def test_get_input(self, mocker):
        mocker.patch('builtins.input')
        UserInput.get_input("Here's a prompt.", keyword="argument")
        input.assert_called_with("Here's a prompt.", keyword="argument")

    def test_get_pick_up_input(self, mocker):
        mocker.patch('builtins.input', side_effect=['a', '1', 'd'])
        UserInput.get_pick_up_input()
        input.assert_called_with("Enter \x1b[0;32md\x1b[0m to draw or \x1b[0;32mp\x1b[0m to pickup discard: ")
        assert input.call_count == 3
