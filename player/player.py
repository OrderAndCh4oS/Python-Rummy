# -*- coding: utf-8 -*-
from copy import deepcopy

from player.hand import Hand


class Player:
    def __init__(self, num):
        self.num = num
        self.score = 0
        self.hand = Hand()

    def getName(self):
        return "Player %i" % self.num

    def updateScore(self):
        self.score += self.hand.score

    def getHand(self):
        return self.hand

    def getScore(self):
        return self.score

    def displayRoundScore(self):
        return self.hand.score

    def findDiscardScores(self):
        scores = []
        for i in range(8):
            dummyHand = deepcopy(self.hand)
            dummyHand.discardCard(i)
            dummyHand.calculateScore()
            scores.append(dummyHand.score)
        return scores
