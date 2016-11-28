# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:14:18 2016

@author: Sarcoma
"""

from random import shuffle


class Deck:
    cards = [str(d) for d in list(range(2, 11))] + ["J", "Q", "K", "A"]
    suits = [u"\u2660", u"\u2665", u"\u2666", u"\u2663"]
    deck = []
    discard = []

    def stackDeck(self):
        self.deck = []
        self.discard = []
        for suit in self.suits:
            for card in self.cards:
                self.deck.append(Card(card, suit))
        shuffle(self.deck)

    def checkStack(self):
        if len(self.deck) == 0:
            self.deck = self.discard
            self.discard = []

    def printDiscard(self):
        print("Discard Pile: ", self.discard[-1].getCardColour())
        print("..........................\n")


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def getCardColour(self):
        if self.suit in [u"\u2665", u"\u2666"]:
            return self.redCard()
        elif self.suit in [u"\u2660", u"\u2663"]:
            return self.blackCard()

    def redCard(self):
        return str(self.value) + "\033[1;31m" + self.suit + "\033[0m, "

    def blackCard(self):
        return str(self.value) + self.suit + ", "


class Hand:
    def __init__(self):
        self.hand = []

    def drawCard(self, card):
        self.hand.append(card)

    def discardCard(self, choice):
        return self.hand.pop(choice)

    def printHand(self):
        output = ''
        for card in self.hand:
            output += card.getCardColour()
        print(output.strip(', '))

    def printKey(self):
        output = ''
        for i in range(len(self.hand)):
            output += " %i, " % (i + 1)
        print(output.strip(', '))

    def printHandAndKey(self):
        self.printHand()
        self.printKey()


class Dealer(Deck):
    cardCount = 7

    def setCardCount(self, cardCount):
        self.cardCount = cardCount

    def deal(self, deck):
        hand = Hand()
        for _ in range(self.cardCount):
            hand.drawCard(deck.pop())
        return hand


class Player:
    def __init__(self, num):
        self.num = num
        self.score = 0
        self.hand = Hand()

    def getPlayerName(self):
        return "Player %i" % self.num

    def updateScore(self, points):
        self.score += points

    def getScore(self):
        return self.score

    def getHand(self):
        return self.hand

    def enterPlayerScore(self):
        roundScore = False
        while type(roundScore) is not int:
            try:
                roundScore = int(input("Enter %s score: " % self.getPlayerName()))
            except ValueError:
                print("Please enter a valid score")
            else:
                self.score += roundScore


class Round(Dealer):
    firstPlayer = 0
    currentPlayer = 0
    turn = 1
    lastTurn = 1
    knocked = False

    def __init__(self, numberOfPlayers):
        self.numberOfPlayers = numberOfPlayers
        self.stackDeck()

    def prepareNewRound(self):
        self.rotateFirstPlayer()
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
        self.currentPlayer = self.firstPlayer % self.numberOfPlayers


class Rummy:
    players = []

    def __init__(self, numberOfPlayers):
        self.numberOfPlayers = numberOfPlayers
        self.createPlayers()
        self.round = Round(numberOfPlayers)
        self.round.dealCards(self.players)
        self.playGame()

    def createPlayers(self):
        self.players = [Player(i + 1) for i in range(self.numberOfPlayers)]

    def playGame(self):
        while self.round.lastTurn != self.numberOfPlayers:
            self.round.prepareTurn()
            hand = self.getCurrentPlayersHand()
            self.playTurn(hand)
            self.round.endTurn()
        self.endRound()
        self.startNewRoundOrEndGame()

    def playTurn(self, hand):
        self.printPlayersTurn()
        self.playerChooseToDiscardOrPickUp(hand)
        hand.printHandAndKey()
        self.playerDiscardOrKnock(hand)

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
        message = "Enter a number to discard a card or 'k' to Knock: "
        choice = ""
        while choice not in [str(i) for i in range(1, 9)]:
            if self.round.knocked:
                message = "Enter a number to discard a card: "
            choice = input(message)
            if choice.lower() == "k":
                self.round.knocked = True
        choice = int(choice) - 1
        self.round.discard.append(hand.discardCard(choice))

    def choosePickUp(self, hand):
        choice = self.getUserPickUpInput(hand)
        if choice == 'p':
            hand.drawCard(self.round.discard.pop())
        else:
            hand.drawCard(self.round.deck.pop())

    def getUserPickUpInput(self, hand):
        choice = ''
        while choice.lower() not in ['d', 'p']:
            hand.printHand()
            self.round.printDiscard()
            choice = input("Enter 'd' to draw or 'p' to pickup discard: ")
        return choice

    def getCurrentPlayerName(self):
        return self.players[self.round.currentPlayer].getPlayerName()

    def startNewRoundOrEndGame(self):
        if self.isEndOfGame():
            self.endGame()
        else:
            self.displayCurrentScores()
            self.round.prepareNewRound()
            self.playGame()

    def endRound(self):
        print("\n***************************")
        print("Round Ended, Enter Your Scores")
        self.printAllPlayersHands()
        print("***************************")
        self.enterAllPlayersScores()

    def printAllPlayersHands(self):
        for p in self.players:
            print("%s:" % p.getPlayerName())
            p.hand.printHand()

    def enterAllPlayersScores(self):
        for p in self.players:
            p.enterPlayerScore()

    def displayCurrentScores(self):
        for p in self.players:
            print(p.getPlayerName(), ": ", p.getScore())

    def isEndOfGame(self):
        for p in self.players:
            if p.getScore() > 100:
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
Rummy(2)
