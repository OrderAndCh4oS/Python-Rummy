#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:14:18 2016

@author: Sarcoma
"""

from random import choice
from copy import deepcopy
# from time import sleep

from game.setup_players import SetupPlayers
from game.round import Round


class Rummy(SetupPlayers):
    players = []

    def __init__(self):
        super().__init__()
        self.round = Round(self.numberOfPlayers)
        self.round.dealCards(self.players)
        self.playGame()

    def playGame(self):
        while self.round.lastTurn != self.numberOfPlayers:
            self.round.prepareTurn()
            hand = self.getCurrentPlayersHand()
            if not self.ai or (self.round.currentPlayer == 0 and not self.aiOnly):
                self.playerTurn(hand)
            else:
                self.AITurn(hand)
            self.round.endTurn()
        self.endRound()
        self.startNewRoundOrEndGame()

    def AITurn(self, hand):
        self.printPlayersTurn()
        hand.printHand()
        if len(self.round.discard) > 0:
            self.round.printDiscard()
        self.AIDisplay("%s thinking..." % self.players[self.round.currentPlayer].getPlayerName())
        self.AIChooseToDiscardOrPickUp(hand)
        hand.printHand()
        # sleep(700.0 / 1000.0)
        self.AIDiscardOrKnock(hand)
        self.AIDisplay("%s choosing discard..." % self.players[self.round.currentPlayer].getPlayerName())
        self.round.printDiscard()
        # sleep(400.0 / 1000.0)

    @staticmethod
    def AIDisplay(text):
        print(text)
        # sleep(600.0 / 1000.0)

    def AIChooseToDiscardOrPickUp(self, hand):
        if self.round.knocked:
            pass
        if len(self.round.discard) > 0:
            self.AIChoosePickUp(hand)
        else:
            hand.drawCard(self.round.deck.pop())

    def AIChoosePickUp(self, hand):
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
            self.AIDisplay("%s picked up discard" % self.players[self.round.currentPlayer].getPlayerName())
        else:
            hand.drawCard(self.round.deck.pop())
            self.AIDisplay("%s drew from the deck" % self.players[self.round.currentPlayer].getPlayerName())

    def AIDiscardOrKnock(self, hand):
        scores = self.findDiscardScores(hand)
        if scores.count(min(scores)) > 1:
            choices = [(i, x) for (i, x) in enumerate(scores) if (x == min(scores))]
            discard = choice(choices)[0]
        else:
            discard = scores.index(min(scores))
        if min(scores) < 10 and not self.round.knocked:
            self.round.knocked = True
            self.AIDisplay("%s has knocked!!" % self.players[self.round.currentPlayer].getPlayerName())
        self.round.discard.append(hand.discardCard(discard))

    @staticmethod
    def findDiscardScores(hand):
        scores = []
        for i in range(8):
            dummyHand = deepcopy(hand)
            dummyHand.discardCard(i)
            dummyHand.calculateScore()
            scores.append(dummyHand.score)
        return scores

    def playerTurn(self, hand):
        self.printPlayersTurn()
        self.playerChooseToDiscardOrPickUp(hand)
        hand.printHandAndKey()
        self.playerDiscardOrKnock(hand)
        self.round.printDiscard()

    def getCurrentPlayersHand(self):
        hand = self.players[self.round.currentPlayer].getHand()
        return hand

    def printPlayersTurn(self):
        print("###########################\n")
        print("Turn %i, %s\n" % (self.round.turn, self.getCurrentPlayerName()))

    def playerChooseToDiscardOrPickUp(self, hand):
        if self.round.knocked:
            print("A Player has knocked, this is your last turn!!!\n")
        if len(self.round.discard) > 0:
            self.choosePickUp(hand)
        else:
            hand.drawCard(self.round.deck.pop())

    def playerDiscardOrKnock(self, hand):
        scores = self.findDiscardScores(hand)
        if min(scores) < 10 and not self.round.knocked:
            message = "Enter a number to discard a card or 'k' to Knock: "
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
            playerChoice = input("Enter 'd' to draw or 'p' to pickup discard: ")
        return playerChoice

    def getCurrentPlayerName(self):
        return self.players[self.round.currentPlayer].getPlayerName()

    def startNewRoundOrEndGame(self):
        if self.isEndOfGame():
            self.endGame()
        else:
            self.displayCurrentScores()
            self.round.rotateFirstPlayer()
            if not self.aiOnly:
                self.confirmStartNewRound()
            self.round.prepareNewRound()
            self.round.dealCards(self.players)
            self.playGame()

    def confirmStartNewRound(self):
        print("\nReady %s?" % self.players[self.round.currentPlayer].getPlayerName())
        ready = ''
        while ready.lower() != 'y':
            ready = input("Enter 'y' when you are ready for the next round: ")

    def endRound(self):
        print("\n***************************")
        print("Round Ended")
        self.printAllPlayersHands()
        print("***************************")
        self.displayThisRoundScore()
        self.updatePlayerScores()

    def printAllPlayersHands(self):
        for p in self.players:
            print("\n%s:" % p.getPlayerName())
            p.hand.printHand()

    def displayThisRoundScore(self):
        for p in self.players:
            p.displayRoundScore()

    def displayCurrentScores(self):
        print("Game Scores")
        for p in self.players:
            print("%s: %s" % (p.getPlayerName(), p.getScore()))

    def updatePlayerScores(self):
        for p in self.players:
            p.updateScore()

    def isEndOfGame(self):
        for p in self.players:
            if p.getScore() >= 100:
                return True
        return False

    def endGame(self):
        winners = self.findLowestScores()
        if len(winners) == 1:
            print(winners[0].getPlayerName(), "is the Winner!!")
        else:
            print(", ".join([w.getPlayerName() for w in winners]), "are joint winners!")
        self.displayCurrentScores()

    def findLowestScores(self):
        lowest = []
        for p in self.players:
            if not lowest:
                lowest = [p]
                continue
            if p.getScore() < lowest[0].getScore():
                lowest = [p]
            elif p.getScore() == lowest[0].getScore():
                lowest.append(p)
        return lowest


# start game
Rummy()
