# -*- coding: utf-8 -*-
from random import choice

from ui.view import View
from rummy.player.player import Player


class AI(Player):

    def choose_to_discard_or_pick_up(self):
        if self.round.deck.has_discard():
            if self.ai_only:
                View.render(View.template_turn_start(self))
                View.render(View.template_ai_thought(self, 'Choosing pick up'))
            else:
                View.render(View.template_ai_turn_start(self))
            self.choose_pick_up()
        else:
            if self.ai_only:
                View.render(View.template_turn_start(self))
            else:
                View.render(View.template_ai_turn_start(self))
            View.render(View.template_ai_thought(self, 'Drawing first card from deck'))
            self.hand.draw_card(self.round.deck.take_card())

    def choose_pick_up(self):
        current_score = self.hand.get_score()
        if self.ai_only:
            View.render('Current Score: ', current_score)
        scores = self.melds.find_discard_scores(self.hand.get_hand(), self.round.deck.inspect_discard())
        if self.ai_only:
            View.render('Possible Hand Scores: ', scores)
            View.render('Min Score: ', min(scores))
        if min(scores) < current_score - 4 or min(scores) <= 10:
            View.render(View.template_ai_thought(self, 'Drawing from discard'))
            self.hand.draw_card(self.round.deck.take_discard())
        else:
            View.render(View.template_ai_thought(self, 'Drawing from deck'))
            self.hand.draw_card(self.round.deck.take_card())

    def discard_or_knock(self):
        if self.ai_only:
            View.render(View.template_ai_turn_end(self))
        View.render(View.template_ai_thought(self, 'Choosing card to discard'))
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
            View.render('Discarding: ', discard)
            View.render('Hand Score: ', score)
        self.round.deck.discard_card(discard)
