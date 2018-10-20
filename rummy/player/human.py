# -*- coding: utf-8 -*-

from player.player_action_dialogs import PlayerActionDialogs
from player.player_actions import PlayerActions
from rummy.player.player import Player
from ui.user_input import UserInput
from ui.view import View


class Human(Player):

    # Todo separate prints and inputs from methods and move to a new class, methods should return data
    def choose_to_discard_or_pick_up(self):
        if self.round.deck.has_discard():
            self.choose_pick_up()
        else:
            PlayerActions.take_from_deck(self.hand, self.round.deck)

    def show_turn_start(self):
        return View.template_turn_start(self)

    def show_turn_end(self):
        return View.template_player_turn_end(self)

    def choose_pick_up(self):
        user_input = UserInput.create_input(PlayerActionDialogs.pick_up_or_draw())
        self.take_card(user_input)

    def take_card(self, user_input):
        if user_input == 'p':
            PlayerActions.take_from_discard(self.hand, self.round.deck)
        else:
            PlayerActions.take_from_deck(self.hand, self.round.deck)

    def discard_or_knock(self):
        scores = self.melds.find_discard_scores(self.hand.get_hand())
        user_input = ''
        while user_input not in [str(i) for i in range(1, 9)]:
            if min(scores) <= 10 and not self.round.knocked:
                user_input = UserInput.create_input(PlayerActionDialogs.choose_discard_or_knock())
                if user_input == "k":
                    PlayerActions.knock(self.round)
                    continue
            else:
                user_input = UserInput.create_input(PlayerActionDialogs.choose_discard())
        PlayerActions.discard(user_input, self.hand, self.round.deck)

        return self.show_discard()

    def show_discard(self):
        return 'Discarded: %s' % self.round.deck.inspect_discard()
