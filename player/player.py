# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from copy import deepcopy

from player.hand import Hand
from view.view import View


class Player(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, num):
        self.num = num
        self.score = 0
        self.hand = Hand()

    def turn(self, round, aiOnly):
        self.round = round
        self.aiOnly = aiOnly
        self.hasSomeoneKnocked()
        self.chooseToDiscardOrPickUp()
        self.discardOrKnock()

    def getName(self):
        return "Player %i" % self.num

    def updateScore(self):
        self.score += self.hand.getScore()

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

    def hasSomeoneKnocked(self):
        if self.round.knocked:
            print(View.render(template='../templates/knocked.txt'))

    def renderPlayerTurnStart(self):
        print(View.render(
            template='../templates/player-turn-start.txt',
            turn_number=self.round.turn,
            player_number=self.round.currentPlayer + 1,
            score=self.hand.getScore(),
            hand=self.hand.getHand(),
            discard=self.round.getDiscard()
        ))

    def renderPlayerTurnEnd(self):
        print(View.render(
            template='../templates/player-turn-end.txt',
            hand=self.hand.getHand(),
            key=self.hand.getKey()
        ))

    @abstractmethod
    def chooseToDiscardOrPickUp(self):
        pass

    @abstractmethod
    def discardOrKnock(self):
        pass
