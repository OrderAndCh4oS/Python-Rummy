# -*- coding: utf-8 -*-
from rummy.deck.rank import Rank


class Sort:

    @staticmethod
    def sort_hand_by_suit_and_rank(hand):
        return sorted(hand, key=lambda card: Rank().get_suit_and_rank_key(card))

    @staticmethod
    def sort_hand_by_rank(hand):
        return sorted(hand, key=lambda card: Rank().get_rank_key(card))
