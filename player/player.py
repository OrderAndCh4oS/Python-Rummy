# coding=utf-8
from copy import deepcopy


class Player:
    def __init__(self, players, round):
        self.players = players
        self.round = round

    def printPlayersTurn(self):
        print("###########################\n")
        print("Turn %i, %s\n" % (self.round.turn, self.getCurrentPlayerName()))

    def getCurrentPlayersHand(self):
        return self.players[self.round.currentPlayer].getHand()

    def getCurrentPlayerName(self):
        return self.players[self.round.currentPlayer].getPlayerName()

    @staticmethod
    def findDiscardScores(hand):
        scores = []
        for i in range(8):
            dummyHand = deepcopy(hand)
            dummyHand.discardCard(i)
            dummyHand.calculateScore()
            scores.append(dummyHand.score)
        return scores
