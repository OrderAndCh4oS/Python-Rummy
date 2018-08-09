# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from text_template import TextTemplate as View

from rummy.constants.package_resource_path import TEMPLATE_PATH
from rummy.deck.melds import Melds
from rummy.player.hand import Hand


class Player(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, num):
        self.num = num
        self.gameScore = 0
        self.hand = Hand()
        self.melds = Melds()

    def turn(self, round, aiOnly):
        self.round = round
        self.aiOnly = aiOnly
        self.hasSomeoneKnocked()
        self.chooseToDiscardOrPickUp()
        self.discardOrKnock()

    def getName(self):
        return "Player %i" % self.num

    def updateScore(self):
        self.gameScore += self.hand.getScore()

    def getHand(self):
        return self.hand

    def getGameScore(self):
        return self.gameScore

    def displayRoundScore(self):
        return self.hand.score

    def hasSomeoneKnocked(self):
        if self.round.knocked:
            print(View.render(template=TEMPLATE_PATH + '/knocked.txt'))

    def renderPlayerTurnStart(self):
        print(View.render(
            template=TEMPLATE_PATH + '/player-turn-start.txt',
            turn_number=self.round.turn,
            player_number=self.round.currentPlayer + 1,
            score=self.hand.getScore(),
            hand=self.hand.getHandToPrint(),
            discard=self.round.getDiscard()
        ))

    def renderPlayerTurnEnd(self):
        print(View.render(
            template=TEMPLATE_PATH + '/player-turn-end.txt',
            hand=self.hand.getHandToPrint(),
            key=self.hand.getKey()
        ))

    @abstractmethod
    def chooseToDiscardOrPickUp(self):
        pass

    @abstractmethod
    def discardOrKnock(self):
        pass
