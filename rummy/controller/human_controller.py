from rummy.controller.player_controller import PlayerController
from rummy.player.player import Player
from rummy.ui.player_action_dialog import PlayerActionDialog
from rummy.ui.user_input import UserInput
from rummy.ui.view import View
from rummy.view.human_view import HumanView


class HumanController(PlayerController):

    @staticmethod
    def show_start_turn(player: Player):
        View.render(HumanView.turn_start(player))

    @staticmethod
    def show_end_turn(player: Player):
        View.render(HumanView.turn_end(player))

    @staticmethod
    def show_knocked(player):
        if player.has_someone_knocked():
            View.render(HumanView.knocked())

    @staticmethod
    def show_discard(player: Player):
        View.render(HumanView.discarded(player))

    @classmethod
    def draw_card(cls, player):
        if player.round.deck.has_discard():
            View.render(cls._choose_pick_up(player))
        else:
            player.take_from_deck()
            View.render('Drew from deck')

    @staticmethod
    def _choose_pick_up(player):
        user_input = UserInput.create_input(PlayerActionDialog.pick_up_or_draw())
        if user_input == 'p':
            player.take_from_discard()
            return 'Drawing from discard'
        else:
            player.take_from_deck()
            return 'Drawing from deck'

    @classmethod
    def discard_or_knock(cls, player):
        player.discard(cls._choose_discard(player))

    @staticmethod
    def _choose_discard(player):
        user_input = ''
        scores = player.melds.find_discard_scores(player.hand.get_hand())
        while user_input not in [str(i) for i in range(1, 9)]:
            if min(scores) <= 10 and not player.round.show_knocked:
                user_input = UserInput.create_input(PlayerActionDialog.choose_discard_or_knock())
                if user_input == "k":
                    player.knock()
                    continue
            else:
                user_input = UserInput.create_input(PlayerActionDialog.choose_discard())
        return user_input
