# -*- coding: utf-8 -*-
from .card import Card
from ..unicode.check import hasUnicode


class Rank:
    values = ["A"] + [str(d) for d in list(range(2, 10))] + ["T", "J", "Q", "K"]
    suits = [u"\u2660", u"\u2665", u"\u2666", u"\u2663"]

    def __init__(self):
        if not hasUnicode:
            self.suits = ["S", "H", "D", "C"]
        self.rankedCards = [Card(value, suit) for suit in self.suits for value in self.values]

    def __str__(self):
        return str([(i, str(card)) for i, card in
                    enumerate([(Card(value, suit)) for suit in self.suits for value in self.values])])
