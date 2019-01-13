# coding=utf-8

from time import sleep

from text_template import TextTemplate

from rummy.constants.resource_path import TEMPLATE_PATH


class View:

    @staticmethod
    def render(*args, **kwargs):
        # Just a wrapper/abstraction layer for builtins.print
        # Outputs will go through this class, so that if any
        # complete transformations need to be applied,
        # they can be applied in once place.
        print(*args, **kwargs)

    @staticmethod
    def prepare_template(template, **kwargs):
        complete_template = TEMPLATE_PATH + template
        return TextTemplate.render(complete_template, **kwargs)

    @staticmethod
    def template_turn_start(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/player-turn-start.txt',
            turn_number=player.round.turn,
            player_number=player.round.current_player + 1,
            score=player.hand.get_score(),
            hand=str(player.hand),
            discard=player.round.deck.show_discard()
        )

    @staticmethod
    def template_player_turn_end(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/player-turn-end.txt',
            hand=str(player.hand),
            key=player.hand.get_key()
        )

    @staticmethod
    def template_ai_thought(ai, action):
        output = TextTemplate.render(
            TEMPLATE_PATH + '/ai-thinking.txt', action=action)
        if not ai.ai_only:
            sleep(0.8)
        return output

    @staticmethod
    def template_ai_turn_start(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/turn-start.txt',
            turn_number=player.round.turn,
            player_number=player.round.current_player + 1,
            discard=player.round.deck.show_discard()
        )

    @staticmethod
    def template_ai_turn_end(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/ai-turn-end.txt',
            hand=str(player.hand)
        )

    @staticmethod
    def template_player_discarded(discard):
        return TextTemplate.render(
            TEMPLATE_PATH + '/player-discarded.txt',
            discard=discard
        )

    @staticmethod
    def template_ai_discard_data(current_score, scores):
        return TextTemplate.render(
            TEMPLATE_PATH + '/ai-discard-data.txt',
            current_score=str(current_score),
            scores=str(scores),
            min_score=str(min(scores))
        )

    @staticmethod
    def template_ai_hand_data(score):
        return TextTemplate.render(
            TEMPLATE_PATH + '/ai-hand-data.txt',
            score=str(score)
        )

    @staticmethod
    def template_end_of_round_scores(player):
        return TextTemplate.render(
            TEMPLATE_PATH + '/hand-score.txt',
            player=player.get_name(),
            hand=str(player.hand),
            score=player.hand.get_score()
        )

    @staticmethod
    def template_this_round_score(round_scores, game_scores):
        return TextTemplate.render(
            TEMPLATE_PATH + '/round-end.txt',
            round_scores=round_scores,
            game_scores=game_scores
        )
