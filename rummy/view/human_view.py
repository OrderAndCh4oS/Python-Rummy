from text_template import TextTemplate

from rummy.constants.resource_path import TEMPLATE_PATH
from rummy.view.player_view import PlayerView


class HumanView(PlayerView):

    @staticmethod
    def turn_start(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/player-turn-start.txt',
            turn_number=player.round.turn,
            player_number=player.round.current_player + 1,
            score=player.hand.get_score(),
            hand=str(player.hand),
            discard=player.round.deck.show_discard()
        )

    @staticmethod
    def turn_end(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/player-turn-end.txt',
            hand=str(player.hand),
            key=player.hand.get_key()
        )

    @staticmethod
    def discarded(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/player-discarded.txt',
            discard=player.round.deck.inspect_discard()
        )
