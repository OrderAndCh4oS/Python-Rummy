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
    def render_template(template, **kwargs):
        complete_template = TEMPLATE_PATH + template
        output_message = TextTemplate.render(complete_template, **kwargs)
        View.render(output_message)
        return output_message

    @staticmethod
    def render_turn_start(player):
        output_message = TextTemplate.render(TEMPLATE_PATH + '/player-turn-start.txt',
                                             turn_number=player.round.turn,
                                             player_number=player.round.current_player + 1,
                                             score=player.hand.get_score(),
                                             hand=str(player.hand),
                                             discard=player.round.deck.show_discard()
                                             )
        View.render(output_message)
        return output_message

    @staticmethod
    def render_player_turn_end(player):
        output_message = TextTemplate.render(TEMPLATE_PATH + '/player-turn-end.txt',
                                             hand=str(player.hand),
                                             key=player.hand.get_key()
                                             )
        View.render(output_message)
        return output_message

    @staticmethod
    def render_ai_thought(ai, action):
        ai_output_message = TextTemplate.render(TEMPLATE_PATH + '/ai-thinking.txt', action=action)
        View.render(ai_output_message)
        if not ai.ai_only:
            sleep(0.8)
        return ai_output_message

    @staticmethod
    def render_ai_turn_start(ai):
        ai_output_message = TextTemplate.render(TEMPLATE_PATH + '/turn-start.txt',
                                                turn_number=ai.round.turn,
                                                player_number=ai.round.current_player + 1,
                                                discard=ai.round.deck.show_discard()
                                                )
        View.render(ai_output_message)
        return ai_output_message

    @staticmethod
    def render_ai_turn_end(ai):
        ai_output_message = TextTemplate.render(TEMPLATE_PATH + '/ai-turn-end.txt',
                                                hand=str(ai.hand))
        View.render(ai_output_message)
        return ai_output_message
