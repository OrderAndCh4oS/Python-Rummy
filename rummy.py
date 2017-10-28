#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:14:18 2016

@author: Sarcoma
"""

from game.round import Round
from game.score import Score
from game.setup_players import SetupPlayers
from player.ai import AI
from player.human import Human
from colours.colours import green
from colours.colours import grey

class Rummy(SetupPlayers, Score):
    players = []

    def __init__(self):
        super().__init__()
        self.round = Round(self.numberOfPlayers)
        self.round.dealCards(self.players)
        self.playGame()

    def playGame(self):
        while self.round.lastTurn != self.numberOfPlayers:
            self.round.prepareTurn()
            if not self.ai or (self.round.currentPlayer == 0 and not self.aiOnly):
                player = Human(self.players, self.round)
            else:
                player = AI(self.players, self.round, self.aiOnly)
            hand = player.getCurrentPlayersHand()
            player.turn(hand)
            self.round.endTurn()
        self.endRound()
        self.startNewRoundOrEndGame()

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
            ready = input("Enter " + green('y') + " when you are ready for the next round: ")

    def endRound(self):
        print("\n" + grey("***************************"))
        print("Round Ended")
        self.printAllPlayersHands()
        print(grey("***************************"))
        self.displayThisRoundScore()
        self.updatePlayerScores()

    def printAllPlayersHands(self):
        for p in self.players:
            print("\n%s:" % p.getPlayerName())
            p.hand.printHand()


# start game
if __name__ == "__main__":
    Rummy()
