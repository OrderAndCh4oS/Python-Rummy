# -*- coding: utf-8 -*-
from rummy.deck.deck import Deck
from rummy.player.dealer import Dealer


class Round(Dealer, Deck):
    firstPlayer = 0
    currentPlayer = 0
    turn = 1
    lastTurn = 1
    knocked = False

    def __init__(self, players):
        super().__init__()
        self.players = players
        self.stackDeck()

    def prepareNewRound(self):
        self.turn = 1
        self.lastTurn = 1
        self.knocked = False
        self.stackDeck()

    def dealCards(self, players):
        for p in players:
            p.hand = self.deal(self.deck)

    def prepareTurn(self):
        self.checkStack()
        self.checkKnocked()

    def getTurn(self, round):
        return "Turn %i, %s\n" % (round.turn, round.getCurrentPlayersName())

    def getCurrentPlayersHand(self):
        return self.players[self.currentPlayer].getHandToPrint()

    def endTurn(self):
        self.switchCurrentPlayer()
        self.turn += 1

    def checkKnocked(self):
        if self.knocked:
            self.lastTurn += 1

    def switchCurrentPlayer(self):
        self.currentPlayer = (self.currentPlayer + 1) % len(self.players)

    def rotateFirstPlayer(self):
        self.firstPlayer += 1
        self.currentPlayer = self.firstPlayer % len(self.players)
