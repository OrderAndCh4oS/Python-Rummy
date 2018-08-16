# coding=utf-8
from rummy.constants.constants import UNICODE_SUPPORT, ALPHA_SUITS, SUITS


class Suits:

    @staticmethod
    def get() -> tuple:
        return SUITS if UNICODE_SUPPORT else ALPHA_SUITS

    @staticmethod
    def alpha_to_unicode_suit_glyph(suit):
        if UNICODE_SUPPORT and suit in ALPHA_SUITS:
            suit = SUITS[ALPHA_SUITS.index(suit)]
        return suit
