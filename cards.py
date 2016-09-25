# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:14:18 2016

@author: Sarcoma
"""

from random import shuffle

cards = ["A"] + list(range(2, 10)) + ["J", "Q", "K"]
suits = [u"\u2660", u"\u2665", u"\u2666", u"\u2663"]
deck = []
discard = []

for suit in suits:
    for card in cards:
        deck.append((card, suit))
shuffle(deck)

def deal(deck, cardCount, playerCount):
    hands = []
    for _ in range(playerCount):
        hands.append([])
    for _ in range(cardCount):
        for i in range(playerCount):
            hands[i] += (deck.pop(), )
    return (tuple(hands))
    
def printHand(hand):
    output = ''
    for card in hand:
       output += getCardColour(card)
    print(output.strip(', '))
        
def getCardColour(card):
    if card[1] in [u"\u2665",  u"\u2666"]:
        return redCard(card)
    elif card[1] in [u"\u2660",  u"\u2663"]:
        return blackCard(card)
        
def redCard(card):
    return  str(card[0]) + "\033[1;31m" + card[1] + "\033[0m, "
    
def blackCard(card):
    return str(card[0]) + card[1] + ", "
 
def printKey(hand):
    output = ''
    for i in range(len(hand)):
        output += " %i, " % (i+1)
    print(output.strip(', '))
    
def drawCard(hand):
    hand.append(deck.pop())

def choosePickUp(hand):
    choice = ''
    while choice.lower() not in ['d', 'p']:
        printHand(hand)
        print("Discard Pile: ", getCardColour(discard[-1]))
        print("..........................\n")
        choice = input("Enter 'd' to draw or 'p' to pickup discard: ")
    if choice == 'p':
        hand.append(discard.pop())
    else:
        drawCard(hand)
  
def playGame():
    turn = 1
    (playerOneHand, playerTwoHand) = deal(deck, 7, 2)
    knocked = False
    lastTurn = False
    currentPlayer = 1
    while lastTurn == False:
        if len(deck) == 0:
            discard.reverse()
            deck.append(discard)
            discard = []
        if knocked == True:
            lastTurn = True
        hand = playerOneHand if currentPlayer == 1 else playerTwoHand
        print("###########################\n")
        print("Turn %i, Player %i\n" % (turn, currentPlayer))
        if len(discard) > 0:
            choosePickUp(hand)
        else:
            drawCard(hand)
        printHand(hand)
        printKey(hand)
        choice = input("Enter number of card to discard or 'k' to Knock: ")
        if choice.lower() == "k":
            knocked = True
            return False
        if not choice.isnumeric():
            return False
        choice = int(choice)
        if choice > len(hand) or choice < 1:
            return False
        discard.append(hand.pop(choice - 1))
        currentPlayer = (currentPlayer + 1) % 2
        turn += 1
    
    print("Game Ended Count Your Scores")
    print("Player One:")
    printHand(playerOneHand)
    print("Player Two:")
    printHand(playerTwoHand)

#start game
playGame()
        