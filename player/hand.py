# -*- coding: utf-8 -*-
from itertools import combinations
from deck.rank import Rank
from view.colours import green
from view.colours import grey


class Hand(Rank):
    melds = []
    score = 0

    # ToDo: move scoring methods to score class or a calc class
    # ToDo: move meld methods to meld class
    # ToDo: create classes for each sort (Maybe Decorator or Command pattern for combination sorts?)

    def __init__(self):
        super().__init__()
        self.hand = []

    def drawCard(self, card):
        self.hand.append(card)

    def discardCard(self, choice):
        return self.hand.pop(choice)

    def getScore(self):
        self.calculateScore()
        return self.score

    def getHand(self):
        self.sortHandBySuitAndRank()
        return ''.join([card.getCardColour() for card in self.hand]).strip(', ')

    def getKey(self):
        return ''.join([" %s, " % green(str((i + 1))) for i in range(len(self.hand))])

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
            for subset in combinations(self.melds, L):
                allPossibleMelds.append(subset)
        return allPossibleMelds

    def findLowestScoringMelds(self, allPossibleMelds, cards):
        scores = []
        for item in allPossibleMelds:
            if len(item) > 1:
                for i in range(len(item) - 1):
                    if item[i].isdisjoint(item[i + 1]):
                        scores = self.findScores(item, i, cards, scores)
            else:
                remainingCards = cards.difference(item[0])
                scores.append(sum([x[1] + 1 for x in remainingCards]))
        return scores

    @staticmethod
    def findScores(item, i, cards, scores):
        if item[i].isdisjoint(item[i + 1]):
            items = item[i] | item[i + 1]
            remainingCards = cards.difference(items)
            scores.append(sum([x[1] + 1 for x in remainingCards]))
            return scores
        else:
            return []

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
