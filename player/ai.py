# coding=utf-8
from random import choice
from copy import deepcopy

from player.player import Player


class AI(Player):
    def turn(self, round):
        self.round = round
        self.chooseToDiscardOrPickUp()
        self.discardOrKnock()

    def chooseToDiscardOrPickUp(self):
        if self.round.knocked:
            pass
        if len(self.round.discard) > 0:
            self.choosePickUp()
        else:
            self.hand.drawCard(self.round.deck.pop())

    def choosePickUp(self):
        dummyHand = deepcopy(self.hand)
        dummyHand.calculateScore()
        currentScore = dummyHand.score
        dummyHand.drawCard(self.round.discard[-1])
        dummyHand.calculateScore()
        newScore = dummyHand.score
        if newScore < currentScore:
            self.hand.drawCard(self.round.discard.pop())
        else:
            self.hand.drawCard(self.round.deck.pop())

    def discardOrKnock(self):
        scores = self.findDiscardScores()
        if min(scores) <= 10 and not self.round.knocked:
            self.round.knocked = True
        if scores.count(min(scores)) > 1:
            choices = [(i, x) for (i, x) in enumerate(scores) if (x == min(scores))]
            discard = choice(choices)[0]
        else:
            discard = scores.index(min(scores))
        self.round.discard.append(self.hand.discardCard(discard))

    def display(self, text):
        print(text)
