# -*- coding: utf-8 -*-
from rummy.player.hand import Hand


class Dealer:
    cardCount = 7

    def setCardCount(self, cardCount):
        self.cardCount = cardCount

    def deal(self, deck):
        hand = Hand()
        for _ in range(self.cardCount):
            hand.drawCard(deck.pop())
        return hand
