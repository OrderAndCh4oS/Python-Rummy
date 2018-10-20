# -*- coding: utf-8 -*-

from player.player_action_dialogs import PlayerActionDialogs
from rummy.player.player import Player
from ui.user_input import UserInput
from ui.view import View


class Human(Player):

    def show_turn_start(self):
        return View.template_turn_start(self)

    def show_turn_end(self):
        return View.template_player_turn_end(self)

    def draw_from_deck_or_discard_pile(self):
        if self.round.deck.has_discard():
            return self._choose_pick_up()
        else:
            return self.take_from_deck()

    def _choose_pick_up(self):
        user_input = UserInput.create_input(PlayerActionDialogs.pick_up_or_draw())
        if user_input == 'p':
            self.take_from_discard()
            return 'Drawing from discard'
        else:
            self.take_from_deck()
            return 'Drawing from deck'

    def discard_or_knock(self):
        self.discard(self._choose_discard())

    def _choose_discard(self):
        user_input = ''
        scores = self.melds.find_discard_scores(self.hand.get_hand())
        while user_input not in [str(i) for i in range(1, 9)]:
            if min(scores) <= 10 and not self.round.knocked:
                user_input = UserInput.create_input(PlayerActionDialogs.choose_discard_or_knock())
                if user_input == "k":
                    self.knock()
                    continue
            else:
                user_input = UserInput.create_input(PlayerActionDialogs.choose_discard())
        return user_input

    def show_discard(self):
        return 'Discarded: %s' % self.round.deck.inspect_discard()
