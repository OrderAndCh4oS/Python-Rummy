# -*- coding: utf-8 -*-

from rummy.deck.card import Card
from rummy.deck.face_values import FaceValues
from rummy.deck.suits import Suits


class Rank:

    def __init__(self):
        self.ranked_cards = [Card(value, suit) for suit in Suits.get() for value in FaceValues.get()]

    def __repr__(self):
        return str([(i, str(card)) for i, card in enumerate(self.ranked_cards)])

    @staticmethod
    def get_suit_and_rank_key(card):
        return Suits.get().index(card.suit), FaceValues.get().index(card.value)

    @staticmethod
    def get_rank_key(card):
        return FaceValues.get().index(card.value)


if __name__ == '__main__':
    print(Rank().ranked_cards)
