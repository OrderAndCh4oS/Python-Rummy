# -*- coding: utf-8 -*-
from random import choice
from time import sleep

from text_template import TextTemplate as View

from rummy.constants.resource_path import TEMPLATE_PATH
from rummy.player.player import Player


class AI(Player):

    # Todo remove all prints return only data create a new class to handle displaying data
    def choose_to_discard_or_pick_up(self):
        if self.round.deck.has_discard():
            if self.ai_only:
                self.render_turn_start()
                self.ai_thinking('Choosing pick up')
            else:
                self.render_ai_turn_start()
            self.choose_pick_up()
        else:
            if self.ai_only:
                self.render_turn_start()
            else:
                self.render_ai_turn_start()
            self.ai_thinking('Drawing first card from deck')
            self.hand.draw_card(self.round.deck.take_card())

    def choose_pick_up(self):
        current_score = self.hand.get_score()
        if self.ai_only:
            print('Current Score: ', current_score)
        scores = self.melds.find_discard_scores(self.hand.get_hand(), self.round.deck.inspect_discard())
        if self.ai_only:
            print('Possible Hand Scores: ', scores)
            print('Min Score: ', min(scores))
        if min(scores) < current_score - 4 or min(scores) <= 10:
            self.ai_thinking('Drawing from discard')
            self.hand.draw_card(self.round.deck.take_discard())
        else:
            self.ai_thinking('Drawing from deck')
            self.hand.draw_card(self.round.deck.take_card())

    def discard_or_knock(self):
        if self.ai_only:
            self.render_ai_turn_end()
        self.ai_thinking('Choosing card to discard')
        scores = self.melds.find_discard_scores(self.hand.get_hand())
        score = min(scores)
        if score <= 10 and not self.round.knocked:
            self.round.knocked = True
        if scores.count(score) > 1:
            choices = [(i, x) for (i, x) in enumerate(scores) if (x == score)]
            discard = choice(choices)[0]
        else:
            discard = scores.index(score)
        discard = self.hand.discard_card(discard)
        if self.ai_only:
            print('Discarding: ', discard)
            print('Hand Score: ', score)
        self.round.deck.discard_card(discard)

    # Todo: move to new view class
    def ai_thinking(self, action):
        print(View.render(
            template=TEMPLATE_PATH + '/ai-thinking.txt',
            action=action,
        ))
        if not self.ai_only:
            sleep(0.8)

    def render_ai_turn_start(self):
        print(View.render(
            template=TEMPLATE_PATH + '/turn-start.txt',
            turn_number=self.round.turn,
            player_number=self.round.current_player + 1,
            discard=self.round.deck.show_discard()
        ))

    def render_ai_turn_end(self):
        print(View.render(
            template=TEMPLATE_PATH + '/ai-turn-end.txt',
            hand=str(self.hand),
        ))
