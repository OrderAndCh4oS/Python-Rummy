#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:14:18 2016

@author: Sarcoma
"""
from time import sleep

from game.round import Round
from game.score import Score
from game.setup_players import SetupPlayers
from player.human import Human
from view.colour import Colour


class Rummy():
    def __init__(self):
        setup = SetupPlayers()
        self.players = setup.createPlayers()
        self.aiOnly = not any(isinstance(x, Human) for x in self.players)
        self.score = Score(self.players)
        self.round = Round(self.players)
        self.round.dealCards(self.players)
        self.playGame()

    def playGame(self):
        while self.round.lastTurn != len(self.players):
            self.round.prepareTurn()
            player = self.players[self.round.currentPlayer]
            player.turn(self.round, self.aiOnly)
            self.round.endTurn()
        self.endRound()
        sleep(0.8)
        self.startNewRoundOrEndGame()

    def startNewRoundOrEndGame(self):
        if self.score.isEndOfGame():
            self.score.endGame()
        else:
            self.round.rotateFirstPlayer()
            if not self.aiOnly:
                self.confirmStartNewRound()
            self.round.prepareNewRound()
            self.round.dealCards(self.players)
            self.playGame()

    def confirmStartNewRound(self):
        print("\nReady %s?" % self.players[self.round.currentPlayer].getName())
        ready = ''
        while ready.lower() != 'y':
            ready = input("Enter " + Colour.green('y') + " when you are ready for the next round: ")

    def endRound(self):
        self.score.updatePlayerScores()
        self.score.displayThisRoundScore()

# start game
if __name__ == "__main__":
    Rummy()
