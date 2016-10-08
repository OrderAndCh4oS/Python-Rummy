# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:14:18 2016

@author: Sarcoma
"""

from random import shuffle


class Rummy:
    cards = ["A"] + [str(d) for d in list(range(2, 11))] + ["J", "Q", "K"]
    suits = [u"\u2660", u"\u2665", u"\u2666", u"\u2663"]
    deck = []
    discard = []
    playerOneScore = 0
    playerTwoScore = 0

    def __init__(self):
        self.lastTurn = False
        self.knocked = False
        self.turn = 1
        self.setDeck()
        self.playGame()

    def setDeck(self):
        self.deck = []
        self.discard = []
        for suit in self.suits:
            for card in self.cards:
                self.deck.append((card, suit))
        shuffle(self.deck)

    def deal(self, cardCount, playerCount):
        hands = []
        for _ in range(playerCount):
            hands.append([])
        for _ in range(cardCount):
            for i in range(playerCount):
                hands[i] += (self.deck.pop(),)
        return tuple(hands)

    def printHand(self, hand):
        output = ''

        for card in hand:
            output += self.getCardColour(card)
        print(output.strip(', '))

    def getCardColour(self, card):
        if card[1] in [u"\u2665", u"\u2666"]:
            return self.redCard(card)
        elif card[1] in [u"\u2660", u"\u2663"]:
            return self.blackCard(card)

    @staticmethod
    def redCard(card):
        return str(card[0]) + "\033[1;31m" + card[1] + "\033[0m, "

    @staticmethod
    def blackCard(card):
        return str(card[0]) + card[1] + ", "

    @staticmethod
    def printKey(hand):
        output = ''
        for i in range(len(hand)):
            output += " %i, " % (i + 1)
        print(output.strip(', '))

    def drawCard(self, hand):
        hand.append(self.deck.pop())

    def choosePickUp(self, hand):
        choice = ''
        while choice.lower() not in ['d', 'p']:
            self.printHand(hand)
            print("Discard Pile: ", self.getCardColour(self.discard[-1]))
            print("..........................\n")
            choice = input("Enter 'd' to draw or 'p' to pickup discard: ")
        if choice == 'p':
            hand.append(self.discard.pop())
        else:
            self.drawCard(hand)

    def checkStack(self):
        if len(self.deck) == 0:
            self.deck = self.discard
            self.discard = []

    def checkKnocked(self):
        if self.knocked:
            self.lastTurn = True

    def beginTurn(self, currentPlayer, hand):
        print("###########################\n")
        print("Turn %i, Player %i\n" % (self.turn, currentPlayer))
        if self.knocked:
            print("Player %i knocked last turn!!!\n" % ((currentPlayer + 1) % 2))
        if len(self.discard) > 0:
            self.choosePickUp(hand)
        else:
            self.drawCard(hand)

    def playHand(self, hand):
        choice = input("Enter a number to discard a card or 'k' to Knock: ")
        if choice.lower() == "k":
            self.knocked = True
            choice = input("Enter a number to discard a card: ")
        while choice not in [str(i) for i in range(1, 9)]:
            choice = input("Enter a number to discard a card: ")
        choice = int(choice)
        if choice > len(hand) or choice < 1:
            return False
        self.discard.append(hand.pop(choice - 1))
        return

    def endRound(self, playerOneHand, playerTwoHand):
        print("\n***************************")
        print("Round Ended, Enter Your Scores")
        print("Player One:")
        self.printHand(playerOneHand)
        print("Player Two:")
        self.printHand(playerTwoHand)
        print("***************************")
        self.playerOneScore += self.enterPlayerScore("Enter player one score: ")
        self.playerTwoScore += self.enterPlayerScore("Enter player two score: ")

    @staticmethod
    def enterPlayerScore(message):
        roundScore = False
        while type(roundScore) is not int:
            try:
                roundScore = int(input(message))
            except ValueError:
                print("Please enter a valid score")
            else:
                return roundScore

    def displayCurrentScores(self):
        print("Player One Score:", self.playerOneScore)
        print("Player Two Score:", self.playerTwoScore)

    def endGame(self):
        winner = "Player One" if self.playerOneScore < self.playerTwoScore else "Player Two"
        print(winner, "is the Winner!!")
        self.displayCurrentScores()

    def playGame(self):
        (playerOneHand, playerTwoHand) = self.deal(7, 2)
        currentPlayer = 1
        while not self.lastTurn:
            self.checkStack()
            self.checkKnocked()
            hand = playerOneHand if currentPlayer == 1 else playerTwoHand
            self.beginTurn(currentPlayer, hand)
            self.printHand(hand)
            self.printKey(hand)
            self.playHand(hand)
            currentPlayer = (currentPlayer + 1) % 2
            self.turn += 1
        self.endRound(playerOneHand, playerTwoHand)
        if self.playerOneScore < 100 and self.playerTwoScore < 100:
            self.displayCurrentScores()
            self.__init__()
        else:
            self.endGame()


# start game
Rummy()
