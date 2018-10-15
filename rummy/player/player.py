# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from text_template import TextTemplate as View

from rummy.constants.resource_path import TEMPLATE_PATH
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
            print(View.render(template=TEMPLATE_PATH + '/knocked.txt'))

    # Todo: move to new view class
    def render_turn_start(self):
        print(View.render(
            template=TEMPLATE_PATH + '/player-turn-start.txt',
            turn_number=self.round.turn,
            player_number=self.round.current_player + 1,
            score=self.hand.get_score(),
            hand=str(self.hand),
            discard=self.round.deck.show_discard()
        ))

    def render_player_turn_end(self):
        print(View.render(
            template=TEMPLATE_PATH + '/player-turn-end.txt',
            hand=str(self.hand),
            key=self.hand.get_key()
        ))

    @abstractmethod
    def choose_to_discard_or_pick_up(self):
        pass

    @abstractmethod
    def discard_or_knock(self):
        pass
