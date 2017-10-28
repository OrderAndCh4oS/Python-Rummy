# coding=utf-8
from player.player import Player
from colours.colours import green


class Human(Player):
    def turn(self, hand):
        self.printPlayersTurn()
        self.chooseToDiscardOrPickUp(hand)
        hand.printHandAndKey()
        self.discardOrKnock(hand)
        self.round.printDiscard()

    def chooseToDiscardOrPickUp(self, hand):
        if self.round.knocked:
            print("A Player has knocked, this is your last turn!!!\n")
        if len(self.round.discard) > 0:
            self.choosePickUp(hand)
        else:
            hand.drawCard(self.round.deck.pop())

    def discardOrKnock(self, hand):
        scores = self.findDiscardScores(hand)
        if min(scores) < 10 and not self.round.knocked:
            message = "Enter a number to discard a card or " + green('k') + " to Knock: "
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
        self.round.discard.append(hand.discardCard(playerChoice))

    def choosePickUp(self, hand):
        playerChoice = self.getUserPickUpInput(hand)
        if playerChoice == 'p':
            hand.drawCard(self.round.discard.pop())
        else:
            hand.drawCard(self.round.deck.pop())

    def getUserPickUpInput(self, hand):
        playerChoice = ''
        while playerChoice.lower() not in ['d', 'p']:
            hand.printHand()
            self.round.printDiscard()
            playerChoice = input("Enter " + green('d') + " to draw or " + green('p') + " to pickup discard: ")
        return playerChoice
