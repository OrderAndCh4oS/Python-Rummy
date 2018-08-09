# -*- coding: utf-8 -*-

from ansi_colours import AnsiColours as Colour

from rummy.deck.melds import Melds
from rummy.deck.rank import Rank
from rummy.deck.sort import Sort


class Hand(Rank):

    def __init__(self):
        super().__init__()
        self.colour = Colour()
        self.hand = []
        self.score = 0
        self.sort = Sort()
        self.melds = Melds()

    def __str__(self):
        self.hand = self.sort.sortHandBySuitAndRank(self.hand)
        return ''.join([card.getCardColour() for card in self.hand]).strip(', ')

    def setHand(self, hand):
        self.hand = hand

    def getHand(self):
        return self.hand

    def drawCard(self, card):
        self.hand.append(card)

    def discardCard(self, choice):
        return self.hand.pop(choice)

    def getScore(self):
        return self.melds.calculateScore(self.hand)

    def getHandToPrint(self):
        self.hand = self.sort.sortHandBySuitAndRank(self.hand)
        return ''.join([card.getCardColour() for card in self.hand]).strip(', ')

    def getKey(self):
        return ''.join([" %s, " % Colour.green(str((i + 1))) for i in range(len(self.hand))])
