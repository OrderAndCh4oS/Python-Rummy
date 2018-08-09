# coding=utf-8
from random import choice
from time import sleep

from text_template import TextTemplate as View

from rummy.constants.package_resource_path import TEMPLATE_PATH
from rummy.player.player import Player


class AI(Player):

    def chooseToDiscardOrPickUp(self):
        if len(self.round.discard) > 0:
            if self.aiOnly:
                self.renderPlayerTurnStart()
                self.aiThinking('Choosing pick up')
            self.choosePickUp()
        else:
            self.aiThinking('Drawing first card from deck')
            self.hand.drawCard(self.round.deck.pop())

    def choosePickUp(self):
        currentScore = self.hand.getScore()
        if self.aiOnly:
            print('Current Score: ', currentScore)
        scores = self.melds.findDiscardScores(self.hand.getHand(), self.round.discard[-1])
        if self.aiOnly:
            print('Possible Hand Scores: ', scores)
            print('Min Score: ', min(scores))
        if min(scores) < currentScore - 4 or min(scores) < 10:
            self.aiThinking('Drawing from discard')
            self.hand.drawCard(self.round.discard.pop())
        else:
            self.aiThinking('Drawing from deck')
            self.hand.drawCard(self.round.deck.pop())

    def discardOrKnock(self):
        if self.aiOnly:
            self.renderAITurnEnd()
        self.aiThinking('Choosing card to discard')
        scores = self.melds.findDiscardScores(self.hand.getHand())
        score = min(scores)
        if score <= 10 and not self.round.knocked:
            self.round.knocked = True
        if scores.count(score) > 1:
            choices = [(i, x) for (i, x) in enumerate(scores) if (x == score)]
            discard = choice(choices)[0]
        else:
            discard = scores.index(score)
        discard = self.hand.discardCard(discard)
        if self.aiOnly:
            print('Discarding: ', discard)
            print('Hand Score: ', score)
        self.round.discard.append(discard)

    def aiThinking(self, action):
        print(View.render(
            template=TEMPLATE_PATH + '/ai-thinking.txt',
            action=action,
        ))
        if not self.aiOnly:
            sleep(0.8)

    def renderAITurnEnd(self):
        print(View.render(
            template=TEMPLATE_PATH + '/ai-turn-end.txt',
            hand=self.hand.getHandToPrint(),
        ))
