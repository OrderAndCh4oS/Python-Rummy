from rummy.ui.action import Action
from rummy.ui.action_collection import ActionCollection
from rummy.ui.user_input import UserInput


class PlayerActionDialog:

    @staticmethod
    def pick_up_or_draw():
        return ActionCollection(
            Action('p', 'Pick up discard'),
            Action('d', 'Draw from deck')
        )

    @staticmethod
    def choose_discard():
        return ActionCollection(
            Action(range(1, 9), 'Enter a number to discard a card from your hand')
        )

    @staticmethod
    def choose_discard_or_knock():
        return ActionCollection(
            Action('k', 'You may knock to end the round'),
            Action(range(1, 9), 'Enter a number to discard a card from your hand'),
        )


if __name__ == '__main__':
    UserInput.create_input(PlayerActionDialog.choose_discard())
    UserInput.create_input(PlayerActionDialog.choose_discard_or_knock())
