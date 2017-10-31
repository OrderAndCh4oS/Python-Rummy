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
from view.colours import green
from view.colours import grey


class Rummy():
    def __init__(self):
        setup = SetupPlayers()
        self.players = setup.createPlayers()
        self.score = Score(self.players)
        self.round = Round(self.players)
        self.round.dealCards(self.players)
        self.playGame()

    def playGame(self):
        while self.round.lastTurn != len(self.players):
            self.round.prepareTurn()
            player = self.players[self.round.currentPlayer]
            player.turn(self.round)
            self.round.endTurn()
        self.endRound()
        self.startNewRoundOrEndGame()

    def startNewRoundOrEndGame(self):
        if self.score.isEndOfGame():
            self.score.endGame()
        else:
            self.score.displayCurrentScores()
            self.round.rotateFirstPlayer()
            if any(isinstance(x, Human) for x in self.players):
                self.confirmStartNewRound()
            self.round.prepareNewRound()
            self.round.dealCards(self.players)
            self.playGame()

    def confirmStartNewRound(self):
        print("\nReady %s?" % self.players[self.round.currentPlayer].getName())
        ready = ''
        while ready.lower() != 'y':
            ready = input("Enter " + green('y') + " when you are ready for the next round: ")

    def endRound(self):
        print("\n" + grey("***************************"))
        print("Round Ended")
        self.printAllPlayersHands()
        print(grey("***************************"))
        self.score.displayThisRoundScore()
        self.score.updatePlayerScores()

    def printAllPlayersHands(self):
        for p in self.players:
            print("\n%s:" % p.getName())
            p.hand.printHand()


# start game
if __name__ == "__main__":
    Rummy()
