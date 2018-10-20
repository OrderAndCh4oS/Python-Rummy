# coding=utf-8

from ansi_colours import AnsiColours as Colour


class UserInput:

    @staticmethod
    def get_input(*args, **kwargs):
        # Wrapper/abstraction layer for builtins.input
        player_input = input(*args, **kwargs)
        return player_input

    @staticmethod
    def get_pick_up_input():
        player_choice = ''
        while player_choice.lower() not in ['d', 'p']:
            player_choice = UserInput.get_input(
                "Enter " + Colour.green('d') + " to draw or " + Colour.green('p') + " to pickup discard: ")
        return player_choice
