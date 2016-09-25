#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:14:18 2016

@author: Sarcoma
"""
from operator import itemgetter
from random import shuffle
class Rummy:
    cards = ["A"] + list(range(2, 11)) + ["J", "Q", "K"]
    suits = [u"\u2660", u"\u2665", u"\u2666", u"\u2663"]
    deck = []
    discard = []
    playerOneScore = 0
    playerTwoScore = 0

    def __init__(self):
        self.setDeck()

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
                hands[i] += (self.deck.pop(), )
        return (tuple(hands))

    def sortHand(self, hand):
        hand.sort(key=itemgetter(1))

    def printHand(self, hand):
        output = ''
        for card in hand:
           output += self.getCardColour(card)
        print(output.strip(', '))

    def getCardColour(self, card):
        if card[1] in [u"\u2665",  u"\u2666"]:
            return self.redCard(card)
        elif card[1] in [u"\u2660",  u"\u2663"]:
            return self.blackCard(card)

    def redCard(self, card):
        return str(card[0]) + "\033[1;31m" + card[1] + "\033[0m, "

    def blackCard(self, card):
        return str(card[0]) + card[1] + ", "

    def printKey(self, hand):
        output = ''
        for i in range(len(hand)):
            output += " %i, " % (i+1)
        print(output.strip(', '))

    def drawCard(self, hand):
        hand.append(self.deck.pop())

    def choosePickUp(self, hand):
        choice = ''
        while choice.lower() not in ['d', 'p']:
            self.sortHand(hand)
            self.printHand(hand)
            print("Discard Pile: ", self.getCardColour(self.discard[-1]))
            print("..........................\n")
            choice = input("Enter 'd' to draw or 'p' to pickup discard: ")
        if choice == 'p':
            hand.append(self.discard.pop())
        else:
            self.drawCard(hand)

    def playGame(self):
        turn = 1
        (playerOneHand, playerTwoHand) = self.deal(7, 2)
        knocked = False
        lastTurn = False
        currentPlayer = 1
        while lastTurn == False:
            if len(self.deck) == 0:
                self.deck = self.discard
                self.discard = []
            if knocked == True:
                lastTurn = True
            hand = playerOneHand if currentPlayer == 1 else playerTwoHand
            print("###########################\n")
            print("Turn %i, Player %i\n" % (turn, currentPlayer))
            if knocked == True:
                print("Player %i knocked last turn!!!\n" % ((currentPlayer + 1) % 2))
            if len(self.discard) > 0:
                self.choosePickUp(hand)
            else:
                self.drawCard(hand)
            self.sortHand(hand)
            self.printHand(hand)
            self.printKey(hand)
            choice = input("Enter a number to discard a card or 'k' to Knock: ")
            if choice.lower() == "k":
                knocked = True
                choice = input("Enter a number to discard a card: ")
            if not choice.isnumeric():
                return False
            choice = int(choice)
            if choice > len(hand) or choice < 1:
                return False
            self.discard.append(hand.pop(choice - 1))
            currentPlayer = (currentPlayer + 1) % 2
            turn += 1
        print("\n***************************")
        print("Game Ended, Count Your Scores")
        print("Player One:")
        self.printHand(playerOneHand)
        print("Player Two:")
        self.printHand(playerTwoHand)
        print("***************************")
        self.playerOneScore += int(input("Enter player one score: "))
        self.playerTwoScore += int(input("Enter player two score: "))
        if self.playerOneScore < 100 and self.playerTwoScore < 100:
            print("Player One Score:", self.playerOneScore)
            print("Player Two Score:", self.playerTwoScore)
            self.setDeck()
            self.playGame()
        else:
            winner = "Player One" if self.playerOneScore < self.playerTwoScore else "Player Two"
            print(winner, "is the Winner!!")
            print("Player One Score:", self.playerOneScore)
            print("Player Two Score:", self.playerTwoScore)



#start game
game = Rummy()
game.playGame()

