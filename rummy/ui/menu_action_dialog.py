from rummy.ui.action import Action
from rummy.ui.action_collection import ActionCollection
from rummy.ui.user_input import UserInput


class MenuActionDialog:

    @staticmethod
    def human_players():
        return ActionCollection(
            Action(range(0, 5), 'Choose number of human players'),
        )

    @staticmethod
    def ai_players(human_players=0):
        return ActionCollection(
            Action(range(
                1 if human_players is not 0 else 2,
                5 - int(human_players)
            ), 'Choose number of AI players'),
        )

    @staticmethod
    def next_round():
        return ActionCollection(
            Action('y', 'Ready for the next round'),
        )


if __name__ == '__main__':
    UserInput.create_input(MenuActionDialog.ai_players(UserInput.create_input(MenuActionDialog.human_players())))
