from ui.action import Action
from ui.action_collection import ActionCollection
from ui.user_input import UserInput


class MenuActionDialogs:

    @staticmethod
    def human_players():
        return ActionCollection(
            Action(range(0, 5), 'Choose number of human players'),
        )

    @staticmethod
    def ai_players(human_players=0):
        return ActionCollection(
            Action(range(
                1 if human_players is not '0' else 2,
                5 - int(human_players)
            ), 'Choose number of AI players'),
        )


if __name__ == '__main__':
    UserInput.create_input(MenuActionDialogs.ai_players(UserInput.create_input(MenuActionDialogs.human_players())))
