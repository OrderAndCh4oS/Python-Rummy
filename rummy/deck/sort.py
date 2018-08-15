# -*- coding: utf-8 -*-

from rummy.deck.rank import Rank


class Sort:

    def __init__(self):
        self.rank = Rank()

    def sort_hand_by_suit_and_rank(self, hand):
        return sorted(hand, key=lambda card: self.rank.get_suit_and_rank_key(card))

    def sort_hand_by_rank(self, hand):
        return sorted(hand, key=lambda card: self.rank.get_rank_key(card))
