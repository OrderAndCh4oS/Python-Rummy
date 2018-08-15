# -*- coding: utf-8 -*-

from rummy.deck.deck import Deck
from rummy.player.dealer import Dealer


class Round(Dealer):
    first_player = 0
    current_player = 0
    turn = 1
    last_turn = 1
    knocked = False

    def __init__(self, players):
        super().__init__()
        self.players = players
        self.deck = Deck()

    def prepare_new_round(self):
        self.turn = 1
        self.last_turn = 1
        self.knocked = False
        self.deck = Deck()

    def deal_cards(self, players):
        for p in players:
            p.hand = self.deal(self.deck.get_deck())

    def prepare_turn(self):
        self.deck.check_stack()
        self.check_knocked()

    def get_turn(self, round):
        # Todo: find out why round is being passed back to itself
        return "Turn %i, %s\n" % (round.turn, round.get_current_players_name())

    def get_current_players_hand(self):
        return self.players[self.current_player].get_hand_to_print()

    def end_turn(self):
        self.switch_current_player()
        self.turn += 1

    def check_knocked(self):
        if self.knocked:
            self.last_turn += 1

    def switch_current_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def rotate_first_player(self):
        self.first_player += 1
        self.current_player = self.first_player % len(self.players)
