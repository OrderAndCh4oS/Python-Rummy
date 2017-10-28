# -*- coding: utf-8 -*-
from deck.deck import Deck
from player.dealer import Dealer


class Round(Dealer, Deck):
    firstPlayer = 0
    currentPlayer = 0
    turn = 1
    lastTurn = 1
    knocked = False

    def __init__(self, numberOfPlayers):
        super().__init__()
        self.numberOfPlayers = numberOfPlayers
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

    def endTurn(self):
        self.switchCurrentPlayer()
        self.turn += 1

    def checkKnocked(self):
        if self.knocked:
            self.lastTurn += 1

    def switchCurrentPlayer(self):
        self.currentPlayer = (self.currentPlayer + 1) % self.numberOfPlayers

    def rotateFirstPlayer(self):
        self.firstPlayer += 1
        assert isinstance(self.numberOfPlayers, int)
        self.currentPlayer = self.firstPlayer % self.numberOfPlayers
