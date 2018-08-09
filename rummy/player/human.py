# coding=utf-8
from ansi_colours import AnsiColours as Colour

from rummy.player.player import Player


class Human(Player):

    def chooseToDiscardOrPickUp(self):
        self.renderPlayerTurnStart()
        if len(self.round.discard) > 0:
            self.choosePickUp()
        else:
            self.hand.drawCard(self.round.deck.pop())

    def choosePickUp(self):
        playerChoice = self.getUserPickUpInput()
        if playerChoice == 'p':
            self.hand.drawCard(self.round.discard.pop())
        else:
            self.hand.drawCard(self.round.deck.pop())

    def discardOrKnock(self):
        self.renderPlayerTurnEnd()
        scores = self.melds.findDiscardScores(self.hand.getHand())
        if min(scores) <= 10 and not self.round.knocked:
            message = "Enter a number to discard a card or " + Colour.green('k') + " to Knock: "
        else:
            message = "Enter a number to discard a card: "
        playerChoice = ""
        while playerChoice not in [str(i) for i in range(1, 9)]:
            if self.round.knocked:
                message = "Enter a number to discard a card: "
            playerChoice = input(message)
            if playerChoice.lower() == "k" and min(scores) < 10:
                self.round.knocked = True
        playerChoice = int(playerChoice) - 1
        self.round.discard.append(self.hand.discardCard(playerChoice))

    def getUserPickUpInput(self):
        playerChoice = ''
        while playerChoice.lower() not in ['d', 'p']:
            playerChoice = input(
                "Enter " + Colour.green('d') + " to draw or " + Colour.green('p') + " to pickup discard: ")
        return playerChoice
