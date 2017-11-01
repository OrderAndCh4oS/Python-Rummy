# coding=utf-8
from player.player import Player
from view.colours import green
from view.view import View


class Human(Player):
    def turn(self, round):
        self.round = round
        self.chooseToDiscardOrPickUp()
        self.discardOrKnock()

    def chooseToDiscardOrPickUp(self):
        if self.round.knocked:
            view = View()
            view.render(template='./templates/knocked.txt')
        if len(self.round.discard) > 0:
            self.choosePickUp()
        else:
            self.hand.drawCard(self.round.deck.pop())

    def discardOrKnock(self):
        view = View()
        print(view.render(
            template='./templates/player-turn-end.txt',
            hand=self.hand.getHand(),
            key=self.hand.getKey()
        ))
        scores = self.findDiscardScores()
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
        self.round.discard.append(self.hand.discardCard(playerChoice))

    def choosePickUp(self):
        playerChoice = self.getUserPickUpInput()
        if playerChoice == 'p':
            self.hand.drawCard(self.round.discard.pop())
        else:
            self.hand.drawCard(self.round.deck.pop())

    def getUserPickUpInput(self):
        playerChoice = ''
        while playerChoice.lower() not in ['d', 'p']:
            view = View()
            print(view.render(
                template='./templates/player-turn-start.txt',
                turn_number=self.round.turn,
                player_number=self.round.currentPlayer + 1,
                score=self.hand.getScore(),
                hand=self.hand.getHand(),
                discard=self.round.getDiscard().strip(', ')
            ))
            playerChoice = input("Enter " + green('d') + " to draw or " + green('p') + " to pickup discard: ")
        return playerChoice
