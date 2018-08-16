# -*- coding: utf-8 -*-

from ansi_colours import AnsiColours as Colour

from rummy.constants.constants import UNICODE_SUPPORT
from rummy.deck.suits import Suits


class Card:
    value = ""
    suit = ""

    def __init__(self, value, suit):
        self.value = value
        self.suit = Suits.alpha_to_unicode_suit_glyph(suit)

    def __str__(self):
        return "%s%s" % (self.value, self.suit)

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def get_card_colour(self):
        if self.suit in (u"♥", u"♦", "H", "D"):
            return self.red_card()
        elif self.suit in (u"♠", u"♣", "C", "S"):
            return self.black_card()

    def red_card(self):
        if UNICODE_SUPPORT:
            return str(self.value) + Colour.red(self.suit)
        else:
            return str(self.value) + self.suit

    def black_card(self):
        return str(self.value) + self.suit
