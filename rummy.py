#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:14:18 2016

@author: Sarcoma
"""

from random import shuffle, randrange
from copy import deepcopy
import itertools


class Rank:
    values = ["A"] + [str(d) for d in list(range(2, 11))] + ["J", "Q", "K"]
    suits = [u"\u2660", u"\u2665", u"\u2666", u"\u2663"]

    def __init__(self):
        self.rankedCards = [Card(value, suit) for suit in self.suits for value in self.values]


class Deck(Rank):
    deck = []
    discard = []

    def stackDeck(self):
        self.deck = self.rankedCards[:]
        self.discard = []
        shuffle(self.deck)

    def checkStack(self):
        if len(self.deck) == 0:
            self.deck = self.discard
            self.discard = []

    def printDiscard(self):
        print("Discard Pile: ", self.discard[-1].getCardColour())
        print("...........................\n")


class Card:
    value = ""
    suit = ""

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


class Hand(Rank):
    melds = []
    score = 0

    def __init__(self):
        super().__init__()
        self.hand = []

    def drawCard(self, card):
        self.hand.append(card)

    def discardCard(self, choice):
        return self.hand.pop(choice)

    def printHand(self):
        self.sortHandBySuitAndRank()
        self.calculateScore()
        output = ''
        print("...........................")
        print("Hand Score:", self.score)
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

    def sortHandBySuitAndRank(self):
        self.hand = sorted(self.hand, key=lambda card: self.suitAndRankKey(card))

    def sortHandByRank(self):
        self.hand = sorted(self.hand, key=lambda card: self.rankKey(card))

    def suitAndRankKey(self, card):
        return self.suits.index(card.suit), self.values.index(card.value)

    def rankKey(self, card):
        return self.values.index(card.value)

    def calculateScore(self):
        self.sortHandBySuitAndRank()
        cards = {self.suitAndRankKey(card) for card in self.hand}
        self.findSets()
        self.findRuns()
        allPossibleMelds = self.findAllPossibleMelds()
        self.melds = []
        if len(allPossibleMelds) > 0:
            scores = self.findLowestScoringMelds(allPossibleMelds, cards)
            self.score = min(scores)
        else:
            self.score = sum([x[1] + 1 for x in cards])

    def findAllPossibleMelds(self):
        allPossibleMelds = []
        for L in range(1, 3):
            for subset in itertools.combinations(self.melds, L):
                allPossibleMelds.append(subset)
        return allPossibleMelds

    @staticmethod
    def findLowestScoringMelds(allPossibleMelds, cards):
        scores = []
        for item in allPossibleMelds:
            if len(item) > 1:
                for i in range(len(item) - 1):
                    if item[i].isdisjoint(item[i + 1]):
                        items = item[i] | item[i + 1]
                        remainingCards = cards.difference(items)
                        scores.append(sum([x[1] + 1 for x in remainingCards]))
            else:
                remainingCards = cards.difference(item[0])
                scores.append(sum([x[1] + 1 for x in remainingCards]))
        return scores

    def findSets(self):
        self.sortHandByRank()
        cards = [self.suitAndRankKey(card) for card in self.hand]
        i = 1
        while i < len(cards):
            i, meld = self.makeSetMeld(cards, i)
            self.makeAllMelds(meld)
            i += 1

    def findRuns(self):
        self.sortHandBySuitAndRank()
        cards = [self.suitAndRankKey(card) for card in self.hand]
        i = 1
        while i < len(cards):
            i, meld = self.makeRunMeld(cards, i)
            self.makeAllMelds(meld)
            i += 1

    @staticmethod
    def makeSetMeld(cards, i):
        meld = []
        while i < len(cards) and cards[i][1] == cards[i - 1][1]:
            meld.append(cards[i - 1])
            i += 1
        meld.append(cards[i - 1])
        return i, meld

    @staticmethod
    def makeRunMeld(cards, i):
        meld = []
        while i < len(cards) and cards[i][0] == cards[i - 1][0] and cards[i][1] == cards[i - 1][1] + 1:
            meld.append(cards[i - 1])
            i += 1
        meld.append(cards[i - 1])
        return i, meld

    def makeAllMelds(self, meld):
        if len(meld) >= 3:
            self.melds.append(set(meld))
        if len(meld) > 3:
            for width in range(3, len(meld)):
                for i, step in enumerate(range(len(meld) - 2)):
                    self.melds.append(set(meld[step:width + i]))


class Dealer:
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

    def updateScore(self):
        self.score += self.hand.score

    def getScore(self):
        return self.score

    def getHand(self):
        return self.hand

    def displayRoundScore(self):
        return self.hand.score


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
        self.currentPlayer = self.firstPlayer % self.numberOfPlayers


class Rummy:
    players = []
    ai = False

    def __init__(self):
        numberOfPlayers = 0
        while numberOfPlayers not in [i for i in range(1, 5)]:
            numberOfPlayers = int(input("Enter number of players (1-4)? "))
        if numberOfPlayers == 1:
            self.ai = True
            numberOfPlayers = 2
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
            if not self.ai or self.round.currentPlayer == 0:
                self.playerTurn(hand)
            else:
                self.AITurn(hand)
            self.round.endTurn()
        self.endRound()
        self.startNewRoundOrEndGame()

    def AITurn(self, hand):
        # self.printPlayersTurn()
        self.AIChooseToDiscardOrPickUp(hand)
        # hand.printHandAndKey()
        self.AIDiscardOrKnock(hand)

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
        currentScore = dummyHand.score
        dummyHand.drawCard(self.round.discard[-1])
        dummyHand.calculateScore()
        newScore = dummyHand.score
        choice = 0 if newScore < currentScore else 1
        if choice == 0:
            hand.drawCard(self.round.discard.pop())
        else:
            hand.drawCard(self.round.deck.pop())

    def AIDiscardOrKnock(self, hand):
        scores = []
        for i in range(8):
            dummyHand = deepcopy(hand)
            dummyHand.discardCard(i)
            dummyHand.calculateScore()
            scores.append(dummyHand.score)
        choice = scores.index(min(scores))
        if hand.score < 30:
            self.round.knocked = True
        self.round.discard.append(hand.discardCard(choice))

    def playerTurn(self, hand):
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
            self.round.rotateFirstPlayer()
            print("\nReady %s?" % self.players[self.round.currentPlayer].getPlayerName())
            ready = ''
            while ready.lower() != 'y':
                ready = input("Enter 'y' when you are ready for the next round: ")
            self.round.prepareNewRound()
            self.playGame()

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
