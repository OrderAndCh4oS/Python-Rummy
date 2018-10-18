# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from rummy.game.melds import Melds
from rummy.player.hand import Hand
from rummy.game.view import View


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

    def turn(self, game_round, ai_only):
        self.round = game_round
        self.ai_only = ai_only
        self.has_someone_knocked()
        self.choose_to_discard_or_pick_up()
        self.discard_or_knock()

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
        if self.round.knocked:
            View.render(View.prepare_template('/knocked.txt'))

    @abstractmethod
    def choose_to_discard_or_pick_up(self):
        pass

    @abstractmethod
    def discard_or_knock(self):
        pass
