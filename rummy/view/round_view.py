from text_template import TextTemplate

from rummy.constants.resource_path import TEMPLATE_PATH


class RoundView:
    @staticmethod
    def end_of_round_scores(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/hand-score.txt',
            player=player.get_name(),
            hand=str(player.hand),
            score=player.hand.get_score()
        )

    @staticmethod
    def this_round_score(round_scores, game_scores):
        return TextTemplate.render(
            TEMPLATE_PATH + '/round-end.txt',
            round_scores=round_scores,
            game_scores=game_scores
        )
