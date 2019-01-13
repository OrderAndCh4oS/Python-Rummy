# -*- coding: utf-8 -*-

from abc import ABCMeta

from rummy.game.melds import Melds
from rummy.player.hand import Hand


class Player(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, num):
        self.num = num
        self.game_score = 0
        self.hand = Hand()
        self.melds = Melds()
        self.round = None
        self.ai_only = False

    def __str__(self):
        return "Player %i" % self.num

    def turn(self, game_round):
        self.round = game_round

    def take_from_deck(self):
        self.hand.draw_card(self.round.deck.take_card())

    def take_from_discard(self):
        self.hand.draw_card(self.round.deck.take_discard())

    def discard(self, user_input):
        user_input = int(user_input) - 1
        self.round.deck.discard_card(self.hand.discard_card(user_input))

    def knock(self):
        self.round.show_knocked = True

    def get_name(self):
        return str(self)

    def update_score(self):
        self.game_score += self.hand.get_score()

    def get_hand(self):
        return self.hand

    def get_game_score(self):
        return self.game_score

    def display_round_score(self):
        return self.hand.score

    def has_someone_knocked(self):
        return self.round.knocked
