# coding=utf-8
from random import choice
from copy import deepcopy

from player.player import Player


class AI(Player):
    def turn(self, hand):
        self.printPlayersTurn()
        hand.printHand()
        if len(self.round.discard) > 0:
            self.round.printDiscard()
        self.display("%s thinking..." % self.players[self.round.currentPlayer].getPlayerName())
        self.chooseToDiscardOrPickUp(hand)
        hand.printHand()
        # sleep(700.0 / 1000.0)
        self.discardOrKnock(hand)
        self.display("%s choosing discard..." % self.players[self.round.currentPlayer].getPlayerName())
        self.round.printDiscard()
        # sleep(400.0 / 1000.0)

    @staticmethod
    def display(text):
        print(text)
        # sleep(600.0 / 1000.0)

    def chooseToDiscardOrPickUp(self, hand):
        if self.round.knocked:
            pass
        if len(self.round.discard) > 0:
            self.choosePickUp(hand)
        else:
            hand.drawCard(self.round.deck.pop())

    def choosePickUp(self, hand):
        dummyHand = deepcopy(hand)
        dummyHand.calculateScore()
        assert isinstance(dummyHand.score, object)
        currentScore = dummyHand.score
        dummyHand.drawCard(self.round.discard[-1])
        dummyHand.calculateScore()
        newScore = dummyHand.score
        aiChoice = 0 if newScore < currentScore else 1
        if aiChoice == 0:
            hand.drawCard(self.round.discard.pop())
            self.display("%s picked up discard" % self.players[self.round.currentPlayer].getPlayerName())
        else:
            hand.drawCard(self.round.deck.pop())
            self.display("%s drew from the deck" % self.players[self.round.currentPlayer].getPlayerName())

    def discardOrKnock(self, hand):
        scores = self.findDiscardScores(hand)
        if scores.count(min(scores)) > 1:
            choices = [(i, x) for (i, x) in enumerate(scores) if (x == min(scores))]
            discard = choice(choices)[0]
        else:
            discard = scores.index(min(scores))
        if min(scores) < 10 and not self.round.knocked:
            self.round.knocked = True
            self.display("%s has knocked!!" % self.players[self.round.currentPlayer].getPlayerName())
        self.round.discard.append(hand.discardCard(discard))
