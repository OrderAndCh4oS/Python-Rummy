# coding=utf-8

from ui.user_input import UserInput


class TestUserInput:

    def test_get_input(self, mocker):
        mocker.patch('builtins.input')
        message = "Test message!"
        UserInput.get_input(message, keyword="argument")
        input.assert_called_with(message, keyword="argument")

    def test_get_pick_up_input(self, mocker):
        mocker.patch('builtins.input', side_effect=['w', '1', 'd', 'p'])
        mocker.spy(UserInput, 'get_pick_up_input')
        assert UserInput.get_pick_up_input() == 'd'
        input.assert_called_with("Enter \x1b[0;32md\x1b[0m to draw or \x1b[0;32mp\x1b[0m to pickup discard: ")
        assert input.call_count == 3
        assert UserInput.get_pick_up_input.call_count == 1
        assert UserInput.get_pick_up_input() == 'p'
        assert input.call_count == 4
        assert UserInput.get_pick_up_input.call_count == 2
