# coding=utf-8

from ansi_colours import AnsiColours as Colour

from rummy.ui.action_collection import ActionCollection
from rummy.ui.view import View


class UserInput:
    @staticmethod
    def create_input(action_collection: ActionCollection):
        user_input = None
        keys = []
        output = ''
        while True:
            for action in action_collection.actions:
                if isinstance(action.key, range):
                    output += "%s: %s\n" % (
                    str(action), '%s-%s' % (Colour.green(str(action.key[0])), Colour.green(str(action.key[-1]))))
                    keys.extend([str(key) for key in action.key])
                else:
                    output += "%s: %s\n" % (str(action), Colour.green(action.key))
                    keys.append(str(action.key))
            View.render(output)
            while user_input not in keys:
                user_input = UserInput.get_input('Select an option: ')
            break
        return user_input

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
