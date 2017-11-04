# coding=utf-8
from random import choice
from copy import deepcopy
from time import sleep

from player.player import Player
from view.view import View


class AI(Player):

    def chooseToDiscardOrPickUp(self):
        if len(self.round.discard) > 0:
            if self.aiOnly:
                self.renderPlayerTurnStart()
                self.aiThinking('Choosing pick up')
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
        if self.aiOnly:
            self.renderAITurnEnd()
            self.aiThinking('Choosing discard')
        scores = self.findDiscardScores()
        if min(scores) <= 10 and not self.round.knocked:
            self.round.knocked = True
        if scores.count(min(scores)) > 1:
            choices = [(i, x) for (i, x) in enumerate(scores) if (x == min(scores))]
            discard = choice(choices)[0]
        else:
            discard = scores.index(min(scores))
        self.round.discard.append(self.hand.discardCard(discard))

    def aiThinking(self, action):
        print(View.render(
            template='./templates/ai-thinking.txt',
            action=action,
        ))
        sleep(0.8)

    def renderAITurnEnd(self):
        print(View.render(
            template='./templates/ai-turn-end.txt',
            hand=self.hand.getHand(),
        ))
