from copy import deepcopy
from itertools import combinations

from rummy.deck.sort import Sort


class Melds:

    def __init__(self):
        self.sort = Sort()
        self.melds = []

    def findDiscardScores(self, hand, discard=None):
        scores = []
        handCopy = deepcopy(hand)
        if discard:
            handCopy.append(discard)
        for i in range(8):
            dummyHand = deepcopy(handCopy)
            dummyHand.pop(i)
            score = self.calculateScore(dummyHand)
            scores.append(score)
        return scores

    def calculateScore(self, hand):
        self.melds = []
        hand = self.sort.sortHandBySuitAndRank(hand)
        cards = {self.sort.suitAndRankKey(card) for card in hand}
        self.findSets(hand)
        self.findRuns(hand)
        allPossibleMelds = self.findAllPossibleMelds()
        if len(allPossibleMelds) > 0:
            scores = self.findLowestScoringMelds(allPossibleMelds, cards)
            score = min(scores)
        else:
            score = sum([x[1] + 1 for x in cards])
        return score

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

    def findSets(self, hand):
        hand = self.sort.sortHandByRank(hand)
        cards = [self.sort.suitAndRankKey(card) for card in hand]
        i = 1
        while i < len(cards):
            i, meld = self.makeSetMeld(cards, i)
            self.makeAllMelds(meld)
            i += 1

    def findRuns(self, hand):
        hand = self.sort.sortHandBySuitAndRank(hand)
        cards = [self.sort.suitAndRankKey(card) for card in hand]
        i = 1
        while i < len(cards):
            i, meld = self.makeRunMeld(cards, i)
            self.makeAllMelds(meld)
            i += 1

    def makeSetMeld(self, cards, i):
        meld = []
        while i < len(cards) and cards[i][1] == cards[i - 1][1]:
            meld.append(cards[i - 1])
            i += 1
        meld.append(cards[i - 1])
        return i, meld

    def makeRunMeld(self, cards, i):
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


if __name__ == '__main__':
    import sys


    def main():
        from rummy.deck.rank import Rank
        key = [
            'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠',
            '8♠', '9♠', 'T♠', 'J♠', 'Q♠', 'K♠',
            'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
            '8♥', '9♥', 'T♥', 'J♥', 'Q♥', 'K♥',
            'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦',
            '8♦', '9♦', 'T♦', 'J♦', 'Q♦', 'K♦',
            'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣',
            '8♣', '9♣', 'T♣', 'J♣', 'Q♣', 'K♣'
        ]
        rank = Rank()
        melds = Melds()
        cards = rank.rankedCards
        while True:
            handString = input('Hand String: ')
            hand = [cards[key.index(card)] for card in handString.split(', ')]
            if len(hand) > 7:
                scores = melds.findDiscardScores(hand)
                print('Possible Scores: ', scores)
                print('Discard: ', hand.pop(scores.index(min(scores))))
            print('Hand: ', ', '.join([str(card) for card in hand]))
            print('Score: ', melds.calculateScore(hand))
            print("\n==============================\n")


    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
