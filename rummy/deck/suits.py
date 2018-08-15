# coding=utf-8
from constants.constants import UNICODE_SUPPORT


class Suits:
    suits = ("♠", "♥", "♦", "♣")

    def __init__(self):
        if not UNICODE_SUPPORT:
            self.suits = ("S", "H", "D", "C")

    def get(self) -> tuple:
        return self.suits
