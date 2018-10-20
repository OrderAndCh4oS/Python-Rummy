# -*- coding: utf-8 -*-
from random import choice

from rummy.player.player import Player
from ui.view import View


class AI(Player):

    def show_turn_start(self):
        output = ''
        if self.ai_only:
            output += View.template_turn_start(self)
        else:
            output += View.template_ai_turn_start(self)
        output += View.template_ai_thought(self, 'Choosing pick up')
        return output

    def show_turn_end(self):
        output = ''
        if self.ai_only:
            output += View.template_ai_turn_end(self)
        output += View.template_ai_thought(self, 'Choosing card to discard')
        return output

    def draw_from_deck_or_discard_pile(self):
        output = ''
        if self.round.deck.has_discard():
            current_score = self.hand.get_score()
            scores = self.melds.find_discard_scores(self.hand.get_hand(), self.round.deck.inspect_discard())
            if self.ai_only:
                output += View.template_ai_discard_data(current_score, scores)
            output += self._choose_pickup(current_score, scores)
        else:
            self.take_from_deck()
            output += View.template_ai_thought(self, 'Drawing from deck')
        return output

    def _choose_pickup(self, current_score, scores):
        output = ''
        if min(scores) < current_score - 4 or min(scores) <= 10:
            self.take_from_discard()
            output += View.template_ai_thought(self, 'Drawing from discard')
        else:
            self.take_from_deck()
            output += View.template_ai_thought(self, 'Drawing from deck')
        return output

    def discard_or_knock(self):
        scores = self.melds.find_discard_scores(self.hand.get_hand())
        score = min(scores)
        if score <= 10 and not self.round.knocked:
            self.round.knocked = True
        discard = self._choose_discard(score, scores)
        self.round.deck.discard_card(discard)

    def _choose_discard(self, score, scores):
        if scores.count(score) > 1:
            choices = [(i, x) for (i, x) in enumerate(scores) if (x == score)]
            discard = choice(choices)[0]
        else:
            discard = scores.index(score)
        return self.hand.discard_card(discard)

    def show_discard(self):
        output = ''
        if self.ai_only:
            output += View.template_ai_hand_data(self.round.deck.inspect_discard(), self.hand.get_score())
        output += 'Discarded: %s' % self.round.deck.inspect_discard()
        return output
