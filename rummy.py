#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:14:18 2016

@author: Sarcoma
"""

from copy import deepcopy
from random import choice

from game.round import Round
from game.setup_players import SetupPlayers


# from time import sleep
from player.ai import AI
from player.human import Human


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
            if not self.ai or (self.round.currentPlayer == 0 and not self.aiOnly):
                player = Human(self.players, self.round)
                hand = player.getCurrentPlayersHand()
                player.turn(hand)
            else:
                player = AI(self.players, self.round)
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
