# -*- coding: utf-8 -*-
from random import shuffle
from deck.rank import Rank
from view.colours import grey

class Deck(Rank):
    deck = []
    discard = []

    def stackDeck(self):
        self.deck = self.rankedCards[:]
        self.discard = []
        shuffle(self.deck)

    def checkStack(self):
        if len(self.deck) == 0:
            self.deck = self.discard
            self.discard = []

    def getDiscard(self):
        return self.discard[-1].getCardColour()
