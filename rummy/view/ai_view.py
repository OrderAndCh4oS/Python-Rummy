from time import sleep

from text_template import TextTemplate

from rummy.constants.resource_path import TEMPLATE_PATH
from rummy.view.player_view import PlayerView


class AiView(PlayerView):

    @staticmethod
    def thinking(ai, action):
        output = TextTemplate.render(
            TEMPLATE_PATH + '/ai-thinking.txt', action=action)
        if not ai.ai_only:
            sleep(0.8)
        return output

    @staticmethod
    def turn_start(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/turn-start.txt',
            turn_number=player.round.turn,
            player_number=player.round.current_player + 1,
            discard=player.round.deck.show_discard()
        )

    @staticmethod
    def turn_end(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/ai-turn-end.txt',
            hand=str(player.hand)
        )

    @staticmethod
    def discarded(discard):
        return TextTemplate.render(
            TEMPLATE_PATH + '/player-discarded.txt',
            discard=discard
        )

    @staticmethod
    def discard_data(current_score, scores):
        return TextTemplate.render(
            TEMPLATE_PATH + '/ai-discard-data.txt',
            current_score=str(current_score),
            scores=str(scores),
            min_score=str(min(scores))
        )

    @staticmethod
    def hand_data(score):
        return TextTemplate.render(
            TEMPLATE_PATH + '/ai-hand-data.txt',
            score=str(score)
        )
