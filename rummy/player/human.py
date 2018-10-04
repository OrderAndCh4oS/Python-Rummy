# -*- coding: utf-8 -*-

from ansi_colours import AnsiColours as Colour

from rummy.player.player import Player


class Human(Player):

    # Todo separate prints and inputs from methods and move to a new class, methods should return data
    def choose_to_discard_or_pick_up(self):
        self.render_turn_start()
        if self.round.deck.has_discard():
            self.choose_pick_up()
        else:
            self.hand.draw_card(self.round.deck.take_card())

    def choose_pick_up(self):
        player_choice = self.get_user_pick_up_input()
        if player_choice == 'p':
            self.hand.draw_card(self.round.deck.take_discard())
        else:
            self.hand.draw_card(self.round.deck.take_card())

    def discard_or_knock(self):
        self.render_player_turn_end()
        scores = self.melds.find_discard_scores(self.hand.get_hand())
        if min(scores) <= 10 and not self.round.knocked:
            message = "Enter a number to discard a card or " + Colour.green('k') + " to Knock: "
        else:
            message = "Enter a number to discard a card: "
        player_choice = ""
        while player_choice not in [str(i) for i in range(1, 9)]:
            if self.round.knocked:
                message = "Enter a number to discard a card: "
            player_choice = input(message)
            if player_choice.lower() == "k" and min(scores) <= 10:
                self.round.knocked = True
        player_choice = int(player_choice) - 1
        self.round.deck.discard_card(self.hand.discard_card(player_choice))

    # Todo: move to new UI class
    def get_user_pick_up_input(self):
        player_choice = ''
        while player_choice.lower() not in ['d', 'p']:
            player_choice = input(
                "Enter " + Colour.green('d') + " to draw or " + Colour.green('p') + " to pickup discard: ")
        return player_choice
