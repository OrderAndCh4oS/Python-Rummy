# -*- coding: utf-8 -*-

from ansi_colours import AnsiColours as Colour

from rummy.player.player import Player
from ui.view import View
from ui.user_input import UserInput


class Human(Player):

    # Todo separate prints and inputs from methods and move to a new class, methods should return data
    def choose_to_discard_or_pick_up(self):
        View.render(View.template_turn_start(self))
        if self.round.deck.has_discard():
            self.choose_pick_up()
        else:
            self.hand.draw_card(self.round.deck.take_card())

    def choose_pick_up(self):
        player_choice = UserInput.get_pick_up_input()
        if player_choice == 'p':
            self.hand.draw_card(self.round.deck.take_discard())
        else:
            self.hand.draw_card(self.round.deck.take_card())

    def discard_or_knock(self):
        View.render(View.template_player_turn_end(self))
        scores = self.melds.find_discard_scores(self.hand.get_hand())
        if min(scores) <= 10 and not self.round.knocked:
            message = "Enter a number to discard a card or " + Colour.green('k') + " to Knock: "
        else:
            message = "Enter a number to discard a card: "
        player_choice = ""
        while player_choice not in [str(i) for i in range(1, 9)]:
            if self.round.knocked:
                message = "Enter a number to discard a card: "
            player_choice = UserInput.get_input(message)
            if player_choice.lower() == "k" and min(scores) <= 10:
                self.round.knocked = True
        player_choice = int(player_choice) - 1
        self.round.deck.discard_card(self.hand.discard_card(player_choice))
