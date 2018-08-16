# -*- coding: utf-8 -*-

from ansi_colours import AnsiColours as Colour

from rummy.deck.rank import Rank
from rummy.deck.sort import Sort
from rummy.game.melds import Melds


class Hand(Rank):

    def __init__(self):
        super().__init__()
        self.colour = Colour()
        self.hand = []
        self.score = 0
        self.sort = Sort()
        self.melds = Melds()

    def __str__(self):
        self.hand = self.sort.sort_hand_by_suit_and_rank(self.hand)
        return ', '.join([card.get_card_colour() for card in self.hand])

    def set_hand(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def draw_card(self, card):
        self.hand.append(card)

    def discard_card(self, choice):
        return self.hand.pop(choice)

    def get_score(self):
        return self.melds.calculate_score(self.hand)

    def get_key(self):
        return ',  '.join(["%s" % Colour.green(str((i + 1))) for i in range(len(self.hand))])
