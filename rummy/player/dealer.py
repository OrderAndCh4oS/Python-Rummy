# -*- coding: utf-8 -*-

from rummy.player.hand import Hand


class Dealer:
    cardCount = 7

    def set_card_count(self, card_count: int):
        self.cardCount = card_count

    def deal(self, deck: list):
        hand = Hand()
        for _ in range(self.cardCount):
            hand.draw_card(deck.pop())
        return hand
